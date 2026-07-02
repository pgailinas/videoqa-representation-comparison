---
title: Project Directory Structure
nav_order: 1
---

# Project Directory Structure

## Overview

This document describes the two complementary directory structures that together comprise the VideoQA research project:

1. **GitHub Repository** — stores source code, notebooks, documentation, and configuration under version control.
2. **Google Drive Project Storage** — stores large datasets and generated artifacts that are impractical to maintain in GitHub.

The repository and Google Drive should be considered a single logical project. Notebooks execute from the GitHub repository while reading from and writing to the Google Drive project structure.

This document is intended to evolve into the authoritative reference for both:

- the project directory structures, and
- the generated artifacts created and consumed by each notebook.

## GitHub Repository Structure

The GitHub repository contains the version-controlled project materials: notebooks, source modules, documentation, configuration, and diagrams.

```text
videoqa-representation-comparison/
├── README.md
├── notebooks/
│   ├── 01_Run_Qwen2VL_Baseline.ipynb
│   ├── 02_Prepare_Autoencoder_Training_Data.ipynb
│   ├── 03_Train_Video_Autoencoder.ipynb
│   ├── 04_Generate_Autoencoder_Video_Representations.ipynb
│   ├── 05_Generate_CLIP_Text_Representations.ipynb
│   ├── 06_Generate_CLIP_Video_Representations.ipynb
│   ├── 07_Run_Representation_VideoQA.ipynb
│   ├── 08_Evaluate_Development_Results.ipynb
│   └── 09_Run_Final_Comparison_Experiment.ipynb
├── docs/
│   ├── _config.yml
│   ├── index.md
│   ├── Project_Directory_Structure.md
│   ├── Project_Decisions.md
│   ├── References.md
│   ├── Results_and_Insights.md
│   ├── 01_Run_Qwen2VL_Baseline.md
│   ├── 02_Prepare_Autoencoder_Training_Data.md
│   ├── 03_Train_Video_Autoencoder.md
│   ├── 04_Generate_Autoencoder_Video_Representations.md
│   ├── 05_Generate_CLIP_Text_Representations.md
│   ├── 06_Generate_CLIP_Video_Representations.md
│   ├── 07_Run_Representation_VideoQA.md
│   ├── 08_Evaluate_Development_Results.md
│   ├── 09_Run_Final_Comparison_Experiment.md
│   └── images/
│       └── overview_pipeline.png
└── src/
    ├── videoqa_representation_config.py
    ├── nextqa_metadata.py
    ├── nextqa_video_cache.py
    ├── training_metadata_io.py
    ├── training_validation.py
    └── video_segments.py
```

### GitHub Repository Directory Purposes

| Directory | Purpose |
|-----------|---------|
| `notebooks/` | Google Colab notebooks implementing each project stage. |
| `docs/` | GitHub Pages documentation, notebook descriptions, decisions, references, and results. |
| `docs/images/` | Diagrams and documentation images, including the pipeline overview figure. |
| `src/` | Shared Python modules and centralized project configuration. |

## Google Drive Project Structure

Google Drive stores persistent datasets and generated artifacts. This includes large files that should not be committed to GitHub, such as video archives, learned representations, trained models, prediction outputs, and evaluation reports.

The current Google Drive project root is:

```text
/content/drive/MyDrive/VideoQA_Project
```

Current observed structure:

```text
VideoQA_Project/
├── NExT-QA/
│   ├── releases/
│   │   └── NExTVideo_combined.zip
│   ├── NExTVideo.z01
│   ├── NExTVideo.z02
│   ├── NExTVideo.z03
│   ├── NExTVideo.z04
│   ├── NExTVideo.z05
│   ├── NExTVideo.z06
│   └── NExTVideo.zip
├── representations/
│   └── clip/
│       ├── text/
│       │   ├── clip_text_representations.csv
│       │   └── clip_text_representation_summary.csv
│       └── video/
│           ├── clip_video_representations.csv
│           └── clip_video_representation_summary.csv
├── experiments/
│   ├── ae_seg6s_stride4_dev25/
│   │   ├── training/
│   │   │   ├── metadata/
│   │   │   │   └── training_metadata.csv
│   │   │   └── reports/
│   │   │       └── training_data_summary.csv
│   │   └── autoencoder/
│   │       ├── models/
│   │       │   └── autoencoder.pt
│   │       ├── reconstructions/
│   │       ├── reports/
│   │       │   ├── config.json
│   │       │   ├── frame_metrics.csv
│   │       │   ├── reconstruction_metrics.csv
│   │       │   ├── reconstruction_samples.csv
│   │       │   ├── summary.csv
│   │       │   └── training_history.csv
│   │       └── representations/
│   │           ├── autoencoder_segment_representations.csv
│   │           ├── autoencoder_video_representations.csv
│   │           ├── autoencoder_representation_summary.csv
│   │           └── evaluation_representation_dataset.csv
│   └── Run_Qwen2VL_Baseline/
│       └── outputs/
│           └── baseline/
│               ├── baseline_predictions.csv
│               └── baseline_summary.csv
├── videoqa/
│   ├── baseline/
│   │   ├── baseline_predictions.csv
│   │   ├── baseline_summary.csv
│   │   └── baseline_validation.csv
│   └── clip_video/
│       ├── representation_videoqa_predictions.csv
│       ├── representation_videoqa_summary.csv
│       └── representation_videoqa_validation.csv
└── evaluation/
    └── clip_video/
        ├── answer_choice_distribution.csv
        ├── error_choice_pattern.csv
        ├── error_type_summary.csv
        ├── evaluation_dataset.csv
        ├── evaluation_metrics.csv
        ├── generated_figures.csv
        ├── incorrect_predictions.csv
        ├── prediction_quality_checks.csv
        └── question_type_metrics.csv
```

