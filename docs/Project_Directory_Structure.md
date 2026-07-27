---
title: Project Directory Structure
nav_order: 1
---

# Project Directory Structure

## Overview

This document describes the three complementary storage locations that together comprise the VideoQA research project:

1. **GitHub Repository** — stores version-controlled source code, notebooks, documentation, dataset metadata, and shared Python modules.
2. **Hugging Face Dataset Repository** — stores the large public ZIP archives required to restore the tutorial datasets and project artifacts.
3. **Google Drive Project Storage** — provides optional persistent storage for local archive copies and generated experiment artifacts.

Together, these three storage locations form a single logical project. The notebooks execute from the GitHub repository, restore required resources from locally available or mounted Google Drive archives when present, and otherwise download the public archives from Hugging Face.

This document serves as the primary reference for the project directory organization, storage conventions, public archive distribution, and notebook artifact dependencies.

## GitHub Repository Structure

The GitHub repository contains the version-controlled implementation of the VideoQA research project.

```text
videoqa-representation-comparison/
├── datasets/
│   └── NExT-QA/
│       ├── metadata/
│       ├── questions/
│       └── videos/
├── docs/
│   ├── index.md
│   ├── Project_Directory_Structure.md
│   ├── References.md
│   ├── Results_and_Insights.md
│   ├── 01_Run_Qwen2VL_Baseline.md
│   ├── 02_Prepare_Autoencoder_Segment_Metadata.md
│   ├── 03_Train_Video_Autoencoder.md
│   ├── 04_Validate_Autoencoder_Video_Representations.md
│   ├── 05_Generate_CLIP_Text_Representations.md
│   ├── 06_Generate_CLIP_Video_Representations.md
│   ├── 07_Run_Representation_VideoQA.md
│   ├── 08_Evaluate_Development_Results.md
│   └── images/
│       ├── overview_pipeline.png
│       └── workflow/
│           ├── 01_Run_Qwen2VL_Baseline_workflow.png
│           ├── 02_Prepare_Autoencoder_Segment_Metadata_workflow.png
│           ├── 03_Train_Video_Autoencoder_workflow.png
│           ├── 04_Validate_Autoencoder_Video_Representations_workflow.png
│           ├── 05_Generate_CLIP_Text_Representations_workflow.png
│           ├── 06_Generate_CLIP_Video_Representations_workflow.png
│           ├── 07_Run_Representation_VideoQA_workflow.png
│           ├── 08_Evaluate_Development_Results_workflow.png
│           └── code/
│               ├── 01_Run_Qwen2VL_Baseline_workflow.mmd
│               ├── 02_Prepare_Autoencoder_Segment_Metadata_workflow.mmd
│               ├── 03_Train_Video_Autoencoder_workflow.mmd
│               ├── 04_Validate_Autoencoder_Video_Representations_workflow.mmd
│               ├── 05_Generate_CLIP_Text_Representations_workflow.mmd
│               ├── 06_Generate_CLIP_Video_Representations_workflow.mmd
│               ├── 07_Run_Representation_VideoQA_workflow.mmd
│               └── 08_Evaluate_Development_Results_workflow.mmd
├── notebooks/
│   ├── 01_Run_Qwen2VL_Baseline.ipynb
│   ├── 02_Prepare_Autoencoder_Segment_Metadata.ipynb
│   ├── 03_Train_Video_Autoencoder.ipynb
│   ├── 04_Validate_Autoencoder_Video_Representations.ipynb
│   ├── 05_Generate_CLIP_Text_Representations.ipynb
│   ├── 06_Generate_CLIP_Video_Representations.ipynb
│   ├── 07_Run_Representation_VideoQA.ipynb
│   └── 08_Evaluate_Development_Results.ipynb
├── paper/
│   └── ECE-551_VideoQA_Representation_Comparison.pdf
├── src/
│   ├── autoencoder_model.py
│   ├── nextqa_metadata.py
│   ├── nextqa_video_cache.py
│   ├── training_metadata_io.py
│   ├── training_validation.py
│   ├── video_segments.py
│   ├── videoqa_fusion_training.py
│   ├── videoqa_project_restore.py
│   └── videoqa_representation_config.py
└── README.md
```

### GitHub Repository Directory Purposes

| Directory | Purpose |
|-----------|---------|
| `datasets/`  | NExT-QA dataset metadata, question annotations, and repository documentation. Large benchmark video archives are distributed separately through the project's public Hugging Face dataset repository. |
| `docs/` | GitHub Pages documentation, notebook descriptions, project documentation, references, and supporting images. |
| `notebooks/` | Google Colab notebooks implementing the complete VideoQA experimental workflow. |
| `src/` | Shared Python modules providing centralized project configuration, data management, validation, model definitions, and reusable utilities used throughout the notebooks. |
| `README.md` | Repository overview, project introduction, and navigation entry point. |

## Google Drive Project Structure

Google Drive provides optional persistent storage for local copies of the public tutorial archives and for experiment artifacts generated during notebook execution. While the public tutorial downloads the required archives from the project's Hugging Face dataset repository when necessary, Google Drive may be used to cache those archives locally and to preserve generated outputs between notebook sessions.

The current Google Drive project root is:

```text
/content/drive/MyDrive/VideoQA_Project
```

### Google Drive Directory Structure

