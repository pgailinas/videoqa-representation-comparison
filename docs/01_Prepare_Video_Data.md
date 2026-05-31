---
title: 01 Prepare Video Data
nav_order: 3
has_toc: false
---

# 01 Prepare Video Data

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/iterative-video-rag/blob/main/notebooks/01_Prepare_Video_Data.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

## Purpose

This notebook prepares the NExT-QA benchmark dataset for iterative Retrieval-Augmented Generation (RAG) Video Question Answering (VideoQA) experimentation. The workflow configures the runtime environment, verifies required dataset resources, reconstructs and extracts video archives, organizes dataset files, and validates the dataset structure required for downstream preprocessing, embedding generation, retrieval, and inference workflows.

## Inputs

* NExT-QA multipart video archive files stored in Google Drive
  * NExTVideo.z01
  * NExTVideo.z02
  * NExTVideo.z03
  * NExTVideo.z04
  * NExTVideo.z05
  * NExTVideo.z06
  * NExTVideo.zip
* NExT-QA question-answer annotation files
  * train.csv
  * val.csv
  * test.csv
* NExT-QA metadata resources
  * map_vid_vidorID.json
* Project configuration modules
* Google Drive access credentials

## Outputs

* Verified NExT-QA dataset directory structure
* Reconstructed and extracted NExT-QA video dataset
* Validated question-answer annotation files
* Verified metadata resources
* Dataset statistics and verification summaries
* Runtime environment configuration information

## Processing Workflow

* Configure runtime environment and project settings
* Mount Google Drive and verify dataset resources
* Verify NExT-QA archive, annotation, and metadata files
* Copy multipart video archives to local Colab storage
* Reconstruct the complete NExT-QA video archive
* Extract and organize video files into the project dataset structure
* Validate video, annotation, and metadata resources
* Display dataset statistics and verification summaries

## Notes

* This notebook focuses on dataset preparation and validation only.
* The NExT-QA benchmark serves as the primary VideoQA dataset for this project.
* Video archives are copied to local Colab storage and extracted locally to improve reliability and avoid Google Drive file-operation limitations.
* The NExTVideo dataset is distributed as a multipart ZIP archive consisting of seven archive files that reconstruct the complete video collection.
* Frame extraction, clip generation, embedding creation, vector indexing, retrieval, and inference workflows are performed in later notebooks.
* Video archive reconstruction and extraction may require significant storage space and execution time depending on the runtime environment.

## Next Notebook

➡️ [02 Build Video Knowledge Base](02_Build_Video_Knowledge_Base.md)

