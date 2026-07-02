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
#      GOOGLE_DRIVE_ROOT / "experiments" / <experiment_name>.
#
# Shared CLIP text/video representations are intentionally not stored
# inside individual experiment folders. Prediction and evaluation results
# are experiment-specific and should be stored inside each experiment.
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
# 2. Experiment Names
# ============================================================
#
# These names define persistent experiment folders under:
#
#   /content/drive/MyDrive/VideoQA_Project/experiments/
#
# Notebook 07 and later notebooks may scan EXPERIMENTS_DRIVE_DIR to
# discover available experiments instead of hard-coding experiment names.
# ============================================================

BASELINE_EXPERIMENT_NAME = "qwen2vl_baseline_dev25"
CLIP_VIDEO_EXPERIMENT_NAME = "clip_video_dev25"

# EXTREMELY IMPORTANT:
# This is the active autoencoder experiment used by Notebooks 02-04.
EXPERIMENT_NAME = "ae_seg6s_stride4_dev25"
AUTOENCODER_EXPERIMENT_NAME = EXPERIMENT_NAME


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

DEVELOPMENT_SUBSET_SIZE = 25
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
# 7. Baseline Experiment Paths
# ============================================================

BASELINE_EXPERIMENT_DIR = get_drive_experiment_dir(BASELINE_EXPERIMENT_NAME)
BASELINE_VIDEOQA_DRIVE_DIR = BASELINE_EXPERIMENT_DIR / "videoqa"
BASELINE_EVALUATION_DRIVE_DIR = BASELINE_EXPERIMENT_DIR / "evaluation"

BASELINE_PREDICTIONS_DRIVE_CSV = (
    BASELINE_VIDEOQA_DRIVE_DIR / "baseline_predictions.csv"
)
BASELINE_VALIDATION_DRIVE_CSV = (
    BASELINE_VIDEOQA_DRIVE_DIR / "baseline_validation.csv"
)
BASELINE_SUMMARY_DRIVE_CSV = (
    BASELINE_VIDEOQA_DRIVE_DIR / "baseline_summary.csv"
)

# Local temporary baseline outputs.
BASELINE_LOCAL_EXPERIMENT_DIR = get_local_experiment_dir(BASELINE_EXPERIMENT_NAME)
BASELINE_DIR = BASELINE_LOCAL_EXPERIMENT_DIR / "videoqa"

BASELINE_PREDICTIONS_CSV = BASELINE_DIR / "baseline_predictions.csv"
BASELINE_VALIDATION_CSV = BASELINE_DIR / "baseline_validation.csv"
BASELINE_SUMMARY_CSV = BASELINE_DIR / "baseline_summary.csv"


# ============================================================
# 8. CLIP Video Experiment Paths
# ============================================================
#
# The shared CLIP video embeddings remain under representations/clip/video.
# The downstream VideoQA and evaluation results belong to this experiment.
# ============================================================

CLIP_VIDEO_EXPERIMENT_DIR = get_drive_experiment_dir(CLIP_VIDEO_EXPERIMENT_NAME)
CLIP_VIDEOQA_DRIVE_DIR = CLIP_VIDEO_EXPERIMENT_DIR / "videoqa"
CLIP_VIDEO_EVALUATION_DRIVE_DIR = CLIP_VIDEO_EXPERIMENT_DIR / "evaluation"

CLIP_VIDEOQA_PREDICTIONS_DRIVE_CSV = (
    CLIP_VIDEOQA_DRIVE_DIR / "representation_videoqa_predictions.csv"
)
CLIP_VIDEOQA_VALIDATION_DRIVE_CSV = (
    CLIP_VIDEOQA_DRIVE_DIR / "representation_videoqa_validation.csv"
)
CLIP_VIDEOQA_SUMMARY_DRIVE_CSV = (
    CLIP_VIDEOQA_DRIVE_DIR / "representation_videoqa_summary.csv"
)

# Local temporary CLIP VideoQA outputs.
CLIP_VIDEO_LOCAL_EXPERIMENT_DIR = get_local_experiment_dir(CLIP_VIDEO_EXPERIMENT_NAME)
CLIP_VIDEOQA_DIR = CLIP_VIDEO_LOCAL_EXPERIMENT_DIR / "videoqa"

CLIP_VIDEOQA_PREDICTIONS_CSV = (
    CLIP_VIDEOQA_DIR / "representation_videoqa_predictions.csv"
)
CLIP_VIDEOQA_VALIDATION_CSV = (
    CLIP_VIDEOQA_DIR / "representation_videoqa_validation.csv"
)
CLIP_VIDEOQA_SUMMARY_CSV = (
    CLIP_VIDEOQA_DIR / "representation_videoqa_summary.csv"
)


# ============================================================
# 9. Autoencoder Experiment Paths
# ============================================================

AUTOENCODER_EXPERIMENT_DIR = get_drive_experiment_dir(AUTOENCODER_EXPERIMENT_NAME)

