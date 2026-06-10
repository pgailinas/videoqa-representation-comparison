---
title: 03 Run Baseline VideoQA
nav_order: 5
has_children: true
has_toc: false
---
# 03 Run Baseline VideoQA

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/iterative-video-rag/blob/main/notebooks/03_Run_Baseline_VideoQA.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

## Purpose

This notebook establishes baseline Video Question Answering (VideoQA) performance for the NExT-QA benchmark dataset using the Qwen2-VL-7B multimodal foundation model. The notebook evaluates question-answering performance using prepared video evidence and generates prediction results, inference statistics, and experiment summaries.

## Inputs

* Prepared NExT-QA video dataset
* Evidence metadata generated during video preprocessing
* NExT-QA question-answer annotation files

  * train.csv
  * val.csv
  * test.csv
* NExT-QA metadata resources
* Project configuration settings
* Shared utility modules and helper functions
* Qwen2-VL-7B model and processor

## Outputs

* Baseline VideoQA prediction dataset
* Predicted answers
* Ground-truth answers
* Question and video metadata
* Evidence usage statistics
* Inference timing metrics
* Baseline experiment summary report
* Sample prediction results for verification

## Processing Workflow

The notebook begins by configuring the project environment, loading required configuration settings, and restoring the prepared NExT-QA video dataset. NExT-QA question-answer annotations, video inventory information, and evidence metadata are then loaded and validated. Baseline inference parameters are configured, the runtime environment and GPU resources are verified, and the Qwen2-VL-7B multimodal model and processor are initialized. An evaluation dataset is prepared from the selected NExT-QA dataset split, after which VideoQA inference is performed using sampled video evidence supplied directly to the model. Generated predictions, ground-truth answers, evidence usage statistics, and inference timing information are collected and validated before being saved to persistent storage. Finally, summary statistics and experiment reports are generated, and representative prediction samples are displayed for qualitative review and verification.

## Notes

* Video evidence is sampled directly from source videos during inference.
* Baseline predictions, timing statistics, and experiment summaries are saved for later analysis.
* Runtime performance and GPU memory requirements depend on the selected model configuration, evaluation dataset size, and available Colab hardware resources.

## Next Notebook

➡️ [04 Build Video Knowledge Base](04_Build_Video_Knowledge_Base.md)



