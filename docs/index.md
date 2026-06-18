---
title: Home
nav_order: 0
---

# Investigating Self-Supervised Autoencoder Learning for VideoQA

## Project Overview

This project investigates self-supervised autoencoder learning for Video Question Answering (VideoQA) using the NExT-QA benchmark dataset and the Qwen2-VL-7B multimodal foundation model.

The central objective is to determine whether video representations learned through self-supervised training on unlabeled video data preserve sufficient semantic and temporal information to support downstream VideoQA tasks. Rather than training a new VideoQA model from scratch, the project focuses on learning compact video representations and evaluating their effectiveness using a fixed VideoQA inference model.

The study compares a baseline VideoQA workflow using original video evidence with an autoencoder-based workflow using reconstructed video evidence. By holding the VideoQA model constant and varying only the representation-learning stage, the project evaluates how representation compression affects downstream reasoning performance.

Experiments are conducted using a two-stage methodology consisting of development-subset experimentation followed by full-dataset evaluation. The repository provides a reproducible notebook-driven research environment for investigating self-supervised representation learning, video compression, multimodal reasoning, and downstream VideoQA performance.

## Motivation and Research Problem

The rapid growth of video-based data has created increasing demand for artificial intelligence systems capable of understanding visual content, motion, temporal relationships, and contextual interactions within complex video sequences. Unlike static-image analysis, Video Question Answering (VideoQA) requires reasoning across both spatial and temporal dimensions, making it a challenging benchmark for multimodal machine learning systems.

Recent advances in self-supervised learning have demonstrated that useful visual representations can be learned directly from unlabeled data. Autoencoders provide a particularly attractive approach because they learn compact latent representations by reconstructing input data rather than relying on manually annotated labels. This capability has the potential to reduce dependence on costly labeled datasets while still capturing meaningful semantic and temporal information.

Although self-supervised representation learning has achieved promising results across many computer vision tasks, an important question remains: do the learned representations preserve the information required for downstream reasoning tasks such as VideoQA? In particular, it is unclear how much video information can be compressed into latent representations before performance on temporal, causal, and descriptive reasoning tasks begins to degrade.

This project investigates that question by training autoencoders using unlabeled videos from the NExT-QA dataset and evaluating the resulting representations through downstream VideoQA performance. A baseline VideoQA workflow using original video evidence is compared with an autoencoder-based workflow using reconstructed video evidence. By holding the VideoQA model constant and varying only the representation-learning stage, the study seeks to determine whether self-supervised autoencoder learning can produce compact video representations that preserve sufficient information for accurate VideoQA reasoning.

## Research Objectives

The objectives of this project are:

1. Learn compact video representations using self-supervised autoencoder training.
2. Evaluate reconstructed-video performance on downstream VideoQA tasks.
3. Measure the relationship between compression, reconstruction quality, and VideoQA accuracy.
4. Compare autoencoder-based VideoQA against a baseline workflow using original video evidence.
5. Analyze reasoning performance across NExT-QA categories.

## Research Questions

This project investigates the following research questions:

1. Can self-supervised autoencoder training learn compact video representations from unlabeled video data while preserving information relevant to Video Question Answering (VideoQA)?

2. How does VideoQA performance change when reconstructed video evidence generated from learned autoencoder representations is used instead of original video evidence?

3. What relationship exists between representation compression, reconstruction quality, and downstream VideoQA performance?

4. How do learned autoencoder representations affect causal, temporal, and descriptive reasoning performance within the NExT-QA benchmark dataset?

5. Can self-supervised autoencoder representations reduce storage and computational requirements while maintaining acceptable VideoQA accuracy?

6. To what extent does information loss introduced by video compression impact downstream multimodal reasoning performance?

## Dataset

The primary benchmark dataset used in this project is NExT-QA, a Video Question Answering (VideoQA) dataset designed to evaluate visual understanding and reasoning across real-world video content. NExT-QA contains questions that require models to reason about actions, events, temporal relationships, and contextual interactions occurring within video sequences.

The dataset provides raw video files, question-answer annotations, official training, validation, and test splits, and supporting metadata that associates questions with their corresponding source videos.

The experimental dataset includes:

