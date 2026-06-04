# ============================================================
# NExT-QA Metadata Utilities
# ============================================================
#
# Purpose:
#     Shared NExT-QA annotation and video-inventory metadata
#     functions used by:
#
#         02_Prepare_Video_Evidence
#         03_Build_Video_Knowledge_Base
#         04_Run_Baseline_VideoQA
#         05_Run_RAG_VideoQA
#         06_Run_Iterative_RAG_Experiments
#         07_Evaluate_and_Visualize_Results
#
# Notes:
#     This module intentionally contains only reusable metadata
#     loading, normalization, inventory, and split-summary logic.
#
#     Archive extraction and local video-cache management remain in
#     nextqa_video_cache.py.
#
#     Evidence segmentation, evidence validation, and evidence I/O
#     remain in their own dedicated modules.
# ============================================================

from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence

import pandas as pd


# ------------------------------------------------------------
# Default Metadata Configuration
# ------------------------------------------------------------

DEFAULT_NEXTQA_SPLIT_FILES: Dict[str, str] = {
    "train": "train.csv",
    "val": "val.csv",
    "test": "test.csv",
}

DEFAULT_VIDEO_EXTENSIONS: Sequence[str] = (
    ".mp4",
    ".avi",
    ".mov",
    ".mkv",
)

DEFAULT_VIDEO_ID_COLUMNS: Sequence[str] = (
    "video",
    "video_id",
    "vid",
    "video_name",
)

DEFAULT_QUESTION_ID_COLUMNS: Sequence[str] = (
    "qid",
    "question_id",
    "id",
)


# ------------------------------------------------------------
# Helper Functions
# ------------------------------------------------------------

def _as_path(path: str | Path) -> Path:
    """Convert a string or Path-like value to a Path object."""

    return Path(path)


def _print_if_verbose(message: str, verbose: bool = True) -> None:
    """Print a message only when verbose output is enabled."""

    if verbose:
        print(message)


def _find_first_existing_column(
    dataframe: pd.DataFrame,
    candidate_columns: Iterable[str],
) -> Optional[str]:
    """Return the first candidate column found in a DataFrame."""

    for column_name in candidate_columns:
        if column_name in dataframe.columns:
            return column_name

    return None


def _normalize_video_id(value: object) -> str:
    """Normalize a video identifier for joins and lookups."""

    if pd.isna(value):
        return ""

    video_id = str(value).strip()

    for suffix in DEFAULT_VIDEO_EXTENSIONS:
        if video_id.lower().endswith(suffix):
            video_id = video_id[: -len(suffix)]
            break

    return video_id


# ------------------------------------------------------------
# Annotation Loading
# ------------------------------------------------------------

def load_nextqa_split_annotations(
    annotations_dir: str | Path,
    split_files: Optional[Dict[str, str]] = None,
    video_id_columns: Sequence[str] = DEFAULT_VIDEO_ID_COLUMNS,
    question_id_columns: Sequence[str] = DEFAULT_QUESTION_ID_COLUMNS,
    verbose: bool = True,
) -> Dict[str, pd.DataFrame]:
    """
    Load NExT-QA annotation CSV files by split.

    Parameters
    ----------
    annotations_dir:
        Directory containing NExT-QA train, validation, and test CSV files.

    split_files:
        Optional mapping from split name to CSV filename. When omitted,
        the standard NExT-QA split filenames are used.

    video_id_columns:
        Candidate column names used to identify the video ID field.

    question_id_columns:
        Candidate column names used to identify the question ID field.

    verbose:
        Whether to print split loading information.

    Returns
    -------
    dict
        Mapping from split name to annotation DataFrame. Each DataFrame
        includes normalized helper columns when possible.
    """

    annotations_dir = _as_path(annotations_dir)
    split_files = split_files or DEFAULT_NEXTQA_SPLIT_FILES

    if not annotations_dir.exists():
        raise FileNotFoundError(
            f"NExT-QA annotations directory not found: {annotations_dir}"
        )

    split_dataframes: Dict[str, pd.DataFrame] = {}

    _print_if_verbose("Loading NExT-QA annotation split files...", verbose)

    for split_name, filename in split_files.items():

        split_path = annotations_dir / filename

        if not split_path.exists():
            raise FileNotFoundError(
                f"NExT-QA annotation file not found for split "
                f"'{split_name}': {split_path}"
            )

        dataframe = pd.read_csv(split_path)
        dataframe = dataframe.copy()
        dataframe["split"] = split_name

        video_column = _find_first_existing_column(
            dataframe,
            video_id_columns,
        )

        if video_column is not None:
            dataframe["video_id"] = dataframe[video_column].map(
                _normalize_video_id
            )

        question_column = _find_first_existing_column(
            dataframe,
            question_id_columns,
        )

        if question_column is not None and question_column != "question_id":
            dataframe["question_id"] = dataframe[question_column]

        split_dataframes[split_name] = dataframe

        _print_if_verbose(
            f"  Loaded {split_name:<5}: {len(dataframe):>7} records",
            verbose,
        )

    return split_dataframes


