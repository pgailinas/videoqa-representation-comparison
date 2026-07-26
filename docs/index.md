---
title: Home
nav_order: 0
---

# Investigating Self-Supervised Autoencoder Learning for VideoQA

## Project Overview

This project investigates self-supervised autoencoder learning for Video Question Answering (VideoQA) using the NExT-QA benchmark dataset, pretrained CLIP representations, and the Qwen2-VL-7B multimodal foundation model.

The project evaluates three complementary VideoQA pipelines: (1) direct multimodal inference using Qwen2-VL, (2) representation-based VideoQA using pretrained CLIP video representations, and (3) representation-based VideoQA using self-supervised autoencoder video representations. In addition, the experimental framework supports hybrid CLIP–autoencoder video representations to investigate whether reconstruction-based and pretrained semantic representations provide complementary information.

Both representation-based pipelines use shared CLIP question-answer representations and a common evaluation framework, allowing different video representations and prediction methods to be compared independently.

**IMPORTANT: This documentation is part of a complete VideoQA tutorial and research framework available through the project's public GitHub repository. The documentation and notebooks may be viewed directly on GitHub without an account. Running the notebooks in Google Colab requires a Google account. Alternatively, the repository may be cloned or downloaded, and the notebooks can be run locally using Jupyter or any compatible notebook environment.**

## Research Paper

A complete IEEE-format paper describing this project is available.

📄 **Investigating Self-Supervised Representation Learning for Video Question Answering**

- Complete methodology
- Experimental design
- Results
- Discussion
- Conclusions

[View the paper](paper/ECE-551_VideoQA_Representation_Comparison.pdf)

## Motivation and Research Problem

VideoQA requires models to understand both the visual content of individual frames and the temporal relationships that occur throughout a video. Unlike static-image recognition, VideoQA demands reasoning about actions, events, object interactions, and causal relationships, making it a challenging benchmark for multimodal machine learning systems.

Recent advances in foundation models have demonstrated impressive VideoQA performance by processing video and text directly. At the same time, self-supervised learning has shown that compact feature representations can be learned from large collections of unlabeled data without requiring manual annotation. These learned representations have proven effective across a wide range of computer vision tasks, suggesting that they may also provide useful information for downstream VideoQA.

This project investigates whether learned video representations can support VideoQA reasoning without relying solely on direct processing of the original videos. Specifically, the study compares pretrained CLIP video representations with self-supervised autoencoder representations using shared `clip_text` question-answer representations within a common evaluation framework.

## Research Questions

This project investigates the following research questions:

1. Can self-supervised autoencoder training learn compact video representations that support competitive downstream VideoQA performance?

2. How does VideoQA performance compare across reconstruction-based autoencoder representations, pretrained CLIP representations, hybrid CLIP–autoencoder representations, and direct Qwen2-VL foundation-model inference?

3. How does the quality of the underlying video representation influence downstream VideoQA performance under a common evaluation framework?

## Dataset

The primary benchmark dataset used in this project is **NExT-QA**, a VideoQA benchmark designed to evaluate visual understanding and reasoning across real-world video content. The dataset contains questions that require models to reason about actions, events, temporal relationships, and contextual interactions occurring within video sequences.

The NExT-QA benchmark contains 5,440 videos, 47,692 multiple-choice question-answer pairs, official training/validation/test splits, and supporting metadata linking questions to their corresponding videos.

Within this project, the NExT-QA videos serve three complementary purposes:

* **Baseline VideoQA** — Original videos are processed directly by Qwen2-VL-7B to establish baseline performance.
* **Representation Learning** — Unlabeled videos are used to train self-supervised autoencoder models and to generate pretrained CLIP video representations.
* **Evaluation** — The benchmark questions and answer choices are encoded once as a reusable shared CLIP question-answer representation dataset and combined with the video representations to evaluate downstream multiple-choice VideoQA performance.

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

In addition to the official dataset splits, pretrained CLIP text and video representations are generated once for the entire NExT-QA dataset and reused throughout the representation-based pipelines. Because the CLIP encoders remain frozen, generating these representations for all dataset splits does not introduce information leakage while eliminating redundant computation and ensuring identical pretrained features are used across all experiments.

The three VideoQA pipelines use the dataset splits differently depending on whether model learning is required.

| Pipeline | Training Split | Validation Split |
|----------|----------------|------------------|
| **Qwen2-VL Baseline** | Not required. The pretrained Qwen2-VL-7B foundation model performs inference directly on the original videos without additional training. | Performs multiple-choice VideoQA inference and evaluation using the validation split. |
| **CLIP Representation Pipeline** | Uses the precomputed CLIP video and shared CLIP question-answer representations to train the selected learned fusion classifier when applicable. Cosine similarity requires no training. | Uses the corresponding validation representations to generate predictions and evaluate the selected representation-based method. |
| **Autoencoder Representation Pipeline** | Trains the self-supervised video autoencoder using the training videos, generates learned video representations, and trains the selected learned fusion classifier when applicable. | Uses the learned validation representations to generate predictions and evaluate the selected representation-based method. |

