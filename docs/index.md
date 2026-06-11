---
title: Home
nav_order: 0
---

# Iterative RAG for VideoQA

## Project Overview

This project investigates iterative Retrieval-Augmented Generation (RAG) workflows for Video Question Answering (VideoQA) using the NExT-QA benchmark dataset and pretrained multimodal foundation models.

Rather than training a new VideoQA model from scratch, the project evaluates how retrieval-augmented evidence selection and iterative evidence refinement influence VideoQA performance when using a fixed multimodal foundation model. Qwen2-VL-7B serves as the common VideoQA foundation model across all experimental workflows, allowing performance differences to be attributed to retrieval and evidence-refinement strategies rather than model architecture.

The framework processes raw videos into sampled frames, clips, evidence metadata, embedding representations, and searchable vector indexes. Comparative experiments evaluate baseline inference, single-pass RAG, and iterative retrieval refinement workflows to measure the impact of retrieved video evidence on answer quality, reasoning accuracy, and execution latency.

The repository provides a reproducible notebook-driven research environment using public VideoQA datasets, modular AI workflows, and configurable multimodal components suitable for research experimentation and future IEEE-style publication development.

## Motivation and Research Problem

The rapid growth of video-based data has increased demand for AI systems capable of understanding visual scenes, motion, temporal relationships, and contextual interactions across long video sequences. Unlike static-image understanding, VideoQA requires reasoning across both spatial and temporal information, making it a challenging benchmark for multimodal AI systems.

Recent RAG methods improve VideoQA by retrieving relevant frames, clips, captions, transcripts, and embedding representations prior to inference. These approaches aim to improve contextual accuracy and reduce hallucinations during question answering.

Despite recent advances, major challenges remain involving temporal grounding, retrieval refinement, and the interaction between retrieval workflows and LLM inference behavior. This project investigates these challenges through comparative evaluation of baseline, single-pass, and iterative RAG workflows across public VideoQA benchmarks.

## Research Objectives

This project investigates how iterative RAG workflows influence VideoQA performance within multimodal video understanding systems. The research emphasizes comparative evaluation of baseline inference, single-pass retrieval, and multi-pass retrieval refinement strategies.

The objectives of this work include measuring how retrieval depth and evidence refinement affect temporal reasoning, retrieval quality, answer accuracy, and execution latency using the NExT-QA benchmark dataset. Comparative experiments analyze direct inference without retrieval alongside progressively deeper RAG workflows incorporating recursive evidence refinement across multimodal video representations.

Additional objectives include evaluating latency-versus-performance tradeoffs, retrieval behavior across multiple inference passes, and the point at which additional retrieval refinement produces diminishing returns.

To isolate the impact of retrieval strategies, the same multimodal foundation model is used throughout all experiments. Baseline VideoQA, single-pass RAG, and iterative RAG workflows are evaluated using Qwen2-VL-7B, enabling direct comparison of retrieval-assisted inference methods while controlling for model architecture.

The primary research hypothesis is that iterative evidence refinement can improve VideoQA answer accuracy and temporal reasoning performance relative to both direct inference and single-pass retrieval workflows.

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

The experimental framework is centered on the Qwen2-VL-7B multimodal foundation model. Video evidence generated during preprocessing is organized into searchable evidence representations consisting of sampled frames, clips, metadata records, and derived evidence artifacts. During inference, natural-language questions are matched against the evidence repository using configurable retrieval strategies. Retrieved evidence is then supplied to Qwen2-VL-7B for VideoQA reasoning and answer generation.

The system architecture supports three primary inference workflows:

1. **Baseline VideoQA** — Direct VideoQA inference using Qwen2-VL-7B and sampled video evidence without retrieval assistance.

2. **Single-Pass RAG VideoQA** — Retrieval of relevant video evidence from the evidence repository followed by VideoQA inference using Qwen2-VL-7B.

3. **Iterative RAG VideoQA** — Multi-pass retrieval and evidence refinement workflows that revisit relevant portions of the source video to improve evidence selection, temporal grounding, and answer quality.

