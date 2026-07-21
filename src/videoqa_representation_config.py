# ============================================================
# VideoQA Project Configuration
# ============================================================
#
# This file centralizes dataset paths, experiment paths, shared
# representation paths, model settings, and notebook artifact aliases.
#
# Directory philosophy:
#
#   1. GitHub repository paths live under BASE_DIR.
#   2. Google Drive persistent project storage lives under GOOGLE_DRIVE_ROOT.
#   3. Shared artifacts live under GOOGLE_DRIVE_ROOT / "representations".
#   4. Experiment-specific artifacts live under
#      GOOGLE_DRIVE_ROOT / "experiments" / EXPERIMENT_NAME.
#
# Shared CLIP text/video representations are intentionally not stored
# inside individual experiment folders. Prediction and evaluation results
# are experiment-specific and should be stored inside each experiment.
#
# ============================================================

from pathlib import Path


# ============================================================
# 1. Project Roots
# ============================================================

# GitHub repository cloned into the Colab runtime.
BASE_DIR = Path("/content/videoqa-representation-comparison")

# Local notebook output root inside the Colab runtime.
# These artifacts are temporary unless promoted to Google Drive.
OUTPUTS_DIR = BASE_DIR / "outputs"

# Persistent Google Drive project root.
GOOGLE_DRIVE_ROOT = Path("/content/drive/MyDrive/VideoQA_Project")

# Persistent Google Drive experiment root.
EXPERIMENTS_DRIVE_DIR = GOOGLE_DRIVE_ROOT / "experiments"

# Persistent Google Drive shared representation root.
SHARED_REPRESENTATIONS_DRIVE_DIR = GOOGLE_DRIVE_ROOT / "representations"


# ============================================================
# 3. Dataset Configuration
# ============================================================

DATASETS_DIR = BASE_DIR / "datasets"

DATASET_NAME = "NExT-QA"
EXPECTED_VIDEO_COUNT = 5440

DATASET_CONFIG = {
    "NExT-QA": {
        "dataset_dir": DATASETS_DIR / "NExT-QA",
        "videos_dir": DATASETS_DIR / "NExT-QA" / "videos",
        "questions_dir": DATASETS_DIR / "NExT-QA" / "questions",
        "metadata_dir": DATASETS_DIR / "NExT-QA" / "metadata",
    },
}

DATASET_DIR = DATASET_CONFIG[DATASET_NAME]["dataset_dir"]
VIDEOS_DIR = DATASET_CONFIG[DATASET_NAME]["videos_dir"]
QUESTIONS_DIR = DATASET_CONFIG[DATASET_NAME]["questions_dir"]
METADATA_DIR = DATASET_CONFIG[DATASET_NAME]["metadata_dir"]

ARCHIVES_DIR = DATASET_DIR / "archives"
NEXTQA_COMBINED_ARCHIVE_NAME = "NExTVideo_combined.zip"
NEXTQA_COMBINED_ARCHIVE_PATH = ARCHIVES_DIR / NEXTQA_COMBINED_ARCHIVE_NAME


# ============================================================
# 4. Common Development Settings
# ============================================================

DEVELOPMENT_SUBSET_SIZE = 100
EVALUATION_SPLIT = "val"
RANDOM_SEED = 42

ANSWER_MODE = "multiple_choice"
CHOICE_COLUMNS = ["a0", "a1", "a2", "a3", "a4"]
GROUND_TRUTH_ANSWER_COLUMN = "answer"
QUESTION_COLUMN = "question"
VIDEO_ID_COLUMN = "video"


# ============================================================
# 5. Experiment Directory Helpers
# ============================================================

def get_drive_experiment_dir(experiment_name: str) -> Path:
    """Return the persistent Google Drive directory for an experiment."""
    return EXPERIMENTS_DRIVE_DIR / experiment_name


def get_local_experiment_dir(experiment_name: str) -> Path:
    """Return the temporary local runtime output directory for an experiment."""
    return OUTPUTS_DIR / "experiments" / experiment_name


def get_experiment_videoqa_dir(experiment_name: str) -> Path:
    """Return the Google Drive VideoQA output directory for an experiment."""
    return get_drive_experiment_dir(experiment_name) / "videoqa"


def get_experiment_evaluation_dir(experiment_name: str) -> Path:
    """Return the Google Drive evaluation output directory for an experiment."""
    return get_drive_experiment_dir(experiment_name) / "evaluation"


def get_experiment_manifest_path(experiment_name: str) -> Path:
    """Return the optional manifest file for an experiment."""
    return get_drive_experiment_dir(experiment_name) / "experiment.json"

def get_experiment_paths(experiment_name):
    experiment_drive_dir = get_drive_experiment_dir(experiment_name)
    experiment_local_dir = get_local_experiment_dir(experiment_name)

    return {
        "experiment_drive_dir": experiment_drive_dir,
        "experiment_local_dir": experiment_local_dir,
        "videoqa_drive_dir": experiment_drive_dir / "videoqa",
        "evaluation_drive_dir": experiment_drive_dir / "evaluation",
        "videoqa_local_dir": experiment_local_dir / "videoqa",
        "evaluation_local_dir": experiment_local_dir / "evaluation",
        "manifest_path": experiment_drive_dir / "experiment.json",
    }

VIDEOQA_PREDICTIONS_FILENAME = "predictions.csv"
VIDEOQA_VALIDATION_FILENAME = "validation.csv"
VIDEOQA_SUMMARY_FILENAME = "summary.csv"


# ============================================================
# 6. Shared CLIP Representation Paths
# ============================================================

CLIP_SHARED_REPRESENTATIONS_DRIVE_DIR = SHARED_REPRESENTATIONS_DRIVE_DIR / "clip"

CLIP_TEXT_REPRESENTATIONS_DRIVE_DIR = CLIP_SHARED_REPRESENTATIONS_DRIVE_DIR / "text"
CLIP_VIDEO_REPRESENTATIONS_DRIVE_DIR = CLIP_SHARED_REPRESENTATIONS_DRIVE_DIR / "video"

CLIP_TEXT_REPRESENTATIONS_DRIVE_CSV = (
    CLIP_TEXT_REPRESENTATIONS_DRIVE_DIR / "clip_text_representations.csv"
)
CLIP_TEXT_SUMMARY_DRIVE_CSV = (
    CLIP_TEXT_REPRESENTATIONS_DRIVE_DIR / "clip_text_representation_summary.csv"
)

