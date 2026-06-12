---
title: Home
nav_order: 0
---

# Comparing Autoencoder-Based and Pretrained Video Representations for VideoQA

## Project Overview

This project investigates self-supervised representation learning for Video Question Answering (VideoQA) using the NExT-QA benchmark dataset and the Qwen2-VL-7B multimodal foundation model.

Rather than training a new VideoQA model from scratch, the project evaluates how different video representations influence downstream VideoQA performance. The study compares pretrained video representations with latent representations learned through self-supervised autoencoder training while maintaining a fixed VideoQA model across all experiments.

Qwen2-VL-7B serves as the common VideoQA inference model, allowing performance differences to be attributed primarily to the quality of the underlying video representations rather than changes in model architecture.

The framework processes raw videos into structured evidence segments that are used for representation learning, feature extraction, evidence retrieval, and VideoQA experimentation. Comparative experiments evaluate baseline inference, pretrained video representations, and autoencoder-based latent representations to measure their impact on answer quality, reasoning performance, representation efficiency, and execution latency.

The repository provides a reproducible notebook-driven research environment using public VideoQA datasets, self-supervised learning techniques, modular AI workflows, and configurable multimodal components suitable for research experimentation and future IEEE-style publication development.

## Motivation and Research Problem

The rapid growth of video-based data has increased demand for AI systems capable of understanding visual scenes, motion, temporal relationships, and contextual interactions across long video sequences. Unlike static-image understanding, VideoQA requires reasoning across both spatial and temporal information, making it a challenging benchmark for multimodal AI systems.

Recent RAG methods improve VideoQA by retrieving relevant frames, clips, captions, transcripts, and embedding representations prior to inference. These approaches aim to improve contextual accuracy and reduce hallucinations during question answering.

Despite recent advances, major challenges remain involving temporal grounding, retrieval refinement, and the interaction between retrieval workflows and LLM inference behavior. This project investigates these challenges through comparative evaluation of baseline, single-pass, and iterative RAG workflows across public VideoQA benchmarks.

## Research Objectives

This project investigates how learned video representations influence downstream VideoQA performance within multimodal video understanding systems. The research emphasizes comparative evaluation of baseline video evidence, pretrained video representations, and self-supervised autoencoder-based representations.

The objectives of this work include measuring how representation quality affects temporal reasoning, answer accuracy, evidence selection, representation compactness, and execution latency using the NExT-QA benchmark dataset.

Additional objectives include evaluating whether latent representations learned through self-supervised training can provide competitive or improved evidence representations when compared with pretrained feature representations.

To isolate the impact of representation learning, the same multimodal foundation model is used throughout all experiments. Baseline VideoQA, pretrained-representation VideoQA, and autoencoder-representation VideoQA workflows are evaluated using Qwen2-VL-7B, enabling direct comparison of representation-learning strategies while controlling for downstream model architecture.

The primary research hypothesis is that self-supervised autoencoder-based video representations can provide evidence representations that are competitive with or superior to pretrained video representations for downstream VideoQA tasks.

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

These reasoning categories provide an important evaluation dimension for this project. Experimental results will be analyzed both overall and by reasoning category to evaluate how retrieval and iterative evidence refinement affect different forms of video understanding.

Raw videos are processed into frames, clips, evidence metadata, embedding representations, and other derived evidence artifacts during knowledge base construction. These generated artifacts serve as the evidence repository used by downstream retrieval and VideoQA workflows, reducing the need to repeatedly process the original video files.

## System Architecture

The experimental framework is centered on the Qwen2-VL-7B multimodal foundation model and a representation-learning pipeline built upon NExT-QA video evidence segments.

Video preprocessing generates structured evidence records consisting of temporal video segments, frame samples, metadata, and supporting evidence artifacts. These evidence units serve as inputs to both pretrained representation models and self-supervised autoencoder training workflows.

The system architecture supports three primary experimental workflows:

1. **Baseline VideoQA** — Direct VideoQA inference using Qwen2-VL-7B and sampled video evidence.

2. **Pretrained Representation VideoQA** — Evidence selection using pretrained video representations followed by Qwen2-VL-7B inference.

3. **Autoencoder Representation VideoQA** — Evidence selection using latent representations learned through self-supervised autoencoder training followed by Qwen2-VL-7B inference.

The autoencoder learns compact latent representations of video evidence without requiring manual labels. The resulting encoder serves as a learned feature extractor whose latent embeddings are evaluated through downstream VideoQA performance.

The architecture is designed to isolate the effects of representation learning while maintaining a consistent VideoQA foundation model across all experiments. This enables direct comparison of baseline evidence, pretrained representations, and learned latent representations while controlling for inference model architecture.

---

### Pipeline Flowchart

<a href="images/overview_pipeline.png" target="_blank">
  <img src="images/overview_pipeline.png" width="800">
</a>

### Notebook Workflow

The project is organized into a sequence of notebooks that support reproducible experimentation across baseline, Retrieval-Augmented Generation (RAG), and iterative RAG VideoQA workflows.

