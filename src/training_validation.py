# ============================================================
# Training Metadata Validation Utilities
# ============================================================
#
# Purpose:
#     Shared training metadata validation functions used by:
#
#         02_Prepare_Autoencoder_Training_Data
#         03_Train_Video_Autoencoder
#         04_Generate_Autoencoder_Video_Representations
#
# Notes:
#     This module intentionally contains reusable schema, consistency,
#     timestamp, relationship, and video-reference validation logic.
#
#     Segment generation and training metadata I/O remain in separate
#     modules.
# ============================================================

from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional, Sequence

import pandas as pd


# ------------------------------------------------------------
# Default Training Metadata Schema
# ------------------------------------------------------------

DEFAULT_REQUIRED_TRAINING_METADATA_COLUMNS: Sequence[str] = (
    "segment_id",
    "video_id",
    "video_path",
    "segment_level",
    "segment_strategy",
    "segment_index",
    "start_time_sec",
    "midpoint_time_sec",
    "end_time_sec",
    "segment_duration_sec",
    "start_frame_idx",
    "midpoint_frame_idx",
    "end_frame_idx",
    "representative_frame_index",
    "fps",
    "frame_count",
)

DEFAULT_OPTIONAL_TRAINING_METADATA_COLUMNS: Sequence[str] = (
    "split",
    "parent_segment_id",
    "width",
    "height",
    "motion_score",
    "scene_change_score",
    "sampling_notes",
    "created_by_notebook",
)

DEFAULT_NUMERIC_TRAINING_METADATA_COLUMNS: Sequence[str] = (
    "segment_index",
    "segment_level",
    "start_time_sec",
    "midpoint_time_sec",
    "end_time_sec",
    "segment_duration_sec",
    "start_frame_idx",
    "midpoint_frame_idx",
    "end_frame_idx",
    "representative_frame_index",
    "fps",
    "frame_count",
    "width",
    "height",
    "motion_score",
    "scene_change_score",
)


# ------------------------------------------------------------
# Helper Functions
# ------------------------------------------------------------

def _as_path(path: str | Path) -> Path:
    """Convert a string or Path-like value to a Path object."""

    return Path(path)


def _append_issue(
    issues: List[Dict[str, object]],
    severity: str,
    check_name: str,
    message: str,
    count: Optional[int] = None,
) -> None:
    """Append a validation issue to the issue list."""

    issues.append(
        {
            "severity": severity,
            "check": check_name,
            "message": message,
            "count": count,
        }
    )


# ------------------------------------------------------------
# Schema Validation
# ------------------------------------------------------------

def validate_training_metadata_schema(
    training_metadata: pd.DataFrame,
    required_columns: Sequence[str] = DEFAULT_REQUIRED_TRAINING_METADATA_COLUMNS,
    numeric_columns: Sequence[str] = DEFAULT_NUMERIC_TRAINING_METADATA_COLUMNS,
) -> List[Dict[str, object]]:
    """Validate training metadata schema requirements."""

    issues: List[Dict[str, object]] = []

    missing_columns = [
        column_name for column_name in required_columns
        if column_name not in training_metadata.columns
    ]

    if missing_columns:
        _append_issue(
            issues=issues,
            severity="error",
            check_name="required_columns",
            message="Missing required training metadata columns: "
            + ", ".join(missing_columns),
            count=len(missing_columns),
        )

    for column_name in numeric_columns:

        if column_name not in training_metadata.columns:
            continue

        numeric_values = pd.to_numeric(
            training_metadata[column_name],
            errors="coerce",
        )

        invalid_count = int(
            numeric_values.isna().sum()
            - training_metadata[column_name].isna().sum()
        )

        if invalid_count > 0:
            _append_issue(
                issues=issues,
                severity="error",
                check_name="numeric_columns",
                message=f"Column contains non-numeric values: {column_name}",
                count=invalid_count,
            )

    return issues


# ------------------------------------------------------------
# Field Validation
# ------------------------------------------------------------

def validate_required_training_metadata_values(
    training_metadata: pd.DataFrame,
    required_columns: Sequence[str] = DEFAULT_REQUIRED_TRAINING_METADATA_COLUMNS,
) -> List[Dict[str, object]]:
    """Validate that required training metadata fields are populated."""

    issues: List[Dict[str, object]] = []

    for column_name in required_columns:

        if column_name not in training_metadata.columns:
            continue

        missing_count = int(training_metadata[column_name].isna().sum())

        if missing_count > 0:
            _append_issue(
                issues=issues,
                severity="error",
                check_name="required_values",
                message=f"Required training metadata field contains missing values: {column_name}",
                count=missing_count,
            )

    return issues


def validate_unique_segment_ids(
    training_metadata: pd.DataFrame,
    segment_id_column: str = "segment_id",
) -> List[Dict[str, object]]:
    """Validate that segment identifiers are unique."""

    issues: List[Dict[str, object]] = []

    if segment_id_column not in training_metadata.columns:
        return issues

    duplicate_count = int(
        training_metadata[segment_id_column].duplicated().sum()
    )

    if duplicate_count > 0:
        _append_issue(
            issues=issues,
            severity="error",
            check_name="unique_segment_ids",
            message="Duplicate segment identifiers detected.",
            count=duplicate_count,
        )

    return issues