CLIP_VIDEO_REPRESENTATIONS_DRIVE_CSV = (
    CLIP_VIDEO_REPRESENTATIONS_DRIVE_DIR / "clip_video_representations.csv"
)
CLIP_VIDEO_SUMMARY_DRIVE_CSV = (
    CLIP_VIDEO_REPRESENTATIONS_DRIVE_DIR / "clip_video_representation_summary.csv"
)

# Local temporary shared CLIP outputs.
CLIP_TEXT_LOCAL_OUTPUT_DIR = OUTPUTS_DIR / "representations" / "clip" / "text"
CLIP_VIDEO_LOCAL_OUTPUT_DIR = OUTPUTS_DIR / "representations" / "clip" / "video"

CLIP_TEXT_REPRESENTATIONS_LOCAL_CSV = (
    CLIP_TEXT_LOCAL_OUTPUT_DIR / "clip_text_representations.csv"
)
CLIP_TEXT_SUMMARY_LOCAL_CSV = (
    CLIP_TEXT_LOCAL_OUTPUT_DIR / "clip_text_representation_summary.csv"
)

CLIP_VIDEO_REPRESENTATIONS_LOCAL_CSV = (
    CLIP_VIDEO_LOCAL_OUTPUT_DIR / "clip_video_representations.csv"
)
CLIP_VIDEO_SUMMARY_LOCAL_CSV = (
    CLIP_VIDEO_LOCAL_OUTPUT_DIR / "clip_video_representation_summary.csv"
)

# Backward-compatible local aliases.
REPRESENTATIONS_DIR = OUTPUTS_DIR / "representations"
CLIP_REPRESENTATIONS_DIR = REPRESENTATIONS_DIR / "clip"
CLIP_TEXT_REPRESENTATIONS_DIR = CLIP_REPRESENTATIONS_DIR / "text"
CLIP_VIDEO_REPRESENTATIONS_DIR = CLIP_REPRESENTATIONS_DIR / "video"

CLIP_TEXT_REPRESENTATIONS_CSV = CLIP_TEXT_REPRESENTATIONS_LOCAL_CSV
CLIP_VIDEO_REPRESENTATIONS_CSV = CLIP_VIDEO_REPRESENTATIONS_LOCAL_CSV


# ============================================================
# 7. Experiment-Specific Path Helpers
# ============================================================
#
# EXPERIMENT_NAME is intentionally not defined in this file.
# Each notebook should define EXPERIMENT_NAME locally after importing
# this configuration module, then call the helper functions below.
#
# This keeps the configuration import-safe and prevents notebooks from
# requiring edits to this shared file just to run a different experiment.
# ============================================================

BASELINE_PREDICTIONS_FILENAME = "baseline_predictions.csv"
BASELINE_VALIDATION_FILENAME = "baseline_validation.csv"
BASELINE_SUMMARY_FILENAME = "baseline_summary.csv"

REPRESENTATION_VIDEOQA_PREDICTIONS_FILENAME = "representation_videoqa_predictions.csv"
REPRESENTATION_VIDEOQA_VALIDATION_FILENAME = "representation_videoqa_validation.csv"
REPRESENTATION_VIDEOQA_SUMMARY_FILENAME = "representation_videoqa_summary.csv"

EVALUATION_DATASET_FILENAME = "evaluation_dataset.csv"
EVALUATION_METRICS_FILENAME = "evaluation_metrics.csv"
EVALUATION_DETAILS_FILENAME = "evaluation_details.csv"
EVALUATION_REPORT_SUMMARY_FILENAME = "evaluation_summary.csv"


def get_baseline_videoqa_paths(experiment_name: str) -> dict:
    """Return Notebook 01 baseline VideoQA paths for an experiment."""
    paths = get_experiment_paths(experiment_name)
    videoqa_drive_dir = paths["videoqa_drive_dir"]
    videoqa_local_dir = paths["videoqa_local_dir"]

    return {
        **paths,
        "baseline_experiment_dir": paths["experiment_drive_dir"],
        "baseline_videoqa_drive_dir": videoqa_drive_dir,
        "baseline_evaluation_drive_dir": paths["evaluation_drive_dir"],
        "baseline_local_experiment_dir": paths["experiment_local_dir"],
        "baseline_dir": videoqa_local_dir,
        "baseline_predictions_drive_csv": videoqa_drive_dir / BASELINE_PREDICTIONS_FILENAME,
        "baseline_validation_drive_csv": videoqa_drive_dir / BASELINE_VALIDATION_FILENAME,
        "baseline_summary_drive_csv": videoqa_drive_dir / BASELINE_SUMMARY_FILENAME,
        "baseline_predictions_csv": videoqa_local_dir / BASELINE_PREDICTIONS_FILENAME,
        "baseline_validation_csv": videoqa_local_dir / BASELINE_VALIDATION_FILENAME,
        "baseline_summary_csv": videoqa_local_dir / BASELINE_SUMMARY_FILENAME,
    }


def get_representation_videoqa_paths(experiment_name: str) -> dict:
    """Return Notebook 07 representation-based VideoQA paths for an experiment."""
    paths = get_experiment_paths(experiment_name)
    videoqa_drive_dir = paths["videoqa_drive_dir"]
    videoqa_local_dir = paths["videoqa_local_dir"]

    return {
        **paths,
        "representation_videoqa_drive_dir": videoqa_drive_dir,
        "representation_videoqa_local_dir": videoqa_local_dir,
        "representation_videoqa_predictions_drive_csv": (
            videoqa_drive_dir / REPRESENTATION_VIDEOQA_PREDICTIONS_FILENAME
        ),
        "representation_videoqa_validation_drive_csv": (
            videoqa_drive_dir / REPRESENTATION_VIDEOQA_VALIDATION_FILENAME
        ),
        "representation_videoqa_summary_drive_csv": (
            videoqa_drive_dir / REPRESENTATION_VIDEOQA_SUMMARY_FILENAME
        ),
        "representation_videoqa_predictions_csv": (
            videoqa_local_dir / REPRESENTATION_VIDEOQA_PREDICTIONS_FILENAME
        ),
        "representation_videoqa_validation_csv": (
            videoqa_local_dir / REPRESENTATION_VIDEOQA_VALIDATION_FILENAME
        ),
        "representation_videoqa_summary_csv": (
            videoqa_local_dir / REPRESENTATION_VIDEOQA_SUMMARY_FILENAME
        ),
    }


