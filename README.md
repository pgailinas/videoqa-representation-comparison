# Iterative RAG for VideoQA

This project investigates iterative Retrieval-Augmented Generation (RAG) workflows for Video Question Answering (VideoQA) using the NExT-QA benchmark dataset and the Qwen2-VL-7B multimodal foundation model.

Rather than training a new VideoQA model from scratch, the project evaluates how evidence retrieval and iterative evidence refinement influence VideoQA performance. Qwen2-VL-7B serves as the fixed foundation model across all experiments, allowing performance differences to be attributed to retrieval strategy rather than model architecture.

The experimental framework compares three inference workflows:

1. **Baseline VideoQA** — Direct VideoQA inference using sampled video evidence.
2. **Single-Pass RAG VideoQA** — Retrieval of relevant video evidence prior to inference.
3. **Iterative RAG VideoQA** — Multi-pass retrieval and evidence refinement that revisits relevant portions of source videos to improve evidence selection and answer quality.

The project focuses on:

* Video Question Answering (VideoQA)
* Retrieval-Augmented Generation (RAG)
* Iterative evidence refinement
* Temporal reasoning
* Evidence-based video retrieval
* Multimodal foundation models
* Vector similarity search
* Retrieval effectiveness
* Latency-versus-performance tradeoffs

## Dataset

The primary benchmark dataset is **NExT-QA**, containing:

* 5,440 videos
* 47,692 question-answer pairs
* Official training, validation, and test splits
* Temporal, causal, and descriptive reasoning tasks

## Experimental Hypothesis

The primary research hypothesis is:

> Iterative evidence refinement can improve VideoQA answer accuracy and temporal reasoning performance relative to both direct inference and single-pass retrieval workflows.

## ⚙️ Execution Notes

* Designed primarily for Google Colab
* Supports local Jupyter execution
* Notebook-driven workflow
* GPU acceleration used where appropriate
* Modular execution allows independent experimentation stages

## 🌐 Documentation

Complete project documentation, notebook walkthroughs, architecture diagrams, and experimental methodology are available at:

https://pgailinas.github.io/iterative-video-rag/

## 👤 Author

**Phil Gailinas**

* M.S. Computer Engineering Candidate
* University of New Mexico

## 📄 License

This project is intended for academic and research use.



