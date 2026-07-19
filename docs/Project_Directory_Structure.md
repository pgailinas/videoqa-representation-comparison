---
title: Project Directory Structure
nav_order: 1
---

# Project Directory Structure

## Overview

This document describes the two complementary directory structures that together comprise the VideoQA research project:

1. **GitHub Repository** — stores version-controlled source code, notebooks, documentation, dataset metadata, and shared Python modules.
2. **Google Drive Project Storage** — stores large benchmark datasets and generated experiment artifacts that are impractical to maintain within the GitHub repository.

Together, these two storage locations form a single logical project. The notebooks execute from the GitHub repository while reading from and writing to the Google Drive project structure.

This document serves as the authoritative reference for:

- the GitHub repository organization,
- the Google Drive project organization,
- generated experiment artifacts,
- notebook artifact dependencies, and
- project storage conventions.

## GitHub Repository Structure

The GitHub repository contains the version-controlled implementation of the VideoQA research project, including datasets, notebooks, documentation, shared Python modules, and project configuration.

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
│   ├── 04_Generate_Autoencoder_Video_Representations.md
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
│           ├── 04_Generate_Autoencoder_Video_Representations_workflow.png
│           ├── 05_Generate_CLIP_Text_Representations_workflow.png
│           ├── 06_Generate_CLIP_Video_Representations_workflow.png
│           ├── 07_Run_Representation_VideoQA_workflow.png
│           ├── 08_Evaluate_Development_Results_workflow.png
│           └── code/
│               ├── 01_Run_Qwen2VL_Baseline_workflow.mmd
│               ├── 02_Prepare_Autoencoder_Segment_Metadata_workflow.mmd
│               ├── 03_Train_Video_Autoencoder_workflow.mmd
│               ├── 04_Generate_Autoencoder_Video_Representations_workflow.mmd
│               ├── 05_Generate_CLIP_Text_Representations_workflow.mmd
│               ├── 06_Generate_CLIP_Video_Representations_workflow.mmd
│               ├── 07_Run_Representation_VideoQA_workflow.mmd
│               └── 08_Evaluate_Development_Results_workflow.mmd
├── notebooks/
│   ├── 01_Run_Qwen2VL_Baseline.ipynb
│   ├── 02_Prepare_Autoencoder_Segment_Metadata.ipynb
│   ├── 03_Train_Video_Autoencoder.ipynb
│   ├── 04_Generate_Autoencoder_Video_Representations.ipynb
│   ├── 05_Generate_CLIP_Text_Representations.ipynb
│   ├── 06_Generate_CLIP_Video_Representations.ipynb
│   ├── 07_Run_Representation_VideoQA.ipynb
│   └── 08_Evaluate_Development_Results.ipynb
├── src/
│   ├── autoencoder_model.py
│   ├── nextqa_metadata.py
│   ├── nextqa_video_cache.py
│   ├── training_metadata_io.py
│   ├── training_validation.py
│   ├── video_segments.py
│   └── videoqa_representation_config.py
└── README.md
```

### GitHub Repository Directory Purposes

| Directory | Purpose |
|-----------|---------|
| `datasets/` | NExT-QA dataset metadata, question annotations, and repository documentation. Large benchmark videos are stored separately in Google Drive. |
| `docs/` | GitHub Pages documentation, notebook descriptions, project documentation, references, and supporting images. |
| `notebooks/` | Google Colab notebooks implementing the complete VideoQA experimental workflow. |
| `src/` | Shared Python modules providing configuration, data management, validation, model definitions, and reusable utilities used throughout the notebooks. |
| `README.md` | Repository overview, project introduction, and navigation entry point. |

## Google Drive Project Structure

Google Drive stores the persistent datasets and generated artifacts created during notebook execution. Large benchmark video archives, trained models, learned representations, prediction artifacts, and evaluation outputs are intentionally stored outside the GitHub repository.

The current Google Drive project root is:

```text
/content/drive/MyDrive/VideoQA_Project
```

### Google Drive Directory Structure

```text
VideoQA_Project/
├── NExT-QA/
│   ├── NExTVideo.z01
│   ├── NExTVideo.z02
│   ├── NExTVideo.z03
│   ├── NExTVideo.z04
│   ├── NExTVideo.z05
│   ├── NExTVideo.z06
│   ├── NExTVideo.zip
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

| Directory | Purpose |
|-----------|---------|
| `NExT-QA/` | Benchmark video archives and reconstructed release files used by the VideoQA experiments. |
| `representations/` | Reusable CLIP representation artifacts generated independently of any specific experiment. |
| `representations/clip/text/` | Shared `clip_text` representations used by both representation-based VideoQA methods. |
| `representations/clip/video/` | `clip_video` representations used by the CLIP representation-based VideoQA method. |
| `experiments/` | Experiment-specific artifacts, including training metadata, trained models, autoencoder representations, and VideoQA prediction artifacts. |
| `evaluation/` | Cross-experiment evaluation summaries and final experiment-selection artifacts generated by Notebook 08. |

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