def get_autoencoder_paths(experiment_name: str) -> dict:
    """Return Notebook 02-04 autoencoder training/model/representation paths."""
    paths = get_experiment_paths(experiment_name)

    experiment_drive_dir = paths["experiment_drive_dir"]
    experiment_local_dir = paths["experiment_local_dir"]

    training_dir = experiment_drive_dir / "training"
    training_metadata_dir = training_dir / "metadata"
    training_reports_dir = training_dir / "reports"

    autoencoder_dir = experiment_drive_dir / "autoencoder"
    autoencoder_models_dir = autoencoder_dir / "models"
    autoencoder_reconstructions_dir = autoencoder_dir / "reconstructions"
    autoencoder_reports_dir = autoencoder_dir / "reports"
    autoencoder_representations_drive_dir = autoencoder_dir / "representations"

    local_training_dir = experiment_local_dir / "training"
    local_training_metadata_dir = local_training_dir / "metadata"
    local_training_reports_dir = local_training_dir / "reports"

    autoencoder_local_dir = experiment_local_dir / "autoencoder"
    autoencoder_local_models_dir = autoencoder_local_dir / "models"
    autoencoder_local_reconstructions_dir = autoencoder_local_dir / "reconstructions"
    autoencoder_local_reports_dir = autoencoder_local_dir / "reports"
    autoencoder_local_representations_dir = autoencoder_local_dir / "representations"

    return {
        **paths,
        "autoencoder_experiment_dir": experiment_drive_dir,
        "autoencoder_training_dir": training_dir,
        "autoencoder_training_metadata_dir": training_metadata_dir,
        "autoencoder_training_reports_dir": training_reports_dir,
        "autoencoder_dir": autoencoder_dir,
        "autoencoder_models_dir": autoencoder_models_dir,
        "autoencoder_reconstructions_dir": autoencoder_reconstructions_dir,
        "autoencoder_reports_dir": autoencoder_reports_dir,
        "autoencoder_representations_drive_dir": autoencoder_representations_drive_dir,
        "autoencoder_videoqa_drive_dir": paths["videoqa_drive_dir"],
        "autoencoder_evaluation_drive_dir": paths["evaluation_drive_dir"],
        "autoencoder_training_metadata_csv": (
            training_metadata_dir / "training_metadata.csv"
        ),
        "autoencoder_training_summary_csv": (
            training_reports_dir / "training_data_summary.csv"
        ),
        "autoencoder_training_validation_csv": (
            training_reports_dir / "training_metadata_validation.csv"
        ),
        "autoencoder_model_path": autoencoder_models_dir / "autoencoder.pt",
        "autoencoder_segment_representations_csv": (
            autoencoder_representations_drive_dir
            / "autoencoder_segment_representations.csv"
        ),
        "autoencoder_video_representations_csv": (
            autoencoder_representations_drive_dir
            / "autoencoder_video_representations.csv"
        ),
        "autoencoder_representation_summary_csv": (
            autoencoder_representations_drive_dir
            / "autoencoder_representation_summary.csv"
        ),
        "autoencoder_evaluation_representation_dataset_csv": (
            autoencoder_representations_drive_dir
            / "evaluation_representation_dataset.csv"
        ),
        "autoencoder_videoqa_predictions_drive_csv": (
            paths["videoqa_drive_dir"] / REPRESENTATION_VIDEOQA_PREDICTIONS_FILENAME
        ),
        "autoencoder_videoqa_validation_drive_csv": (
            paths["videoqa_drive_dir"] / REPRESENTATION_VIDEOQA_VALIDATION_FILENAME
        ),
        "autoencoder_videoqa_summary_drive_csv": (
            paths["videoqa_drive_dir"] / REPRESENTATION_VIDEOQA_SUMMARY_FILENAME
        ),
        "local_experiment_dir": experiment_local_dir,
        "training_data_dir": local_training_dir,
        "training_metadata_dir": local_training_metadata_dir,
        "training_reports_dir": local_training_reports_dir,
        "training_metadata_csv": local_training_metadata_dir / "training_metadata.csv",
        "training_validation_csv": (
            local_training_reports_dir / "training_metadata_validation.csv"
        ),
        "training_summary_csv": local_training_reports_dir / "training_data_summary.csv",
        "autoencoder_local_dir": autoencoder_local_dir,
        "autoencoder_local_models_dir": autoencoder_local_models_dir,
        "autoencoder_local_reconstructions_dir": autoencoder_local_reconstructions_dir,
        "autoencoder_local_reports_dir": autoencoder_local_reports_dir,
        "autoencoder_local_representations_dir": autoencoder_local_representations_dir,
        "autoencoder_local_segment_representations_csv": (
            autoencoder_local_representations_dir
            / "autoencoder_segment_representations.csv"
        ),
        "autoencoder_local_video_representations_csv": (
            autoencoder_local_representations_dir
            / "autoencoder_video_representations.csv"
        ),
    }


def get_hybrid_video_representation_paths(
    autoencoder_experiment_name: str,
) -> dict:
    """Return source paths used to construct hybrid video embeddings."""
    autoencoder_paths = get_autoencoder_paths(
        autoencoder_experiment_name
    )

    return {
        "hybrid_clip_video_representations_csv": (
            CLIP_VIDEO_REPRESENTATIONS_DRIVE_CSV
        ),
        "hybrid_autoencoder_video_representations_csv": (
            autoencoder_paths[
                "autoencoder_video_representations_csv"
            ]
        ),
        "hybrid_autoencoder_experiment_name": (
            autoencoder_experiment_name
        ),
    }


def get_videoqa_artifact_filenames(experiment_type: str) -> dict:
    """Return prediction/validation/summary filenames for an experiment type."""
    if experiment_type == "baseline":
        return {
            "predictions": BASELINE_PREDICTIONS_FILENAME,
            "validation": BASELINE_VALIDATION_FILENAME,
            "summary": BASELINE_SUMMARY_FILENAME,
        }

    if experiment_type in {
        "clip",
        "clip_video",
        "autoencoder",
        "ae",
        "hybrid",
        "hybrid_video",
    }:
        return {
            "predictions": REPRESENTATION_VIDEOQA_PREDICTIONS_FILENAME,
            "validation": REPRESENTATION_VIDEOQA_VALIDATION_FILENAME,
            "summary": REPRESENTATION_VIDEOQA_SUMMARY_FILENAME,
        }

    raise ValueError(
        "Unsupported experiment_type. Expected one of: "
        "baseline, clip, clip_video, autoencoder, ae, "
        "hybrid, hybrid_video."
    )