# ------------------------------------------------------------
# Timestamp and Frame Validation
# ------------------------------------------------------------

def validate_segment_timestamps(
    training_metadata: pd.DataFrame,
) -> List[Dict[str, object]]:
    """Validate segment timestamp ordering and duration consistency."""

    issues: List[Dict[str, object]] = []

    required_columns = [
        "start_time_sec",
        "midpoint_time_sec",
        "end_time_sec",
        "segment_duration_sec",
    ]

    if any(column_name not in training_metadata.columns for column_name in required_columns):
        return issues

    start_time = pd.to_numeric(training_metadata["start_time_sec"], errors="coerce")
    midpoint_time = pd.to_numeric(training_metadata["midpoint_time_sec"], errors="coerce")
    end_time = pd.to_numeric(training_metadata["end_time_sec"], errors="coerce")
    duration = pd.to_numeric(training_metadata["segment_duration_sec"], errors="coerce")

    negative_start_count = int((start_time < 0).sum())

    if negative_start_count > 0:
        _append_issue(
            issues=issues,
            severity="error",
            check_name="timestamp_ranges",
            message="Segment start times must be non-negative.",
            count=negative_start_count,
        )

    invalid_order_count = int(
        ((start_time > midpoint_time) | (midpoint_time > end_time)).sum()
    )

    if invalid_order_count > 0:
        _append_issue(
            issues=issues,
            severity="error",
            check_name="timestamp_order",
            message="Invalid segment timestamp ordering detected.",
            count=invalid_order_count,
        )

    invalid_duration_count = int((duration <= 0).sum())

    if invalid_duration_count > 0:
        _append_issue(
            issues=issues,
            severity="error",
            check_name="duration_positive",
            message="Segment durations must be positive.",
            count=invalid_duration_count,
        )

    duration_mismatch_count = int(
        ((end_time - start_time - duration).abs() > 0.01).sum()
    )

    if duration_mismatch_count > 0:
        _append_issue(
            issues=issues,
            severity="warning",
            check_name="duration_consistency",
            message="Segment duration does not match end-start time within tolerance.",
            count=duration_mismatch_count,
        )

    return issues


def validate_segment_frame_indices(
    training_metadata: pd.DataFrame,
) -> List[Dict[str, object]]:
    """Validate segment frame index ordering and bounds."""

    issues: List[Dict[str, object]] = []

    required_columns = [
        "start_frame_idx",
        "midpoint_frame_idx",
        "end_frame_idx",
        "representative_frame_index",
        "frame_count",
    ]

    if any(column_name not in training_metadata.columns for column_name in required_columns):
        return issues

    start_frame = pd.to_numeric(training_metadata["start_frame_idx"], errors="coerce")
    midpoint_frame = pd.to_numeric(training_metadata["midpoint_frame_idx"], errors="coerce")
    end_frame = pd.to_numeric(training_metadata["end_frame_idx"], errors="coerce")
    representative_frame = pd.to_numeric(training_metadata["representative_frame_index"], errors="coerce")
    frame_count = pd.to_numeric(training_metadata["frame_count"], errors="coerce")

    negative_frame_count = int(
        (
            (start_frame < 0)
            | (midpoint_frame < 0)
            | (end_frame < 0)
            | (representative_frame < 0)
        ).sum()
    )

    if negative_frame_count > 0:
        _append_issue(
            issues=issues,
            severity="error",
            check_name="frame_index_ranges",
            message="Segment frame indices must be non-negative.",
            count=negative_frame_count,
        )

    invalid_order_count = int(
        ((start_frame > midpoint_frame) | (midpoint_frame > end_frame)).sum()
    )

    if invalid_order_count > 0:
        _append_issue(
            issues=issues,
            severity="error",
            check_name="frame_index_order",
            message="Invalid segment frame index ordering detected.",
            count=invalid_order_count,
        )

    invalid_representative_count = int(
        (
            (representative_frame < start_frame)
            | (representative_frame > end_frame)
        ).sum()
    )

    if invalid_representative_count > 0:
        _append_issue(
            issues=issues,
            severity="error",
            check_name="representative_frame_index",
            message="Representative frame index must fall within segment frame bounds.",
            count=invalid_representative_count,
        )

    out_of_bounds_count = int(
        (
            (end_frame >= frame_count)
            | (representative_frame >= frame_count)
        ).sum()
    )

    if out_of_bounds_count > 0:
        _append_issue(
            issues=issues,
            severity="warning",
            check_name="frame_index_bounds",
            message="Segment end frame index is outside frame_count bounds.",
            count=out_of_bounds_count,
        )

    return issues


# ------------------------------------------------------------
# Metric Validation
# ------------------------------------------------------------