This separation of responsibilities follows standard machine learning practice by reserving the validation split exclusively for development evaluation while using the training split for all learned model components.

---

### System Architecture

The experimental framework consists of three complementary VideoQA pipelines that share a common evaluation methodology while varying the source of the video representation.

- **Baseline Pipeline** — Performs direct VideoQA inference using Qwen2-VL on the original videos.

- **CLIP Representation Pipeline** — Uses pretrained `clip_video` and shared `clip_text` representations for representation-based VideoQA.

- **Autoencoder Representation Pipeline** — Uses learned `autoencoder_video` representations together with the same shared `clip_text` representations for representation-based VideoQA.

The representation-based framework also supports optional hybrid CLIP–autoencoder video representations, enabling experiments that combine pretrained semantic and learned reconstruction-based representations within the same evaluation pipeline.

All representation-based experiments use the same downstream VideoQA framework and evaluation procedures while supporting the same configurable prediction methods, enabling controlled comparison of different video representations.

---

### Pipeline Flowchart

<a href="images/overview_pipeline.png" target="_blank">
  <img src="images/overview_pipeline.png" width="800">
</a>

### Experimental Results at a Glance

The completed experiments compared four complementary VideoQA approaches using a common evaluation framework. The highest observed accuracy for each approach is summarized below.

| Approach | Best Accuracy |
|----------|--------------:|
| **Qwen2-VL Baseline** | **79.84%** |
| **Pretrained CLIP Representations** | **46.42%** |
| **Hybrid CLIP + Autoencoder Representations** | **31.29%** |
| **Self-Supervised Autoencoder Representations** | **21.78%** |

These results demonstrate that pretrained semantic representations substantially outperform reconstruction-based representations for downstream VideoQA. Although the hybrid representation improved upon the autoencoder-only approach, it did not surpass pretrained CLIP representations, indicating that semantic representation quality—not simply combining multiple representation sources—is the primary determinant of representation-based VideoQA performance.

### Notebook Workflow

The project is organized as eight modular notebooks supporting the three primary VideoQA pipelines together with additional hybrid representation experiments.

| Notebook | Purpose |
|----------|---------|
| **01_Run_Qwen2VL_Baseline** | Execute baseline multiple-choice VideoQA experiments using the original NExT-QA videos and Qwen2-VL-7B. |
| **02_Prepare_Autoencoder_Segment_Metadata** | Prepare standardized segment metadata required for self-supervised autoencoder learning. |
| **03_Train_Video_Autoencoder** | Train a self-supervised video autoencoder using unlabeled NExT-QA videos and generate segment-level and video-level representations. |
| **04_Validate_Autoencoder_Video_Representations** | Load, standardize, and validate the autoencoder video representation artifacts generated by Notebook 03 for downstream VideoQA experiments. |
| **05_Generate_CLIP_Text_Representations** | Generate reusable shared CLIP question-answer representations for every candidate answer in the NExT-QA dataset. |
| **06_Generate_CLIP_Video_Representations** | Generate reusable pretrained CLIP video representations for the NExT-QA videos. |
| **07_Run_Representation_VideoQA** | Execute representation-based multiple-choice VideoQA using shared `clip_text` question-answer representations together with `clip_video`, `autoencoder_video`, or `hybrid_clip_autoencoder` video representations using the selected scoring or learned fusion prediction method. |
| **08_Evaluate_Development_Results** | Compare all completed development experiments using common validation metrics, error analysis, question-type analysis, visualization, and experiment selection. |

Development-subset experiments are used to compare competing methods before full-validation evaluation. Once the experimental configuration has been finalized, the complete NExT-QA dataset is processed to generate the project's primary evaluation results.

---

### Expected Contributions

This project makes four primary contributions:

- A reproducible notebook-driven framework for investigating VideoQA representation learning.
- A controlled comparison of foundation-model inference, pretrained CLIP representations, hybrid CLIP–autoencoder representations, and self-supervised autoencoder representations.
- A modular workflow that separates representation generation from downstream VideoQA evaluation, enabling rapid experimentation with alternative representation-learning strategies.
- Experimental evidence demonstrating that semantic representation quality is the primary determinant of downstream VideoQA performance, including a hybrid CLIP–autoencoder study showing that simply combining reconstruction-based and pretrained semantic representations does not improve performance without stronger semantic alignment.

---

## References and Further Reading

Additional papers, datasets, models, and technical resources related to this project are available on the [References](References.md) page.

---

## Author

**Phil Gailinas**  
- M.S. Computer Engineering candidate  
- University of New Mexico
- Project initiated May 2026

## License

This project is intended for academic and research use.