def infer_experiment_type(experiment_name: str) -> str:
    """Infer the experiment type from the notebook-selected experiment name."""
    if experiment_name.startswith("qwen2vl"):
        return "baseline"

    if experiment_name.startswith("hybrid_"):
        return "hybrid_video"

    if experiment_name.startswith("clip"):
        return "clip_video"

    if experiment_name.startswith("ae_"):
        return "autoencoder"

    raise ValueError(
        "Unable to infer experiment type from experiment_name. "
        "Expected prefixes: qwen2vl, hybrid_, clip, or ae_."
    )


def get_evaluation_paths(experiment_name: str, experiment_type: str | None = None) -> dict:
    """Return Notebook 08 evaluation paths for an experiment."""
    if experiment_type is None:
        experiment_type = infer_experiment_type(experiment_name)

    paths = get_experiment_paths(experiment_name)
    artifact_filenames = get_videoqa_artifact_filenames(experiment_type)

    videoqa_drive_dir = paths["videoqa_drive_dir"]
    videoqa_local_dir = paths["videoqa_local_dir"]
    evaluation_drive_dir = paths["evaluation_drive_dir"]
    evaluation_local_dir = paths["evaluation_local_dir"]

    return {
        **paths,
        "experiment_type": experiment_type,
        "evaluation_artifact_filenames": artifact_filenames,
        "evaluation_experiment_dir": paths["experiment_drive_dir"],
        "evaluation_output_drive_dir": evaluation_drive_dir,
        "evaluation_dir": evaluation_local_dir,
        "evaluation_output_dir": evaluation_local_dir,
        "evaluation_predictions_drive_csv": (
            videoqa_drive_dir / artifact_filenames["predictions"]
        ),
        "evaluation_validation_drive_csv": (
            videoqa_drive_dir / artifact_filenames["validation"]
        ),
        "evaluation_summary_drive_csv": (
            videoqa_drive_dir / artifact_filenames["summary"]
        ),
        "evaluation_predictions_csv": (
            videoqa_local_dir / artifact_filenames["predictions"]
        ),
        "evaluation_validation_csv": (
            videoqa_local_dir / artifact_filenames["validation"]
        ),
        "evaluation_summary_csv": (
            videoqa_local_dir / artifact_filenames["summary"]
        ),
        "evaluation_dataset_csv": evaluation_local_dir / EVALUATION_DATASET_FILENAME,
        "evaluation_metrics_csv": evaluation_local_dir / EVALUATION_METRICS_FILENAME,
        "evaluation_details_csv": evaluation_local_dir / EVALUATION_DETAILS_FILENAME,
        "evaluation_report_summary_csv": (
            evaluation_local_dir / EVALUATION_REPORT_SUMMARY_FILENAME
        ),
    }





