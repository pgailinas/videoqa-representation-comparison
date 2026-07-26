"""
Shared project setup utilities for the VideoQA tutorial notebooks.
"""

import shutil
import zipfile
from pathlib import Path
from typing import Iterable


DEFAULT_DRIVE_ARCHIVE_PATH = Path(
    "/content/drive/MyDrive/VideoQA_Project_Artifacts.zip"
)

DEFAULT_LOCAL_ARCHIVE_PATH = Path(
    "/content/VideoQA_Project_Artifacts.zip"
)

DEFAULT_EXTRACTION_DIR = Path("/content")

DEFAULT_PROJECT_DIR = Path(
    "/content/VideoQA_Project"
)

DEFAULT_REQUIRED_DIRECTORIES = (
    "representations",
    "experiments",
    "evaluation",
)


def restore_project_artifacts(
    drive_archive_path: str | Path = DEFAULT_DRIVE_ARCHIVE_PATH,
    local_archive_path: str | Path = DEFAULT_LOCAL_ARCHIVE_PATH,
    extraction_dir: str | Path = DEFAULT_EXTRACTION_DIR,
    project_dir: str | Path = DEFAULT_PROJECT_DIR,
    required_directories: Iterable[str] = DEFAULT_REQUIRED_DIRECTORIES,
    force_restore: bool = False,
    remove_local_archive: bool = True,
) -> Path:
    """
    Copy and extract the VideoQA artifacts-only ZIP archive.

    The archive is expected to contain:

        VideoQA_Project/
            representations/
            experiments/
            evaluation/

    Parameters
    ----------
    drive_archive_path:
        Google Drive path to VideoQA_Project_Artifacts.zip.
    local_archive_path:
        Temporary local path used for the copied archive.
    extraction_dir:
        Directory into which the archive is extracted.
    project_dir:
        Expected restored VideoQA project directory.
    required_directories:
        Subdirectories that must exist after extraction.
    force_restore:
        Restore even when all required directories already exist.
    remove_local_archive:
        Delete the temporary local ZIP after successful extraction.

    Returns
    -------
    pathlib.Path
        Path to the restored VideoQA project directory.
    """

    drive_archive_path = Path(drive_archive_path)
    local_archive_path = Path(local_archive_path)
    extraction_dir = Path(extraction_dir)
    project_dir = Path(project_dir)
    required_directories = tuple(required_directories)

    expected_paths = [
        project_dir / directory_name
        for directory_name in required_directories
    ]

    if not force_restore and all(path.is_dir() for path in expected_paths):
        print("VideoQA project artifacts are already available.")
        print(f"Project directory: {project_dir}")
        return project_dir

    if not drive_archive_path.is_file():
        raise FileNotFoundError(
            "Missing VideoQA artifacts archive:\n"
            f"{drive_archive_path}\n\n"
            "Confirm that Google Drive is mounted and the archive exists."
        )

    extraction_dir.mkdir(parents=True, exist_ok=True)
    local_archive_path.parent.mkdir(parents=True, exist_ok=True)

    print("Restoring VideoQA project artifacts...")
    print("-" * 60)

    archive_size_gb = drive_archive_path.stat().st_size / (1024 ** 3)

    print(
        "Copying artifacts archive "
        f"({archive_size_gb:.2f} GB)..."
    )

    shutil.copy2(
        drive_archive_path,
        local_archive_path,
    )

    print("Artifacts archive copied.")
    print("Extracting artifacts archive...")

    try:
        with zipfile.ZipFile(local_archive_path, "r") as archive:
            bad_member = archive.testzip()

            if bad_member is not None:
                raise zipfile.BadZipFile(
                    "Corrupt file found in artifacts archive: "
                    f"{bad_member}"
                )

            archive.extractall(extraction_dir)

    finally:
        if remove_local_archive and local_archive_path.exists():
            local_archive_path.unlink()

    missing_paths = [
        path
        for path in expected_paths
        if not path.is_dir()
    ]

    if missing_paths:
        missing_path_list = "\n".join(
            str(path)
            for path in missing_paths
        )

        raise FileNotFoundError(
            "Artifact restoration completed, but required directories "
            "were not found:\n"
            f"{missing_path_list}\n\n"
            "Verify the internal directory structure of the ZIP archive."
        )

    print("VideoQA project artifacts restored.")
    print(f"Project directory: {project_dir}")

    for path in expected_paths:
        print(f"Verified: {path}")

    return project_dir
