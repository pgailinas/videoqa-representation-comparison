---
title: Project Directory Structure
nav_order: 2
---

# Project Directory Structure

## Overview

This project uses a structured directory layout to organize Video Question Answering (VideoQA) datasets, metadata, knowledge-base artifacts, retrieval indexes, and experiment workflows.

The design supports a reproducible research pipeline using Google Colab, GitHub, and modular notebook execution. Each processing stage produces artifacts that are reused by later stages, enabling comparison between baseline VideoQA, retrieval-augmented generation (RAG), and iterative retrieval approaches.

## Key Directories

### notebooks/

Contains the Google Colab notebooks implementing each stage of the VideoQA experimental workflow.

### docs/

Contains GitHub Pages documentation describing the project architecture, notebook workflows, results, and references.

- **images/** — stores diagrams and documentation images

### src/

Contains reusable project source files.

- **iterative_rag_config.py** — centralized configuration file for paths, constants, and shared project settings

### datasets/

Contains original benchmark dataset resources.

For NExT-QA:

- **archives/** — original benchmark video files in ZIP files
- **videos/** — original benchmark video files organized by source folders
- **questions/** — train, validation, and test question-answer splits
- **metadata/** — dataset mapping files and annotation resources

### knowledge_base/

Contains generated artifacts used by retrieval and reasoning pipelines.

- **frames/** — extracted video frames
- **clips/** — generated or processed video segments
- **captions/** — generated textual video descriptions
- **embeddings/** — multimodal feature representations
- **vector_index/** — searchable retrieval indexes
- **metadata/** — processed knowledge-base metadata

## Repository Structure

```text
iterative-video-rag/
│
├── README.md
│
├── notebooks/
│   ├── 01_Prepare_Video_Data.ipynb
│   ├── 02_Prepare_Video_Evidence.ipynb
│   ├── 03_Build_Video_Knowledge_Base.ipynb
│   ├── 04_Run_Baseline_VideoQA.ipynb
│   ├── 05_Run_RAG_VideoQA.ipynb
│   ├── 06_Run_Iterative_RAG_Experiments.ipynb
│   └── 07_Evaluate_and_Visualize_Results.ipynb
│
├── docs/
│   ├── _config.yml
│   ├── index.md
│   ├── 01_Prepare_Video_Data.md
│   ├── 02_Prepare_Video_Evidence.md
│   ├── 03_Build_Video_Knowledge_Base.md
│   ├── 04_Run_Baseline_VideoQA.md
│   ├── 05_Run_RAG_VideoQA.md
│   ├── 06_Run_Iterative_RAG_Experiments.md
│   ├── 07_Evaluate_and_Visualize_Results.md
│   ├── Project_Directory_Structure.md
│   ├── References.md
│   ├── Results_and_Insights.md
│   └── images/
│       └── overview_pipeline.png
│
├── src/
│   ├── nextqa_video_cache.py
│   └── iterative_rag_config.py
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
└── knowledge_base/
    └── NExT-QA/
        ├── frames/
        ├── clips/
        ├── captions/
        ├── embeddings/
        ├── vector_index/
        └── metadata/
```

## Google Drive Structure

Due to GitHub file size limitations, all image datasets are stored externally in Google Drive as ZIP files. When needed, notebooks download and extract the required ZIP file into the local Colab runtime.

```text
iterative-video-rag/
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

This file contains centralized constants and shared settings used throughout the notebook pipeline, including dataset locations, knowledge-base paths, generated artifacts, and experiment configuration.

## Important Notes

- Original benchmark datasets remain separated from generated knowledge-base artifacts.
- Large video files and generated embeddings may be stored externally when required due to repository size limits.
- Notebook stages are designed to be reproducible and independently verifiable.

## Summary

This directory structure supports a modular VideoQA research workflow where datasets, retrieval artifacts, model inputs, and evaluation results remain clearly separated. The organization enables reproducible experimentation with baseline models, RAG-enhanced inference, and iterative retrieval strategies.

