---
title: Home
nav_order: 0
---

# Iterative Retrieval-Augmented Video Question Answering

## Project Overview

## Project Overview

This project investigates iterative Retrieval-Augmented Generation (RAG) workflows for Video Question Answering (VideoQA) through comparative evaluation of baseline inference, single-pass retrieval, and multi-pass retrieval refinement strategies within multimodal video understanding systems.

The framework combines video preprocessing, frame and clip extraction, embedding generation, vector database indexing, and multimodal large language model (LLM) inference to examine how iterative evidence retrieval influences temporal reasoning, answer quality, retrieval effectiveness, and execution latency across VideoQA tasks.

The project emphasizes analysis of retrieval refinement behavior by comparing direct inference without retrieval against progressively deeper retrieval-assisted workflows, including single-pass, two-pass, and three-pass RAG pipelines.

The repository provides a reproducible notebook-driven research environment using public VideoQA datasets, modular AI workflows, and configurable multimodal components suitable for research experimentation and future IEEE-style publication development.

## Motivation and Research Problem

The rapid growth of video-based data has increased demand for AI systems capable of understanding visual scenes, motion, temporal relationships, and contextual interactions across long video sequences. Unlike static-image understanding, VideoQA requires reasoning across both spatial and temporal information, making it a challenging benchmark for multimodal AI systems.

Recent RAG methods improve VideoQA by retrieving relevant frames, clips, captions, transcripts, and embedding representations prior to inference. These approaches aim to improve contextual accuracy and reduce hallucinations during question answering.

Despite recent advances, major challenges remain involving temporal grounding, retrieval refinement, and the interaction between retrieval workflows and LLM inference behavior. This project investigates these challenges through comparative evaluation of baseline, single-pass, and iterative RAG workflows across public VideoQA benchmarks.

## Research Objectives

This project investigates how iterative RAG workflows influence VideoQA performance within multimodal video understanding systems. The research emphasizes comparative evaluation of baseline inference, single-pass retrieval, and multi-pass retrieval refinement strategies.

The objectives of this work include measuring how retrieval depth and evidence refinement affect temporal reasoning, retrieval quality, answer accuracy, and execution latency across public VideoQA datasets. Comparative experiments analyze direct inference without retrieval alongside progressively deeper RAG workflows incorporating recursive evidence refinement across frames, clips, captions, and transcript representations.

Additional objectives include evaluating latency-versus-performance tradeoffs, retrieval behavior across multiple inference passes, and the point at which additional retrieval refinement produces diminishing returns.

## Datasets

Public VideoQA benchmark datasets, including MSVD-QA and TGIF-QA, are used to evaluate baseline and iterative RAG-based video understanding workflows. These datasets provide annotated video samples, captions, and question-answer pairs spanning diverse visual scenes, actions, temporal relationships, and reasoning tasks.

The selected datasets support reproducible evaluation of retrieval refinement strategies, temporal reasoning performance, answer accuracy, and latency across varying VideoQA question types and inference workflows.

## System Architecture

The experimental framework integrates embedding generation, vector database indexing, evidence retrieval, and multimodal LLM inference to support evaluation of baseline and iterative RAG-based VideoQA workflows.

Raw video inputs are processed into frames and short clips for feature extraction. Pretrained multimodal models generate embeddings, captions, and optional transcript representations, which are indexed within a vector database for similarity-based retrieval during inference.

At query time, natural-language questions are converted into query embeddings and matched against indexed video representations to retrieve relevant frames, clips, captions, or transcript segments. Retrieved evidence is then provided to a multimodal LLM to generate contextually informed responses.

The framework supports baseline inference without retrieval alongside single-pass, two-pass, and three-pass iterative RAG workflows, enabling analysis of temporal reasoning performance, retrieval refinement behavior, and latency-versus-accuracy tradeoffs.

---

### Pipeline Flowchart

![VideoQA Pipeline](images/overview_pipeline.png)

## Experimental Methodology

The experimental framework evaluates baseline VideoQA workflows alongside retrieval-assisted approaches using multiple retrieval configurations, embedding strategies, and inference pipelines. Comparative analysis is performed across frame-level, clip-level, and multimodal evidence representations to investigate their impact on answer accuracy, temporal reasoning, contextual relevance, and retrieval effectiveness.

The methodology includes evaluation of baseline multimodal models and inference workflows without external retrieval, as well as single-pass and iterative RAG pipelines incorporating recursive evidence refinement across frames, clips, captions, and transcript representations. Representative components may include architectures such as CLIP, BLIP-2, Video-LLaVA, Qwen-VL, and related vision-language models integrated within experimental workflows.

Experiments are designed to analyze how retrieval granularity, embedding selection, vector similarity search strategies, and iterative inference behavior influence VideoQA performance across benchmark datasets. Evaluation metrics may include answer accuracy, retrieval precision and recall, semantic similarity measures, contextual relevance, and comparative inference performance across baseline and retrieval-augmented systems.

## Implementation Framework

The implementation framework integrates open-source multimodal models, vector databases, and Python-based AI frameworks to support reproducible VideoQA experimentation across multiple inference workflows. The framework is designed to support modular evaluation of embedding approaches, retrieval configurations, vector indexing strategies, and inference behavior within both Google Colab and local development environments.

The implementation incorporates pretrained vision-language models, multimodal LLMs, vector similarity search systems, and GPU-accelerated inference libraries to support scalable experimentation. Supporting technologies include PyTorch, Hugging Face Transformers, LangChain, FAISS, ChromaDB, OpenCV, and related libraries used for feature extraction, embedding generation, vector indexing, retrieval, and experimental evaluation.

## Repository Organization

The repository is organized as a modular notebook-driven research environment designed to support reproducible VideoQA experimentation and comparative evaluation workflows. The structure separates dataset preparation, media extraction, embedding generation, vector indexing, retrieval workflows, inference pipelines, evaluation procedures, and visualization stages into independently executable notebooks and configuration modules.

The organization emphasizes scalable dataset management, reusable configuration infrastructure, reproducible experiment execution, and clear separation between preprocessing, retrieval, inference, evaluation, and analysis stages. Supporting directories include benchmark datasets, extracted media assets, metadata resources, vector indexes, generated embeddings, experimental outputs, figures, configuration modules, and documentation resources intended to support extensible multimodal AI research workflows.

## Expected Contributions

This work contributes a reproducible experimental framework for investigating retrieval-assisted inference within VideoQA systems. The research is designed to provide insight into evidence retrieval strategies, embedding approaches, iterative refinement workflows, and their impact on temporally complex video understanding tasks.

The framework supports systematic evaluation across multiple benchmark datasets, retrieval methods, and inference configurations. Expected contributions include comparative performance benchmarks, retrieval and inference analysis visualizations, and architectural insights into how retrieved evidence affects VideoQA behavior and response quality.

The repository additionally provides an extensible multimodal AI research platform intended to support future experimentation involving vector databases, embedding models, retrieval workflows, and scalable video inference systems.

---

## References and Further Reading

Additional papers, datasets, models, and technical resources related to this project are available on the [References and Further Reading](References.md) page.

---

## Author

**Phil Gailinas**  
- M.S. Computer Engineering candidate  
- University of New Mexico
- Project initiated 05-20-2026

## License

This project is intended for academic and research use.

