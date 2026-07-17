---
title: Home
nav_order: 0
---

# Investigating Self-Supervised Autoencoder Learning for VideoQA

## Project Overview

This project investigates self-supervised autoencoder learning for Video Question Answering (VideoQA) using the NExT-QA benchmark dataset, pretrained CLIP representations, and the Qwen2-VL-7B multimodal foundation model.

The project evaluates three complementary VideoQA pipelines. The first establishes a baseline using Qwen2-VL and the original NExT-QA videos. The second performs representation-based VideoQA using pretrained `clip_video` representations together with shared `clip_text` representations. The third evaluates self-supervised `autoencoder_video` representations using the same shared `clip_text` representations.

Both representation-based pipelines use the same shared `clip_text` question-answer representations and a common evaluation framework. The active representation-based experiment may use cosine similarity or one of several learned multimodal fusion classifiers, allowing both the video representation source and the prediction method to be evaluated independently.

Experiments are conducted using a two-stage methodology consisting of development-mode experimentation followed by full-dataset evaluation. Shared `clip_text` and `clip_video` representation datasets are generated once and reused across experiments, while `autoencoder_video` representations remain experiment-specific. The repository provides a reproducible notebook-driven research environment for investigating representation learning and downstream VideoQA performance.

## Motivation and Research Problem

Video Question Answering (VideoQA) requires models to understand both the visual content of individual frames and the temporal relationships that occur throughout a video. Unlike static-image recognition, VideoQA demands reasoning about actions, events, object interactions, and causal relationships, making it a challenging benchmark for multimodal machine learning systems.

Recent advances in foundation models have demonstrated impressive VideoQA performance by processing video and text directly. At the same time, self-supervised learning has shown that compact feature representations can be learned from large collections of unlabeled data without requiring manual annotation. These learned representations have proven effective across a wide range of computer vision tasks, suggesting that they may also provide useful information for downstream VideoQA.

This project investigates whether learned video representations can support VideoQA reasoning without relying solely on direct processing of the original videos. Specifically, the study compares pretrained CLIP video representations with representations learned through self-supervised autoencoder training while using shared `clip_text` question-answer representations and a common representation-based evaluation framework.

By maintaining a consistent evaluation framework and varying only the method used to generate video representations, the project seeks to determine how representation learning influences VideoQA performance across temporal, causal, and descriptive reasoning tasks.

## Research Questions

This project investigates the following research questions:

1. Can self-supervised autoencoder training learn compact video representations that preserve the semantic and temporal information required for VideoQA?

2. How does VideoQA performance using learned autoencoder video representations compare with pretrained CLIP video embeddings under a common evaluation framework?

3. How closely do representation-based VideoQA approaches perform relative to the baseline Qwen2-VL system operating directly on the original videos?

4. Which NExT-QA reasoning categories (causal, temporal, and descriptive) are most affected by the choice of video representation?

5. What insights can be gained from comparing foundation-model inference with representation-based VideoQA using identical evaluation procedures?

## Dataset

The primary benchmark dataset used in this project is **NExT-QA**, a Video Question Answering (VideoQA) benchmark designed to evaluate visual understanding and reasoning across real-world video content. The dataset contains questions that require models to reason about actions, events, temporal relationships, and contextual interactions occurring within video sequences.

The NExT-QA benchmark contains 5,440 videos, 47,692 multiple-choice question-answer pairs, official training/validation/test splits, and supporting metadata linking questions to their corresponding videos.

Within this project, the NExT-QA videos serve three complementary purposes:

* **Baseline VideoQA** — Original videos are processed directly by Qwen2-VL-7B to establish baseline performance.
* **Representation Learning** — Unlabeled videos are used to train self-supervised autoencoder models and to generate pretrained CLIP video embeddings.
* **Evaluation** — The benchmark questions and answer choices are encoded once as a reusable shared CLIP question-answer representation dataset and combined with the video representations to evaluate downstream multiple-choice VideoQA performance.

Development-mode execution is used to validate notebook functionality and optimize experimental parameters before full-dataset evaluation. Final experimental results are generated using the complete NExT-QA dataset with the selected experimental configuration.

### NExT-QA Reasoning Categories

NExT-QA is designed to evaluate video understanding through three primary reasoning categories:

| Category | Description |
|----------|-------------|
| **Causal** | Why events occur and how actions produce outcomes. |
| **Temporal** | Event order and temporal relationships. |
| **Descriptive** | Objects, actions, attributes, locations, and counts. |

Evaluation results are reported both overall and by reasoning category to provide insight into how different video representations support temporal, causal, and descriptive reasoning tasks.

## Dataset Split Strategy

The NExT-QA benchmark provides three official dataset splits: **training**, **validation**, and **test**. Each split serves a distinct role within the experimental framework to ensure reproducible model development and unbiased performance evaluation.

| Dataset Split | Primary Purpose | Project Usage |
|---------------|-----------------|---------------|
| **Training** | Learn model parameters | Train the representation-based prediction models used by the learned fusion methods. |
| **Validation** | Development evaluation | Evaluate all experimental pipelines, compare competing video representations, perform error analysis, and select the best-performing experimental configuration. Development experiments may use reproducible subsets of the validation split (for example, 100 samples) to reduce computational cost while maintaining fair comparisons. |
| **Test** | Final benchmark evaluation | Reserved for future work and final benchmark evaluation. The test split is not used during model development or experiment selection. |

