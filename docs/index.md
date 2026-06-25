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

## Research Objectives

The objectives of this project are:

1. Establish a baseline multiple-choice VideoQA benchmark using the Qwen2-VL-7B multimodal foundation model.
2. Learn compact video representations through self-supervised autoencoder training using unlabeled NExT-QA videos.
3. Generate pretrained CLIP video and text representations for comparison with learned representations.
4. Compare pretrained and learned video representations using a common downstream VideoQA classification framework.
5. Evaluate representation quality through downstream VideoQA performance across the NExT-QA reasoning categories.
6. Develop a reproducible notebook-based experimental framework for investigating video representation learning and VideoQA.

## Research Questions

This project investigates the following research questions:

1. Can self-supervised autoencoder training learn compact video representations from unlabeled video data while preserving information relevant to Video Question Answering (VideoQA)?

2. How does VideoQA performance change when reconstructed video evidence generated from learned autoencoder representations is used instead of original video evidence?

3. What relationship exists between representation compression, reconstruction quality, and downstream VideoQA performance?

4. How do different evidence preparation strategies affect learned representations and downstream VideoQA performance?

5. What relationship exists between evidence generation, reconstruction quality, and VideoQA accuracy?

6. To what extent can evidence enhancement techniques improve downstream VideoQA performance compared to standard evidence generation methods?

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

The system architecture supports a baseline VideoQA workflow together with multiple autoencoder-based workflows.

The baseline workflow performs VideoQA inference directly on original NExT-QA video evidence using Qwen2-VL-7B.

The autoencoder workflows generate video evidence segments using alternative evidence preparation strategies, train self-supervised autoencoders, reconstruct video segments, and evaluate reconstructed-video performance using Qwen2-VL-7B.

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
| **01_Run_Baseline_VideoQA**          | Execute development-subset baseline VideoQA experiments using original video evidence and Qwen2-VL-7B.                                |
| **02_Prepare_Video_Evidence**        | Generate evidence metadata, video segments, and supporting resources required for autoencoder training and VideoQA experimentation.   |
| **03_Train_Autoencoder**             | Train self-supervised autoencoder models using unlabeled video evidence and learn compact latent representations.                     |
| **04_Run_Autoencoder_VideoQA**       | Execute development-subset VideoQA experiments using autoencoder-reconstructed video evidence and Qwen2-VL-7B.                        |
| **05_Evaluate_Development_Results**  | Generate evaluation metrics, compression analysis, runtime analysis, visualizations, and development-subset comparison reports.       |
| **06_Run_Final_Full_Experiment**     | Train and evaluate the selected autoencoder configuration using the complete NExT-QA dataset and generate final experimental results. |

The notebook workflow follows a two-stage experimental methodology. Development-subset experiments are used to evaluate autoencoder architectures, compression settings, reconstruction quality, and VideoQA performance. After parameter selection, a final full-dataset experiment is performed to generate the project's primary results and conclusions.


## Experimental Methodology

The experimental framework evaluates baseline VideoQA performance together with multiple autoencoder-based workflows.

The baseline workflow answers questions using original video evidence and the Qwen2-VL-7B multimodal foundation model.

The autoencoder workflows train self-supervised autoencoders using video evidence generated from alternative evidence preparation strategies, reconstruct video segments, and evaluate downstream VideoQA performance using Qwen2-VL-7B.

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

Expected contributions include performance benchmarks comparing baseline VideoQA inference using original video evidence with VideoQA inference using autoencoder-reconstructed video evidence generated from multiple evidence preparation strategies.

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

