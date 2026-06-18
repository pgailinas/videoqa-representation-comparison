---
title: Home
nav_order: 0
---

# Investigating Self-Supervised Autoencoder Learning for VideoQA

## Project Overview

This project investigates self-supervised autoencoder learning for Video Question Answering (VideoQA) using the NExT-QA benchmark dataset and the Qwen2-VL-7B multimodal foundation model.

The central objective is to determine whether video representations learned through self-supervised training on unlabeled video data preserve sufficient semantic and temporal information to support downstream VideoQA tasks. Rather than training a new VideoQA model from scratch, the project focuses on learning compact video representations and evaluating their effectiveness using a fixed VideoQA inference model.

Video evidence generated from the NExT-QA dataset is used to train an autoencoder without access to questions, answer choices, or ground-truth labels. The autoencoder learns compressed latent representations by reconstructing video segments from encoded feature vectors, enabling representation learning through self-supervision rather than manual annotation.

To evaluate representation quality, reconstructed video segments are provided to Qwen2-VL-7B together with NExT-QA questions and answer choices. VideoQA performance is then compared against a baseline workflow that performs direct inference on the original video evidence. This approach enables assessment of how well learned representations preserve information required for temporal, causal, and descriptive reasoning.

The experimental methodology uses a two-stage process. Development-subset experiments are first conducted using a small collection of videos to evaluate model configurations, compression settings, and reconstruction quality. After parameter selection, a final experiment is performed using the complete NExT-QA dataset to generate full-scale results and performance analysis.

The repository provides a reproducible notebook-driven research environment for investigating self-supervised representation learning, video compression, multimodal reasoning, and downstream VideoQA performance. The framework is designed to support academic research, experimental evaluation, and future IEEE-style publication development.

## Motivation and Research Problem

The rapid growth of video-based data has created increasing demand for artificial intelligence systems capable of understanding visual content, motion, temporal relationships, and contextual interactions within complex video sequences. Unlike static-image analysis, Video Question Answering (VideoQA) requires reasoning across both spatial and temporal dimensions, making it a challenging benchmark for multimodal machine learning systems.

Recent advances in self-supervised learning have demonstrated that useful visual representations can be learned directly from unlabeled data. Autoencoders provide a particularly attractive approach because they learn compact latent representations by reconstructing input data rather than relying on manually annotated labels. This capability has the potential to reduce dependence on costly labeled datasets while still capturing meaningful semantic and temporal information.

Although self-supervised representation learning has achieved promising results across many computer vision tasks, an important question remains: do the learned representations preserve the information required for downstream reasoning tasks such as VideoQA? In particular, it is unclear how much video information can be compressed into latent representations before performance on temporal, causal, and descriptive reasoning tasks begins to degrade.

This project investigates that question by training autoencoders using unlabeled videos from the NExT-QA dataset and evaluating the resulting representations through downstream VideoQA performance. A baseline VideoQA workflow using original video evidence is compared with an autoencoder-based workflow using reconstructed video evidence. By holding the VideoQA model constant and varying only the representation-learning stage, the study seeks to determine whether self-supervised autoencoder learning can produce compact video representations that preserve sufficient information for accurate VideoQA reasoning.

## Research Objectives

This project investigates whether self-supervised autoencoder learning can produce compact video representations that preserve the information required for downstream Video Question Answering (VideoQA). The research focuses on learning video representations from unlabeled video data and evaluating their effectiveness through VideoQA performance on the NExT-QA benchmark dataset.

The primary objectives of this work are:

1. Train self-supervised autoencoder models using unlabeled NExT-QA video data and learn compact latent video representations without the use of questions, answer choices, or ground-truth labels.

2. Evaluate the ability of reconstructed video evidence generated from learned representations to support downstream VideoQA reasoning using a fixed multimodal foundation model.

3. Measure the relationship between representation compression and VideoQA performance, including the effects of reconstruction quality, latent dimensionality, and compression ratio.

4. Compare autoencoder-based VideoQA performance against a baseline VideoQA workflow using original video evidence.

5. Analyze how learned representations affect causal, temporal, and descriptive reasoning performance within the NExT-QA benchmark.

To isolate the effects of representation learning, the same multimodal foundation model, Qwen2-VL-7B, is used throughout all VideoQA experiments. This design ensures that observed performance differences can be attributed primarily to the quality of the learned representations rather than changes in downstream model architecture.

The primary research hypothesis is that self-supervised autoencoder learning can produce compact video representations that preserve sufficient semantic and temporal information to support accurate VideoQA reasoning while reducing the amount of information required to represent the original video content.

## Research Questions

This project investigates the following research questions:

1. Can self-supervised autoencoder training learn compact latent video representations that preserve information relevant to VideoQA?

2. How do autoencoder-based latent representations compare with pretrained video representations on downstream VideoQA tasks?