def configure_experiment(
    experiment_name: str,
    experiment_type: str | None = None,
    update_caller_globals: bool = True,
) -> dict:
    """Configure experiment-specific uppercase aliases for notebook compatibility.

    This function intentionally performs the experiment-specific path binding
    after a notebook has selected EXPERIMENT_NAME locally. The configuration
    module remains import-safe because no experiment-specific aliases are
    created during import.

    Typical notebook usage:

        from src.videoqa_representation_config import *

        EXPERIMENT_NAME = "qwen2vl_baseline_dev25"
        configure_experiment(EXPERIMENT_NAME)

    The returned dictionary contains the configured aliases. The same values
    are also written into this module's global namespace and, by default, into
    the calling notebook's global namespace. This allows existing notebook
    code imported with ``from src.videoqa_representation_config import *`` to
    continue using names such as BASELINE_DIR, BASELINE_PREDICTIONS_CSV,
    AUTOENCODER_MODEL_PATH, and EVALUATION_DIR.
    """
    if experiment_type is None:
        experiment_type = infer_experiment_type(experiment_name)

    experiment_paths = get_experiment_paths(experiment_name)
    baseline_paths = get_baseline_videoqa_paths(experiment_name)
    representation_paths = get_representation_videoqa_paths(experiment_name)
    autoencoder_paths = get_autoencoder_paths(experiment_name)
    evaluation_paths = get_evaluation_paths(experiment_name, experiment_type)

    aliases = {
        # Active experiment identity.
        "EXPERIMENT_NAME": experiment_name,
        "EXPERIMENT_TYPE": experiment_type,

        # Generic experiment directories.
        "EXPERIMENT_DRIVE_DIR": experiment_paths["experiment_drive_dir"],
        "EXPERIMENT_LOCAL_DIR": experiment_paths["experiment_local_dir"],
        "EXPERIMENT_VIDEOQA_DRIVE_DIR": experiment_paths["videoqa_drive_dir"],
        "EXPERIMENT_EVALUATION_DRIVE_DIR": experiment_paths["evaluation_drive_dir"],
        "EXPERIMENT_VIDEOQA_LOCAL_DIR": experiment_paths["videoqa_local_dir"],
        "EXPERIMENT_EVALUATION_LOCAL_DIR": experiment_paths["evaluation_local_dir"],
        "EXPERIMENT_MANIFEST_PATH": experiment_paths["manifest_path"],

        # Baseline aliases used by Notebook 01.
        "BASELINE_EXPERIMENT_DIR": baseline_paths["baseline_experiment_dir"],
        "BASELINE_VIDEOQA_DRIVE_DIR": baseline_paths["baseline_videoqa_drive_dir"],
        "BASELINE_EVALUATION_DRIVE_DIR": baseline_paths["baseline_evaluation_drive_dir"],
        "BASELINE_LOCAL_EXPERIMENT_DIR": baseline_paths["baseline_local_experiment_dir"],
        "BASELINE_DIR": baseline_paths["baseline_dir"],
        "BASELINE_PREDICTIONS_DRIVE_CSV": baseline_paths["baseline_predictions_drive_csv"],
        "BASELINE_VALIDATION_DRIVE_CSV": baseline_paths["baseline_validation_drive_csv"],
        "BASELINE_SUMMARY_DRIVE_CSV": baseline_paths["baseline_summary_drive_csv"],
        "BASELINE_PREDICTIONS_CSV": baseline_paths["baseline_predictions_csv"],
        "BASELINE_VALIDATION_CSV": baseline_paths["baseline_validation_csv"],
        "BASELINE_SUMMARY_CSV": baseline_paths["baseline_summary_csv"],

        # CLIP representation VideoQA aliases used by Notebook 07 when running
        # the pretrained representation pipeline.
        "CLIP_VIDEO_EXPERIMENT_DIR": experiment_paths["experiment_drive_dir"],
        "CLIP_VIDEOQA_DRIVE_DIR": experiment_paths["videoqa_drive_dir"],
        "CLIP_VIDEO_EVALUATION_DRIVE_DIR": experiment_paths["evaluation_drive_dir"],
        "CLIP_VIDEO_LOCAL_EXPERIMENT_DIR": experiment_paths["experiment_local_dir"],
        "CLIP_VIDEOQA_DIR": experiment_paths["videoqa_local_dir"],
        "CLIP_VIDEOQA_PREDICTIONS_DRIVE_CSV": representation_paths[
            "representation_videoqa_predictions_drive_csv"
        ],
        "CLIP_VIDEOQA_VALIDATION_DRIVE_CSV": representation_paths[
            "representation_videoqa_validation_drive_csv"
        ],
        "CLIP_VIDEOQA_SUMMARY_DRIVE_CSV": representation_paths[
            "representation_videoqa_summary_drive_csv"
        ],
        "CLIP_VIDEOQA_PREDICTIONS_CSV": representation_paths[
            "representation_videoqa_predictions_csv"
        ],
        "CLIP_VIDEOQA_VALIDATION_CSV": representation_paths[
            "representation_videoqa_validation_csv"
        ],
        "CLIP_VIDEOQA_SUMMARY_CSV": representation_paths[
            "representation_videoqa_summary_csv"
        ],

        # Generic representation VideoQA aliases.
        "REPRESENTATION_VIDEOQA_DRIVE_DIR": representation_paths[
            "representation_videoqa_drive_dir"
        ],
        "REPRESENTATION_VIDEOQA_LOCAL_DIR": representation_paths[
            "representation_videoqa_local_dir"
        ],
        "REPRESENTATION_VIDEOQA_PREDICTIONS_DRIVE_CSV": representation_paths[
            "representation_videoqa_predictions_drive_csv"
        ],
        "REPRESENTATION_VIDEOQA_VALIDATION_DRIVE_CSV": representation_paths[
            "representation_videoqa_validation_drive_csv"
        ],
        "REPRESENTATION_VIDEOQA_SUMMARY_DRIVE_CSV": representation_paths[
            "representation_videoqa_summary_drive_csv"
        ],
        "REPRESENTATION_VIDEOQA_PREDICTIONS_CSV": representation_paths[
            "representation_videoqa_predictions_csv"
        ],
        "REPRESENTATION_VIDEOQA_VALIDATION_CSV": representation_paths[
            "representation_videoqa_validation_csv"
        ],
        "REPRESENTATION_VIDEOQA_SUMMARY_CSV": representation_paths[
            "representation_videoqa_summary_csv"
        ],

        "FUSION_MODEL_PATH": (
            representation_paths["representation_videoqa_local_dir"]
            / FUSION_MODEL_FILENAME
        ),

        # Autoencoder aliases used by Notebooks 02-04 and Notebook 07 when
        # running the self-supervised representation pipeline.
        "AUTOENCODER_EXPERIMENT_DIR": autoencoder_paths["autoencoder_experiment_dir"],
        "AUTOENCODER_TRAINING_DIR": autoencoder_paths["autoencoder_training_dir"],
        "AUTOENCODER_TRAINING_METADATA_DIR": autoencoder_paths[
            "autoencoder_training_metadata_dir"
        ],
        "AUTOENCODER_TRAINING_REPORTS_DIR": autoencoder_paths[
            "autoencoder_training_reports_dir"
        ],
        "AUTOENCODER_DIR": autoencoder_paths["autoencoder_dir"],
        "AUTOENCODER_MODELS_DIR": autoencoder_paths["autoencoder_models_dir"],
        "AUTOENCODER_RECONSTRUCTIONS_DIR": autoencoder_paths[
            "autoencoder_reconstructions_dir"
        ],
        "AUTOENCODER_REPORTS_DIR": autoencoder_paths["autoencoder_reports_dir"],
        "AUTOENCODER_REPRESENTATIONS_DRIVE_DIR": autoencoder_paths[
            "autoencoder_representations_drive_dir"
        ],
        "AUTOENCODER_VIDEOQA_DRIVE_DIR": autoencoder_paths[
            "autoencoder_videoqa_drive_dir"
        ],
        "AUTOENCODER_EVALUATION_DRIVE_DIR": autoencoder_paths[
            "autoencoder_evaluation_drive_dir"
        ],
        "AUTOENCODER_TRAINING_METADATA_CSV": autoencoder_paths[
            "autoencoder_training_metadata_csv"
        ],
        "AUTOENCODER_TRAINING_SUMMARY_CSV": autoencoder_paths[
            "autoencoder_training_summary_csv"
        ],
        "AUTOENCODER_TRAINING_VALIDATION_CSV": autoencoder_paths[
            "autoencoder_training_validation_csv"
        ],
        "AUTOENCODER_MODEL_PATH": autoencoder_paths["autoencoder_model_path"],
        "AUTOENCODER_SEGMENT_REPRESENTATIONS_CSV": autoencoder_paths[
            "autoencoder_segment_representations_csv"
        ],
        "AUTOENCODER_VIDEO_REPRESENTATIONS_CSV": autoencoder_paths[
            "autoencoder_video_representations_csv"
        ],
        "AUTOENCODER_REPRESENTATION_SUMMARY_CSV": autoencoder_paths[
            "autoencoder_representation_summary_csv"
        ],
        "AUTOENCODER_EVALUATION_REPRESENTATION_DATASET_CSV": autoencoder_paths[
            "autoencoder_evaluation_representation_dataset_csv"
        ],
        "AUTOENCODER_VIDEOQA_PREDICTIONS_DRIVE_CSV": autoencoder_paths[
            "autoencoder_videoqa_predictions_drive_csv"
        ],
        "AUTOENCODER_VIDEOQA_VALIDATION_DRIVE_CSV": autoencoder_paths[
            "autoencoder_videoqa_validation_drive_csv"
        ],
        "AUTOENCODER_VIDEOQA_SUMMARY_DRIVE_CSV": autoencoder_paths[
            "autoencoder_videoqa_summary_drive_csv"
        ],
        "LOCAL_EXPERIMENT_DIR": autoencoder_paths["local_experiment_dir"],
        "TRAINING_DATA_DIR": autoencoder_paths["training_data_dir"],
        "TRAINING_METADATA_DIR": autoencoder_paths["training_metadata_dir"],
        "TRAINING_REPORTS_DIR": autoencoder_paths["training_reports_dir"],
        "TRAINING_METADATA_CSV": autoencoder_paths["training_metadata_csv"],
        "TRAINING_VALIDATION_CSV": autoencoder_paths["training_validation_csv"],
        "TRAINING_SUMMARY_CSV": autoencoder_paths["training_summary_csv"],
        "AUTOENCODER_LOCAL_DIR": autoencoder_paths["autoencoder_local_dir"],
        "AUTOENCODER_LOCAL_MODELS_DIR": autoencoder_paths[
            "autoencoder_local_models_dir"
        ],
        "AUTOENCODER_LOCAL_RECONSTRUCTIONS_DIR": autoencoder_paths[
            "autoencoder_local_reconstructions_dir"
        ],
        "AUTOENCODER_LOCAL_REPORTS_DIR": autoencoder_paths[
            "autoencoder_local_reports_dir"
        ],
        "AUTOENCODER_LOCAL_REPRESENTATIONS_DIR": autoencoder_paths[
            "autoencoder_local_representations_dir"
        ],
        "AUTOENCODER_LOCAL_SEGMENT_REPRESENTATIONS_CSV": autoencoder_paths[
            "autoencoder_local_segment_representations_csv"
        ],
        "AUTOENCODER_LOCAL_VIDEO_REPRESENTATIONS_CSV": autoencoder_paths[
            "autoencoder_local_video_representations_csv"
        ],

        # Evaluation aliases used by Notebook 08.
        "EVALUATION_EXPERIMENT_DIR": evaluation_paths["evaluation_experiment_dir"],
        "EVALUATION_OUTPUT_DRIVE_DIR": evaluation_paths[
            "evaluation_output_drive_dir"
        ],
        "EVALUATION_ARTIFACT_FILENAMES": evaluation_paths[
            "evaluation_artifact_filenames"
        ],
        "EVALUATION_PREDICTIONS_DRIVE_CSV": evaluation_paths[
            "evaluation_predictions_drive_csv"
        ],
        "EVALUATION_VALIDATION_DRIVE_CSV": evaluation_paths[
            "evaluation_validation_drive_csv"
        ],
        "EVALUATION_SUMMARY_DRIVE_CSV": evaluation_paths[
            "evaluation_summary_drive_csv"
        ],
        "EVALUATION_DIR": evaluation_paths["evaluation_dir"],
        "EVALUATION_OUTPUT_DIR": evaluation_paths["evaluation_output_dir"],
        "EVALUATION_PREDICTIONS_CSV": evaluation_paths[
            "evaluation_predictions_csv"
        ],
        "EVALUATION_VALIDATION_CSV": evaluation_paths["evaluation_validation_csv"],
        "EVALUATION_SUMMARY_CSV": evaluation_paths["evaluation_summary_csv"],
        "EVALUATION_DATASET_CSV": evaluation_paths["evaluation_dataset_csv"],
        "EVALUATION_METRICS_CSV": evaluation_paths["evaluation_metrics_csv"],
        "EVALUATION_DETAILS_CSV": evaluation_paths["evaluation_details_csv"],
        "EVALUATION_REPORT_SUMMARY_CSV": evaluation_paths[
            "evaluation_report_summary_csv"
        ],
    }

    globals().update(aliases)

    if update_caller_globals:
        # Support notebook usage with:
        #     from src.videoqa_representation_config import *
        #     EXPERIMENT_NAME = "..."
        #     configure_experiment(EXPERIMENT_NAME)
        #
        # Without this caller update, aliases created inside this module would
        # not be visible as bare names in the notebook namespace after a
        # star import.
        import inspect

        caller_frame = inspect.currentframe().f_back
        if caller_frame is not None:
            caller_frame.f_globals.update(aliases)

    return aliases


