# ============================================================
# NExT-QA Video Cache Utilities
# ============================================================
#
# Purpose:
#     Shared archive reconstruction and video-cache
#     management functions used by:
#
#         01_Prepare_Video_Data
#         02_Prepare_Video_Evidence
#         03_Build_Video_Knowledge_Base
#
# Notes:
#     This module intentionally contains only archive,
#     extraction, and local-cache management logic.
#
#     Dataset validation, cross-reference verification,
#     sample inspection, and readiness reporting remain
#     in the notebooks.
# ============================================================

from __future__ import annotations

import shutil
import subprocess
import time

from pathlib import Path
from typing import Dict, Iterable, List, Optional


# ------------------------------------------------------------
# Default Archive Configuration
# ------------------------------------------------------------

DEFAULT_NEXTQA_ARCHIVE_FILES: List[str] = [
    "NExTVideo.z01",
    "NExTVideo.z02",
    "NExTVideo.z03",
    "NExTVideo.z04",
    "NExTVideo.z05",
    "NExTVideo.z06",
    "NExTVideo.zip",
]

DEFAULT_COMBINED_ARCHIVE_NAME = "NExTVideo_combined.zip"
DEFAULT_SPLIT_ARCHIVE_NAME = "NExTVideo.zip"


# ------------------------------------------------------------
# Helper Functions
# ------------------------------------------------------------

def _as_path(path: str | Path) -> Path:
    """Convert a string or Path-like value to a Path object."""

    return Path(path)


def _format_gb(size_bytes: int) -> str:
    """Format a byte count as gigabytes."""

    return f"{size_bytes / (1024 ** 3):.2f} GB"


def _print_if_verbose(message: str, verbose: bool = True) -> None:
    """Print a message only when verbose output is enabled."""

    if verbose:
        print(message)


# ------------------------------------------------------------
# Archive Verification
# ------------------------------------------------------------

def verify_nextqa_archive_parts(
    archive_parts_dir: str | Path,
    required_archive_files: Optional[Iterable[str]] = None,
    verbose: bool = True,
) -> Dict[str, object]:
    """
    Verify that all required NExT-QA multipart archive files exist.

    Parameters
    ----------
    archive_parts_dir:
        Directory containing the NExT-QA multipart archive files.

    required_archive_files:
        Optional iterable of required archive filenames. When omitted,
        the standard seven NExT-QA archive files are used.

    verbose:
        Whether to print progress and file information.

    Returns
    -------
    dict
        Verification summary containing the archive directory, required
        files, and total size in bytes.
    """

    archive_parts_dir = _as_path(archive_parts_dir)
    required_files = list(
        required_archive_files
        if required_archive_files is not None
        else DEFAULT_NEXTQA_ARCHIVE_FILES
    )

    if not archive_parts_dir.exists():
        raise FileNotFoundError(
            f"NExT-QA archive directory not found: {archive_parts_dir}"
        )

    missing_files: List[str] = []
    found_files: List[Path] = []

    _print_if_verbose(
        "Checking NExT-QA video archive files...",
        verbose,
    )

    for filename in required_files:

        file_path = archive_parts_dir / filename

        if not file_path.exists():

            missing_files.append(filename)

        else:

            found_files.append(file_path)

            if verbose:

                print(
                    f"  FOUND: {filename:<16} "
                    f"{_format_gb(file_path.stat().st_size):>10}"
                )

    if missing_files:
        raise FileNotFoundError(
            "Missing required NExT-QA archive files: "
            + ", ".join(missing_files)
        )

    total_size_bytes = sum(
        file_path.stat().st_size
        for file_path in found_files
    )

    _print_if_verbose(
        "All required NExT-QA video archive files were found.",
        verbose,
    )

    if verbose:

        print("\nArchive Directory:")
        print(f"  {archive_parts_dir}")

        print("\nTotal Archive Size:")
        print(f"  {_format_gb(total_size_bytes)}")

    return {
        "archive_parts_dir": archive_parts_dir,
        "required_archive_files": required_files,
        "found_archive_files": found_files,
        "total_size_bytes": total_size_bytes,
    }


