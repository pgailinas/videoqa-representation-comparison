# ============================================================
# Evidence Metadata Validation Utilities
# ============================================================
#
# Purpose:
#     Shared evidence metadata validation functions used by:
#
#         02_Prepare_Video_Evidence
#         03_Build_Video_Knowledge_Base
#         05_Run_RAG_VideoQA
#         06_Run_Iterative_RAG_Experiments
#         07_Evaluate_and_Visualize_Results
#         08_Interactive_Demo
#
# Notes:
#     This module intentionally contains only reusable schema,
#     consistency, timestamp, relationship, and video-reference
#     validation logic.
#
#     Evidence generation and evidence file I/O remain in separate
#     modules.
# ============================================================

from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence

import pandas as pd


# ------------------------------------------------------------
# Default Evidence Schema
# ------------------------------------------------------------

DEFAULT_REQUIRED_EVIDENCE_COLUMNS: Sequence[str] = (
    "evidence_id",
    "video_id",
    "video_path",
    "evidence_level",
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

DEFAULT_OPTIONAL_EVIDENCE_COLUMNS: Sequence[str] = (
    "split",
    "parent_evidence_id",
    "width",
    "height",
    "motion_score",
    "scene_change_score",
    "sampling_notes",
    "created_by_notebook",
)

DEFAULT_NUMERIC_EVIDENCE_COLUMNS: Sequence[str] = (
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


def _print_if_verbose(message: str, verbose: bool = True) -> None:
    """Print a message only when verbose output is enabled."""

    if verbose:
        print(message)


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

def validate_evidence_schema(
    evidence_metadata: pd.DataFrame,
    required_columns: Sequence[str] = DEFAULT_REQUIRED_EVIDENCE_COLUMNS,
    numeric_columns: Sequence[str] = DEFAULT_NUMERIC_EVIDENCE_COLUMNS,
) -> List[Dict[str, object]]:
    """
    Validate evidence metadata schema requirements.

    Parameters
    ----------
    evidence_metadata:
        Evidence metadata DataFrame to validate.

    required_columns:
        Columns that must be present.

    numeric_columns:
        Columns expected to contain numeric values when present.

    Returns
    -------
    list of dict
        Validation issues. Empty list indicates success.
    """

    issues: List[Dict[str, object]] = []

    missing_columns = [
        column_name for column_name in required_columns
        if column_name not in evidence_metadata.columns
    ]

    if missing_columns:
        _append_issue(
            issues=issues,
            severity="error",
            check_name="required_columns",
            message="Missing required evidence metadata columns: "
            + ", ".join(missing_columns),
            count=len(missing_columns),
        )

    for column_name in numeric_columns:

        if column_name not in evidence_metadata.columns:
            continue

        numeric_values = pd.to_numeric(
            evidence_metadata[column_name],
            errors="coerce",
        )

        invalid_count = int(
            numeric_values.isna().sum()
            - evidence_metadata[column_name].isna().sum()
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

def validate_required_evidence_values(
    evidence_metadata: pd.DataFrame,
    required_columns: Sequence[str] = DEFAULT_REQUIRED_EVIDENCE_COLUMNS,
) -> List[Dict[str, object]]:
    """
    Validate that required evidence fields are populated.

    Parameters
    ----------
    evidence_metadata:
        Evidence metadata DataFrame to validate.

    required_columns:
        Columns that must contain non-null values.

    Returns
    -------
    list of dict
        Validation issues. Empty list indicates success.
    """

    issues: List[Dict[str, object]] = []

    for column_name in required_columns:

        if column_name not in evidence_metadata.columns:
            continue

        missing_count = int(evidence_metadata[column_name].isna().sum())

        if missing_count > 0:
            _append_issue(
                issues=issues,
                severity="error",
                check_name="required_values",
                message=f"Required evidence field contains missing values: {column_name}",
                count=missing_count,
            )

    return issues


def validate_unique_evidence_ids(
    evidence_metadata: pd.DataFrame,
    evidence_id_column: str = "evidence_id",
) -> List[Dict[str, object]]:
    """
    Validate that evidence identifiers are unique.

    Parameters
    ----------
    evidence_metadata:
        Evidence metadata DataFrame to validate.

    evidence_id_column:
        Column containing evidence identifiers.

    Returns
    -------
    list of dict
        Validation issues. Empty list indicates success.
    """

    issues: List[Dict[str, object]] = []

    if evidence_id_column not in evidence_metadata.columns:
        return issues

    duplicate_count = int(
        evidence_metadata[evidence_id_column].duplicated().sum()
    )

    if duplicate_count > 0:
        _append_issue(
            issues=issues,
            severity="error",
            check_name="unique_evidence_ids",
            message="Duplicate evidence identifiers detected.",
            count=duplicate_count,
        )

    return issues


# ------------------------------------------------------------
# Timestamp and Frame Validation
# ------------------------------------------------------------

def validate_evidence_timestamps(
    evidence_metadata: pd.DataFrame,
) -> List[Dict[str, object]]:
    """
    Validate evidence timestamp ordering and duration consistency.

    Parameters
    ----------
    evidence_metadata:
        Evidence metadata DataFrame to validate.

    Returns
    -------
    list of dict
        Validation issues. Empty list indicates success.
    """

    issues: List[Dict[str, object]] = []

    required_columns = [
        "start_time_sec",
        "midpoint_time_sec",
        "end_time_sec",
        "segment_duration_sec",
    ]

    if any(column_name not in evidence_metadata.columns for column_name in required_columns):
        return issues

    start_time = pd.to_numeric(
        evidence_metadata["start_time_sec"],
        errors="coerce",
    )
    midpoint_time = pd.to_numeric(
        evidence_metadata["midpoint_time_sec"],
        errors="coerce",
    )
    end_time = pd.to_numeric(
        evidence_metadata["end_time_sec"],
        errors="coerce",
    )
    duration = pd.to_numeric(
        evidence_metadata["segment_duration_sec"],
        errors="coerce",
    )

    negative_start_count = int((start_time < 0).sum())

    if negative_start_count > 0:
        _append_issue(
            issues=issues,
            severity="error",
            check_name="timestamp_ranges",
            message="Evidence start times must be non-negative.",
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
            message="Invalid timestamp ordering detected.",
            count=invalid_order_count,
        )

    invalid_duration_count = int((duration <= 0).sum())

    if invalid_duration_count > 0:
        _append_issue(
            issues=issues,
            severity="error",
            check_name="duration_positive",
            message="Evidence durations must be positive.",
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
            message="Evidence duration does not match end-start time within tolerance.",
            count=duration_mismatch_count,
        )

    return issues


def validate_evidence_frame_indices(
    evidence_metadata: pd.DataFrame,
) -> List[Dict[str, object]]:
    """
    Validate evidence frame index ordering and bounds.

    Parameters
    ----------
    evidence_metadata:
        Evidence metadata DataFrame to validate.

    Returns
    -------
    list of dict
        Validation issues. Empty list indicates success.
    """

    issues: List[Dict[str, object]] = []

    required_columns = [
        "start_frame_idx",
        "midpoint_frame_idx",
        "end_frame_idx",
        "representative_frame_index",
        "frame_count",
    ]

    if any(column_name not in evidence_metadata.columns for column_name in required_columns):
        return issues

    start_frame = pd.to_numeric(
        evidence_metadata["start_frame_idx"],
        errors="coerce",
    )
    midpoint_frame = pd.to_numeric(
        evidence_metadata["midpoint_frame_idx"],
        errors="coerce",
    )
    end_frame = pd.to_numeric(
        evidence_metadata["end_frame_idx"],
        errors="coerce",
    )
    representative_frame = pd.to_numeric(
        evidence_metadata["representative_frame_index"],
        errors="coerce",
    )
    frame_count = pd.to_numeric(
        evidence_metadata["frame_count"],
        errors="coerce",
    )

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
            message="Evidence frame indices must be non-negative.",
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
            message="Invalid frame index ordering detected.",
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
            message=(
                "Representative frame index must fall within "
                "segment frame bounds."
            ),
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
            message="Evidence end frame index is outside frame_count bounds.",
            count=out_of_bounds_count,
        )

    return issues




# ------------------------------------------------------------
# Metric Validation
# ------------------------------------------------------------

def validate_evidence_metric_ranges(
    evidence_metadata: pd.DataFrame,
) -> List[Dict[str, object]]:
    """
    Validate optional normalized evidence metric ranges.

    Parameters
    ----------
    evidence_metadata:
        Evidence metadata DataFrame to validate.

    Returns
    -------
    list of dict
        Validation issues. Empty list indicates success.
    """

    issues: List[Dict[str, object]] = []

    metric_columns = [
        "motion_score",
        "scene_change_score",
    ]

    for column_name in metric_columns:

        if column_name not in evidence_metadata.columns:
            continue

        metric_values = pd.to_numeric(
            evidence_metadata[column_name],
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
                message=(
                    f"{column_name} values should be between "
                    "0.0 and 1.0."
                ),
                count=invalid_count,
            )

    return issues


# ------------------------------------------------------------
# Relationship and Reference Validation
# ------------------------------------------------------------

def validate_parent_evidence_relationships(
    evidence_metadata: pd.DataFrame,
    evidence_id_column: str = "evidence_id",
    parent_id_column: str = "parent_evidence_id",
) -> List[Dict[str, object]]:
    """
    Validate optional parent evidence relationships.

    Parameters
    ----------
    evidence_metadata:
        Evidence metadata DataFrame to validate.

    evidence_id_column:
        Column containing evidence identifiers.

    parent_id_column:
        Column containing optional parent evidence identifiers.

    Returns
    -------
    list of dict
        Validation issues. Empty list indicates success.
    """

    issues: List[Dict[str, object]] = []

    if parent_id_column not in evidence_metadata.columns:
        return issues

    if evidence_id_column not in evidence_metadata.columns:
        return issues

    parent_values = evidence_metadata[parent_id_column].dropna()

    if parent_values.empty:
        return issues

    self_parent_count = int(
        (
            evidence_metadata[evidence_id_column].astype(str)
            == evidence_metadata[parent_id_column].astype(str)
        ).sum()
    )

    if self_parent_count > 0:
        _append_issue(
            issues=issues,
            severity="error",
            check_name="parent_relationships",
            message="Evidence records cannot reference themselves as parents.",
            count=self_parent_count,
        )

    return issues


def validate_evidence_video_paths(
    evidence_metadata: pd.DataFrame,
    video_path_column: str = "video_path",
    check_exists: bool = True,
) -> List[Dict[str, object]]:
    """
    Validate evidence source video path references.

    Parameters
    ----------
    evidence_metadata:
        Evidence metadata DataFrame to validate.

    video_path_column:
        Column containing source video paths.

    check_exists:
        Whether to verify that referenced video paths exist locally.

    Returns
    -------
    list of dict
        Validation issues. Empty list indicates success.
    """

    issues: List[Dict[str, object]] = []

    if video_path_column not in evidence_metadata.columns:
        return issues

    missing_path_count = int(evidence_metadata[video_path_column].isna().sum())

    if missing_path_count > 0:
        _append_issue(
            issues=issues,
            severity="error",
            check_name="video_path_values",
            message="Evidence records contain missing source video paths.",
            count=missing_path_count,
        )

    if not check_exists:
        return issues

    unique_paths = evidence_metadata[video_path_column].dropna().unique()
    missing_files = [
        str(path_value) for path_value in unique_paths
        if not _as_path(path_value).exists()
    ]

    if missing_files:
        _append_issue(
            issues=issues,
            severity="error",
            check_name="video_path_exists",
            message="Evidence records reference source video files that do not exist.",
            count=len(missing_files),
        )

    return issues


# ------------------------------------------------------------
# Validation Orchestration
# ------------------------------------------------------------

def validate_evidence_metadata(
    evidence_metadata: pd.DataFrame,
    required_columns: Sequence[str] = DEFAULT_REQUIRED_EVIDENCE_COLUMNS,
    numeric_columns: Sequence[str] = DEFAULT_NUMERIC_EVIDENCE_COLUMNS,
    check_video_paths_exist: bool = True,
    verbose: bool = True,
) -> Dict[str, object]:
    """
    Run standard validation checks on an evidence metadata table.

    Parameters
    ----------
    evidence_metadata:
        Evidence metadata DataFrame to validate.

    required_columns:
        Columns that must be present and populated.

    numeric_columns:
        Columns expected to contain numeric values.

    check_video_paths_exist:
        Whether to verify that referenced source video files exist.

    verbose:
        Whether to print validation summary information.

    Returns
    -------
    dict
        Validation summary containing issues, counts, and pass/fail status.
    """

    issues: List[Dict[str, object]] = []

    issues.extend(
        validate_evidence_schema(
            evidence_metadata=evidence_metadata,
            required_columns=required_columns,
            numeric_columns=numeric_columns,
        )
    )

    issues.extend(
        validate_required_evidence_values(
            evidence_metadata=evidence_metadata,
            required_columns=required_columns,
        )
    )

    issues.extend(validate_unique_evidence_ids(evidence_metadata))
    issues.extend(validate_evidence_timestamps(evidence_metadata))
    issues.extend(validate_evidence_frame_indices(evidence_metadata))
    issues.extend(validate_evidence_metric_ranges(evidence_metadata))
    issues.extend(validate_parent_evidence_relationships(evidence_metadata))
    issues.extend(
        validate_evidence_video_paths(
            evidence_metadata=evidence_metadata,
            check_exists=check_video_paths_exist,
        )
    )

    error_count = sum(1 for issue in issues if issue["severity"] == "error")
    warning_count = sum(1 for issue in issues if issue["severity"] == "warning")
    passed = error_count == 0

    if verbose:

        print("Evidence metadata validation complete.")
        print(f"Evidence records: {len(evidence_metadata)}")
        print(f"Errors:           {error_count}")
        print(f"Warnings:         {warning_count}")
        print(f"Passed:           {passed}")

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
        "record_count": int(len(evidence_metadata)),
    }


def validation_issues_to_dataframe(
    validation_summary: Dict[str, object],
) -> pd.DataFrame:
    """
    Convert a validation summary issue list to a DataFrame.

    Parameters
    ----------
    validation_summary:
        Validation summary returned by ``validate_evidence_metadata``.

    Returns
    -------
    pandas.DataFrame
        Validation issue table.
    """

    issues = validation_summary.get("issues", [])
    return pd.DataFrame.from_records(issues)
