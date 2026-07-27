# ============================================================
# VideoQA Project Restoration Utilities
# ============================================================

import shutil
import zipfile
from pathlib import Path

from src.nextqa_video_cache import extract_nextqa_video_archive


def download_google_drive_archive(
    download_url: str,
    destination_path: Path,
    verbose: bool = True,
) -> None:
    """Download a shared tutorial archive from Google Drive."""

    try:
        import gdown
    except ImportError as exc:
        raise ImportError(
            "The gdown package is required to download shared "
            "Google Drive archives."
        ) from exc

    destination_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    if verbose:
        print("Downloading shared tutorial archive...")

    downloaded_path = gdown.download(
        url=download_url,
        output=str(destination_path),
        quiet=not verbose,
        fuzzy=True,
    )

    if (
        downloaded_path is None
        or not destination_path.exists()
    ):
        raise FileNotFoundError(
            "Failed to download shared tutorial archive locally:\n"
            f"{destination_path}"
        )


def restore_project_artifacts(
    drive_archive_path: Path,
    local_archive_path: Path,
    project_dir: Path,
    required_paths: list[Path],
    download_url: str | None = None,
    verbose: bool = True,
) -> None:
    """Restore the local VideoQA project artifact mirror."""

    missing_paths = [
        path
        for path in required_paths
        if not path.exists()
    ]

    if not missing_paths:
        if verbose:
            print("Local project artifacts already available.")
        return

    if verbose:
        print("Local project artifacts missing or incomplete.")
        print("Restoring project artifacts...")

    local_archive_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    if drive_archive_path.exists():
        if verbose:
            print("Copying project artifacts archive...")

        shutil.copy2(
            drive_archive_path,
            local_archive_path,
        )

    elif download_url is not None:
        download_google_drive_archive(
            download_url=download_url,
            destination_path=local_archive_path,
            verbose=verbose,
        )

    else:
        raise FileNotFoundError(
            "Missing VideoQA project artifacts archive:\n"
            f"{drive_archive_path}"
        )

    if not local_archive_path.exists():
        raise FileNotFoundError(
            "Failed to obtain project artifacts archive locally:\n"
            f"{local_archive_path}"
        )

    if verbose:
        print("Extracting project artifacts archive...")

    try:
        with zipfile.ZipFile(
            local_archive_path,
            mode="r",
        ) as archive:
            archive.extractall(
                project_dir.parent
            )

    finally:
        if local_archive_path.exists():
            local_archive_path.unlink()

    missing_paths = [
        path
        for path in required_paths
        if not path.exists()
    ]

    if missing_paths:
        for path in missing_paths:
            print(f"Missing restored artifact path: {path}")

        raise FileNotFoundError(
            "One or more project artifact directories "
            "were not restored."
        )

    if verbose:
        print("Project artifacts restored.")
        print(f"Local project mirror ready: {project_dir}")


def restore_nextqa_videos(
    drive_archive_path: Path,
    local_archive_path: Path,
    videos_dir: Path,
    expected_video_count: int,
    download_url: str | None = None,
    verbose: bool = True,
) -> None:
    """Restore and verify the local NExT-QA video cache."""

    existing_video_files = sorted(
        videos_dir.rglob("*.mp4")
    )

    if len(existing_video_files) == expected_video_count:
        if verbose:
            print("Local video cache already available.")
            print(f"Videos found: {len(existing_video_files):,}")
        return

    if verbose:
        print("Local video cache missing or incomplete.")
        print(f"Videos found locally: {len(existing_video_files):,}")
        print("Restoring videos...")

    local_archive_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    if drive_archive_path.exists():
        if verbose:
            print("Copying dataset archive from Google Drive...")

        shutil.copy2(
            drive_archive_path,
            local_archive_path,
        )

    elif download_url is not None:
        download_google_drive_archive(
            download_url=download_url,
            destination_path=local_archive_path,
            verbose=verbose,
        )

    else:
        raise FileNotFoundError(
            "Missing NExT-QA combined archive in Google Drive:\n"
            f"{drive_archive_path}"
        )

    if not local_archive_path.exists():
        raise FileNotFoundError(
            "Failed to obtain NExT-QA archive locally:\n"
            f"{local_archive_path}"
        )

    if verbose:
        print("Extracting or verifying video archive...")

    try:
        extract_nextqa_video_archive(
            combined_archive_path=local_archive_path,
            local_videos_dir=videos_dir,
            force_extract=False,
            verbose=verbose,
        )

    finally:
        if local_archive_path.exists():
            local_archive_path.unlink()

    restored_video_files = sorted(
        videos_dir.rglob("*.mp4")
    )

    if len(restored_video_files) != expected_video_count:
        raise ValueError(
            "NExT-QA video cache verification failed. "
            f"Expected {expected_video_count:,} videos, "
            f"found {len(restored_video_files):,}."
        )

    if verbose:
        print("Video cache restored.")
        print(f"Videos found: {len(restored_video_files):,}")