## Generated Artifacts

The following table summarizes the primary artifacts generated throughout the VideoQA workflow. It identifies where each artifact is stored, which notebook generates it, which notebook consumes it, and its purpose within the project.

| Artifact Category| Generated By |
|----------|--------------|
| Baseline predictions | Notebook 01 |
| Training metadata | Notebook 02 |
| Autoencoder models and representations | Notebook 03 |
| Vaidated representations | Notebook 04 |
| CLIP text representations | Notebook 05 |
| CLIP video representations | Notebook 06 |
| Representation VideoQA predictions | Notebook 07 |
| Evaluation reports | Notebook 08 |

## Notebook Artifact Flow

The following table summarizes the primary artifacts generated by each notebook and the downstream notebooks that consume them.

| Notebook | Primary Artifacts Generated | Primary Consumers |
|----------|-----------------------------|-------------------|
| **01** | Baseline prediction, validation, and summary artifacts | Notebook 08 |
| **02** | Autoencoder training metadata and training summary artifacts | Notebook 03 |
| **03** | Trained autoencoder model, segment representations, video representations, and training reports | Notebooks 04, 07 |
| **04** | Validated autoencoder representations and standardized representation artifacts | Notebook 07 |
| **05** | Shared `clip_text` representation artifacts | Notebook 07 |
| **06** | `clip_video` representation artifacts | Notebook 07 |
| **07** | Representation-based prediction, validation, summary and training-history artifacts | Notebook 08 |
| **08** | Evaluation metrics, comparison reports, visualizations, and experiment selection artifacts | Notebook 09 |
| **09** | Final full-dataset experiment results and comparison artifacts | Final project report |

## Project Configuration

Project-wide paths, experiment parameters, artifact locations, and notebook configuration are centralized in:

```text
src/videoqa_representation_config.py
```

This shared configuration module provides a consistent interface across all notebooks by defining:

- Project directory locations
- Dataset paths
- Experiment names and output directories
- Development and full-dataset execution settings
- Representation source selection (`clip_video` or `autoencoder_video`)
- Prediction method configuration (cosine similarity or learned fusion classifier)
- Standardized artifact filenames
- Evaluation inputs and output locations

Centralizing these settings ensures that all notebooks use consistent directory structures, artifact names, and experiment configurations throughout the project.

## Important Notes

- The GitHub repository is the authoritative source for the project implementation. Google Drive stores datasets and generated experiment artifacts.
- Shared `clip_text` representations are generated once by Notebook 05 and are reused by both representation-based VideoQA methods.
- `clip_video` representations are generated by Notebook 06 and are used only by the CLIP representation-based VideoQA method.
- `autoencoder_video` representations are generated by Notebook 03 and validated and standardized by Notebook 04.
- Experiment-specific artifacts are organized under `experiments/<experiment_name>/`, allowing multiple experiments to coexist without overwriting one another.
- Notebook 07 implements a configurable representation-based VideoQA framework supporting cosine similarity and multiple learned fusion classifiers.
- The primary experimental variables are the video representation source and the selected representation-based prediction method.
- Notebook 08 evaluates all implemented methods using a common multiple-choice evaluation framework and standardized evaluation metrics.
- Multiple-choice VideoQA is the only supported evaluation mode in the current implementation.
- Project-wide paths, artifact locations, and experiment settings are centrally managed through `src/videoqa_representation_config.py`.

## Summary

The VideoQA research project uses a dual-storage architecture that separates version-controlled implementation from generated experiment artifacts.

The GitHub repository contains the notebooks, source code, dataset metadata, documentation, and shared project modules. Google Drive provides persistent storage for benchmark video archives, reusable representations, experiment-specific artifacts, trained models, prediction artifacts, and evaluation outputs.

The project implements three VideoQA methods:

- **Qwen2-VL Baseline** — Direct multiple-choice VideoQA using the original NExT-QA videos.
- **CLIP Representation Method** — Representation-based VideoQA using shared `clip_text` representations together with `clip_video` representations.
- **Autoencoder Representation Method** — Representation-based VideoQA using shared `clip_text` representations together with `autoencoder_video` representations.

The project organization, artifact registry, and notebook workflow provide a reproducible framework for training, validating, and comparing multiple VideoQA methods under a common multiple-choice evaluation framework while supporting multiple video representation sources and configurable representation-based prediction methods.