# Backward-compatible local root aliases that do not depend on EXPERIMENT_NAME.
# These roots are legacy locations and should not be used for new outputs.
REPRESENTATION_VIDEOQA_DIR = OUTPUTS_DIR / "representation_videoqa"
AUTOENCODER_REPRESENTATIONS_DIR = REPRESENTATIONS_DIR / "autoencoder"
AUTOENCODER_REPRESENTATIONS_CSV = (
    AUTOENCODER_REPRESENTATIONS_DIR / "autoencoder_representations.csv"
)


# ============================================================
# 10. Representation-Based VideoQA Settings
# ============================================================

# -----------------------------------------------------------------
# Representation Sources
# -----------------------------------------------------------------
CLIP_VIDEO_REPRESENTATION_SOURCE = "clip_video"
AUTOENCODER_VIDEO_REPRESENTATION_SOURCE = "autoencoder_video"
HYBRID_VIDEO_REPRESENTATION_SOURCE = "hybrid_clip_autoencoder"

SUPPORTED_VIDEO_REPRESENTATION_SOURCES = {
    CLIP_VIDEO_REPRESENTATION_SOURCE,
    AUTOENCODER_VIDEO_REPRESENTATION_SOURCE,
    HYBRID_VIDEO_REPRESENTATION_SOURCE,
}

DEFAULT_VIDEO_REPRESENTATION_SOURCE = CLIP_VIDEO_REPRESENTATION_SOURCE
DEFAULT_TEXT_REPRESENTATION_SOURCE = "clip_text"

# -----------------------------------------------------------------
# Hybrid CLIP + Autoencoder Representation
# -----------------------------------------------------------------

# Each source is normalized independently before concatenation.
HYBRID_NORMALIZE_CLIP_VIDEO = True
HYBRID_NORMALIZE_AUTOENCODER_VIDEO = True

# Concatenate normalized CLIP and autoencoder video embeddings.
HYBRID_VIDEO_COMBINATION_METHOD = "concatenate"