def validate_segment_metric_ranges(
    training_metadata: pd.DataFrame,
) -> List[Dict[str, object]]:
    """Validate optional normalized segment metric ranges."""

    issues: List[Dict[str, object]] = []

    metric_columns = [
        "motion_score",
        "scene_change_score",
    ]

    for column_name in metric_columns:

        if column_name not in training_metadata.columns:
            continue

        metric_values = pd.to_numeric(
            training_metadata[column_name],
            errors="coerce",
        )

        invalid_count = int(
            (
                (metric_values < 0.0)
                | (metric_values > 1.0)
            ).sum()
        )

        if invalid_count > 0:
            _append_issue(
                issues=issues,
                severity="warning",
                check_name=f"{column_name}_range",
                message=f"{column_name} values should be between 0.0 and 1.0.",
                count=invalid_count,
            )

    return issues


# ------------------------------------------------------------
# Relationship and Reference Validation
# ------------------------------------------------------------

def validate_parent_segment_relationships(
    training_metadata: pd.DataFrame,
    segment_id_column: str = "segment_id",
    parent_id_column: str = "parent_segment_id",
) -> List[Dict[str, object]]:
    """Validate optional parent segment relationships."""

    issues: List[Dict[str, object]] = []

    if parent_id_column not in training_metadata.columns:
        return issues

    if segment_id_column not in training_metadata.columns:
        return issues

    parent_values = training_metadata[parent_id_column].dropna()

    if parent_values.empty:
        return issues

    self_parent_count = int(
        (
            training_metadata[segment_id_column].astype(str)
            == training_metadata[parent_id_column].astype(str)
        ).sum()
    )

    if self_parent_count > 0:
        _append_issue(
            issues=issues,
            severity="error",
            check_name="parent_relationships",
            message="Segment records cannot reference themselves as parents.",
            count=self_parent_count,
        )

    return issues


def validate_training_video_paths(
    training_metadata: pd.DataFrame,
    video_path_column: str = "video_path",
    check_exists: bool = True,
) -> List[Dict[str, object]]:
    """Validate source video path references."""

    issues: List[Dict[str, object]] = []

    if video_path_column not in training_metadata.columns:
        return issues

    missing_path_count = int(training_metadata[video_path_column].isna().sum())

    if missing_path_count > 0:
        _append_issue(
            issues=issues,
            severity="error",
            check_name="video_path_values",
            message="Segment records contain missing source video paths.",
            count=missing_path_count,
        )

    if not check_exists:
        return issues

    unique_paths = training_metadata[video_path_column].dropna().unique()
    missing_files = [
        str(path_value) for path_value in unique_paths
        if not _as_path(path_value).exists()
    ]

    if missing_files:
        _append_issue(
            issues=issues,
            severity="error",
            check_name="video_path_exists",
            message="Segment records reference source video files that do not exist.",
            count=len(missing_files),
        )

    return issues


# ------------------------------------------------------------
# Validation Orchestration
# ------------------------------------------------------------

def validate_training_metadata(
    training_metadata: pd.DataFrame,
    required_columns: Sequence[str] = DEFAULT_REQUIRED_TRAINING_METADATA_COLUMNS,
    numeric_columns: Sequence[str] = DEFAULT_NUMERIC_TRAINING_METADATA_COLUMNS,
    check_video_paths_exist: bool = True,
    verbose: bool = True,
) -> Dict[str, object]:
    """Run standard validation checks on a training metadata table."""

    issues: List[Dict[str, object]] = []

    issues.extend(
        validate_training_metadata_schema(
            training_metadata=training_metadata,
            required_columns=required_columns,
            numeric_columns=numeric_columns,
        )
    )

    issues.extend(
        validate_required_training_metadata_values(
            training_metadata=training_metadata,
            required_columns=required_columns,
        )
    )

    issues.extend(validate_unique_segment_ids(training_metadata))
    issues.extend(validate_segment_timestamps(training_metadata))
    issues.extend(validate_segment_frame_indices(training_metadata))
    issues.extend(validate_segment_metric_ranges(training_metadata))
    issues.extend(validate_parent_segment_relationships(training_metadata))
    issues.extend(
        validate_training_video_paths(
            training_metadata=training_metadata,
            check_exists=check_video_paths_exist,
        )
    )

    error_count = sum(1 for issue in issues if issue["severity"] == "error")
    warning_count = sum(1 for issue in issues if issue["severity"] == "warning")
    passed = error_count == 0

    if verbose:

        print("Training metadata validation complete.")
        print(f"Segment records: {len(training_metadata)}")
        print(f"Errors:          {error_count}")
        print(f"Warnings:        {warning_count}")
        print(f"Passed:          {passed}")

        if issues:
            print("\nValidation Issues:")
            for issue in issues:
                count_text = (
                    f" ({issue['count']})"
                    if issue.get("count") is not None
                    else ""
                )
                print(
                    f"  [{issue['severity'].upper()}] "
                    f"{issue['check']}: {issue['message']}{count_text}"
                )

    return {
        "passed": passed,
        "error_count": error_count,
        "warning_count": warning_count,
        "issues": issues,
        "record_count": int(len(training_metadata)),
    }


def validation_issues_to_dataframe(
    validation_summary: Dict[str, object],
) -> pd.DataFrame:
    """Convert a validation summary issue list to a DataFrame."""

    issues = validation_summary.get("issues", [])
    return pd.DataFrame.from_records(issues)