AUTOENCODER_TRAINING_DIR = AUTOENCODER_EXPERIMENT_DIR / "training"
AUTOENCODER_TRAINING_METADATA_DIR = AUTOENCODER_TRAINING_DIR / "metadata"
AUTOENCODER_TRAINING_REPORTS_DIR = AUTOENCODER_TRAINING_DIR / "reports"

AUTOENCODER_DIR = AUTOENCODER_EXPERIMENT_DIR / "autoencoder"
AUTOENCODER_MODELS_DIR = AUTOENCODER_DIR / "models"
AUTOENCODER_RECONSTRUCTIONS_DIR = AUTOENCODER_DIR / "reconstructions"
AUTOENCODER_REPORTS_DIR = AUTOENCODER_DIR / "reports"
AUTOENCODER_REPRESENTATIONS_DRIVE_DIR = AUTOENCODER_DIR / "representations"

AUTOENCODER_VIDEOQA_DRIVE_DIR = AUTOENCODER_EXPERIMENT_DIR / "videoqa"
AUTOENCODER_EVALUATION_DRIVE_DIR = AUTOENCODER_EXPERIMENT_DIR / "evaluation"

AUTOENCODER_TRAINING_METADATA_CSV = (
    AUTOENCODER_TRAINING_METADATA_DIR / "training_metadata.csv"
)
AUTOENCODER_TRAINING_SUMMARY_CSV = (
    AUTOENCODER_TRAINING_REPORTS_DIR / "training_data_summary.csv"
)
AUTOENCODER_TRAINING_VALIDATION_CSV = (
    AUTOENCODER_TRAINING_REPORTS_DIR / "training_metadata_validation.csv"
)

AUTOENCODER_MODEL_CSV_PLACEHOLDER = None  # Reserved for future model metadata if needed.
AUTOENCODER_MODEL_PATH = AUTOENCODER_MODELS_DIR / "autoencoder.pt"

AUTOENCODER_SEGMENT_REPRESENTATIONS_CSV = (
    AUTOENCODER_REPRESENTATIONS_DRIVE_DIR / "autoencoder_segment_representations.csv"
)
AUTOENCODER_VIDEO_REPRESENTATIONS_CSV = (
    AUTOENCODER_REPRESENTATIONS_DRIVE_DIR / "autoencoder_video_representations.csv"
)
AUTOENCODER_REPRESENTATION_SUMMARY_CSV = (
    AUTOENCODER_REPRESENTATIONS_DRIVE_DIR / "autoencoder_representation_summary.csv"
)
AUTOENCODER_EVALUATION_REPRESENTATION_DATASET_CSV = (
    AUTOENCODER_REPRESENTATIONS_DRIVE_DIR / "evaluation_representation_dataset.csv"
)

AUTOENCODER_VIDEOQA_PREDICTIONS_DRIVE_CSV = (
    AUTOENCODER_VIDEOQA_DRIVE_DIR / "representation_videoqa_predictions.csv"
)
AUTOENCODER_VIDEOQA_VALIDATION_DRIVE_CSV = (
    AUTOENCODER_VIDEOQA_DRIVE_DIR / "representation_videoqa_validation.csv"
)
AUTOENCODER_VIDEOQA_SUMMARY_DRIVE_CSV = (
    AUTOENCODER_VIDEOQA_DRIVE_DIR / "representation_videoqa_summary.csv"
)

# Local temporary autoencoder outputs mirror the experiment layout.
LOCAL_EXPERIMENT_DIR = get_local_experiment_dir(AUTOENCODER_EXPERIMENT_NAME)

TRAINING_DATA_DIR = LOCAL_EXPERIMENT_DIR / "training"
TRAINING_METADATA_DIR = TRAINING_DATA_DIR / "metadata"
TRAINING_REPORTS_DIR = TRAINING_DATA_DIR / "reports"

AUTOENCODER_LOCAL_DIR = LOCAL_EXPERIMENT_DIR / "autoencoder"
AUTOENCODER_LOCAL_MODELS_DIR = AUTOENCODER_LOCAL_DIR / "models"
AUTOENCODER_LOCAL_RECONSTRUCTIONS_DIR = AUTOENCODER_LOCAL_DIR / "reconstructions"
AUTOENCODER_LOCAL_REPORTS_DIR = AUTOENCODER_LOCAL_DIR / "reports"
AUTOENCODER_LOCAL_REPRESENTATIONS_DIR = AUTOENCODER_LOCAL_DIR / "representations"

TRAINING_METADATA_CSV = TRAINING_METADATA_DIR / "training_metadata.csv"
TRAINING_VALIDATION_CSV = TRAINING_REPORTS_DIR / "training_metadata_validation.csv"
TRAINING_SUMMARY_CSV = TRAINING_REPORTS_DIR / "training_data_summary.csv"