* NExT-QA video collection containing 5,440 MP4 videos organized within the NExTVideo directory structure
* Training, validation, and test question-answer splits containing 47,692 benchmark questions
* Video identifier mapping metadata
* Question categories and reasoning annotations

Within this project, the NExT-QA videos serve two distinct purposes. During self-supervised learning, the videos are used without questions, answer choices, or ground-truth labels to train autoencoder models and learn compact video representations. During evaluation, the NExT-QA questions and answers are used to measure how well the learned representations support downstream VideoQA reasoning.

### NExT-QA Reasoning Categories

NExT-QA is designed to evaluate video understanding through three primary reasoning categories:

| Category    | Description                                          |
| ----------- | ---------------------------------------------------- |
| Causal      | Why events occur and how actions produce outcomes.   |
| Temporal    | Event order and temporal relationships.              |
| Descriptive | Objects, actions, attributes, locations, and counts. |

These reasoning categories provide an important evaluation dimension for this project. Experimental results will be analyzed both overall and by reasoning category to determine how well information learned through self-supervised autoencoder training supports causal, temporal, and descriptive reasoning tasks.

Raw videos are processed into structured evidence segments containing temporal metadata, video segment boundaries, and representative frame information. These evidence segments serve as the foundation for autoencoder training, video reconstruction, compression analysis, and downstream VideoQA experimentation.

## System Architecture

The experimental framework combines self-supervised autoencoder learning with multimodal Video Question Answering (VideoQA) using the NExT-QA benchmark dataset and the Qwen2-VL-7B foundation model.

Video preprocessing generates structured evidence records consisting of temporal video segments, frame samples, and associated metadata. These evidence segments serve as the foundation for both baseline VideoQA experiments and self-supervised autoencoder training.

The system architecture supports two primary experimental workflows:

1. **Baseline VideoQA** — Direct VideoQA inference using original video evidence and Qwen2-VL-7B.

2. **Autoencoder-Based VideoQA** — Self-supervised autoencoder training using unlabeled video evidence, generation of reconstructed video segments, and downstream VideoQA inference using Qwen2-VL-7B.

During the self-supervised learning phase, the autoencoder is trained using only video evidence. Questions, answer choices, and ground-truth labels are not used during representation learning. The autoencoder learns compact latent representations by encoding and reconstructing video segments, encouraging the model to capture meaningful semantic and temporal information while reducing data dimensionality.

The learned representations are evaluated by reconstructing video evidence and providing the reconstructed videos to Qwen2-VL-7B for VideoQA inference. Performance is compared against a baseline workflow that uses the original video evidence directly. This design enables assessment of how much information is preserved by the learned representations and how representation compression affects downstream reasoning performance.

Qwen2-VL-7B serves as the fixed VideoQA inference model throughout all experiments. By holding the downstream reasoning model constant and varying only the representation-learning stage, the architecture isolates the effects of self-supervised autoencoder learning on VideoQA performance, reasoning quality, compression efficiency, and computational requirements.

---

### Pipeline Flowchart

<a href="images/overview_pipeline.png" target="_blank">
  <img src="images/overview_pipeline.png" width="800">
</a>

### Notebook Workflow

The project is organized as a sequence of notebooks that support reproducible experimentation in self-supervised autoencoder learning and downstream Video Question Answering (VideoQA). The workflow includes development-subset experimentation for parameter selection followed by full-dataset experiments using optimized configurations.

| Notebook                             | Purpose                                                                                                                               |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **01_Prepare_Video_Evidence**        | Generate evidence metadata, video segments, and supporting resources required for autoencoder training and VideoQA experimentation.   |
| **02_Run_Baseline_VideoQA**          | Execute development-subset baseline VideoQA experiments using original video evidence and Qwen2-VL-7B.                                |
| **03_Train_Autoencoder**             | Train self-supervised autoencoder models using unlabeled video evidence and learn compact latent representations.                     |
| **04_Generate_Reconstructed_Videos** | Generate reconstructed video segments and measure reconstruction quality and compression characteristics.                             |
| **05_Run_Autoencoder_VideoQA**       | Execute development-subset VideoQA experiments using autoencoder-reconstructed video evidence and Qwen2-VL-7B.                        |
| **06_Evaluate_Development_Results**  | Generate evaluation metrics, compression analysis, runtime analysis, visualizations, and development-subset comparison reports.       |
| **07_Run_Final_Full_Experiment**     | Train and evaluate the selected autoencoder configuration using the complete NExT-QA dataset and generate final experimental results. |