SUPPORTED_HYBRID_VIDEO_COMBINATION_METHODS = {
    "concatenate",
}

# -----------------------------------------------------------------
# Representation-Based VideoQA Prediction Methods
# -----------------------------------------------------------------
#
# Supported methods:
#
#   cosine_similarity
#       CLIP zero-shot cosine-similarity baseline.
#
#   fusion_mlp_classifier
#       Learned Fusion MLP classifier using projected video and
#       question-answer embeddings.
#
#   interaction_fusion_classifier
#       Learned fusion classifier using explicit video-text
#       interaction features.
#
#   gated_fusion_classifier
#       Learned fusion classifier using adaptive modality gates.
#
#   bilinear_fusion_classifier
#       Learned fusion classifier using multiplicative bilinear
#       video-text interactions.
#
# Notebook 07 selects the active method locally.
REPRESENTATION_VIDEOQA_METHOD = None

SUPPORTED_REPRESENTATION_VIDEOQA_METHODS = {
    "cosine_similarity",
    "fusion_mlp_classifier",
    "interaction_fusion_classifier",
    "gated_fusion_classifier",
    "bilinear_fusion_classifier",
}

REPRESENTATION_VIDEOQA_METHOD_LABELS = {
    "cosine_similarity": "Cosine Similarity",
    "fusion_mlp_classifier": "Fusion MLP",
    "interaction_fusion_classifier": "Interaction Fusion",
    "gated_fusion_classifier": "Gated Fusion",
    "bilinear_fusion_classifier": "Bilinear Fusion",
}

REPRESENTATION_VIDEOQA_METHOD_EXPERIMENT_TOKENS = {
    "cosine_similarity": "similarity",
    "fusion_mlp_classifier": "mlp",
    "interaction_fusion_classifier": "interaction",
    "gated_fusion_classifier": "gated",
    "bilinear_fusion_classifier": "bilinear",
}

VIDEO_REPRESENTATION_SOURCE_SUPPORTED_METHODS = {
    CLIP_VIDEO_REPRESENTATION_SOURCE: {
        "cosine_similarity",
        "fusion_mlp_classifier",
        "interaction_fusion_classifier",
        "gated_fusion_classifier",
        "bilinear_fusion_classifier",
    },
    AUTOENCODER_VIDEO_REPRESENTATION_SOURCE: {
        "fusion_mlp_classifier",
        "interaction_fusion_classifier",
        "gated_fusion_classifier",
        "bilinear_fusion_classifier",
    },
    HYBRID_VIDEO_REPRESENTATION_SOURCE: {
        "fusion_mlp_classifier",
        "interaction_fusion_classifier",
        "gated_fusion_classifier",
        "bilinear_fusion_classifier",
    },
}

if (
    set(VIDEO_REPRESENTATION_SOURCE_SUPPORTED_METHODS)
    != SUPPORTED_VIDEO_REPRESENTATION_SOURCES
):
    raise ValueError(
        "VIDEO_REPRESENTATION_SOURCE_SUPPORTED_METHODS must "
        "define exactly the supported video representation sources."
    )

invalid_source_methods = {
    source: methods - SUPPORTED_REPRESENTATION_VIDEOQA_METHODS
    for source, methods
    in VIDEO_REPRESENTATION_SOURCE_SUPPORTED_METHODS.items()
    if methods - SUPPORTED_REPRESENTATION_VIDEOQA_METHODS
}

if invalid_source_methods:
    raise ValueError(
        "Video representation sources contain unsupported "
        f"prediction methods: {invalid_source_methods}"
    )

# -----------------------------------------------------------------
# Prediction Method Configuration Validation
# -----------------------------------------------------------------

if (
    set(REPRESENTATION_VIDEOQA_METHOD_LABELS)
    != SUPPORTED_REPRESENTATION_VIDEOQA_METHODS
):
    raise ValueError(
        "REPRESENTATION_VIDEOQA_METHOD_LABELS must define exactly "
        "the supported representation-based VideoQA methods."
    )

if (
    set(REPRESENTATION_VIDEOQA_METHOD_EXPERIMENT_TOKENS)
    != SUPPORTED_REPRESENTATION_VIDEOQA_METHODS
):
    raise ValueError(
        "REPRESENTATION_VIDEOQA_METHOD_EXPERIMENT_TOKENS must define "
        "exactly the supported representation-based VideoQA methods."
    )

method_experiment_tokens = list(
    REPRESENTATION_VIDEOQA_METHOD_EXPERIMENT_TOKENS.values()
)

if len(method_experiment_tokens) != len(
    set(method_experiment_tokens)
):
    raise ValueError(
        "Representation-based VideoQA experiment tokens must be unique."
    )

invalid_method_experiment_tokens = [
    token
    for token in method_experiment_tokens
    if (
        not token
        or token != token.lower()
        or not token.replace("_", "").isalnum()
    )
]

if invalid_method_experiment_tokens:
    raise ValueError(
        "Invalid representation-based VideoQA experiment tokens: "
        + ", ".join(invalid_method_experiment_tokens)
    )

# -----------------------------------------------------------------
# Shared Representation Dimensions
# -----------------------------------------------------------------
CLIP_VIDEO_EMBEDDING_DIM = 512
CLIP_TEXT_EMBEDDING_DIM = 512
AUTOENCODER_VIDEO_EMBEDDING_DIM = 256

HYBRID_VIDEO_EMBEDDING_DIM = (
    CLIP_VIDEO_EMBEDDING_DIM
    + AUTOENCODER_VIDEO_EMBEDDING_DIM
)

# Common latent dimension used by the fusion classifier.
FUSION_EMBEDDING_DIM = 128

VIDEO_REPRESENTATION_SOURCE_DIMENSIONS = {
    CLIP_VIDEO_REPRESENTATION_SOURCE: CLIP_VIDEO_EMBEDDING_DIM,
    AUTOENCODER_VIDEO_REPRESENTATION_SOURCE: (
        AUTOENCODER_VIDEO_EMBEDDING_DIM
    ),
    HYBRID_VIDEO_REPRESENTATION_SOURCE: (
        HYBRID_VIDEO_EMBEDDING_DIM
    ),
}


# -----------------------------------------------------------------
# Classifier Architecture
# -----------------------------------------------------------------
FUSION_MODEL_TYPE = "mlp"