AUTOENCODER_LOCAL_SEGMENT_REPRESENTATIONS_CSV = (
    AUTOENCODER_LOCAL_REPRESENTATIONS_DIR / "autoencoder_segment_representations.csv"
)
AUTOENCODER_LOCAL_VIDEO_REPRESENTATIONS_CSV = (
    AUTOENCODER_LOCAL_REPRESENTATIONS_DIR / "autoencoder_video_representations.csv"
)

# Backward-compatible local autoencoder representation aliases.
AUTOENCODER_REPRESENTATIONS_DIR = REPRESENTATIONS_DIR / "autoencoder"
AUTOENCODER_REPRESENTATIONS_CSV = (
    AUTOENCODER_REPRESENTATIONS_DIR / "autoencoder_representations.csv"
)


# ============================================================
# 10. Representation-Based VideoQA Settings
# ============================================================

REPRESENTATION_VIDEOQA_METHOD = "cosine_similarity"

DEFAULT_VIDEO_REPRESENTATION_SOURCE = "clip_video"
DEFAULT_TEXT_REPRESENTATION_SOURCE = "clip_text"

REPRESENTATION_VIDEOQA_PREDICTIONS_FILENAME = "representation_videoqa_predictions.csv"
REPRESENTATION_VIDEOQA_VALIDATION_FILENAME = "representation_videoqa_validation.csv"
REPRESENTATION_VIDEOQA_SUMMARY_FILENAME = "representation_videoqa_summary.csv"

# Backward-compatible local root alias.
REPRESENTATION_VIDEOQA_DIR = OUTPUTS_DIR / "representation_videoqa"


# ============================================================
# 11. Development Evaluation Settings and Aliases
# ============================================================
#
# Select which completed experiment Notebook 08 evaluates by setting
# EVALUATION_EXPERIMENT_NAME and the corresponding source label.
# ============================================================

EVALUATION_SOURCE_NAME = "clip_video"
EVALUATION_EXPERIMENT_NAME = CLIP_VIDEO_EXPERIMENT_NAME

EVALUATION_EXPERIMENT_DIR = get_drive_experiment_dir(EVALUATION_EXPERIMENT_NAME)
EVALUATION_OUTPUT_DRIVE_DIR = EVALUATION_EXPERIMENT_DIR / "evaluation"

EVALUATION_PREDICTIONS_DRIVE_CSV = (
    EVALUATION_EXPERIMENT_DIR / "videoqa" / REPRESENTATION_VIDEOQA_PREDICTIONS_FILENAME
)
EVALUATION_VALIDATION_DRIVE_CSV = (
    EVALUATION_EXPERIMENT_DIR / "videoqa" / REPRESENTATION_VIDEOQA_VALIDATION_FILENAME
)
EVALUATION_SUMMARY_DRIVE_CSV = (
    EVALUATION_EXPERIMENT_DIR / "videoqa" / REPRESENTATION_VIDEOQA_SUMMARY_FILENAME
)

# Local temporary evaluation outputs.
EVALUATION_DIR = get_local_experiment_dir(EVALUATION_EXPERIMENT_NAME) / "evaluation"
EVALUATION_OUTPUT_DIR = EVALUATION_DIR

EVALUATION_PREDICTIONS_CSV = (
    get_local_experiment_dir(EVALUATION_EXPERIMENT_NAME)
    / "videoqa"
    / REPRESENTATION_VIDEOQA_PREDICTIONS_FILENAME
)
EVALUATION_VALIDATION_CSV = (
    get_local_experiment_dir(EVALUATION_EXPERIMENT_NAME)
    / "videoqa"
    / REPRESENTATION_VIDEOQA_VALIDATION_FILENAME
)
EVALUATION_SUMMARY_CSV = (
    get_local_experiment_dir(EVALUATION_EXPERIMENT_NAME)
    / "videoqa"
    / REPRESENTATION_VIDEOQA_SUMMARY_FILENAME
)

EVALUATION_DATASET_CSV = EVALUATION_OUTPUT_DIR / "evaluation_dataset.csv"
EVALUATION_METRICS_CSV = EVALUATION_OUTPUT_DIR / "evaluation_metrics.csv"
EVALUATION_DETAILS_CSV = EVALUATION_OUTPUT_DIR / "evaluation_details.csv"
EVALUATION_REPORT_SUMMARY_CSV = EVALUATION_OUTPUT_DIR / "evaluation_summary.csv"

# Optional compatibility aliases for older notebook code.
EVALUATION_DRIVE_DIR = GOOGLE_DRIVE_ROOT / "evaluation"
VIDEOQA_DRIVE_DIR = GOOGLE_DRIVE_ROOT / "videoqa"


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
    "question",
    "answer_choice",
]


# ============================================================
# 16. CLIP Video Representation Settings
# ============================================================

CLIP_VIDEO_MODEL_NAME = "openai/clip-vit-base-patch32"
CLIP_VIDEO_REPRESENTATION_SCOPE = "referenced_videos"
CLIP_VIDEO_REPRESENTATION_SOURCE = "clip_video"

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
