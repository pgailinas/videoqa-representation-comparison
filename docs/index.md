---
title: Home
nav_order: 0
---

# Investigating Self-Supervised Autoencoder Learning for VideoQA

## Project Overview

This project investigates self-supervised autoencoder learning for Video Question Answering (VideoQA) using the NExT-QA benchmark dataset, pretrained CLIP representations, and the Qwen2-VL-7B multimodal foundation model.

The project compares three complementary approaches to VideoQA. The first establishes a baseline using Qwen2-VL and the original NExT-QA videos. The second evaluates pretrained CLIP video representations, while the third investigates whether compact video representations learned through self-supervised autoencoder training can provide comparable downstream VideoQA performance.

To enable a controlled comparison, both representation-based approaches use a common set of CLIP text representations for the questions and answer choices together with the same downstream VideoQA classifier. This experimental design isolates the impact of the video representation while minimizing differences introduced by the inference architecture.

Experiments are conducted using a two-stage methodology consisting of development-subset experimentation followed by full-dataset evaluation. The repository provides a reproducible notebook-driven research environment for investigating representation learning, multimodal reasoning, and downstream VideoQA performance.

## Motivation and Research Problem

Video Question Answering (VideoQA) requires models to understand both the visual content of individual frames and the temporal relationships that occur throughout a video. Unlike static-image recognition, VideoQA demands reasoning about actions, events, object interactions, and causal relationships, making it a challenging benchmark for multimodal machine learning systems.

Recent advances in foundation models have demonstrated impressive VideoQA performance by processing video and text directly. At the same time, self-supervised learning has shown that compact feature representations can be learned from large collections of unlabeled data without requiring manual annotation. These learned representations have proven effective across a wide range of computer vision tasks, suggesting that they may also provide useful information for downstream VideoQA.

This project investigates whether learned video representations can support VideoQA reasoning without relying solely on direct processing of the original videos. Specifically, the study compares pretrained CLIP video representations with representations learned through self-supervised autoencoder training while using a common set of text representations and a shared downstream classifier.

By maintaining a consistent evaluation framework and varying only the method used to generate video representations, the project seeks to determine how representation learning influences downstream VideoQA performance across temporal, causal, and descriptive reasoning tasks.

## Research Questions

This project investigates the following research questions:

1. Can self-supervised autoencoder training learn compact video representations that preserve the semantic and temporal information required for downstream VideoQA?

2. How does VideoQA performance using learned autoencoder video representations compare with pretrained CLIP video representations under a common evaluation framework?

3. How closely do representation-based VideoQA approaches perform relative to the baseline Qwen2-VL system operating directly on the original videos?

4. Which NExT-QA reasoning categories (causal, temporal, and descriptive) are most affected by the choice of video representation?

5. Does self-supervised representation learning provide a practical alternative to pretrained video representations for downstream VideoQA tasks?

6. What insights can be gained from comparing foundation-model inference with representation-based VideoQA using identical evaluation procedures?

## Dataset

The primary benchmark dataset used in this project is **NExT-QA**, a Video Question Answering (VideoQA) benchmark designed to evaluate visual understanding and reasoning across real-world video content. The dataset contains questions that require models to reason about actions, events, temporal relationships, and contextual interactions occurring within video sequences.

The dataset provides raw video files, multiple-choice question-answer annotations, official training, validation, and test splits, together with supporting metadata linking each question to its corresponding source video.

The experimental dataset includes:

* NExT-QA video collection containing 5,440 MP4 videos organized within the NExTVideo directory structure
* Training, validation, and test question-answer splits containing 47,692 benchmark questions
* Video identifier mapping metadata
* Question categories and reasoning annotations

Within this project, the NExT-QA videos serve three complementary purposes:

* **Baseline VideoQA** — Original videos are processed directly by Qwen2-VL-7B to establish baseline performance.
* **Representation Learning** — Unlabeled videos are used to train self-supervised autoencoder models and to generate pretrained CLIP video representations.
* **Evaluation** — The benchmark questions and answer choices are encoded as CLIP text representations and combined with the video representations to evaluate downstream multiple-choice VideoQA performance.

Development-subset experiments are used during parameter optimization to reduce computational cost. Final experimental results are generated using the complete NExT-QA dataset using the selected experimental configuration.

### NExT-QA Reasoning Categories

NExT-QA is designed to evaluate video understanding through three primary reasoning categories:

| Category | Description |
|----------|-------------|
| **Causal** | Why events occur and how actions produce outcomes. |
| **Temporal** | Event order and temporal relationships. |
| **Descriptive** | Objects, actions, attributes, locations, and counts. |

Evaluation results are reported both overall and by reasoning category to provide insight into how different video representations support temporal, causal, and descriptive reasoning tasks.

## System Architecture

