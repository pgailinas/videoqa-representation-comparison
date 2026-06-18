# Investigating Self-Supervised Autoencoder Learning for VideoQA

This project investigates self-supervised autoencoder learning for Video Question Answering (VideoQA) using the NExT-QA benchmark dataset and the Qwen2-VL-7B multimodal foundation model.

Rather than training a VideoQA model from scratch, the project investigates whether compact video representations learned through self-supervised autoencoder training preserve sufficient semantic and temporal information to support downstream VideoQA tasks. The study compares a baseline VideoQA workflow using original video evidence with an autoencoder-based workflow using reconstructed video evidence while maintaining a fixed VideoQA inference model across all experiments.

Qwen2-VL-7B serves as the common VideoQA inference model, allowing performance differences to be attributed primarily to the quality of the learned video representations rather than changes in model architecture.

## Research Objective

The objective of this project is to investigate whether compact video representations learned through self-supervised autoencoder training can preserve sufficient semantic and temporal information to support downstream VideoQA tasks. The study evaluates the relationship between representation compression, reconstruction quality, and VideoQA performance using a common inference model and evaluation framework.

## Experimental Framework

The experimental framework evaluates two VideoQA workflows using a two-stage methodology. Development-subset experiments are used for parameter optimization and workflow validation. Optimized configurations are then applied to full-dataset experiments for final performance evaluation.

1. **Direct VideoQA Baseline** — Direct VideoQA inference using original video evidence and Qwen2-VL-7B.

2. **Autoencoder-Based VideoQA** — Self-supervised autoencoder training, reconstructed video generation, and downstream VideoQA inference using Qwen2-VL-7B.

The project focuses on:

* Video Question Answering (VideoQA)
* Self-Supervised Learning
* Autoencoders
* Video Representation Learning
* Video Compression
* Reconstruction Quality Analysis
* Temporal Reasoning
* Multimodal Foundation Models
* Downstream Task Evaluation
* Experimental Performance Analysis

## Dataset

The primary benchmark dataset is **NExT-QA**, containing:

* 5,440 videos
* 47,692 question-answer pairs
* Official training, validation, and test splits
* Temporal, causal, and descriptive reasoning tasks

The NExT-QA videos are used for self-supervised autoencoder training, while the benchmark questions and answers are used to evaluate downstream VideoQA performance.

Development-subset experiments are used during parameter optimization to reduce computational cost. Final experimental results are generated using full-dataset execution with optimized configurations.

## Experimental Hypothesis

The primary research hypothesis is:

> Self-supervised autoencoder learning can produce compact video representations that preserve sufficient semantic and temporal information to support effective downstream VideoQA reasoning.

The project further investigates how representation compression, reconstruction quality, and information loss influence VideoQA performance across causal, temporal, and descriptive reasoning tasks.

## ⚙️ Execution Notes

* Designed primarily for Google Colab
* Supports local Jupyter execution
* Notebook-driven workflow
* Development-subset experiments support parameter optimization
* Full-dataset experiments use selected configurations
* GPU acceleration used where appropriate
* Modular execution allows independent experimentation stages
* Reproducible evaluation framework

## 🌐 Documentation

Complete project documentation, notebook walkthroughs, architecture diagrams, and experimental methodology are available at:

https://pgailinas.github.io/videoqa-representation-comparison/

## 👤 Author

**Phil Gailinas**

* M.S. Computer Engineering Candidate
* University of New Mexico

## 📄 License

This project is intended for academic and research use.


