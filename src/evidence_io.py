# ============================================================
# Evidence Metadata I/O Utilities
# ============================================================
#
# Purpose:
#     Shared evidence metadata input/output functions used by:
#
#         02_Prepare_Video_Evidence
#         03_Build_Video_Knowledge_Base
#         05_Run_RAG_VideoQA
#         06_Run_Iterative_RAG_Experiments
#         07_Evaluate_and_Visualize_Results
#         08_Interactive_Demo
#
# Notes:
#     This module intentionally contains only reusable evidence
#     metadata save/load, summary export, and manifest logic.
#
#     Evidence generation and validation remain in separate modules.
# ============================================================

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional

import pandas as pd


# ------------------------------------------------------------
# Default Evidence I/O Configuration
# ------------------------------------------------------------

DEFAULT_EVIDENCE_METADATA_FILENAME = "evidence_metadata.csv"
DEFAULT_EVIDENCE_SUMMARY_FILENAME = "evidence_summary.csv"
DEFAULT_EVIDENCE_MANIFEST_FILENAME = "evidence_manifest.json"
DEFAULT_VALIDATION_ISSUES_FILENAME = "evidence_validation_issues.csv"


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
# Evidence Metadata Save/Load
# ------------------------------------------------------------

def save_evidence_metadata(
    evidence_metadata: pd.DataFrame,
    output_path: str | Path,
    index: bool = False,
    verbose: bool = True,
) -> Dict[str, object]:
    """
    Save evidence metadata to a CSV file.

    Parameters
    ----------
    evidence_metadata:
        Evidence metadata DataFrame to save.

    output_path:
        Destination CSV path.

    index:
        Whether to write the DataFrame index.

    verbose:
        Whether to print save summary information.

    Returns
    -------
    dict
        Save summary containing output path, record count, and file size.
    """

    output_path = _as_path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    evidence_metadata.to_csv(
        output_path,
        index=index,
    )

    if not output_path.exists():
        raise FileNotFoundError(
            f"Evidence metadata file was not created: {output_path}"
        )

    file_size_bytes = output_path.stat().st_size

    if verbose:

        print("Evidence metadata saved.")
        print(f"Output path: {output_path}")
        print(f"Records:     {len(evidence_metadata)}")
        print(f"File size:   {_format_mb(file_size_bytes)}")

    return {
        "output_path": output_path,
        "record_count": int(len(evidence_metadata)),
        "file_size_bytes": file_size_bytes,
    }


def load_evidence_metadata(
    input_path: str | Path,
    required_columns: Optional[Iterable[str]] = None,
    verbose: bool = True,
) -> pd.DataFrame:
    """
    Load evidence metadata from a CSV file.

    Parameters
    ----------
    input_path:
        Source CSV path.

    required_columns:
        Optional iterable of required column names.

    verbose:
        Whether to print load summary information.

    Returns
    -------
    pandas.DataFrame
        Loaded evidence metadata DataFrame.
    """

    input_path = _as_path(input_path)

    if not input_path.exists():
        raise FileNotFoundError(
            f"Evidence metadata file not found: {input_path}"
        )

    evidence_metadata = pd.read_csv(input_path)

    if required_columns is not None:

        missing_columns = [
            column_name for column_name in required_columns
            if column_name not in evidence_metadata.columns
        ]

        if missing_columns:
            raise ValueError(
                "Evidence metadata file is missing required columns: "
                + ", ".join(missing_columns)
            )

    if verbose:

        print("Evidence metadata loaded.")
        print(f"Input path: {input_path}")
        print(f"Records:    {len(evidence_metadata)}")
        print(f"Columns:    {len(evidence_metadata.columns)}")

    return evidence_metadata


# ------------------------------------------------------------
# Summary Export
# ------------------------------------------------------------

