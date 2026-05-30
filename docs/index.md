---
title: Home
nav_order: 0
---

# Iterative RAG for VideoQA

## Project Overview

This project investigates iterative Retrieval-Augmented Generation (RAG) workflows for Video Question Answering (VideoQA) using the NExT-QA benchmark dataset and pretrained multimodal foundation models.

Rather than training a new VideoQA model from scratch, the project evaluates how pretrained vision encoders, vision-language captioning models, vector retrieval systems, and large language models can be combined to improve video understanding and temporal reasoning performance.

The framework processes raw videos into sampled frames, generated captions, embedding representations, and searchable vector indexes. Comparative experiments evaluate baseline inference, single-pass RAG, and iterative retrieval refinement workflows to measure the impact of retrieved video evidence on answer quality, reasoning accuracy, and execution latency.

The repository provides a reproducible notebook-driven research environment using public VideoQA datasets, modular AI workflows, and configurable multimodal components suitable for research experimentation and future IEEE-style publication development.

## Motivation and Research Problem

The rapid growth of video-based data has increased demand for AI systems capable of understanding visual scenes, motion, temporal relationships, and contextual interactions across long video sequences. Unlike static-image understanding, VideoQA requires reasoning across both spatial and temporal information, making it a challenging benchmark for multimodal AI systems.

Recent RAG methods improve VideoQA by retrieving relevant frames, clips, captions, transcripts, and embedding representations prior to inference. These approaches aim to improve contextual accuracy and reduce hallucinations during question answering.

Despite recent advances, major challenges remain involving temporal grounding, retrieval refinement, and the interaction between retrieval workflows and LLM inference behavior. This project investigates these challenges through comparative evaluation of baseline, single-pass, and iterative RAG workflows across public VideoQA benchmarks.

## Research Objectives

This project investigates how iterative RAG workflows influence VideoQA performance within multimodal video understanding systems. The research emphasizes comparative evaluation of baseline inference, single-pass retrieval, and multi-pass retrieval refinement strategies.

The objectives of this work include measuring how retrieval depth and evidence refinement affect temporal reasoning, retrieval quality, answer accuracy, and execution latency using the NExT-QA benchmark dataset. Comparative experiments analyze direct inference without retrieval alongside progressively deeper RAG workflows incorporating recursive evidence refinement across multimodal video representations.

Additional objectives include evaluating latency-versus-performance tradeoffs, retrieval behavior across multiple inference passes, and the point at which additional retrieval refinement produces diminishing returns.

## Dataset

The primary benchmark dataset used in this project is NExT-QA, a VideoQA dataset designed for causal and temporal reasoning over video content.

The dataset provides raw video files, question-answer annotations, official training, validation, and test splits, and metadata required to associate questions with source videos.

The experimental dataset includes:

- NExT-QA video collection containing 5,440 MP4 videos
- Training, validation, and test question-answer splits
- Video identifier mapping metadata
- Optional relation annotations for advanced reasoning experiments

Raw videos are processed into frames, clips, captions, embeddings, and metadata representations during knowledge base construction. These generated artifacts are used by downstream RAG pipelines rather than repeatedly processing the original video files.

## System Architecture

The experimental framework integrates pretrained multimodal models, vector database indexing, evidence retrieval, and LLM inference to support baseline and iterative RAG-based VideoQA workflows.

The system is built around three primary pretrained model components:

1. **Vision Encoder** — generates embedding representations from sampled video frames and clips.

2. **Vision-Language Model** — generates textual descriptions and captions from visual content.

3. **Large Language Model** — performs question answering and reasoning using retrieved video evidence.

Raw video inputs are processed into frames and short clips during knowledge base construction. The generated embeddings, captions, and metadata representations are stored within a persistent vector database for similarity-based retrieval.

During inference, natural-language questions are converted into retrieval queries and matched against indexed video representations to identify relevant frames, clips, captions, and contextual evidence. Retrieved information is provided to the reasoning model to generate contextually grounded VideoQA responses.

