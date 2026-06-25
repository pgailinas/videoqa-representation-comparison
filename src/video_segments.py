# ============================================================
# Video Segment Generation Utilities
# ============================================================
#
# Purpose:
#     Shared video evidence generation and metadata utilities used by:
#
#         02_Prepare_Video_Evidence
#         03_Train_Autoencoder
#         07_Run_Final_Full_Experiment
#
# Notes:
#     This module contains reusable functions for:
#
#         • Video property inspection
#         • Evidence segmentation
#         • Evidence metadata generation
#         • Evidence summary generation
#
#     Project-wide evidence configuration values are defined in:
#
#         videoqa_representation_config.py
#
#     This module consumes those configuration values and provides
#     reusable implementation functions used throughout the project.
#
#     This module stores lightweight evidence metadata that references
#     original video files rather than duplicating video content.
# ============================================================

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional

import pandas as pd

from src.videoqa_representation_config import *

DEFAULT_VIDEO_PROPERTY_COLUMNS = (
    "video_id",
    "video_path",
    "duration_sec",
    "fps",
    "frame_count",
    "width",
    "height",
)


# ------------------------------------------------------------
# Data Classes
# ------------------------------------------------------------

@dataclass(frozen=True)
class VideoSegmentationParameters:
    """Configuration values for video segment generation."""

    segment_duration_sec: float = DEFAULT_SEGMENT_DURATION_SEC
    segment_stride_sec: float = DEFAULT_SEGMENT_STRIDE_SEC
    min_segment_duration_sec: float = DEFAULT_MIN_SEGMENT_DURATION_SEC
    segment_strategy: str = DEFAULT_SEGMENT_STRATEGY
    segment_level: int = DEFAULT_SEGMENT_LEVEL
    include_hierarchical_segments: bool = ENABLE_HIERARCHICAL_SEGMENTS
    parent_segment_duration_sec: Optional[float] = PARENT_SEGMENT_DURATION_SEC


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


def _safe_float(value: object, default: float = 0.0) -> float:
    """Convert a value to float, returning a default when invalid."""

    try:
        if pd.isna(value):
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def _time_to_frame_index(time_sec: float, fps: float) -> int:
    """Convert a timestamp in seconds to a zero-based frame index."""

    if fps <= 0:
        return 0

    return max(0, int(round(time_sec * fps)))


def _format_evidence_id(
    video_id: str,
    segment_index: int,
    prefix: str = "EV",
) -> str:
    """Create a deterministic evidence identifier."""

    safe_video_id = str(video_id).replace("/", "_").replace(" ", "_")
    return f"{prefix}_{safe_video_id}_{segment_index:05d}"


def _format_parent_evidence_id(
    video_id: str,
    parent_index: int,
    prefix: str = "PEV",
) -> str:
    """Create a deterministic parent evidence identifier."""

    safe_video_id = str(video_id).replace("/", "_").replace(" ", "_")
    return f"{prefix}_{safe_video_id}_{parent_index:05d}"


# ------------------------------------------------------------
# Video Property Inspection
# ------------------------------------------------------------

def inspect_video_properties(
    video_path: str | Path,
) -> Dict[str, object]:
    """
    Inspect basic properties of a single video file.

    Parameters
    ----------
    video_path:
        Path to a local video file.

    Returns
    -------
    dict
        Video properties including duration, frame rate, frame count,
        width, and height.

    Notes
    -----
    OpenCV is imported inside this function so the module can still be
    imported in lightweight environments where video inspection is not
    required.
    """

    video_path = _as_path(video_path)

    if not video_path.exists():
        raise FileNotFoundError(f"Video file not found: {video_path}")

    import cv2  # pylint: disable=import-outside-toplevel

    capture = cv2.VideoCapture(str(video_path))

    if not capture.isOpened():
        raise RuntimeError(f"Unable to open video file: {video_path}")

    try:
        fps = float(capture.get(cv2.CAP_PROP_FPS) or 0.0)
        frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
        width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH) or 0)
        height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT) or 0)
    finally:
        capture.release()

    duration_sec = frame_count / fps if fps > 0 else 0.0

    return {
        "video_path": str(video_path),
        "duration_sec": duration_sec,
        "fps": fps,
        "frame_count": frame_count,
        "width": width,
        "height": height,
    }