### Google Drive Directory Purposes

| Directory | Purpose |
|-----------|---------|
| `NExT-QA/` | Original NExT-QA dataset archives and reconstructed release archive. |
| `representations/` | Shared reusable representations that are not experiment-specific. |
| `representations/clip/text/` | Shared CLIP text embeddings generated once and reused by representation-based QA. |
| `representations/clip/video/` | Shared CLIP video embeddings generated once and reused by representation-based QA. |
| `experiments/` | Experiment-specific artifacts, especially autoencoder training data, models, and learned representations. |
| `videoqa/` | Prediction outputs from baseline and representation-based VideoQA notebooks. |
| `evaluation/` | Evaluation metrics, analysis reports, and generated result summaries. |

## Relationship Between GitHub and Google Drive

| GitHub Repository | Google Drive Project Storage |
|-------------------|------------------------------|
| Version-controlled notebooks | Large benchmark video archives |
| Source modules | Generated representations |
| Configuration files | Trained models |
| Documentation | Prediction outputs |
| Pipeline diagrams | Evaluation artifacts |

The notebooks are the bridge between the two structures. They are stored in GitHub, executed in Google Colab, and generate persistent artifacts in Google Drive.

## Generated Artifacts

This section is intended to evolve into the authoritative artifact registry. The initial entries below reflect the currently observed project artifacts.

