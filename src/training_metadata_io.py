# ============================================================
# Training Metadata I/O Utilities
# ============================================================
#
# Purpose:
#     Shared training metadata input/output functions used by:
#
#         02_Prepare_Autoencoder_Training_Data
#         03_Train_Video_Autoencoder
#         04_Generate_Autoencoder_Video_Representations
#
# Notes:
#     This module intentionally contains only reusable training metadata
#     save/load, summary export, and manifest logic.
#
#     Segment generation and validation remain in separate modules.
# ============================================================

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional

import pandas as pd


# ------------------------------------------------------------
# Default Training Metadata I/O Configuration
# ------------------------------------------------------------

DEFAULT_TRAINING_METADATA_FILENAME = "training_metadata.csv"
DEFAULT_TRAINING_SUMMARY_FILENAME = "training_data_summary.csv"
DEFAULT_TRAINING_MANIFEST_FILENAME = "training_manifest.json"
DEFAULT_VALIDATION_ISSUES_FILENAME = "training_validation_issues.csv"


# ------------------------------------------------------------
# Helper Functions
# ------------------------------------------------------------

def _as_path(path: str | Path) -> Path:
    """Convert a string or Path-like value to a Path object."""

    return Path(path)


def _format_mb(size_bytes: int) -> str:
    """Format a byte count as megabytes."""

    return f"{size_bytes / (1024 ** 2):.2f} MB"


def _json_default(value: object) -> object:
    """JSON serializer fallback for common non-JSON scalar objects."""

    if isinstance(value, Path):
        return str(value)

    if hasattr(value, "item"):
        return value.item()

    return str(value)


# ------------------------------------------------------------
# Training Metadata Save/Load
# ------------------------------------------------------------

def save_training_metadata(
    training_metadata: pd.DataFrame,
    output_path: str | Path,
    index: bool = False,
    verbose: bool = True,
) -> Dict[str, object]:
    """Save training metadata to a CSV file."""

    output_path = _as_path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    training_metadata.to_csv(output_path, index=index)

    if not output_path.exists():
        raise FileNotFoundError(
            f"Training metadata file was not created: {output_path}"
        )

    file_size_bytes = output_path.stat().st_size

    if verbose:
        print("Training metadata saved.")
        print(f"Output path: {output_path}")
        print(f"Records:     {len(training_metadata)}")
        print(f"File size:   {_format_mb(file_size_bytes)}")

    return {
        "output_path": output_path,
        "record_count": int(len(training_metadata)),
        "file_size_bytes": file_size_bytes,
    }


def load_training_metadata(
    input_path: str | Path,
    required_columns: Optional[Iterable[str]] = None,
    verbose: bool = True,
) -> pd.DataFrame:
    """Load training metadata from a CSV file."""

    input_path = _as_path(input_path)

    if not input_path.exists():
        raise FileNotFoundError(
            f"Training metadata file not found: {input_path}"
        )

    training_metadata = pd.read_csv(input_path)

    if required_columns is not None:
        missing_columns = [
            column_name for column_name in required_columns
            if column_name not in training_metadata.columns
        ]

        if missing_columns:
            raise ValueError(
                "Training metadata file is missing required columns: "
                + ", ".join(missing_columns)
            )

    if verbose:
        print("Training metadata loaded.")
        print(f"Input path: {input_path}")
        print(f"Records:    {len(training_metadata)}")
        print(f"Columns:    {len(training_metadata.columns)}")

    return training_metadata


# ------------------------------------------------------------
# Summary Export
# ------------------------------------------------------------

def build_training_summary_table(
    training_metadata: pd.DataFrame,
) -> pd.DataFrame:
    """Build a compact training metadata summary table."""

    if training_metadata.empty:
        return pd.DataFrame(
            [
                {
                    "group": "all",
                    "segment_count": 0,
                    "video_count": 0,
                    "total_duration_sec": 0.0,
                }
            ]
        )

    group_column = "split" if "split" in training_metadata.columns else None

    if group_column is None:
        grouped_items = [("all", training_metadata)]
    else:
        grouped_items = list(training_metadata.groupby(group_column, dropna=False))

    records: List[Dict[str, object]] = []

    for group_name, group_df in grouped_items:
        record = {
            "group": str(group_name),
            "segment_count": int(len(group_df)),
        }

        if "video_id" in group_df.columns:
            record["video_count"] = int(group_df["video_id"].nunique())

        if "segment_duration_sec" in group_df.columns:
            record["total_duration_sec"] = float(group_df["segment_duration_sec"].sum())
            record["mean_duration_sec"] = float(group_df["segment_duration_sec"].mean())
            record["min_duration_sec"] = float(group_df["segment_duration_sec"].min())
            record["max_duration_sec"] = float(group_df["segment_duration_sec"].max())

        records.append(record)

    return pd.DataFrame.from_records(records)


def save_training_summary(
    training_metadata: pd.DataFrame,
    output_path: str | Path,
    verbose: bool = True,
) -> Dict[str, object]:
    """Save a compact training metadata summary CSV."""

    output_path = _as_path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    summary_table = build_training_summary_table(training_metadata)
    summary_table.to_csv(output_path, index=False)

    if not output_path.exists():
        raise FileNotFoundError(
            f"Training summary file was not created: {output_path}"
        )

    if verbose:
        print("Training metadata summary saved.")
        print(f"Output path: {output_path}")
        print(f"Rows:        {len(summary_table)}")

    return {
        "output_path": output_path,
        "row_count": int(len(summary_table)),
        "summary_table": summary_table,
    }


