# ============================================
# Core Project Directories
# ============================================
from pathlib import Path

# -------------------------------------------------
# Base project directory
# -------------------------------------------------
BASE_DIR = Path("/content/videoqa_representation_comparison")

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

# ============================================================
# Dataset Directories
# ============================================================
DATASET_DIR = DATASET_CONFIG[DATASET_NAME]["dataset_dir"]
VIDEOS_DIR = DATASET_CONFIG[DATASET_NAME]["videos_dir"]
QUESTIONS_DIR = DATASET_CONFIG[DATASET_NAME]["questions_dir"]
METADATA_DIR = DATASET_CONFIG[DATASET_NAME]["metadata_dir"]

# ============================================================
# Project Output Directories
# ============================================================
OUTPUTS_DIR = BASE_DIR / "outputs"
EVIDENCE_DIR = OUTPUTS_DIR / "evidence"
KNOWLEDGE_BASE_DIR = OUTPUTS_DIR / "knowledge_base"
EVALUATION_DIR = OUTPUTS_DIR / "evaluation"

# ============================================================
# Frame / Clip Extraction Settings
# ============================================================

# ============================================================
# Embedding Model Configuration
# ============================================================

# ============================================================
# Vector Database Configuration
# ============================================================

# ============================================================
# RAG Workflow Configuration
# ============================================================

# ============================================================
# Evaluation Settings
# ============================================================

# ============================================================
# Runtime / Debug Settings
# ============================================================