def build_evidence_summary_table(
    evidence_metadata: pd.DataFrame,
) -> pd.DataFrame:
    """
    Build a compact evidence summary table.

    Parameters
    ----------
    evidence_metadata:
        Evidence metadata DataFrame.

    Returns
    -------
    pandas.DataFrame
        Summary table grouped by split when available, otherwise a
        single all-records summary.
    """

    if evidence_metadata.empty:
        return pd.DataFrame(
            [
                {
                    "group": "all",
                    "evidence_count": 0,
                    "video_count": 0,
                    "total_duration_sec": 0.0,
                }
            ]
        )

    group_column = "split" if "split" in evidence_metadata.columns else None

    if group_column is None:
        grouped_items = [("all", evidence_metadata)]
    else:
        grouped_items = list(evidence_metadata.groupby(group_column, dropna=False))

    records: List[Dict[str, object]] = []

    for group_name, group_df in grouped_items:

        record = {
            "group": str(group_name),
            "evidence_count": int(len(group_df)),
        }

        if "video_id" in group_df.columns:
            record["video_count"] = int(group_df["video_id"].nunique())

        if "duration_sec" in group_df.columns:
            record["total_duration_sec"] = float(group_df["duration_sec"].sum())
            record["mean_duration_sec"] = float(group_df["duration_sec"].mean())
            record["min_duration_sec"] = float(group_df["duration_sec"].min())
            record["max_duration_sec"] = float(group_df["duration_sec"].max())

        records.append(record)

    return pd.DataFrame.from_records(records)


def save_evidence_summary(
    evidence_metadata: pd.DataFrame,
    output_path: str | Path,
    verbose: bool = True,
) -> Dict[str, object]:
    """
    Save a compact evidence metadata summary CSV.

    Parameters
    ----------
    evidence_metadata:
        Evidence metadata DataFrame to summarize.

    output_path:
        Destination summary CSV path.

    verbose:
        Whether to print save summary information.

    Returns
    -------
    dict
        Save summary containing output path and row count.
    """

    output_path = _as_path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    summary_table = build_evidence_summary_table(evidence_metadata)
    summary_table.to_csv(output_path, index=False)

    if not output_path.exists():
        raise FileNotFoundError(
            f"Evidence summary file was not created: {output_path}"
        )

    if verbose:

        print("Evidence summary saved.")
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
    """
    Save evidence validation issues to a CSV file.

    Parameters
    ----------
    validation_issues:
        Validation issue DataFrame.

    output_path:
        Destination CSV path.

    verbose:
        Whether to print save summary information.

    Returns
    -------
    dict
        Save summary containing output path and row count.
    """

    output_path = _as_path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    validation_issues.to_csv(output_path, index=False)

    if not output_path.exists():
        raise FileNotFoundError(
            f"Validation issue file was not created: {output_path}"
        )

    if verbose:

        print("Evidence validation issues saved.")
        print(f"Output path: {output_path}")
        print(f"Rows:        {len(validation_issues)}")

    return {
        "output_path": output_path,
        "row_count": int(len(validation_issues)),
    }


# ------------------------------------------------------------
# Manifest Export
# ------------------------------------------------------------

def build_evidence_manifest(
    evidence_metadata_path: str | Path,
    evidence_summary_path: Optional[str | Path] = None,
    validation_issues_path: Optional[str | Path] = None,
    metadata: Optional[Dict[str, object]] = None,
) -> Dict[str, object]:
    """
    Build a JSON-serializable manifest for evidence outputs.

    Parameters
    ----------
    evidence_metadata_path:
        Path to the primary evidence metadata CSV.

    evidence_summary_path:
        Optional path to the evidence summary CSV.

    validation_issues_path:
        Optional path to the validation issues CSV.

    metadata:
        Optional additional manifest metadata.

    Returns
    -------
    dict
        Evidence output manifest.
    """

    evidence_metadata_path = _as_path(evidence_metadata_path)

    manifest: Dict[str, object] = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "evidence_metadata_path": str(evidence_metadata_path),
        "evidence_metadata_exists": evidence_metadata_path.exists(),
    }

    if evidence_metadata_path.exists():
        manifest["evidence_metadata_size_bytes"] = evidence_metadata_path.stat().st_size

    if evidence_summary_path is not None:
        summary_path = _as_path(evidence_summary_path)
        manifest["evidence_summary_path"] = str(summary_path)
        manifest["evidence_summary_exists"] = summary_path.exists()

    if validation_issues_path is not None:
        issues_path = _as_path(validation_issues_path)
        manifest["validation_issues_path"] = str(issues_path)
        manifest["validation_issues_exists"] = issues_path.exists()

    if metadata:
        manifest["metadata"] = metadata

    return manifest


