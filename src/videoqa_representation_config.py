# ============================================
# Core Project Directories
# ============================================
from pathlib import Path

# EXTREMELY IMPORTANT
EXPERIMENT_NAME = "ae_seg6s_stride4_dev25"

# -------------------------------------------------
# Base project directory
# -------------------------------------------------
BASE_DIR = Path("/content/videoqa-representation-comparison")

# -------------------------------------------------
# Main data directories
# -------------------------------------------------
DATASETS_DIR = BASE_DIR / "datasets"

# ============================================
# Dataset Configuration
# ============================================
DATASET_CONFIG = {
    "NExT-QA": {
        "dataset_dir": DATASETS_DIR / "NExT-QA",
        "videos_dir": DATASETS_DIR / "NExT-QA" / "videos",
        "questions_dir": DATASETS_DIR / "NExT-QA" / "questions",
        "metadata_dir": DATASETS_DIR / "NExT-QA" / "metadata",
    },
}

# ============================================================
# Dataset Selection
# ============================================================
DATASET_NAME = "NExT-QA"
EXPECTED_VIDEO_COUNT = 5440

# ============================================================
# Dataset Directories
# ============================================================
DATASET_DIR = DATASET_CONFIG[DATASET_NAME]["dataset_dir"]
VIDEOS_DIR = DATASET_CONFIG[DATASET_NAME]["videos_dir"]
QUESTIONS_DIR = DATASET_CONFIG[DATASET_NAME]["questions_dir"]
METADATA_DIR = DATASET_CONFIG[DATASET_NAME]["metadata_dir"]

# ============================================================
# Archive Configuration
# ============================================================
ARCHIVES_DIR = DATASET_DIR / "archives"
NEXTQA_COMBINED_ARCHIVE_NAME = "NExTVideo_combined.zip"
NEXTQA_COMBINED_ARCHIVE_PATH = (ARCHIVES_DIR / NEXTQA_COMBINED_ARCHIVE_NAME)

# ============================================================
# Google Drive Output Directory# ============================================================
GOOGLE_DRIVE_ROOT = Path("/content/drive/MyDrive/VideoQA_Project")
EXPERIMENTS_DRIVE_DIR = GOOGLE_DRIVE_ROOT / "experiments"

# ============================================================
# Project Output Directories
# ============================================================
OUTPUTS_DIR = BASE_DIR / "outputs"
TRAINING_DATA_DIR = OUTPUTS_DIR / "training"
TRAINING_METADATA_DIR = TRAINING_DATA_DIR / "metadata"
TRAINING_REPORTS_DIR = TRAINING_DATA_DIR / "reports"
BASELINE_DIR = OUTPUTS_DIR / "baseline"
REPRESENTATIONS_DIR = OUTPUTS_DIR / "representations"
FINAL_EXPERIMENTS_DIR = OUTPUTS_DIR / "final"
EVALUATION_DIR = OUTPUTS_DIR / "evaluation"

# ============================================================
# Common Output Files
# ============================================================
TRAINING_METADATA_CSV = (TRAINING_METADATA_DIR / "training_metadata.csv")
TRAINING_VALIDATION_CSV = (TRAINING_REPORTS_DIR / "training_metadata_validation.csv")
TRAINING_SUMMARY_CSV = (TRAINING_REPORTS_DIR / "training_data_summary.csv")
BASELINE_PREDICTIONS_CSV = (BASELINE_DIR / "baseline_predictions.csv")
BASELINE_SUMMARY_CSV = (BASELINE_DIR / "baseline_summary.csv")

# ============================================================
# Video Segmentation Settings
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
# Development Experiment Settings
# ============================================================
DEVELOPMENT_SUBSET_SIZE = 25
EVALUATION_SPLIT = "val"
RANDOM_SEED = 42

# ============================================================
# Baseline VideoQA Settings
# ============================================================
MAX_SEGMENTS_PER_VIDEO = 5
MAX_FRAMES_PER_QUESTION = 8
MAX_NEW_TOKENS = 64
TEMPERATURE = 0.0
DO_SAMPLE = False