def build_video_property_table(
    video_inventory: pd.DataFrame,
    video_path_column: str = "video_path",
    video_id_column: str = "video_id",
    max_videos: Optional[int] = None,
    verbose: bool = True,
) -> pd.DataFrame:
    """
    Build a table of video properties for a video inventory.

    Parameters
    ----------
    video_inventory:
        DataFrame containing local video paths.

    video_path_column:
        Column containing video file paths.

    video_id_column:
        Column containing video identifiers.

    max_videos:
        Optional maximum number of videos to inspect.

    verbose:
        Whether to print progress information.

    Returns
    -------
    pandas.DataFrame
        Video property table suitable for evidence generation.
    """

    if video_path_column not in video_inventory.columns:
        raise ValueError(
            f"Video inventory must contain column: {video_path_column}"
        )

    if video_id_column not in video_inventory.columns:
        raise ValueError(
            f"Video inventory must contain column: {video_id_column}"
        )

    records: List[Dict[str, object]] = []
    rows = video_inventory.reset_index(drop=True)

    if max_videos is not None:
        rows = rows.head(max_videos)

    total_count = len(rows)

    _print_if_verbose(
        f"Inspecting video properties for {total_count} videos...",
        verbose,
    )

    for row_index, row in rows.iterrows():

        video_id = str(row[video_id_column])
        video_path = row[video_path_column]

        properties = inspect_video_properties(video_path)
        properties["video_id"] = video_id
        records.append(properties)

        if verbose and ((row_index + 1) % 100 == 0 or row_index + 1 == total_count):
            print(f"  Inspected {row_index + 1:>6} / {total_count:<6} videos")

    property_table = pd.DataFrame.from_records(records)

    _print_if_verbose("Video property inspection complete.", verbose)

    return property_table


# ------------------------------------------------------------
# Evidence Segment Generation
# ------------------------------------------------------------

def generate_fixed_window_segments(
    duration_sec: float,
    segment_duration_sec: float = DEFAULT_SEGMENT_DURATION_SEC,
    segment_stride_sec: float = DEFAULT_SEGMENT_STRIDE_SEC,
    min_segment_duration_sec: float = DEFAULT_MIN_SEGMENT_DURATION_SEC,
) -> List[Dict[str, float]]:
    """
    Generate fixed-window segment boundaries for a video duration.

    Parameters
    ----------
    duration_sec:
        Total video duration in seconds.

    segment_duration_sec:
        Target evidence segment duration in seconds.

    segment_stride_sec:
        Step size between segment starts in seconds.

    min_segment_duration_sec:
        Minimum duration required for the final segment.

    Returns
    -------
    list of dict
        Segment timing dictionaries containing start, midpoint, end, and
        duration values.
    """

    duration_sec = max(0.0, float(duration_sec))
    segment_duration_sec = max(0.001, float(segment_duration_sec))
    segment_stride_sec = max(0.001, float(segment_stride_sec))
    min_segment_duration_sec = max(0.0, float(min_segment_duration_sec))

    if duration_sec <= 0:
        return []

    segments: List[Dict[str, float]] = []
    start_time_sec = 0.0

    while start_time_sec < duration_sec:

        end_time_sec = min(start_time_sec + segment_duration_sec, duration_sec)
        segment_duration = end_time_sec - start_time_sec

        if segment_duration < min_segment_duration_sec:
            break

        midpoint_time_sec = start_time_sec + (segment_duration / 2.0)

        segments.append(
            {
                "start_time_sec": round(start_time_sec, 4),
                "midpoint_time_sec": round(midpoint_time_sec, 4),
                "end_time_sec": round(end_time_sec, 4),
                "duration_sec": round(segment_duration, 4),
            }
        )

        if end_time_sec >= duration_sec:
            break

        start_time_sec += segment_stride_sec

    return segments


def generate_evidence_records_for_video(
    video_properties: Dict[str, object],
    parameters: VideoSegmentationParameters,
    split: Optional[str] = None,
) -> List[Dict[str, object]]:
    """
    Generate evidence metadata records for a single video.

    Parameters
    ----------
    video_properties:
        Dictionary containing video_id, video_path, duration, fps, frame
        count, width, and height values.

    parameters:
        Evidence segmentation configuration.

    split:
        Optional dataset split label associated with the video.

    Returns
    -------
    list of dict
        Evidence metadata records for the video.
    """

    video_id = str(video_properties.get("video_id", ""))

    if not video_id:
        raise ValueError("video_properties must contain a non-empty video_id.")

    duration_sec = _safe_float(video_properties.get("duration_sec"))
    fps = _safe_float(video_properties.get("fps"))
    frame_count = int(_safe_float(video_properties.get("frame_count")))

    segments = generate_fixed_window_segments(
        duration_sec=duration_sec,
        segment_duration_sec=parameters.segment_duration_sec,
        segment_stride_sec=parameters.segment_stride_sec,
        min_segment_duration_sec=parameters.min_segment_duration_sec,
    )

    records: List[Dict[str, object]] = []

    parent_duration = parameters.parent_segment_duration_sec

    for segment_index, segment in enumerate(segments):

        start_time = segment["start_time_sec"]
        midpoint_time = segment["midpoint_time_sec"]
        end_time = segment["end_time_sec"]

        start_frame_idx = _time_to_frame_index(start_time, fps)
        midpoint_frame_idx = _time_to_frame_index(midpoint_time, fps)
        end_frame_idx = min(
            max(0, frame_count - 1),
            _time_to_frame_index(end_time, fps),
        )

        parent_evidence_id = None

        if parameters.include_parent_evidence and parent_duration:
            parent_index = int(math.floor(start_time / parent_duration))
            parent_evidence_id = _format_parent_evidence_id(
                video_id=video_id,
                parent_index=parent_index,
            )

        record = {
            "evidence_id": _format_evidence_id(video_id, segment_index),
            "video_id": video_id,
            "split": split,
            "video_path": video_properties.get("video_path"),
            "evidence_level": parameters.evidence_level,
            "segment_strategy": parameters.segment_strategy,
            "segment_index": segment_index,
            "parent_evidence_id": parent_evidence_id,
            "start_time_sec": start_time,
            "midpoint_time_sec": midpoint_time,
            "end_time_sec": end_time,
            "duration_sec": segment["duration_sec"],
            "start_frame_idx": start_frame_idx,
            "midpoint_frame_idx": midpoint_frame_idx,
            "end_frame_idx": end_frame_idx,
            "fps": fps,
            "frame_count": frame_count,
            "width": int(_safe_float(video_properties.get("width"))),
            "height": int(_safe_float(video_properties.get("height"))),
        }

        records.append(record)

    return records