Video preprocessing generates frames, clips, motion and scene metadata, evidence records, and other supporting representations that are stored within a searchable evidence repository. During inference, retrieval strategies identify relevant evidence for a given question and provide this context to Qwen2-VL-7B for reasoning and answer generation.

The architecture is designed to isolate the effects of retrieval and evidence-refinement strategies while maintaining a consistent foundation model across all experiments. This enables direct comparison of baseline inference, single-pass retrieval, and iterative retrieval workflows while controlling for underlying model architecture.

---

### Pipeline Flowchart

<a href="images/overview_pipeline.png" target="_blank">
  <img src="images/overview_pipeline.png" width="800">
</a>

### Notebook Workflow

The project is organized into a sequence of notebooks that support reproducible experimentation across baseline, Retrieval-Augmented Generation (RAG), and iterative RAG VideoQA workflows.

| Notebook                         | Purpose                                                                                  |
| -------------------------------- | ---------------------------------------------------------------------------------------- |
| 01_Prepare_Video_Data            | Prepare and validate the NExT-QA dataset.                                                |
| 02_Prepare_Video_Evidence        | Generate evidence metadata and video evidence representations.                           |
| 03_Run_Baseline_VideoQA          | Perform baseline VideoQA inference using Qwen2-VL-7B.                                    |
| 04_Build_Video_Knowledge_Base    | Generate embeddings and retrieval indexes for video evidence.                            |
| 05_Run_RAG_VideoQA               | Perform single-pass Retrieval-Augmented VideoQA inference.                               |
| 06_Run_Iterative_RAG_Experiments | Execute iterative retrieval and evidence refinement experiments.                         |
| 07_Generate_Reports              | Generate evaluation metrics, analysis summaries, visualizations, and experiment reports. |


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

| Component                    | Purpose                                                             |
| ---------------------------- | ------------------------------------------------------------------- |
| Evidence Generation Pipeline | Generate evidence metadata and video evidence representations       |
| Knowledge Base Pipeline      | Generate embeddings and retrieval indexes                           |
| Qwen2-VL-7B Foundation Model | Perform VideoQA reasoning and answer generation                     |
| Retrieval Engine             | Select relevant evidence for inference                              |
| Reporting Pipeline           | enerate evaluation metrics, visualizations, and experiment reports  |

## Repository Organization

The repository is organized as a modular notebook-driven research environment designed to support reproducible experimentation across baseline and iterative RAG-based VideoQA workflows.

The structure separates dataset preparation, media extraction, evidence generation, knowledge base construction, retrieval workflows, inference pipelines, evaluation procedures, reporting workflows, and visualization stages into independently executable notebooks and configuration modules.

Supporting directories include benchmark dataset resources, extracted video assets, question-answer annotations, metadata resources, vector indexes, generated embeddings, experimental outputs, configuration modules, notebooks, and documentation resources intended to support extensible multimodal AI research workflows.

## Notebook Design Philosophy

The notebooks are designed to be independently executable and reproducible within Google Colab and local Jupyter environments. Every major code cell should produce visible output confirming successful execution, key runtime information, or generated artifacts.

## Expected Contributions

This work contributes a reproducible experimental framework for investigating iterative retrieval-assisted inference within VideoQA systems. The research is designed to provide insight into retrieval refinement strategies, temporal reasoning behavior, and latency-versus-performance tradeoffs across baseline and multi-pass RAG workflows.

Expected contributions include comparative performance benchmarks, retrieval analysis visualizations, and evaluation of how iterative retrieval depth influences VideoQA performance and inference latency.

The repository additionally provides an extensible notebook-driven research platform intended to support future experimentation involving iterative RAG workflows, vector databases, embedding models, and scalable VideoQA inference systems.

The project emphasizes system-level evaluation of modern foundation models and retrieval architectures rather than supervised training of a new VideoQA model.

A central contribution of this work is the evaluation of iterative evidence refinement while holding the underlying VideoQA foundation model constant. This enables quantitative analysis of how evidence selection strategies influence answer quality, temporal reasoning performance, and retrieval effectiveness independent of model architecture.

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