| Notebook                             | Purpose                                                                                  |
| ------------------------------------ | ---------------------------------------------------------------------------------------- |
| 01_Prepare_Video_Data                | Prepare and validate the NExT-QA dataset.                                                |
| 02_Prepare_Video_Evidence            | Generate evidence metadata and video evidence segments.                                  |
| 03_Run_Baseline_VideoQA              | Perform baseline VideoQA inference using Qwen2-VL-7B.                                    |
| 04_Train_Autoencoder_Representations | Train self-supervised autoencoder models and generate latent representations.            |
| 05_Build_Representation_Indexes      | Generate pretrained and autoencoder-based representation indexes.                        |
| 06_Run_Representation_Comparison     | Execute pretrained versus autoencoder representation experiments.                        |
| 07_Evaluate_VideoQA_Results          | Generate evaluation metrics, analysis summaries, visualizations, and experiment reports. |



## Experimental Methodology

The experimental framework evaluates how retrieval strategies and multimodal knowledge representations influence VideoQA performance. Experiments compare baseline inference against single-pass and iterative Retrieval-Augmented Generation (RAG) workflows using frame-level, clip-level, evidence-based, and embedding-based video representations.

The experiments evaluate three primary workflows:

1. **Baseline VideoQA Inference** — questions are answered using pretrained reasoning models without retrieval assistance.

2. **Single-Pass RAG Inference** — relevant video evidence is retrieved from the knowledge base and provided as additional context during answer generation.

3. **Iterative RAG Inference** — retrieval and reasoning are performed across multiple refinement passes to improve evidence selection and answer quality.

Qwen2-VL-7B serves as the fixed multimodal foundation model for all experiments. Baseline, single-pass RAG, and iterative RAG workflows differ only in the evidence retrieval and refinement process. This design isolates the impact of retrieval strategy while maintaining a consistent VideoQA reasoning model.

Experiments measure how retrieval strategy, evidence quality, evidence utilization, and refinement depth affect temporal reasoning, answer accuracy, retrieval effectiveness, and execution efficiency. Evaluation metrics may include answer accuracy, retrieval precision and recall, semantic relevance, execution time, and latency-versus-performance tradeoffs.

Evaluation results will be analyzed across NExT-QA causal, temporal, and descriptive reasoning categories, as well as the dataset's individual question types (CH, CW, TN, TP, TC, DL, DO, and DC).

The objective is not to train a new VideoQA neural network, but to evaluate how modern foundation models and retrieval architectures can be combined to improve video reasoning performance.

## Implementation Framework

The implementation framework integrates open-source multimodal models, vector databases, and Python-based AI frameworks to support reproducible experimentation across baseline and iterative RAG-based VideoQA workflows.

The framework incorporates the Qwen2-VL-7B multimodal foundation model, vector similarity search systems, GPU-accelerated inference libraries, and supporting video-processing frameworks within Google Colab and local Jupyter environments. Supporting technologies may include PyTorch, Hugging Face Transformers, LangChain, FAISS, ChromaDB, OpenCV, and related libraries used for embedding generation, vector indexing, retrieval, inference, and experimental evaluation.

| Component                    | Purpose                                                              |
| ---------------------------- | -------------------------------------------------------------------- |
| Evidence Generation Pipeline | Generate evidence metadata and video evidence representations        |
| Knowledge Base Pipeline      | Generate embeddings and retrieval indexes                            |
| Qwen2-VL-7B Foundation Model | Perform VideoQA reasoning and answer generation                      |
| Retrieval Engine             | Select relevant evidence for inference                               |
| Reporting Pipeline           | Generate evaluation metrics, visualizations, and experiment reports  |

## Repository Organization

The repository is organized as a modular notebook-driven research environment designed to support reproducible experimentation across baseline and iterative RAG-based VideoQA workflows.

The structure separates dataset preparation, media extraction, evidence generation, knowledge base construction, retrieval workflows, inference pipelines, evaluation procedures, reporting workflows, and visualization stages into independently executable notebooks and configuration modules.

Supporting directories include benchmark dataset resources, extracted video assets, question-answer annotations, metadata resources, vector indexes, generated embeddings, experimental outputs, configuration modules, notebooks, and documentation resources intended to support extensible multimodal AI research workflows.

## Notebook Design Philosophy

The notebooks are designed to be independently executable and reproducible within Google Colab and local Jupyter environments. Every major code cell should produce visible output confirming successful execution, key runtime information, or generated artifacts.

## Expected Contributions

This work contributes a reproducible experimental framework for investigating self-supervised representation learning within VideoQA systems. The research is designed to provide insight into latent representation learning, feature extraction, representation quality, and downstream VideoQA performance.

Expected contributions include comparative performance benchmarks, representation analysis visualizations, and evaluation of how learned latent representations influence VideoQA answer quality and reasoning performance when compared with pretrained video representations.

The repository additionally provides an extensible notebook-driven research platform intended to support future experimentation involving autoencoders, self-supervised learning, representation learning, multimodal foundation models, and VideoQA inference systems.

The project emphasizes machine-learning evaluation of learned video representations rather than retrieval-system engineering or development of a new VideoQA model.

A central contribution of this work is the evaluation of self-supervised representation learning while holding the underlying VideoQA foundation model constant. This enables quantitative analysis of how representation quality influences answer accuracy, temporal reasoning performance, and evidence utilization independent of downstream model architecture.

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