def combine_nextqa_annotations(
    split_dataframes: Dict[str, pd.DataFrame],
    verbose: bool = True,
) -> pd.DataFrame:
    """
    Combine loaded NExT-QA split DataFrames into one annotation table.

    Parameters
    ----------
    split_dataframes:
        Mapping from split name to annotation DataFrame.

    verbose:
        Whether to print combined annotation summary information.

    Returns
    -------
    pandas.DataFrame
        Combined annotation table containing all supplied splits.
    """

    if not split_dataframes:
        raise ValueError("No NExT-QA split DataFrames were provided.")

    combined_annotations = pd.concat(
        list(split_dataframes.values()),
        ignore_index=True,
        sort=False,
    )

    if verbose:

        print("Combined NExT-QA annotations created.")
        print(f"Total annotation records: {len(combined_annotations)}")

        if "split" in combined_annotations.columns:
            print("\nRecords by split:")
            print(combined_annotations["split"].value_counts().sort_index())

        if "video_id" in combined_annotations.columns:
            unique_video_count = combined_annotations["video_id"].nunique()
            print(f"\nUnique videos referenced: {unique_video_count}")

    return combined_annotations


# ------------------------------------------------------------
# Video Inventory
# ------------------------------------------------------------

def build_nextqa_video_inventory(
    videos_dir: str | Path,
    video_extensions: Sequence[str] = DEFAULT_VIDEO_EXTENSIONS,
    verbose: bool = True,
) -> pd.DataFrame:
    """
    Build a reusable inventory of local NExT-QA video files.

    Parameters
    ----------
    videos_dir:
        Directory containing extracted NExT-QA videos.

    video_extensions:
        Video file extensions to include in the inventory.

    verbose:
        Whether to print inventory summary information.

    Returns
    -------
    pandas.DataFrame
        Video inventory with video identifiers, paths, extensions, and
        file sizes.
    """

    videos_dir = _as_path(videos_dir)

    if not videos_dir.exists():
        raise FileNotFoundError(
            f"NExT-QA videos directory not found: {videos_dir}"
        )

    extensions = tuple(extension.lower() for extension in video_extensions)

    video_files = sorted(
        path for path in videos_dir.rglob("*")
        if path.is_file() and path.suffix.lower() in extensions
    )

    if not video_files:
        raise FileNotFoundError(
            f"No video files found in NExT-QA videos directory: {videos_dir}"
        )

    records: List[Dict[str, object]] = []

    for video_path in video_files:

        relative_path = video_path.relative_to(videos_dir)
        video_id = _normalize_video_id(video_path.stem)

        records.append(
            {
                "video_id": video_id,
                "video_filename": video_path.name,
                "video_relative_path": str(relative_path),
                "video_path": str(video_path),
                "video_extension": video_path.suffix.lower(),
                "video_size_bytes": video_path.stat().st_size,
            }
        )

    inventory = pd.DataFrame.from_records(records)

    if verbose:

        print("NExT-QA video inventory created.")
        print(f"Video files found: {len(inventory)}")
        print(f"Video directory: {videos_dir}")

    return inventory