The notebook workflow follows a two-stage experimental methodology. Development-subset experiments are used to evaluate autoencoder architectures, compression settings, reconstruction quality, and VideoQA performance. After parameter selection, a final full-dataset experiment is performed to generate the project's primary results and conclusions.


## Experimental Methodology

The experimental framework investigates whether self-supervised autoencoder learning can produce compact video representations that preserve the information required for downstream Video Question Answering (VideoQA). To balance computational efficiency with experimental rigor, the project employs a two-stage methodology consisting of development-subset experimentation followed by full-dataset evaluation.

During the development phase, a small subset of NExT-QA videos is used to evaluate autoencoder architectures, latent dimensionality, compression settings, reconstruction quality, and VideoQA performance. This phase enables rapid experimentation, workflow validation, and parameter optimization while minimizing computational cost.

The experimental framework evaluates two primary workflows:

1. **Baseline VideoQA** — Questions are answered using original video evidence and the Qwen2-VL-7B multimodal foundation model.

2. **Autoencoder-Based VideoQA** — An autoencoder is trained using unlabeled video evidence, reconstructed video segments are generated from learned representations, and VideoQA inference is performed using Qwen2-VL-7B.

Following development-subset experimentation, the selected autoencoder configuration is trained and evaluated using the complete NExT-QA dataset. This final experiment generates the project's primary performance results and enables assessment of how well the learned representations generalize across the full benchmark.

Qwen2-VL-7B serves as the fixed VideoQA inference model throughout all experiments. By maintaining a consistent downstream reasoning model, the study isolates the effects of representation learning and compression while minimizing the influence of changes in model architecture.

Experimental measurements include reconstruction quality, latent dimensionality, compression ratio, VideoQA answer quality, runtime performance, and storage efficiency. Baseline and autoencoder-based workflows are compared to evaluate the extent to which learned representations preserve semantic and temporal information required for accurate VideoQA reasoning.

Evaluation results are analyzed across the NExT-QA causal, temporal, and descriptive reasoning categories, as well as the dataset's individual question types (CH, CW, TN, TP, TC, DL, DO, and DC). This analysis provides insight into how representation learning affects different forms of video understanding and reasoning.

The objective of this work is not to develop a new VideoQA model, but rather to investigate whether self-supervised autoencoder learning can produce compact video representations that support effective downstream multimodal reasoning.

## Notebook Design Philosophy

The notebooks are designed to be independently executable, reproducible, and suitable for both Google Colab and local Jupyter environments. Development notebooks support rapid experimentation using a small dataset subset, while the final experiment notebook executes full-dataset evaluation using the selected configuration. Each notebook produces visible outputs that validate execution progress and generated artifacts.

## Expected Contributions

This work contributes a reproducible experimental framework for investigating self-supervised autoencoder learning within Video Question Answering (VideoQA) systems. The research is intended to provide insight into how compact video representations learned from unlabeled data affect downstream reasoning performance, reconstruction quality, compression efficiency, and VideoQA accuracy.

A primary contribution of this work is the evaluation of self-supervised video representation learning while maintaining a fixed VideoQA inference model. By holding the downstream reasoning architecture constant and varying only the representation-learning stage, the project enables direct analysis of how learned representations influence VideoQA performance.

Expected contributions include performance benchmarks comparing baseline VideoQA inference using original video evidence with VideoQA inference using autoencoder-reconstructed video evidence. These results will provide quantitative measures of how representation compression affects answer quality, temporal reasoning, causal reasoning, descriptive reasoning, runtime performance, and storage requirements.

The project also contributes analysis of the relationship between representation quality and downstream task performance. Reconstruction quality, latent dimensionality, compression ratio, and VideoQA metrics will be examined to better understand how information preservation influences multimodal reasoning capabilities.

In addition to the experimental results, the repository provides a reproducible notebook-driven research platform that supports future investigation of self-supervised learning, autoencoder architectures, video representation learning, multimodal foundation models, and VideoQA systems.

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