| Artifact | Location | Generated By | Used By | Purpose | Essential |
|----------|----------|--------------|---------|---------|-----------|
| `baseline_predictions.csv` | `videoqa/baseline/` | Notebook 01 | Notebook 08 | Baseline Qwen2-VL predictions. | Yes |
| `baseline_summary.csv` | `videoqa/baseline/` | Notebook 01 | Notebook 08 / Notebook 09 | Baseline runtime and prediction summary. | Yes |
| `baseline_validation.csv` | `videoqa/baseline/` | Notebook 01 | Notebook 08 | Validation checks for baseline prediction artifacts. | Yes |
| `training_metadata.csv` | `experiments/<experiment>/training/metadata/` | Notebook 02 | Notebook 03 | Autoencoder training metadata. | Yes |
| `training_data_summary.csv` | `experiments/<experiment>/training/reports/` | Notebook 02 | Documentation / validation | Summary of prepared autoencoder training data. | Yes |
| `autoencoder.pt` | `experiments/<experiment>/autoencoder/models/` | Notebook 03 | Notebook 04 | Trained autoencoder model checkpoint. | Yes |
| `training_history.csv` | `experiments/<experiment>/autoencoder/reports/` | Notebook 03 | Documentation / analysis | Autoencoder training history. | Yes |
| `summary.csv` | `experiments/<experiment>/autoencoder/reports/` | Notebook 03 | Documentation / analysis | Autoencoder training summary. | Yes |
| `autoencoder_segment_representations.csv` | `experiments/<experiment>/autoencoder/representations/` | Notebook 04 | Notebook 04 / analysis | Segment-level autoencoder latent representations. | Yes |
| `autoencoder_video_representations.csv` | `experiments/<experiment>/autoencoder/representations/` | Notebook 04 | Notebook 07 | Video-level autoencoder representations. | Yes |
| `autoencoder_representation_summary.csv` | `experiments/<experiment>/autoencoder/representations/` | Notebook 04 | Documentation / validation | Summary of generated autoencoder representations. | Yes |
| `clip_text_representations.csv` | `representations/clip/text/` | Notebook 05 | Notebook 07 | Shared CLIP question and answer-choice embeddings. | Yes |
| `clip_text_representation_summary.csv` | `representations/clip/text/` | Notebook 05 | Documentation / validation | Summary of shared CLIP text embeddings. | Yes |
| `clip_video_representations.csv` | `representations/clip/video/` | Notebook 06 | Notebook 07 | Shared CLIP video embeddings. | Yes |
| `clip_video_representation_summary.csv` | `representations/clip/video/` | Notebook 06 | Documentation / validation | Summary of shared CLIP video embeddings. | Yes |
| `representation_videoqa_predictions.csv` | `videoqa/clip_video/` | Notebook 07 | Notebook 08 | Representation-based VideoQA predictions. | Yes |
| `representation_videoqa_summary.csv` | `videoqa/clip_video/` | Notebook 07 | Notebook 08 / Notebook 09 | Summary of representation-based VideoQA execution. | Yes |
| `representation_videoqa_validation.csv` | `videoqa/clip_video/` | Notebook 07 | Notebook 08 | Validation checks for representation-based predictions. | Yes |
| `evaluation_metrics.csv` | `evaluation/clip_video/` | Notebook 08 | Notebook 09 / reporting | Development evaluation metrics. | Yes |
| `evaluation_dataset.csv` | `evaluation/clip_video/` | Notebook 08 | Notebook 09 / analysis | Evaluation-ready joined dataset. | Yes |
| `incorrect_predictions.csv` | `evaluation/clip_video/` | Notebook 08 | Error analysis / reporting | Incorrect prediction records. | Optional |
| `question_type_metrics.csv` | `evaluation/clip_video/` | Notebook 08 | Reporting | Metrics grouped by question type. | Optional |
| `answer_choice_distribution.csv` | `evaluation/clip_video/` | Notebook 08 | Reporting | Distribution of predicted answer choices. | Optional |
| `generated_figures.csv` | `evaluation/clip_video/` | Notebook 08 | Reporting | Index of generated evaluation figures. | Optional |

## Notebook Artifact Flow

| Notebook | Primary Outputs | Primary Consumers |
|----------|-----------------|-------------------|
| 01 | Baseline predictions and summary | 08, 09 |
| 02 | Autoencoder training metadata | 03 |
| 03 | Trained autoencoder model and training reports | 04 |
| 04 | Autoencoder video representations | 07 |
| 05 | Shared CLIP text representations | 07 |
| 06 | Shared CLIP video representations | 07 |
| 07 | Representation-based VideoQA predictions | 08, 09 |
| 08 | Development evaluation reports | 09, final report |
| 09 | Final comparison results | Final report |

## Project Configuration

Project-wide paths, constants, and experiment settings are centralized in:

```text
src/videoqa_representation_config.py
```

This configuration file defines shared artifact locations, experiment-specific paths, notebook aliases, evaluation inputs, and output directories.

## Important Notes

- Shared CLIP text embeddings are not experiment-specific.
- Shared CLIP video embeddings are not experiment-specific.
- Autoencoder training outputs and learned representations are experiment-specific.
- Multiple-choice VideoQA is the only supported evaluation mode.
- Notebook 07 is intended to support both CLIP and autoencoder video representations through configuration.
- Notebook 08 is intended to evaluate baseline, CLIP representation, and autoencoder representation outputs through common evaluation logic.
- The `experiments/Run_Qwen2VL_Baseline/` directory appears to contain older baseline outputs; `videoqa/baseline/` should be treated as the current baseline output location unless the configuration indicates otherwise.

## Summary

This project uses a dual-storage architecture. GitHub manages source code, notebooks, configuration, and documentation. Google Drive stores large datasets and generated artifacts. Together, these structures support reproducible comparison of three VideoQA approaches:

- Qwen2-VL baseline inference,
- CLIP-based pretrained representations, and
- self-supervised autoencoder representations.

This document should be updated as the artifact registry matures, especially after Notebook 07 fully supports both representation sources and Notebook 09 produces final comparison outputs.

## TARGET STRUCTURE

VideoQA_Project/
├── representations/
│   └── clip/
│       ├── text/
│       └── video/
│
└── experiments/
    ├── qwen2vl_baseline_dev25/
    │   ├── videoqa/
    │   └── evaluation/
    │
    ├── clip_video_dev25/
    │   ├── videoqa/
    │   └── evaluation/
    │
    └── ae_seg6s_stride4_dev25/
        ├── training/
        ├── autoencoder/
        ├── videoqa/
        └── evaluation/