def attach_video_inventory_to_annotations(
    annotations: pd.DataFrame,
    video_inventory: pd.DataFrame,
    how: str = "left",
    verbose: bool = True,
) -> pd.DataFrame:
    """
    Attach video inventory information to NExT-QA annotations.

    Parameters
    ----------
    annotations:
        Annotation DataFrame containing a ``video_id`` column.

    video_inventory:
        Video inventory DataFrame containing a ``video_id`` column.

    how:
        Pandas merge strategy. Defaults to ``left`` to preserve all
        annotation records.

    verbose:
        Whether to print merge summary information.

    Returns
    -------
    pandas.DataFrame
        Annotation records with local video path information attached.
    """

    if "video_id" not in annotations.columns:
        raise ValueError("Annotations DataFrame must contain a video_id column.")

    if "video_id" not in video_inventory.columns:
        raise ValueError("Video inventory DataFrame must contain a video_id column.")

    merged = annotations.merge(
        video_inventory,
        on="video_id",
        how=how,
        validate="many_to_one",
    )

    if verbose:

        missing_video_count = merged["video_path"].isna().sum()
        print("Video inventory attached to annotation records.")
        print(f"Annotation records: {len(merged)}")
        print(f"Records missing local video path: {missing_video_count}")

    return merged


# ------------------------------------------------------------
# Summary and Verification
# ------------------------------------------------------------

def summarize_nextqa_splits(
    annotations: pd.DataFrame,
) -> pd.DataFrame:
    """
    Summarize NExT-QA annotation counts by dataset split.

    Parameters
    ----------
    annotations:
        Combined annotation DataFrame containing ``split`` and optionally
        ``video_id`` columns.

    Returns
    -------
    pandas.DataFrame
        Split-level summary table.
    """

    if "split" not in annotations.columns:
        raise ValueError("Annotations DataFrame must contain a split column.")

    group = annotations.groupby("split", dropna=False)

    summary = group.size().rename("annotation_count").to_frame()

    if "video_id" in annotations.columns:
        summary["unique_video_count"] = group["video_id"].nunique()

    return summary.reset_index()


def verify_annotation_video_coverage(
    annotations: pd.DataFrame,
    video_inventory: pd.DataFrame,
    verbose: bool = True,
) -> Dict[str, object]:
    """
    Verify that annotation video IDs are present in the local inventory.

    Parameters
    ----------
    annotations:
        Annotation DataFrame containing ``video_id``.

    video_inventory:
        Video inventory DataFrame containing ``video_id``.

    verbose:
        Whether to print coverage information.

    Returns
    -------
    dict
        Coverage summary including missing and extra video IDs.
    """

    if "video_id" not in annotations.columns:
        raise ValueError("Annotations DataFrame must contain a video_id column.")

    if "video_id" not in video_inventory.columns:
        raise ValueError("Video inventory DataFrame must contain a video_id column.")

    annotation_video_ids = set(
        annotations["video_id"].dropna().map(str)
    )
    inventory_video_ids = set(
        video_inventory["video_id"].dropna().map(str)
    )

    missing_video_ids = sorted(annotation_video_ids - inventory_video_ids)
    extra_video_ids = sorted(inventory_video_ids - annotation_video_ids)

    if verbose:

        print("NExT-QA annotation/video coverage verification complete.")
        print(f"Videos referenced by annotations: {len(annotation_video_ids)}")
        print(f"Videos found in local inventory:  {len(inventory_video_ids)}")
        print(f"Missing referenced videos:        {len(missing_video_ids)}")
        print(f"Extra inventory videos:           {len(extra_video_ids)}")

    return {
        "annotation_video_count": len(annotation_video_ids),
        "inventory_video_count": len(inventory_video_ids),
        "missing_video_ids": missing_video_ids,
        "extra_video_ids": extra_video_ids,
    }
