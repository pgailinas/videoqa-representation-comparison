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

This notebook establishes baseline Video Question Answering (VideoQA) performance for the NExT-QA benchmark dataset using the Qwen2-VL-7B multimodal foundation model. The workflow loads prepared video resources and evidence metadata, configures baseline inference parameters, executes VideoQA inference on selected evaluation samples, validates generated predictions, and produces baseline experiment reports and performance statistics.

## Inputs

* Prepared NExT-QA video dataset
* Evidence metadata generated during video preprocessing
* NExT-QA question-answer annotation files
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

* Configure runtime environment and project settings
* Restore the prepared NExT-QA video dataset
* Load NExT-QA annotations and video inventory information
* Load evidence metadata generated during preprocessing
* Configure baseline inference parameters
* Verify GPU runtime and model dependencies
* Load the Qwen2-VL-7B model and processor
* Prepare the evaluation dataset
* Execute baseline VideoQA inference using sampled video evidence
* Validate generated prediction results
* Save prediction datasets and experiment outputs
* Generate baseline summary statistics and reports
* Display representative prediction samples for qualitative review

## Runtime Requirements

Baseline VideoQA inference was evaluated using Google Colab GPU runtimes.

### Recommended GPU

* NVIDIA L4 GPU
  * Successfully executed Qwen2-VL-7B inference
  * Stable memory utilization
  * Average runtime approximately 2.2 seconds per sample during baseline testing

### Limited-Support GPU

* NVIDIA T4 GPU
  * Model loading is possible
  * Inference may encounter CUDA out-of-memory errors
  * Reliability depends on available Colab memory allocation and runtime configuration

### CPU Execution

* Supported for functional testing
* Significantly slower than GPU execution
* Not recommended for large-scale evaluation

## Notes

* This notebook establishes baseline VideoQA performance using direct multimodal inference.
* Video evidence is sampled directly from source videos during inference execution.
* Prediction results include generated answers, ground-truth answers, evidence statistics, and inference timing information.
* Runtime performance depends on the selected evaluation dataset size, inference configuration, and available GPU resources.
* GPU memory requirements may vary significantly based on the number of sampled video frames and model generation settings.
* Generated prediction datasets and summary reports provide the foundation for subsequent experimental evaluation and analysis.