In addition to the official dataset splits, this project generates reusable CLIP text and CLIP video representation datasets. Because the CLIP encoders are pretrained and remain frozen throughout the experiments, these representations are generated once for the entire NExT-QA dataset (training, validation, and test) and reused by all representation-based pipelines. This avoids redundant computation while ensuring identical pretrained representations are used throughout the experimental framework.

The three VideoQA pipelines use the dataset splits differently depending on whether model learning is required.

| Pipeline | Training Split | Validation Split |
|----------|----------------|------------------|
| **Qwen2-VL Baseline** | Not required. The pretrained Qwen2-VL-7B foundation model performs inference directly on the original videos without additional training. | Performs multiple-choice VideoQA inference and evaluation using the validation split. |
| **CLIP Representation Pipeline** | Uses the precomputed CLIP video and shared CLIP question-answer representations to train the selected learned fusion classifier when applicable. Cosine similarity requires no training. | Uses the corresponding validation representations to generate predictions and evaluate the selected representation-based method. |
| **Autoencoder Representation Pipeline** | Trains the self-supervised video autoencoder using the training videos, generates learned video representations, and trains the selected learned fusion classifier when applicable. | Uses the learned validation representations to generate predictions and evaluate the selected representation-based method. |

This separation of responsibilities follows standard machine learning practice by reserving the validation split exclusively for development evaluation while using the training split for all learned model components. Because the CLIP representations are fixed pretrained features rather than learned models, they may be generated once for the complete dataset without introducing information leakage between the training and validation splits. As a result, all reported comparisons evaluate models on validation data that were not used to train the representation-based learning components.

## System Architecture

The experimental framework is organized around three complementary VideoQA pipelines that maintain a common evaluation methodology while varying the source of the video representations.

The **Baseline Pipeline** establishes a performance reference by processing the original NExT-QA videos directly with the Qwen2-VL-7B multimodal foundation model.

The **CLIP Representation Pipeline** combines reusable shared `clip_video` and `clip_text` question-answer representations and performs multiple-choice VideoQA using the configured representation-based prediction method.

The **Autoencoder Representation Pipeline** trains a self-supervised video autoencoder, generates experiment-specific `autoencoder_video` representations, and combines them with the same shared `clip_text` question-answer representations using the same configurable prediction framework.

By maintaining identical text representations, evaluation procedures, and candidate-generation workflow across both representation-based pipelines, the framework enables controlled comparison of different video representation sources while also supporting evaluation of multiple multimodal prediction methods.

---

### Pipeline Flowchart

<a href="images/overview_pipeline.png" target="_blank">
  <img src="images/overview_pipeline.png" width="800">
</a>

### Notebook Workflow

The project is organized as nine modular notebooks supporting the three experimental pipelines.

| Notebook | Purpose |
|----------|---------|
| **01_Run_Qwen2VL_Baseline** | Execute baseline multiple-choice VideoQA experiments using the original NExT-QA videos and Qwen2-VL-7B. |
| **02_Prepare_Autoencoder_Segment_Metadata** | Prepare standardized segment metadata required for self-supervised autoencoder learning. |
| **03_Train_Video_Autoencoder** | Train a self-supervised video autoencoder using unlabeled NExT-QA videos and generate segment-level and video-level latent representations. |
| **04_Validate_Autoencoder_Video_Representations** | Load, standardize, and validate the autoencoder video representation artifacts generated by Notebook 03 for downstream VideoQA experiments. |
| **05_Generate_CLIP_Text_Representations** | Generate reusable shared CLIP question-answer representations for every candidate answer in the NExT-QA dataset. |
| **06_Generate_CLIP_Video_Representations** | Generate reusable pretrained CLIP video representations for the NExT-QA videos. |
| **07_Run_Representation_VideoQA** | Execute representation-based multiple-choice VideoQA using shared `clip_text` question-answer representations together with either `clip_video` or `autoencoder_video` representations using the selected scoring or learned fusion method. |
| **08_Evaluate_Development_Results** | Compare all completed development experiments using common validation metrics, error analysis, question-type analysis, visualization, and experiment selection. |

Development-subset experiments are used to compare baseline, pretrained, and autoencoder representation methods and to select the best-performing configuration before full-dataset evaluation. After the experimental configuration has been finalized, the complete NExT-QA dataset is processed to generate the project's primary evaluation results.

## Expected Contributions

This project contributes a reproducible framework for comparing pretrained and learned video representations using a modular notebook-driven workflow that separates representation learning, representation preparation, and downstream VideoQA evaluation.

The experimental framework enables direct comparison by holding the shared `clip_text` question-answer representations, evaluation methodology, and candidate-generation workflow constant while varying the video representation source and, when desired, the representation-based prediction method. This controlled design supports reproducible comparison between pretrained and self-supervised video representations for downstream multiple-choice VideoQA.

The resulting notebook workflow provides a modular and reproducible research platform that separates shared representation generation, experiment-specific autoencoder representation learning, downstream VideoQA evaluation, and comparative performance analysis.

---

## References and Further Reading

Additional papers, datasets, models, and technical resources related to this project are available on the [References and Further Reading](References.md) page.

---

## Author

**Phil Gailinas**  
- M.S. Computer Engineering candidate  
- University of New Mexico
- Project initiated May 2026

## License

This project is intended for academic and research use.

