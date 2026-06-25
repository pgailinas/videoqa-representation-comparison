---
title: Project Directory Structure
nav_order: 1
---

# Project Directory Structure

## Overview

This project uses a structured directory layout to organize Video Question Answering (VideoQA) datasets, metadata, learned representations, experimental artifacts, and evaluation workflows.

The design supports a reproducible research pipeline using Google Colab, GitHub, and modular notebook execution. Each notebook produces reusable artifacts that support comparison of three VideoQA approaches:

- Qwen2-VL baseline inference
- CLIP-based pretrained video representations
- Self-supervised autoencoder video representations

This modular workflow enables each approach to be developed, evaluated, and compared independently while sharing common datasets, preprocessing, and evaluation procedures.

## Key Directories

### notebooks/

Contains the Google Colab notebooks implementing each stage of the VideoQA experimental workflow.

### docs/

Contains GitHub Pages documentation describing the project architecture, notebook workflows, results, and references.

- **images/** — stores diagrams and documentation images

### src/

Contains reusable project source files shared across multiple notebooks.

- **videoqa_representation_config.py** — centralized configuration file containing dataset locations, experiment parameters, output directories, and shared project constants
- **evidence_io.py** — utility functions for saving and loading generated preprocessing metadata
- **evidence_validation.py** — validation routines for generated metadata, timestamps, missing videos, and data integrity
- **nextqa_metadata.py** — utilities for loading NExT-QA question splits, metadata files, and dataset mappings
- **nextqa_video_cache.py** — functions for reconstructing video archives and managing the Colab video cache
- **video_evidence.py** — utilities for generating video segments and metadata used during autoencoder training

### datasets/

Contains original benchmark dataset resources.

For NExT-QA:

- **archives/** — original benchmark video files in ZIP files
- **videos/** — original benchmark video files organized by source folders
- **questions/** — train, validation, and test question-answer splits
- **metadata/** — dataset mapping files and annotation resources

### outputs/

Contains all artifacts generated during VideoQA experimentation.

Artifacts are organized by workflow stage to support reproducibility, representation comparison, and downstream evaluation.

Typical contents include:

* **baseline/** — Qwen2-VL baseline predictions, runtime summaries, and inference outputs.
* **evidence/** — preprocessing metadata and autoencoder training data generated from the original videos.
* **evaluation/** — evaluation metrics, experiment summaries, performance analysis, runtime statistics, and generated figures.
* **representations/** — CLIP representations, autoencoder latent representations, trained models, and related artifacts.

The outputs directory serves as the primary location for generated experiment artifacts that are reused by later notebooks and included in project reporting and performance comparisons.

## Repository Structure

```text
videoqa-representation-comparison/
│
├── README.md
│
├── notebooks/
│   ├── 01_Run_Qwen2VL_Baseline.ipynb
│   ├── 02_Prepare_Autoencoder_Training_Data.ipynb
│   ├── 03_Train_Video_Autoencoder.ipynb
│   ├── 04_Generate_Autoencoder_Video_Representations.ipynb
│   ├── 05_Generate_CLIP_Text_Representations.ipynb
│   ├── 06_Generate_CLIP_Video_Representations.ipynb
│   ├── 07_Run_Representation_VideoQA.ipynb
│   ├── 08_Evaluate_Development_Results.ipynb
│   └── 09_Run_Final_Full_Experiment.ipynb
│
├── docs/
│   ├── _config.yml
│   ├── index.md
│   ├── 01_Run_Qwen2VL_Baseline.md
│   ├── 02_Prepare_Autoencoder_Training_Data.md
│   ├── 03_Train_Video_Autoencoder.md
│   ├── 04_Generate_Autoencoder_Video_Representations.md
│   ├── 05_Generate_CLIP_Text_Representations.md
│   ├── 06_Generate_CLIP_Video_Representations.md
│   ├── 07_Run_Representation_VideoQA.md
│   ├── 08_Evaluate_Development_Results.md
│   ├── 09_Run_Final_Full_Experiment.md
│   ├── Project_Directory_Structure.md
│   ├── References.md
│   ├── Results_and_Insights.md
│   └── images/
│       └── overview_pipeline.png
│
├── src/
│   ├── videoqa_representation_config.py
│   ├── evidence_io.py
│   ├── evidence_validation.py
│   ├── nextqa_metadata.py
│   ├── nextqa_video_cache.py
│   └── video_evidence.py
│
├── datasets/
│   └── NExT-QA/
│       ├── archives/
│       ├── videos/
│       ├── questions/
│       │   ├── train.csv
│       │   ├── val.csv
│       │   └── test.csv
│       └── metadata/
│           ├── map_vid_vidorID.json
│           └── relation_annotation_nextqa.zip
│
└── outputs/
    ├── baseline/
    │   ├── baseline_predictions.csv
    │   └── baseline_summary.csv
    ├── evaluation/
    │   └── reports/
    │       ├── answer_length_metric.csv
    │       ├── category_metric.csv
    │       ├── evaluation_dataset.csv
    │       ├── evaluation_metrics.csv
    │       ├── evidence_analysis.csv
    │       ├── generated_figures.csv
    │       ├── prediction_analysis.csv
    │       ├── prediction_verification.csv
    │       ├── question_type_metrics.csv
    │       └── runtime_analysis.csv
    ├── evidence/
    │   ├── metadata/
    │   │   └── evidence_metadata.csv        
    │   └── reports/
    │      └── evidence_summary.csv
    └── representations/
        ├── autoencoder/
        ├── clip/
        │   ├── text/
        │   └── video/
        └── models/
```

## Google Drive Structure

Due to GitHub file size limitations, large video dataset files are stored externally in Google Drive as ZIP files. When needed, notebooks download and extract the required ZIP file into the local Colab runtime.

```text
videoqa-representation-comparison/
└── NExT-QA/
    ├── NExTVideo.z01
    ├── NExTVideo.z02
    ├── NExTVideo.z03
    ├── NExTVideo.z04
    ├── NExTVideo.z05
    ├── NExTVideo.z06
    ├── NExTVideo.zip
    └── README.txt
```

## Project Constants Declaration

The project uses a shared configuration file located at:

[Project Constants Declaration](Project_Config.html)

This file contains centralized constants and shared settings used throughout the notebook pipeline, including dataset locations, representation-learning paths, generated artifacts, and experiment configuration.

## Important Notes

- Original benchmark datasets remain separated from generated representation-learning artifacts and experiment outputs.
- Large video files, learned representations, and generated features may be stored externally when required due to repository size limits.
- Notebook stages are designed to be reproducible and independently verifiable.

## Summary

This directory structure supports a modular VideoQA research workflow where datasets, learned representations, model inputs, and evaluation results remain clearly separated. The organization enables reproducible experimentation with baseline VideoQA inference, pretrained video representations, and self-supervised autoencoder-based representation learning.

The structure is designed to support comparative representation-learning experiments while maintaining a consistent downstream VideoQA evaluation framework using Qwen2-VL-7B.