# ------------------------------------------------------------
# Archive Copy
# ------------------------------------------------------------

def copy_nextqa_archive_parts_to_local(
    source_archive_dir: str | Path,
    local_archive_dir: str | Path,
    required_archive_files: Optional[Iterable[str]] = None,
    verbose: bool = True,
) -> Dict[str, object]:
    """
    Copy NExT-QA multipart archive files to local runtime storage.

    Existing local files are skipped when the local file size matches
    the source file size.

    Parameters
    ----------
    source_archive_dir:
        Source directory containing archive parts, typically Google Drive.

    local_archive_dir:
        Local runtime directory where archive parts should be copied.

    required_archive_files:
        Optional iterable of required archive filenames. When omitted,
        the standard seven NExT-QA archive files are used.

    verbose:
        Whether to print progress and summary information.

    Returns
    -------
    dict
        Copy summary containing copied files, skipped files, and local
        archive directory information.
    """

    source_archive_dir = _as_path(source_archive_dir)
    local_archive_dir = _as_path(local_archive_dir)
    required_files = list(
        required_archive_files
        if required_archive_files is not None
        else DEFAULT_NEXTQA_ARCHIVE_FILES
    )

    verify_nextqa_archive_parts(
        archive_parts_dir=source_archive_dir,
        required_archive_files=required_files,
        verbose=verbose,
    )

    local_archive_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    copied_files: List[str] = []
    skipped_files: List[str] = []

    print("Copying NExT-QA archive files to local storage...")

    for filename in required_files:

        source_path = source_archive_dir / filename
        destination_path = local_archive_dir / filename

        source_size = source_path.stat().st_size
        source_size_gb = source_size / (1024 ** 3)

        copy_required = True

        if destination_path.exists():

            destination_size = destination_path.stat().st_size

            if destination_size == source_size:

                copy_required = False
                skipped_files.append(filename)

        if copy_required:

            print(
                f"  Copying: {filename} "
                f"({source_size_gb:.2f} GB)"
            )

            start_time = time.time()

            shutil.copy2(
                source_path,
                destination_path,
            )

            elapsed_time = time.time() - start_time

            copied_files.append(filename)

            print(
                f"  Completed: {filename} "
                f"({elapsed_time:.1f} seconds)"
            )

        else:

            print(
                f"  Skipping: {filename} "
                f"(local copy already exists)"
            )

    missing_local_files: List[str] = []
    size_mismatch_files: List[str] = []

    for filename in required_files:

        source_path = source_archive_dir / filename
        local_file = local_archive_dir / filename

        if not local_file.exists():

            missing_local_files.append(filename)

        elif local_file.stat().st_size != source_path.stat().st_size:

            size_mismatch_files.append(filename)

    if missing_local_files:
        raise FileNotFoundError(
            "Missing local archive files: "
            + ", ".join(missing_local_files)
        )

    if size_mismatch_files:
        raise ValueError(
            "Local archive file size mismatch detected: "
            + ", ".join(size_mismatch_files)
        )

    print("Local archive verification complete.")

    print(f"Files copied:  {len(copied_files)}")
    print(f"Files skipped: {len(skipped_files)}")

    total_archive_size_bytes = sum(
        file_path.stat().st_size
        for file_path in local_archive_dir.iterdir()
        if file_path.is_file()
    )

    if verbose:

        print("\nLocal Archive Directory:")
        print(f"  {local_archive_dir}")

        print("\nTotal Archive Size:")
        print(f"  {_format_gb(total_archive_size_bytes)}")

        print("\nLocal Archive Files:")

        for file_path in sorted(local_archive_dir.iterdir()):

            if file_path.is_file():

                print(
                    f"  {file_path.name:<16} "
                    f"{_format_gb(file_path.stat().st_size):>10}"
                )

    return {
        "source_archive_dir": source_archive_dir,
        "local_archive_dir": local_archive_dir,
        "copied_files": copied_files,
        "skipped_files": skipped_files,
        "total_size_bytes": total_archive_size_bytes,
    }