3. What impact does representation learning have on temporal, causal, and descriptive reasoning performance?

4. Can compressed latent representations reduce storage and computational requirements while maintaining acceptable VideoQA accuracy?

## Dataset

The primary benchmark dataset used in this project is NExT-QA, a Video Question Answering (VideoQA) benchmark designed to evaluate causal, temporal, and descriptive reasoning over video content.

The dataset provides raw video files, question-answer annotations, official training, validation, and test splits, and metadata required to associate questions with source videos.

The experimental dataset includes:

- NExT-QA video collection containing 5,440 MP4 videos organized within the NExTVideo directory structure
- Training, validation, and test question-answer splits containing 47,692 benchmark questions
- Video identifier mapping metadata
- Optional relation annotations for advanced reasoning experiments

### NExT-QA Reasoning Categories

NExT-QA is designed to evaluate video understanding through three primary reasoning categories:

| Category | Description |
|-----------|-------------|
| Causal | Why events occur and how actions produce outcomes. |
| Temporal | Event order and temporal relationships. |
| Descriptive | Objects, actions, attributes, locations, and counts. |

These reasoning categories provide an important evaluation dimension for this project. Experimental results will be analyzed both overall and by reasoning category to evaluate how different video representations affect causal, temporal, and descriptive reasoning performance.

Raw videos are processed into structured evidence segments containing temporal metadata and representative frame samples. These evidence units serve as the foundation for representation learning, latent feature extraction, pretrained feature generation, and downstream VideoQA experimentation.

## System Architecture

The experimental framework is centered on the Qwen2-VL-7B multimodal foundation model and a representation-learning pipeline built upon NExT-QA video evidence segments.

Video preprocessing generates structured evidence records consisting of temporal video segments, frame samples, metadata, and supporting evidence artifacts. These evidence units serve as inputs to both pretrained representation models and self-supervised autoencoder training workflows.

The system architecture supports three primary experimental workflows:

1. **Baseline VideoQA** — Direct VideoQA inference using Qwen2-VL-7B and sampled video evidence.

2. **Pretrained Representation VideoQA** — Video evidence represented using pretrained video features and evaluated through downstream Qwen2-VL-7B VideoQA inference.

3. **Autoencoder Representation VideoQA** — Video evidence represented using latent features learned through self-supervised autoencoder training and evaluated through downstream Qwen2-VL-7B VideoQA inference.

The autoencoder learns compact latent representations of video segments without requiring manual labels. These latent representations serve as compressed feature vectors intended to preserve semantic and temporal information while reducing dimensionality. The resulting encoder serves as a learned feature extractor whose latent embeddings are evaluated through downstream VideoQA performance and compared directly with pretrained video representations.

The architecture is designed to isolate the effects of representation learning while maintaining a consistent VideoQA foundation model across all experiments. This enables direct comparison of baseline evidence, pretrained representations, and learned latent representations while controlling for inference model architecture.

---

### Pipeline Flowchart

<a href="images/overview_pipeline.png" target="_blank">
  <img src="images/overview_pipeline.png" width="800">
</a>

### Notebook Workflow

The project is organized into a sequence of notebooks that support reproducible experimentation across baseline, pretrained-representation, and autoencoder-representation VideoQA workflows.

| Notebook                                | Purpose                                                                         |
| --------------------------------------- | ------------------------------------------------------------------------------- |
| 01_Prepare_Video_Evidence               | Generate evidence metadata and video evidence segments.                         |
| 02_Run_Baseline_VideoQA                 | Execute development-subset baseline VideoQA experiments and optimize inference  |
|                                         |      parameters.                                                                |
| 03_Generate_Pretrained_Representations  | Generate pretrained video representations from video evidence segments.         |
| 04_Generate_Autoencoder_Representations | Train self-supervised autoencoder models and generate latent representations.   |
| 05_Run_Representation_VideoQA           | Execute development-subset representation VideoQA experiments and optimize      |
|                                         |      representation parameters.                                                 |
| 06_Run_Final_Full_Experiments           | Execute full-dataset baseline, pretrained-representation, and autoencoder       |
|                                         |     representation experiments.                                                 |
| 07_Evaluate_VideoQA_Results             | Generate evaluation metrics, analysis summaries, visualizations, and experiment |
|                                         |     reports.                                                                    |

## Experimental Methodology

The experimental framework evaluates how different video representations influence downstream VideoQA performance. To manage computational cost while maintaining experimental rigor, the project uses a two-stage evaluation methodology. Development-subset experiments are first used for parameter optimization, workflow validation, and representation tuning. Optimized configurations are then applied to full-dataset experiments for final comparative evaluation.

Experiments compare baseline video evidence, pretrained video representations, and self-supervised autoencoder-based latent representations using a common VideoQA inference model.