# -----------------------------------------------------------------
# Fusion MLP Architecture
# -----------------------------------------------------------------
FUSION_NUM_INPUT_EMBEDDINGS = 3
FUSION_INPUT_DIM = (
    FUSION_NUM_INPUT_EMBEDDINGS
    * FUSION_EMBEDDING_DIM
)
FUSION_HIDDEN_DIM_1 = 256
FUSION_HIDDEN_DIM_2 = 64
FUSION_OUTPUT_DIM = 1
FUSION_DROPOUT = 0.20

# -----------------------------------------------------------------
# Training Hyperparameters
# -----------------------------------------------------------------
FUSION_BATCH_SIZE = 64
FUSION_LEARNING_RATE = 1e-3
FUSION_WEIGHT_DECAY = 1e-5
FUSION_EPOCHS = 100
FUSION_RANDOM_SEED = RANDOM_SEED

# -----------------------------------------------------------------
# Optimization
# -----------------------------------------------------------------
FUSION_OPTIMIZER = "adam"
FUSION_LOSS = "cross_entropy"

# -----------------------------------------------------------------
# Inference
# -----------------------------------------------------------------
FUSION_SCORE_REDUCTION = "argmax"

# -----------------------------------------------------------------
# Candidate Answers
# -----------------------------------------------------------------
NUM_MULTIPLE_CHOICE_ANSWERS = 5

# -----------------------------------------------------------------
# Projection Layers
# -----------------------------------------------------------------
USE_VIDEO_PROJECTION = True
USE_TEXT_PROJECTION = True
USE_BATCH_NORMALIZATION = False
USE_LAYER_NORMALIZATION = True

# -----------------------------------------------------------------
# Model Checkpoints
# -----------------------------------------------------------------
SAVE_FUSION_MODEL = True
FUSION_MODEL_FILENAME = "fusion_classifier.pt"

# -----------------------------------------------------------------
# Training Data Source
# -----------------------------------------------------------------
FUSION_TRAIN_SPLIT = "train"
FUSION_EVALUATION_SPLIT = "val"

# ============================================================
# 12. Video Segmentation Settings
# ============================================================

DEFAULT_SEGMENT_DURATION_SEC = 6.0
MIN_SEGMENT_DURATION_SEC = 4.0
MAX_SEGMENT_DURATION_SEC = 8.0
DEFAULT_SEGMENT_STRATEGY = "fixed_duration"

ENABLE_HIERARCHICAL_SEGMENTS = False
PARENT_SEGMENT_DURATION_SEC = None
DEFAULT_SEGMENT_LEVEL = 0

ENABLE_MOTION_SCORING = False
ENABLE_SCENE_CHANGE_SCORING = False
DEFAULT_SCENE_CHANGE_SCORE = 0.0

DEFAULT_SEGMENT_STRIDE_SEC = 6.0
DEFAULT_MIN_SEGMENT_DURATION_SEC = 1.0


# ============================================================
# 13. Baseline VideoQA Model Settings
# ============================================================

BASELINE_MODEL_NAME = "Qwen/Qwen2-VL-7B-Instruct"
MAX_SEGMENTS_PER_VIDEO = 5
MAX_FRAMES_PER_QUESTION = 8
MAX_NEW_TOKENS = 64
TEMPERATURE = 0.0
DO_SAMPLE = False


# ============================================================
# 14. Autoencoder Training Settings
# ============================================================

AUTOENCODER_FRAME_SIZE = 128
AUTOENCODER_FRAMES_PER_SEGMENT = 8
AUTOENCODER_BATCH_SIZE = 8
AUTOENCODER_EPOCHS = 3
AUTOENCODER_LATENT_DIM = 256
AUTOENCODER_LEARNING_RATE = 1e-3
AUTOENCODER_RECONSTRUCTION_SAMPLE_COUNT = 10


# ============================================================
# 15. CLIP Text Representation Settings
# ============================================================

CLIP_TEXT_MODEL_NAME = "openai/clip-vit-base-patch32"
CLIP_TEXT_BATCH_SIZE = 32
CLIP_TEXT_REPRESENTATION_SCOPE = "questions_and_answer_choices"

TEXT_INPUT_TYPES = [
    "question_answer",
]


# ============================================================
# 16. CLIP Video Representation Settings
# ============================================================

CLIP_VIDEO_MODEL_NAME = "openai/clip-vit-base-patch32"
CLIP_VIDEO_REPRESENTATION_SCOPE = "referenced_videos"

CLIP_VIDEO_FRAMES_PER_VIDEO = 8
CLIP_VIDEO_FRAME_BATCH_SIZE = 16
CLIP_VIDEO_POOLING_METHOD = "mean"
CLIP_VIDEO_FILE_EXTENSIONS = [".mp4", ".avi", ".mov", ".mkv"]


# ============================================================
# 17. Training Metadata Schema
# ============================================================

TRAINING_SCHEMA = {
    "segment_id": "str",
    "video_id": "str",
    "split": "str",
    "video_path": "str",
    "segment_index": "int",

    "segment_level": "int",
    "parent_segment_id": "str",
    "segment_strategy": "str",

    "start_time_sec": "float",
    "midpoint_time_sec": "float",
    "end_time_sec": "float",

    "segment_duration_sec": "float",

    "start_frame_idx": "int",
    "midpoint_frame_idx": "int",
    "end_frame_idx": "int",

    "representative_frame_index": "int",

    "fps": "float",
    "frame_count": "int",
    "width": "int",
    "height": "int",

    "motion_score": "float",
    "scene_change_score": "float",
}

TRAINING_COLUMNS = list(TRAINING_SCHEMA.keys())

REQUIRED_TRAINING_COLUMNS = [
    "segment_id",
    "video_id",
    "split",
    "video_path",

    "start_time_sec",
    "midpoint_time_sec",
    "end_time_sec",

    "segment_duration_sec",

    "start_frame_idx",
    "midpoint_frame_idx",
    "end_frame_idx",

    "representative_frame_index",
]

UNIQUE_TRAINING_COLUMNS = [
    "segment_id",
]

RETRIEVAL_REFERENCE_COLUMNS = [
    "segment_id",
    "video_id",
    "video_path",

    "start_time_sec",
    "midpoint_time_sec",
    "end_time_sec",

    "start_frame_idx",
    "midpoint_frame_idx",
    "end_frame_idx",

    "representative_frame_index",

    "motion_score",
]