def save_evidence_manifest(
    manifest: Dict[str, object],
    output_path: str | Path,
    verbose: bool = True,
) -> Dict[str, object]:
    """
    Save an evidence output manifest to JSON.

    Parameters
    ----------
    manifest:
        Manifest dictionary to save.

    output_path:
        Destination JSON path.

    verbose:
        Whether to print save summary information.

    Returns
    -------
    dict
        Save summary containing output path and file size.
    """

    output_path = _as_path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as output_file:
        json.dump(
            manifest,
            output_file,
            indent=2,
            default=_json_default,
        )

    if not output_path.exists():
        raise FileNotFoundError(
            f"Evidence manifest file was not created: {output_path}"
        )

    file_size_bytes = output_path.stat().st_size

    if verbose:

        print("Evidence manifest saved.")
        print(f"Output path: {output_path}")
        print(f"File size:   {_format_mb(file_size_bytes)}")

    return {
        "output_path": output_path,
        "file_size_bytes": file_size_bytes,
    }


# ------------------------------------------------------------
# Convenience Wrapper
# ------------------------------------------------------------

def save_evidence_outputs(
    evidence_metadata: pd.DataFrame,
    output_dir: str | Path,
    validation_issues: Optional[pd.DataFrame] = None,
    metadata: Optional[Dict[str, object]] = None,
    evidence_metadata_filename: str = DEFAULT_EVIDENCE_METADATA_FILENAME,
    evidence_summary_filename: str = DEFAULT_EVIDENCE_SUMMARY_FILENAME,
    evidence_manifest_filename: str = DEFAULT_EVIDENCE_MANIFEST_FILENAME,
    validation_issues_filename: str = DEFAULT_VALIDATION_ISSUES_FILENAME,
    verbose: bool = True,
) -> Dict[str, object]:
    """
    Save standard evidence metadata outputs to an output directory.

    Parameters
    ----------
    evidence_metadata:
        Evidence metadata DataFrame to save.

    output_dir:
        Destination directory for all evidence output files.

    validation_issues:
        Optional validation issue DataFrame to save.

    metadata:
        Optional metadata to include in the manifest.

    evidence_metadata_filename:
        Filename for the primary evidence metadata CSV.

    evidence_summary_filename:
        Filename for the evidence summary CSV.

    evidence_manifest_filename:
        Filename for the evidence manifest JSON.

    validation_issues_filename:
        Filename for the validation issue CSV.

    verbose:
        Whether to print output summary information.

    Returns
    -------
    dict
        Output summary containing paths and save results.
    """

    output_dir = _as_path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    evidence_metadata_path = output_dir / evidence_metadata_filename
    evidence_summary_path = output_dir / evidence_summary_filename
    evidence_manifest_path = output_dir / evidence_manifest_filename
    validation_issues_path = output_dir / validation_issues_filename

    metadata_save_summary = save_evidence_metadata(
        evidence_metadata=evidence_metadata,
        output_path=evidence_metadata_path,
        verbose=verbose,
    )

    summary_save_summary = save_evidence_summary(
        evidence_metadata=evidence_metadata,
        output_path=evidence_summary_path,
        verbose=verbose,
    )

    validation_save_summary = None

    if validation_issues is not None:
        validation_save_summary = save_validation_issues(
            validation_issues=validation_issues,
            output_path=validation_issues_path,
            verbose=verbose,
        )

    manifest = build_evidence_manifest(
        evidence_metadata_path=evidence_metadata_path,
        evidence_summary_path=evidence_summary_path,
        validation_issues_path=(
            validation_issues_path if validation_issues is not None else None
        ),
        metadata=metadata,
    )

    manifest_save_summary = save_evidence_manifest(
        manifest=manifest,
        output_path=evidence_manifest_path,
        verbose=verbose,
    )

    return {
        "output_dir": output_dir,
        "evidence_metadata_path": evidence_metadata_path,
        "evidence_summary_path": evidence_summary_path,
        "evidence_manifest_path": evidence_manifest_path,
        "validation_issues_path": (
            validation_issues_path if validation_issues is not None else None
        ),
        "metadata_save_summary": metadata_save_summary,
        "summary_save_summary": summary_save_summary,
        "validation_save_summary": validation_save_summary,
        "manifest_save_summary": manifest_save_summary,
    }