The framework supports configurable retrieval strategies, including baseline inference, single-pass RAG, and iterative retrieval refinement workflows for analyzing temporal reasoning performance, retrieval effectiveness, and latency-versus-accuracy tradeoffs.

---

### Pipeline Flowchart

<a href="images/overview_pipeline.png" target="_blank">
  <img src="images/overview_pipeline.png" width="800">
</a>

## Experimental Methodology

The experimental framework evaluates how retrieval strategies and multimodal knowledge representations influence VideoQA performance. Experiments compare baseline inference against single-pass and iterative Retrieval-Augmented Generation (RAG) workflows using frame-level, clip-level, caption-based, and embedding-based video evidence.

The experiments evaluate three primary workflows:

1. **Baseline VideoQA Inference** — questions are answered using pretrained reasoning models without retrieval assistance.

2. **Single-Pass RAG Inference** — relevant video evidence is retrieved from the knowledge base and provided as additional context during answer generation.

3. **Iterative RAG Inference** — retrieval and reasoning are performed across multiple refinement passes to improve evidence selection and answer quality.

Representative system components may include pretrained vision encoders, vision-language models, LLMs, and vector retrieval systems such as CLIP, BLIP-2, Video-LLaVA, Qwen-VL, FAISS, and related technologies.

Experiments measure how retrieval strategy, evidence quality, and refinement depth affect temporal reasoning, answer accuracy, retrieval performance, and execution efficiency. Evaluation metrics may include answer accuracy, retrieval precision and recall, semantic relevance, execution time, and latency-versus-performance tradeoffs.

The objective is not to train a new VideoQA neural network, but to evaluate how modern foundation models and retrieval architectures can be combined to improve video reasoning performance.

## Implementation Framework

The implementation framework integrates open-source multimodal models, vector databases, and Python-based AI frameworks to support reproducible experimentation across baseline and iterative RAG-based VideoQA workflows.

The framework incorporates pretrained vision encoders, vision-language models, LLMs, vector similarity search systems, and GPU-accelerated inference libraries within Google Colab and local Jupyter environments. Supporting technologies may include PyTorch, Hugging Face Transformers, LangChain, FAISS, ChromaDB, OpenCV, and related libraries used for embedding generation, vector indexing, retrieval, inference, and experimental evaluation.

| Component | Purpose |
|---|---|
| Vision Encoder | Generate frame and video embeddings |
| Vision-Language Model | Generate video captions and descriptions |
| Vector Database | Store searchable video knowledge |
| Large Language Model | Perform answer reasoning |
| Evaluation Pipeline | Compare generated answers with benchmark QA labels |

## Repository Organization

The repository is organized as a modular notebook-driven research environment designed to support reproducible experimentation across baseline and iterative RAG-based VideoQA workflows.

The structure separates dataset preparation, media extraction, embedding generation, vector indexing, retrieval workflows, inference pipelines, evaluation procedures, and visualization stages into independently executable notebooks and configuration modules.

Supporting directories include benchmark dataset resources, extracted media assets, metadata resources, vector indexes, generated embeddings, experimental outputs, figures, configuration modules, and documentation resources intended to support extensible multimodal AI research workflows.

## Notebook Design Philosophy

The notebooks are designed to be independently executable and reproducible within Google Colab and local Jupyter environments. Every major code cell should produce visible output confirming successful execution, key runtime information, or generated artifacts.

## Expected Contributions

This work contributes a reproducible experimental framework for investigating iterative retrieval-assisted inference within VideoQA systems. The research is designed to provide insight into retrieval refinement strategies, temporal reasoning behavior, and latency-versus-performance tradeoffs across baseline and multi-pass RAG workflows.

Expected contributions include comparative performance benchmarks, retrieval analysis visualizations, and evaluation of how iterative retrieval depth influences VideoQA performance and inference latency.

The repository additionally provides an extensible notebook-driven research platform intended to support future experimentation involving iterative RAG workflows, vector databases, embedding models, and scalable VideoQA inference systems.

The project emphasizes system-level evaluation of modern foundation models and retrieval architectures rather than supervised training of a new VideoQA model.

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

