# ============================================
# Core Project Directories
# ============================================
from pathlib import Path

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
# Project Output Directories
# ============================================================
OUTPUTS_DIR = BASE_DIR / "outputs"
EVIDENCE_DIR = OUTPUTS_DIR / "evidence"
EVIDENCE_METADATA_DIR = EVIDENCE_DIR / "metadata"
EVIDENCE_REPORTS_DIR = EVIDENCE_DIR / "reports"
BASELINE_DIR = OUTPUTS_DIR / "baseline"
REPRESENTATIONS_DIR = OUTPUTS_DIR / "representations"
FINAL_EXPERIMENTS_DIR = OUTPUTS_DIR / "final"
EVALUATION_DIR = OUTPUTS_DIR / "evaluation"

# ============================================================
# Common Output Files
# ============================================================
EVIDENCE_METADATA_CSV = (EVIDENCE_METADATA_DIR / "evidence_metadata.csv")
EVIDENCE_VALIDATION_CSV = (EVIDENCE_REPORTS_DIR / "evidence_validation.csv")
EVIDENCE_SUMMARY_CSV = (EVIDENCE_REPORTS_DIR / "evidence_summary.csv")
BASELINE_PREDICTIONS_CSV = (BASELINE_DIR / "baseline_predictions.csv")
BASELINE_SUMMARY_CSV = (BASELINE_DIR / "baseline_summary.csv")

# ============================================================
# Evidence Generation Settings
# ============================================================
DEFAULT_SEGMENT_DURATION_SEC = 6.0
MIN_SEGMENT_DURATION_SEC = 4.0
MAX_SEGMENT_DURATION_SEC = 8.0
DEFAULT_SEGMENT_STRATEGY = "fixed_duration"
ENABLE_PARENT_EVIDENCE = False
PARENT_SEGMENT_DURATION_SEC = None
DEFAULT_EVIDENCE_LEVEL = 0
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
MAX_EVIDENCE_PER_VIDEO = 5
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