The experiments evaluate three primary workflows:

1. **Baseline VideoQA Inference** — Questions are answered using sampled video evidence and Qwen2-VL-7B.

2. **Pretrained Representation VideoQA** — Evidence is represented using pretrained video features and supplied to Qwen2-VL-7B for answer generation.

3. **Autoencoder Representation VideoQA** — Evidence is represented using latent embeddings learned through self-supervised autoencoder training and supplied to Qwen2-VL-7B for answer generation.

Development-subset experiments are conducted using a small portion of the dataset to evaluate parameter settings, representation-learning configurations, and inference workflows. Once parameter optimization is complete, final baseline, pretrained-representation, and autoencoder-representation experiments are executed using the full evaluation dataset. This separation reduces computational cost while ensuring that final results are generated using a consistent optimized configuration.

Qwen2-VL-7B serves as the fixed multimodal foundation model throughout all experiments. The primary experimental variable is the video representation used to support inference. This design isolates the effects of representation quality while maintaining a consistent VideoQA reasoning model.

Potential representation-learning metrics include reconstruction error, latent dimensionality, compression ratio, and downstream VideoQA performance. Evaluation metrics include VideoQA answer quality, representation-learning metrics, runtime measurements, and comparative analysis across reasoning categories.

Evaluation results are analyzed across NExT-QA causal, temporal, and descriptive reasoning categories as well as the dataset's individual question types (CH, CW, TN, TP, TC, DL, DO, and DC).

The objective is not to train a new VideoQA model, but to evaluate how learned video representations influence downstream multimodal reasoning performance.

## Implementation Framework

The implementation framework integrates self-supervised learning models, multimodal foundation models, and Python-based machine learning frameworks to support reproducible experimentation across representation-learning workflows.

The framework incorporates the Qwen2-VL-7B multimodal foundation model, autoencoder architectures, pretrained feature extraction models, GPU-accelerated training and inference libraries, and supporting video-processing frameworks within Google Colab and local Jupyter environments.

Supporting technologies may include PyTorch, Hugging Face Transformers, NumPy, Pandas, OpenCV, and related libraries used for representation learning, latent feature extraction, model training, inference, and experimental evaluation.

| Component                          | Purpose                                                      |
| ---------------------------------- | ------------------------------------------------------------ |
| Evidence Generation Pipeline       | Generate video evidence segments and metadata                |
| Representation Learning Pipeline   | Train autoencoder models and generate latent representations |
| Pretrained Representation Pipeline | Generate pretrained video representations                    |
| Qwen2-VL-7B Foundation Model       | Perform VideoQA reasoning and answer generation              |
| Evaluation Pipeline                | Generate metrics, visualizations, and experiment reports     |

## Repository Organization

The repository is organized as a modular notebook-driven research environment designed to support reproducible experimentation across representation-learning and VideoQA workflows.

The structure separates dataset preparation, evidence generation, representation learning, feature extraction, VideoQA inference, evaluation procedures, reporting workflows, and visualization stages into independently executable notebooks and configuration modules.

Supporting directories include benchmark dataset resources, extracted video assets, question-answer annotations, metadata resources, learned representations, pretrained features, experimental outputs, configuration modules, notebooks, and documentation resources intended to support extensible machine-learning research workflows.

## Notebook Design Philosophy

The notebooks are designed to be independently executable and reproducible within Google Colab and local Jupyter environments. Development notebooks support rapid experimentation and parameter optimization using dataset subsets, while final experiment notebooks execute full-dataset evaluations using optimized configurations. Every major code cell should produce visible output confirming successful execution, key runtime information, or generated artifacts.

## Expected Contributions

This work contributes a reproducible experimental framework for investigating self-supervised representation learning within VideoQA systems. The research is designed to provide insight into latent representation learning, feature extraction, representation quality, and downstream VideoQA performance.

Expected contributions include comparative performance benchmarks, representation analysis visualizations, and evaluation of how learned latent representations influence VideoQA answer quality and reasoning performance when compared with pretrained video representations.

The repository additionally provides an extensible notebook-driven research platform intended to support future experimentation involving autoencoders, self-supervised learning, representation learning, multimodal foundation models, and VideoQA inference systems.

The project emphasizes machine-learning evaluation of learned video representations rather than retrieval-system engineering or development of a new VideoQA model.

A central contribution of this work is the evaluation of self-supervised representation learning while holding the underlying VideoQA foundation model constant. This enables quantitative analysis of how representation quality influences answer accuracy, temporal reasoning performance, representation compactness, and execution efficiency independent of downstream model architecture.

An additional contribution is the comparison of learned and pretrained video representations using a common downstream VideoQA task. This provides a practical evaluation of representation quality based on task performance rather than reconstruction quality alone.

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