def generate_evidence_metadata(
    video_property_table: pd.DataFrame,
    parameters: Optional[EvidenceSegmentationParameters] = None,
    split_lookup: Optional[Dict[str, str]] = None,
    verbose: bool = True,
) -> pd.DataFrame:
    """
    Generate evidence metadata records for a table of videos.

    Parameters
    ----------
    video_property_table:
        DataFrame containing video properties.

    parameters:
        Optional evidence segmentation parameters.

    split_lookup:
        Optional mapping from video_id to dataset split label.

    verbose:
        Whether to print generation progress and summary information.

    Returns
    -------
    pandas.DataFrame
        Evidence metadata table.
    """

    parameters = parameters or VideoSegmentationParameters()
    split_lookup = split_lookup or {}

    for column_name in DEFAULT_VIDEO_PROPERTY_COLUMNS:
        if column_name not in video_property_table.columns:
            raise ValueError(
                f"Video property table must contain column: {column_name}"
            )

    records: List[Dict[str, object]] = []
    total_count = len(video_property_table)

    _print_if_verbose(
        f"Generating evidence metadata for {total_count} videos...",
        verbose,
    )

    for row_index, row in video_property_table.reset_index(drop=True).iterrows():

        video_properties = row.to_dict()
        video_id = str(video_properties["video_id"])
        split = split_lookup.get(video_id)

        records.extend(
            generate_evidence_records_for_video(
                video_properties=video_properties,
                parameters=parameters,
                split=split,
            )
        )

        if verbose and ((row_index + 1) % 100 == 0 or row_index + 1 == total_count):
            print(f"  Processed {row_index + 1:>6} / {total_count:<6} videos")

    evidence_metadata = pd.DataFrame.from_records(records)

    if verbose:
        print("Evidence metadata generation complete.")
        print(f"Evidence records generated: {len(evidence_metadata)}")

    return evidence_metadata


# ------------------------------------------------------------
# Evidence Summaries
# ------------------------------------------------------------

def summarize_evidence_metadata(
    evidence_metadata: pd.DataFrame,
) -> Dict[str, object]:
    """
    Summarize generated evidence metadata.

    Parameters
    ----------
    evidence_metadata:
        Evidence metadata DataFrame.

    Returns
    -------
    dict
        Evidence summary statistics.
    """

    if evidence_metadata.empty:
        return {
            "evidence_count": 0,
            "video_count": 0,
            "total_duration_sec": 0.0,
        }

    required_columns = ["video_id", "duration_sec"]

    for column_name in required_columns:
        if column_name not in evidence_metadata.columns:
            raise ValueError(
                f"Evidence metadata must contain column: {column_name}"
            )

    return {
        "evidence_count": int(len(evidence_metadata)),
        "video_count": int(evidence_metadata["video_id"].nunique()),
        "total_duration_sec": float(evidence_metadata["duration_sec"].sum()),
        "mean_duration_sec": float(evidence_metadata["duration_sec"].mean()),
        "min_duration_sec": float(evidence_metadata["duration_sec"].min()),
        "max_duration_sec": float(evidence_metadata["duration_sec"].max()),
    }


def build_video_to_split_lookup(
    annotations: pd.DataFrame,
) -> Dict[str, str]:
    """
    Build a video_id to split lookup table from annotation records.

    Parameters
    ----------
    annotations:
        Annotation DataFrame containing ``video_id`` and ``split``.

    Returns
    -------
    dict
        Mapping from video_id to split label.

    Notes
    -----
    If a video appears in more than one split, the first observed split is
    retained. Cross-split validation should be handled separately.
    """

    if "video_id" not in annotations.columns:
        raise ValueError("Annotations DataFrame must contain a video_id column.")

    if "split" not in annotations.columns:
        raise ValueError("Annotations DataFrame must contain a split column.")

    unique_pairs = annotations[["video_id", "split"]].drop_duplicates()

    lookup: Dict[str, str] = {}

    for _, row in unique_pairs.iterrows():
        video_id = str(row["video_id"])
        if video_id not in lookup:
            lookup[video_id] = str(row["split"])

    return lookup
