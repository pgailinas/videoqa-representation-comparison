---
title: Home
nav_order: 0
---

# Comparing Autoencoder-Based and Pretrained Video Representations for VideoQA

## Project Overview

This project investigates self-supervised representation learning for Video Question Answering (VideoQA) using the NExT-QA benchmark dataset and the Qwen2-VL-7B multimodal foundation model.

Rather than training a new VideoQA model from scratch, the project evaluates how different video representations influence downstream VideoQA performance. The study compares pretrained video representations with latent representations learned through self-supervised autoencoder training while maintaining a fixed VideoQA model across all experiments.

Qwen2-VL-7B serves as the common VideoQA inference model, allowing performance differences to be attributed primarily to the quality of the underlying video representations rather than changes in model architecture. The framework processes raw videos into structured evidence segments that are used for representation learning, latent feature extraction, representation comparison, and VideoQA experimentation.

Comparative experiments evaluate baseline inference, pretrained video representations, and autoencoder-based latent representations to measure their impact on answer quality, reasoning performance, representation efficiency, and execution latency.

The repository provides a reproducible notebook-driven research environment using public VideoQA datasets, self-supervised learning techniques, modular AI workflows, and configurable multimodal components suitable for research experimentation and future IEEE-style publication development.

## Motivation and Research Problem

The rapid growth of video-based data has increased demand for AI systems capable of understanding visual scenes, motion, temporal relationships, and contextual interactions across long video sequences. Unlike static-image understanding, VideoQA requires reasoning across both spatial and temporal information, making it a challenging benchmark for multimodal AI systems.

Recent advances in self-supervised learning have demonstrated that useful visual representations can be learned without manual annotation. Autoencoders and related representation-learning approaches enable models to learn compact latent representations that capture meaningful structure within images and videos while reducing reliance on labeled training data.

Despite significant progress in representation learning, important questions remain regarding how learned representations influence downstream reasoning tasks such as VideoQA. In particular, it is unclear whether latent representations learned through self-supervised training can provide evidence representations that are competitive with or superior to pretrained video representations.

This project investigates these questions through comparative evaluation of baseline video evidence, pretrained video representations, and autoencoder-based latent representations using the NExT-QA benchmark dataset and a fixed multimodal foundation model.

## Research Objectives

This project investigates how learned video representations influence downstream VideoQA performance within multimodal video understanding systems. The research emphasizes comparative evaluation of baseline video evidence, pretrained video representations, and self-supervised autoencoder-based representations.

The objectives of this work include measuring how representation quality affects temporal reasoning, answer accuracy, representation compactness, and execution latency using the NExT-QA benchmark dataset.

Additional objectives include evaluating whether latent representations learned through self-supervised training can provide competitive or improved video representations when compared with pretrained feature representations.

To isolate the impact of representation learning, the same multimodal foundation model is used throughout all experiments. Baseline VideoQA, pretrained-representation VideoQA, and autoencoder-representation VideoQA workflows are evaluated using Qwen2-VL-7B, enabling direct comparison of representation-learning strategies while controlling for downstream model architecture.

The primary research hypothesis is that self-supervised autoencoder-based video representations can provide compact latent representations that are competitive with or superior to pretrained video representations for downstream VideoQA tasks.

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