# ------------------------------------------------------------
# Validation Issue Export
# ------------------------------------------------------------

def save_validation_issues(
    validation_issues: pd.DataFrame,
    output_path: str | Path,
    verbose: bool = True,
) -> Dict[str, object]:
    """Save training metadata validation issues to a CSV file."""

    output_path = _as_path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    validation_issues.to_csv(output_path, index=False)

    if not output_path.exists():
        raise FileNotFoundError(
            f"Validation issue file was not created: {output_path}"
        )

    if verbose:
        print("Training metadata validation issues saved.")
        print(f"Output path: {output_path}")
        print(f"Rows:        {len(validation_issues)}")

    return {
        "output_path": output_path,
        "row_count": int(len(validation_issues)),
    }


# ------------------------------------------------------------
# Manifest Export
# ------------------------------------------------------------

def build_training_manifest(
    training_metadata_path: str | Path,
    training_summary_path: Optional[str | Path] = None,
    validation_issues_path: Optional[str | Path] = None,
    metadata: Optional[Dict[str, object]] = None,
) -> Dict[str, object]:
    """Build a JSON-serializable manifest for training metadata outputs."""

    training_metadata_path = _as_path(training_metadata_path)

    manifest: Dict[str, object] = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "training_metadata_path": str(training_metadata_path),
        "training_metadata_exists": training_metadata_path.exists(),
    }

    if training_metadata_path.exists():
        manifest["training_metadata_size_bytes"] = training_metadata_path.stat().st_size

    if training_summary_path is not None:
        summary_path = _as_path(training_summary_path)
        manifest["training_summary_path"] = str(summary_path)
        manifest["training_summary_exists"] = summary_path.exists()

    if validation_issues_path is not None:
        issues_path = _as_path(validation_issues_path)
        manifest["validation_issues_path"] = str(issues_path)
        manifest["validation_issues_exists"] = issues_path.exists()

    if metadata:
        manifest["metadata"] = metadata

    return manifest


def save_training_manifest(
    manifest: Dict[str, object],
    output_path: str | Path,
    verbose: bool = True,
) -> Dict[str, object]:
    """Save a training metadata output manifest to JSON."""

    output_path = _as_path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as output_file:
        json.dump(manifest, output_file, indent=2, default=_json_default)

    if not output_path.exists():
        raise FileNotFoundError(
            f"Training manifest file was not created: {output_path}"
        )

    file_size_bytes = output_path.stat().st_size

    if verbose:
        print("Training metadata manifest saved.")
        print(f"Output path: {output_path}")
        print(f"File size:   {_format_mb(file_size_bytes)}")

    return {
        "output_path": output_path,
        "file_size_bytes": file_size_bytes,
    }


# ------------------------------------------------------------
# Convenience Wrapper
# ------------------------------------------------------------

def save_training_outputs(
    training_metadata: pd.DataFrame,
    output_dir: str | Path,
    validation_issues: Optional[pd.DataFrame] = None,
    metadata: Optional[Dict[str, object]] = None,
    training_metadata_filename: str = DEFAULT_TRAINING_METADATA_FILENAME,
    training_summary_filename: str = DEFAULT_TRAINING_SUMMARY_FILENAME,
    training_manifest_filename: str = DEFAULT_TRAINING_MANIFEST_FILENAME,
    validation_issues_filename: str = DEFAULT_VALIDATION_ISSUES_FILENAME,
    verbose: bool = True,
) -> Dict[str, object]:
    """Save standard training metadata outputs to an output directory."""

    output_dir = _as_path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    training_metadata_path = output_dir / training_metadata_filename
    training_summary_path = output_dir / training_summary_filename
    training_manifest_path = output_dir / training_manifest_filename
    validation_issues_path = output_dir / validation_issues_filename

    metadata_save_summary = save_training_metadata(
        training_metadata=training_metadata,
        output_path=training_metadata_path,
        verbose=verbose,
    )

    summary_save_summary = save_training_summary(
        training_metadata=training_metadata,
        output_path=training_summary_path,
        verbose=verbose,
    )

    validation_save_summary = None

    if validation_issues is not None:
        validation_save_summary = save_validation_issues(
            validation_issues=validation_issues,
            output_path=validation_issues_path,
            verbose=verbose,
        )

    manifest = build_training_manifest(
        training_metadata_path=training_metadata_path,
        training_summary_path=training_summary_path,
        validation_issues_path=(
            validation_issues_path if validation_issues is not None else None
        ),
        metadata=metadata,
    )

    manifest_save_summary = save_training_manifest(
        manifest=manifest,
        output_path=training_manifest_path,
        verbose=verbose,
    )

    return {
        "output_dir": output_dir,
        "training_metadata_path": training_metadata_path,
        "training_summary_path": training_summary_path,
        "training_manifest_path": training_manifest_path,
        "validation_issues_path": (
            validation_issues_path if validation_issues is not None else None
        ),
        "metadata_save_summary": metadata_save_summary,
        "summary_save_summary": summary_save_summary,
        "validation_save_summary": validation_save_summary,
        "manifest_save_summary": manifest_save_summary,
    }