```text
VideoQA_Project/
├── VideoQA_Project_Artifacts.zip
│
├── NExT-QA/
│   └── releases/
│       └── NExTVideo_combined.zip
│
├── representations/
│   └── clip/
│       ├── text/
│       └── video/
│
├── experiments/
│   ├── <experiment_1>/
│   ├── <experiment_2>/
│   ├── ...
│   └── <experiment_n>/
│
└── evaluation/
```

### Google Drive Directory Purposes

| Directory or Archive            | Purpose                                                                                                                                    |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `VideoQA_Project_Artifacts.zip` | Optional local Google Drive copy of the public project artifacts archive used by the tutorial.                                             |
| `NExT-QA/`                      | Optional local Google Drive copy of the NExT-QA benchmark video archive distributed through the project's Hugging Face dataset repository. |
| `representations/`              | Reusable CLIP representation artifacts generated independently of any specific experiment.                                                 |
| `representations/clip/text/`    | Shared `clip_text` representations used by both representation-based VideoQA methods.                                                      |
| `representations/clip/video/`   | `clip_video` representations used by the CLIP representation-based VideoQA method.                                                         |
| `experiments/`                  | Experiment-specific artifacts, including training metadata, trained models, autoencoder representations, and VideoQA prediction artifacts. |
| `evaluation/`                   | Cross-experiment evaluation summaries and final experiment-selection artifacts generated by Notebook 08.                                   |


## Relationship Between GitHub and Google Drive

The GitHub repository and Google Drive serve complementary roles within the VideoQA research project.

| GitHub Repository | Google Drive Project Storage |
|-------------------|------------------------------|
| Version-controlled notebooks | NExT-QA video archives |
| Shared Python modules | Shared `clip_text` representations |
| Dataset metadata and question annotations | `clip_video` representations |
| Project documentation | Experiment-specific training artifacts |
| Configuration files | Trained autoencoder models |
| Pipeline diagrams | Autoencoder representation artifacts |
| Repository history | VideoQA prediction artifacts |
| Source code | Evaluation artifacts |

The notebooks provide the connection between these two environments. They are maintained in the GitHub repository, executed within Google Colab, and generate persistent experiment artifacts in Google Drive.

This separation keeps the GitHub repository lightweight and reproducible while allowing Google Drive to store large datasets, trained models, learned representations, prediction artifacts, and evaluation results generated during experimentation.

## Generated Artifact Categories

The following table summarizes the primary artifacts generated throughout the VideoQA workflow.

| Artifact Category | Generated By |
|----------|--------------|
| Baseline predictions | Notebook 01 |
| Training metadata | Notebook 02 |
| Autoencoder models and representations | Notebook 03 |
| Validated representations | Notebook 04 |
| CLIP text representations | Notebook 05 |
| CLIP video representations | Notebook 06 |
| Representation VideoQA predictions | Notebook 07 |
| Evaluation reports | Notebook 08 |

## Notebook Artifact Flow

The following table summarizes the primary artifacts generated by each notebook and the downstream notebooks that consume them.

| Notebook | Primary Outputs | Used By |
|----------|-----------------------------|-------------------|
| **01** | Baseline prediction, validation, and summary artifacts | Notebook 08 |
| **02** | Autoencoder training metadata and training summary artifacts | Notebook 03 |
| **03** | Trained autoencoder model, segment representations, video representations, and training reports | Notebooks 04, 07 |
| **04** | Validated autoencoder representations and standardized representation artifacts | Notebook 07 |
| **05** | Shared `clip_text` representation artifacts | Notebook 07 |
| **06** | `clip_video` representation artifacts | Notebook 07 |
| **07** | Representation-based prediction, validation, summary and training-history artifacts | Notebook 08 |
| **08** | Evaluation metrics, comparison reports, visualizations, and experiment selection artifacts | Final experiment report |

## Project Configuration

Project-wide paths, experiment parameters, artifact locations, and shared project configuration are centralized in:

```text
src/videoqa_representation_config.py
```

Experiment-specific paths and artifact aliases are initialized by each notebook using `configure_experiment(EXPERIMENT_NAME)`. This design keeps the shared configuration module import-safe while providing a consistent set of experiment-specific paths and artifact names across all notebooks.

This shared configuration module provides a consistent interface across all notebooks by defining:

- Repository and Google Drive directory paths
- Dataset configuration and metadata locations
- Shared CLIP representation locations
- Video representation source configuration
- Representation-based VideoQA prediction methods
- Video segmentation parameters
- Baseline and autoencoder model settings
- CLIP text and video representation settings
- Training metadata schema
- Experiment directory helper functions
- Standardized artifact filenames

Centralizing these settings ensures that all notebooks use consistent directory structures, artifact names, and experiment configurations throughout the project.

## Important Notes

- The GitHub repository is the authoritative source for the project implementation. Google Drive stores datasets and generated experiment artifacts.
- Shared `clip_text` representations are generated once by Notebook 05 and are reused by both representation-based VideoQA methods.
- `autoencoder_video` representations are generated by Notebook 03 and validated and standardized by Notebook 04.
- Notebook 07 implements a configurable representation-based VideoQA framework supporting cosine similarity and multiple learned fusion classifiers.
- Notebook 08 evaluates all implemented methods using a common multiple-choice evaluation framework and standardized evaluation metrics.