# ============================================================
# Autoencoder Training Settings
# ============================================================
AUTOENCODER_FRAME_SIZE = 128
AUTOENCODER_FRAMES_PER_SEGMENT = 8
AUTOENCODER_BATCH_SIZE = 8
AUTOENCODER_EPOCHS = 3
AUTOENCODER_LATENT_DIM = 256
AUTOENCODER_LEARNING_RATE = 1e-3
AUTOENCODER_RECONSTRUCTION_SAMPLE_COUNT = 10

# ============================================================
# Autoencoder Output Directories
# ============================================================
AUTOENCODER_DIR = OUTPUTS_DIR / "autoencoder"
AUTOENCODER_MODELS_DIR = (AUTOENCODER_DIR / "models")
AUTOENCODER_RECONSTRUCTIONS_DIR = (AUTOENCODER_DIR / "reconstructions")
AUTOENCODER_REPORTS_DIR = (AUTOENCODER_DIR / "reports")

# ============================================================
# Representation Output Directories
# ============================================================
AUTOENCODER_REPRESENTATIONS_DIR = (
    REPRESENTATIONS_DIR / "autoencoder"
)

CLIP_REPRESENTATIONS_DIR = (
    REPRESENTATIONS_DIR / "clip"
)

CLIP_TEXT_REPRESENTATIONS_DIR = (
    CLIP_REPRESENTATIONS_DIR / "text"
)

CLIP_VIDEO_REPRESENTATIONS_DIR = (
    CLIP_REPRESENTATIONS_DIR / "video"
)

# ============================================================
# Representation Output Files
# ============================================================
AUTOENCODER_REPRESENTATIONS_CSV = (
    AUTOENCODER_REPRESENTATIONS_DIR /
    "autoencoder_representations.csv"
)

AUTOENCODER_REPRESENTATION_SUMMARY_CSV = (
    AUTOENCODER_REPRESENTATIONS_DIR /
    "representation_summary.csv"
)

CLIP_TEXT_REPRESENTATIONS_CSV = (
    CLIP_TEXT_REPRESENTATIONS_DIR /
    "clip_text_representations.csv"
)

CLIP_VIDEO_REPRESENTATIONS_CSV = (
    CLIP_VIDEO_REPRESENTATIONS_DIR /
    "clip_video_representations.csv"
)

# ============================================================
# Training Metadata Schema
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

# Single source of truth
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

# ============================================================
# VideoQA Evaluation Settings
# ============================================================

ANSWER_MODE = "multiple_choice"
CHOICE_COLUMNS = ["a0", "a1", "a2", "a3", "a4"]
GROUND_TRUTH_ANSWER_COLUMN = "answer"
QUESTION_COLUMN = "question"
VIDEO_ID_COLUMN = "video"

# ============================================================
# Autoencoder Experiment Output Directories
# ============================================================

AUTOENCODER_EXPERIMENT_DIR = (
    EXPERIMENTS_DRIVE_DIR / EXPERIMENT_NAME
)

AUTOENCODER_TRAINING_DIR = (
    AUTOENCODER_EXPERIMENT_DIR / "training"
)

AUTOENCODER_TRAINING_METADATA_DIR = (
    AUTOENCODER_TRAINING_DIR / "metadata"
)

AUTOENCODER_REPRESENTATIONS_DRIVE_DIR = (
    AUTOENCODER_EXPERIMENT_DIR / "autoencoder" / "representations"
)

# ============================================================
# Autoencoder Experiment Output Files
# ============================================================

AUTOENCODER_TRAINING_METADATA_CSV = (
    AUTOENCODER_TRAINING_METADATA_DIR /
    "training_metadata.csv"
)

AUTOENCODER_SEGMENT_REPRESENTATIONS_CSV = (
    AUTOENCODER_REPRESENTATIONS_DRIVE_DIR /
    "autoencoder_segment_representations.csv"
)

AUTOENCODER_VIDEO_REPRESENTATIONS_CSV = (
    AUTOENCODER_REPRESENTATIONS_DRIVE_DIR /
    "autoencoder_video_representations.csv"
)