The experimental framework is organized around three complementary VideoQA pipelines that evaluate different approaches to generating video representations while maintaining a consistent downstream evaluation methodology.

The **Baseline Pipeline** establishes a performance reference by processing the original NExT-QA videos directly with the Qwen2-VL-7B multimodal foundation model. This pipeline provides the benchmark against which all representation-based approaches are compared.

The **Pretrained Representation Pipeline** generates CLIP video representations from the NExT-QA videos together with CLIP text representations for the corresponding questions and answer choices. These shared representations are evaluated using a common downstream multiple-choice VideoQA classifier.

The **Autoencoder Representation Pipeline** trains a self-supervised video autoencoder using the NExT-QA videos, then uses the trained encoder to generate compact latent video representations. As with the pretrained pipeline, CLIP text representations and the same downstream classifier are used to evaluate VideoQA performance.

By using identical text representations, classification methods, and evaluation procedures for both representation-based pipelines, the experimental framework isolates the impact of the video representation itself. This controlled design enables direct comparison between pretrained and learned representations while providing a consistent baseline through Qwen2-VL-7B.

The modular notebook workflow allows each stage of the experimental pipeline to be executed, validated, and extended independently while supporting reproducible experimentation using both development subsets and the complete NExT-QA dataset.

---

### Pipeline Flowchart

<a href="images/overview_pipeline.png" target="_blank">
  <img src="images/overview_pipeline.png" width="800">
</a>

### Notebook Workflow

The project is organized as a collection of modular notebooks that support reproducible experimentation in representation learning and downstream multiple-choice Video Question Answering (VideoQA). The workflow consists of three complementary experimental pipelines together with shared evaluation and reporting notebooks.

| Notebook | Purpose |
|----------|---------|
| **01_Run_Qwen2VL_Baseline** | Execute baseline multiple-choice VideoQA experiments using the original NExT-QA videos and Qwen2-VL-7B. |
| **02_Prepare_Autoencoder_Training_Data** | Prepare training datasets and supporting metadata required for self-supervised autoencoder learning. |
| **03_Train_Video_Autoencoder** | Train self-supervised video autoencoder models using unlabeled NExT-QA videos. |
| **04_Generate_Autoencoder_Video_Representations** | Generate compact latent video representations using the trained autoencoder encoder. |
| **05_Generate_CLIP_Text_Representations** | Generate CLIP text representations for VideoQA questions and answer choices. |
| **06_Generate_CLIP_Video_Representations** | Generate pretrained CLIP video representations from the NExT-QA videos. |
| **07_Run_Representation_VideoQA** | Execute representation-based multiple-choice VideoQA using either pretrained CLIP or learned autoencoder video representations together with shared CLIP text representations. |
| **08_Evaluate_Development_Results** | Generate evaluation metrics, reasoning-category analysis, runtime statistics, visualizations, and comparison reports for development-subset experiments. |
| **09_Run_Final_Comparison_Experiment** | Execute the complete experimental workflow using the selected configuration and generate the project's final comparative results. |

The notebook workflow supports three experimental pipelines:

- **Pipeline A — Baseline VideoQA:** Establishes baseline performance using Qwen2-VL-7B and the original NExT-QA videos.
- **Pipeline B — Pretrained Representation VideoQA:** Evaluates pretrained CLIP video representations using shared CLIP text representations and a common downstream classifier.
- **Pipeline C — Autoencoder Representation VideoQA:** Evaluates learned autoencoder video representations using the same text representations, classifier, and evaluation methodology.

Development-subset experiments are used for workflow validation and parameter selection. After the experimental configuration has been finalized, the complete NExT-QA dataset is processed to generate the project's primary evaluation results.

## Expected Contributions

This project contributes a reproducible experimental framework for investigating representation learning within multiple-choice Video Question Answering (VideoQA) systems. By combining baseline foundation-model inference with pretrained and self-supervised representation-based approaches, the project provides a controlled methodology for evaluating how different video representations influence downstream VideoQA performance.

A primary contribution of this work is the direct comparison of pretrained CLIP video representations and self-supervised autoencoder representations under a common experimental framework. By maintaining consistent text representations, classification methods, and evaluation procedures, the study isolates the effect of the video representation itself and enables meaningful comparison between learned and pretrained approaches.

The project also contributes a modular notebook-based workflow that supports reproducible machine learning experimentation. The workflow separates baseline evaluation, representation generation, autoencoder training, downstream inference, and performance analysis into well-defined stages that can be executed, validated, and extended independently.

Experimental results are expected to provide insight into the effectiveness of self-supervised representation learning for VideoQA, the relative strengths of pretrained and learned video representations, and the impact of representation choice across the NExT-QA reasoning categories.

In addition to the experimental findings, the repository provides a documented research platform that can serve as a foundation for future investigations involving representation learning, multimodal foundation models, self-supervised learning, and Video Question Answering.

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