# ------------------------------------------------------------
# Combined Archive Build
# ------------------------------------------------------------

def build_combined_nextqa_archive(
    local_archive_dir: str | Path,
    combined_archive_path: Optional[str | Path] = None,
    split_archive_name: str = DEFAULT_SPLIT_ARCHIVE_NAME,
    required_archive_files: Optional[Iterable[str]] = None,
    force_rebuild: bool = True,
    verbose: bool = True,
) -> Dict[str, object]:
    """
    Build a single combined NExT-QA ZIP archive from split ZIP parts.

    Parameters
    ----------
    local_archive_dir:
        Local directory containing the copied multipart archive files.

    combined_archive_path:
        Output path for the combined ZIP archive. When omitted,
        ``NExTVideo_combined.zip`` is created in ``local_archive_dir``.

    split_archive_name:
        Name of the final split ZIP file used as the input to
        ``zip -s 0``.

    required_archive_files:
        Optional iterable of required archive filenames. When omitted,
        the standard seven NExT-QA archive files are used.

    force_rebuild:
        If True, rebuild the combined archive even if it already exists.
        If False, reuse an existing combined archive.

    verbose:
        Whether to print progress and summary information.

    Returns
    -------
    dict
        Build summary containing the combined archive path, size, and
        whether it was rebuilt.
    """

    local_archive_dir = _as_path(local_archive_dir)
    required_files = list(
        required_archive_files
        if required_archive_files is not None
        else DEFAULT_NEXTQA_ARCHIVE_FILES
    )

    if combined_archive_path is None:
        combined_archive_path = (
            local_archive_dir /
            DEFAULT_COMBINED_ARCHIVE_NAME
        )
    else:
        combined_archive_path = _as_path(combined_archive_path)

    split_archive_path = local_archive_dir / split_archive_name

    verify_nextqa_archive_parts(
        archive_parts_dir=local_archive_dir,
        required_archive_files=required_files,
        verbose=False,
    )

    if combined_archive_path.exists() and not force_rebuild:

        print("Combined NExT-QA archive already exists.")
        print(f"Combined archive path: {combined_archive_path}")

        return {
            "combined_archive_path": combined_archive_path,
            "combined_size_bytes": combined_archive_path.stat().st_size,
            "rebuilt": False,
        }

    if combined_archive_path.exists():

        print("Removing existing combined archive before rebuild.")

        combined_archive_path.unlink()

    print(
        "Building combined NExT-QA archive using "
        "zip split-archive conversion..."
    )
    print("This may take several minutes.")

    start_time = time.time()

    convert_command = [
        "zip",
        "-s",
        "0",
        str(split_archive_path),
        "--out",
        str(combined_archive_path),
    ]

    result = subprocess.run(
        convert_command,
        cwd=str(local_archive_dir),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    elapsed_time = time.time() - start_time

    if result.returncode != 0:
        raise RuntimeError(
            "Failed to build combined NExT-QA archive.\n\n"
            f"Command: {' '.join(convert_command)}\n\n"
            f"Elapsed Time: {elapsed_time:.1f} seconds\n\n"
            f"STDOUT:\n{result.stdout}\n\n"
            f"STDERR:\n{result.stderr}"
        )

    print(
        "Combined archive created "
        f"({elapsed_time:.1f} seconds)."
    )

    if not combined_archive_path.exists():
        raise FileNotFoundError(
            f"Combined archive was not created: {combined_archive_path}"
        )

    combined_size_bytes = combined_archive_path.stat().st_size

    print("Combined archive verification complete.")

    if verbose:

        print("\nCombined Archive Path:")
        print(f"  {combined_archive_path}")

        print("\nCombined Archive Size:")
        print(f"  {_format_gb(combined_size_bytes)}")

    return {
        "combined_archive_path": combined_archive_path,
        "combined_size_bytes": combined_size_bytes,
        "rebuilt": True,
        "elapsed_seconds": elapsed_time,
    }


# ------------------------------------------------------------
# Video Extraction and Verification
# ------------------------------------------------------------

def verify_nextqa_video_cache(
    local_videos_dir: str | Path,
    verbose: bool = True,
    sample_count: int = 10,
) -> Dict[str, object]:
    """
    Verify that the local NExT-QA video cache contains MP4 files.

    Parameters
    ----------
    local_videos_dir:
        Directory containing extracted NExT-QA video files.

    verbose:
        Whether to print summary and sample video paths.

    sample_count:
        Number of sample video file paths to display when verbose is True.

    Returns
    -------
    dict
        Verification summary containing video count, subdirectory count,
        and total video size in bytes.
    """

    local_videos_dir = _as_path(local_videos_dir)

    video_files = sorted(
        local_videos_dir.rglob("*.mp4")
        if local_videos_dir.exists()
        else []
    )

    if not video_files:
        raise FileNotFoundError(
            "No MP4 files were found in the local NExT-QA video cache."
        )

    video_subdirs = sorted(
        path for path in local_videos_dir.rglob("*")
        if path.is_dir()
    )

    total_video_size_bytes = sum(
        file_path.stat().st_size
        for file_path in video_files
    )

    print("NExT-QA video cache verified.")
    print(f"Video files found: {len(video_files)}")

    if verbose:

        print("\nLocal Video Directory:")
        print(f"  {local_videos_dir}")

        print("\nExtracted Video Size:")
        print(f"  {_format_gb(total_video_size_bytes)}")

        print("\nVideo Subdirectories Found:")
        print(f"  {len(video_subdirs)}")

        print("\nSample Video Files:")

        for file_path in video_files[:sample_count]:

            relative_path = file_path.relative_to(local_videos_dir)
            print(f"  {relative_path}")

    return {
        "local_videos_dir": local_videos_dir,
        "video_files": video_files,
        "video_count": len(video_files),
        "video_subdirs": video_subdirs,
        "video_subdir_count": len(video_subdirs),
        "total_video_size_bytes": total_video_size_bytes,
    }


def extract_nextqa_video_archive(
    combined_archive_path: str | Path,
    local_videos_dir: str | Path,
    force_extract: bool = False,
    verbose: bool = True,
) -> Dict[str, object]:
    """
    Extract the combined NExT-QA video archive into local runtime storage.

    Existing extracted videos are reused unless ``force_extract`` is True.

    Parameters
    ----------
    combined_archive_path:
        Path to the combined NExT-QA ZIP archive.

    local_videos_dir:
        Directory where extracted videos should be stored.

    force_extract:
        If True, extract the archive even when MP4 files already exist.

    verbose:
        Whether to print progress and summary information.

    Returns
    -------
    dict
        Extraction summary and video cache verification results.
    """

    combined_archive_path = _as_path(combined_archive_path)
    local_videos_dir = _as_path(local_videos_dir)

    local_videos_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    existing_video_files = sorted(
        local_videos_dir.rglob("*.mp4")
    )

    if existing_video_files and not force_extract:

        print("NExT-QA videos already appear to be extracted.")
        print(f"Existing video files found: {len(existing_video_files)}")

        verification = verify_nextqa_video_cache(
            local_videos_dir=local_videos_dir,
            verbose=verbose,
        )

        verification["extracted"] = False
        return verification

    if not combined_archive_path.exists():
        raise FileNotFoundError(
            f"Combined archive not found: {combined_archive_path}"
        )

    print("Extracting combined NExT-QA video archive...")
    print("This may take several minutes.")

    start_time = time.time()

    extract_command = [
        "unzip",
        "-qo",
        str(combined_archive_path),
        "-d",
        str(local_videos_dir),
    ]

    result = subprocess.run(
        extract_command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    elapsed_time = time.time() - start_time

    if result.returncode != 0:
        raise RuntimeError(
            "NExT-QA video archive extraction failed.\n\n"
            f"Command: {' '.join(extract_command)}\n\n"
            f"Elapsed Time: {elapsed_time:.1f} seconds\n\n"
            f"Error Output:\n{result.stderr}"
        )

    print(
        "NExT-QA video archive extraction complete "
        f"({elapsed_time:.1f} seconds)."
    )

    verification = verify_nextqa_video_cache(
        local_videos_dir=local_videos_dir,
        verbose=verbose,
    )

    verification["extracted"] = True
    verification["elapsed_seconds"] = elapsed_time

    return verification


# ------------------------------------------------------------
# Convenience Restore Wrapper
# ------------------------------------------------------------

def restore_nextqa_video_cache(
    source_archive_dir: str | Path,
    local_archive_dir: str | Path,
    local_videos_dir: str | Path,
    combined_archive_path: Optional[str | Path] = None,
    required_archive_files: Optional[Iterable[str]] = None,
    force_copy: bool = False,
    force_rebuild: bool = False,
    force_extract: bool = False,
    verbose: bool = True,
) -> Dict[str, object]:
    """
    Restore the local NExT-QA video cache from persistent archive parts.

    This convenience wrapper is intended for later notebooks that need
    the videos in local Colab storage without repeating the full archive
    workflow.

    Parameters
    ----------
    source_archive_dir:
        Persistent source directory containing archive parts.

    local_archive_dir:
        Local runtime directory where archive parts and combined archive
        should be stored.

    local_videos_dir:
        Local runtime directory where videos should be extracted.

    combined_archive_path:
        Optional output path for the combined ZIP archive.

    required_archive_files:
        Optional iterable of required archive filenames. When omitted,
        the standard seven NExT-QA archive files are used.

    force_copy:
        Reserved for readability. Existing local archive files are still
        copied only when missing or size-mismatched. Set this to True only
        for future extension needs.

    force_rebuild:
        Whether to rebuild the combined archive when it already exists.

    force_extract:
        Whether to extract videos even when MP4 files already exist.

    verbose:
        Whether to print progress and summary information.

    Returns
    -------
    dict
        Restore summary containing copy, build, and extraction results.
    """

    del force_copy  # Kept in signature for explicit notebook readability.

    local_archive_dir = _as_path(local_archive_dir)

    if combined_archive_path is None:
        combined_archive_path = (
            local_archive_dir /
            DEFAULT_COMBINED_ARCHIVE_NAME
        )

    print("Restoring NExT-QA local video cache...")
    print("=" * 60)

    copy_summary = copy_nextqa_archive_parts_to_local(
        source_archive_dir=source_archive_dir,
        local_archive_dir=local_archive_dir,
        required_archive_files=required_archive_files,
        verbose=verbose,
    )

    build_summary = build_combined_nextqa_archive(
        local_archive_dir=local_archive_dir,
        combined_archive_path=combined_archive_path,
        required_archive_files=required_archive_files,
        force_rebuild=force_rebuild,
        verbose=verbose,
    )

    extraction_summary = extract_nextqa_video_archive(
        combined_archive_path=build_summary["combined_archive_path"],
        local_videos_dir=local_videos_dir,
        force_extract=force_extract,
        verbose=verbose,
    )

    print("\nNExT-QA local video cache restore complete.")
    print("=" * 60)

    return {
        "copy_summary": copy_summary,
        "build_summary": build_summary,
        "extraction_summary": extraction_summary,
    }
