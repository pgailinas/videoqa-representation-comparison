# Comparing Pretrained and Autoencoder-Based Representations for VideoQA

This project investigates self-supervised representation learning for Video Question Answering (VideoQA) using the NExT-QA benchmark dataset and the Qwen2-VL-7B multimodal foundation model.

Rather than training a VideoQA model from scratch, the project explores how different video representations influence downstream VideoQA performance. Specifically, the study compares representations learned through self-supervised autoencoder training against pretrained video representations while maintaining a fixed VideoQA model across all experiments.

Qwen2-VL-7B serves as the common VideoQA inference model, allowing performance differences to be attributed primarily to the quality of the underlying video representations rather than changes in model architecture.

## Research Objective

The objective of this project is to investigate whether compact latent video representations learned through self-supervised autoencoder training can preserve sufficient semantic and temporal information to support downstream VideoQA tasks. Performance is compared against both direct video inference and pretrained video representations using a common VideoQA model and evaluation framework.

## Experimental Framework

The experimental framework compares three VideoQA workflows using a two-stage evaluation process. Development subset experiments are used for parameter optimization and workflow validation. Optimized configurations are then applied to full-dataset experiments for final performance evaluation and comparison.

1. **Direct VideoQA Baseline** — Direct VideoQA inference using sampled video evidence and Qwen2-VL-7B.

2. **Pretrained Representation VideoQA** — Video representations generated using a pretrained representation model and supplied to Qwen2-VL-7B for VideoQA inference.

3. **Autoencoder Representation VideoQA** — Video representations generated through self-supervised autoencoder training and supplied to Qwen2-VL-7B for VideoQA inference.

The project focuses on:

* Video Question Answering (VideoQA)
* Self-Supervised Learning
* Autoencoders
* Representation Learning
* Latent Feature Extraction
* Latent Space Analysis
* Temporal Reasoning
* Multimodal Foundation Models
* Downstream Task Evaluation
* Experimental Performance Comparison

## Dataset

The primary benchmark dataset is **NExT-QA**, containing:

* 5,440 videos
* 47,692 question-answer pairs
* Official training, validation, and test splits
* Temporal, causal, and descriptive reasoning tasks

Video evidence is segmented into structured evidence units that serve as inputs for representation learning, latent feature generation, and VideoQA experimentation.

Development subset experiments are used during parameter optimization to reduce computational cost. Final experimental results are generated using full-dataset execution with optimized configurations.

## Experimental Hypothesis

The primary research hypothesis is:

> Self-supervised video representations learned through autoencoder training can provide compact latent representations that are competitive with or superior to pretrained video representations for downstream VideoQA tasks.

The project further investigates whether learned latent representations preserve semantic and temporal information sufficiently to support effective VideoQA reasoning when compared with pretrained representations and direct baseline inference.

## ⚙️ Execution Notes

* Designed primarily for Google Colab
* Supports local Jupyter execution
* Notebook-driven workflow
* Development subset experiments support parameter optimization
* Full-dataset experiments use frozen optimized configurations
* GPU acceleration used where appropriate
* Modular execution allows independent experimentation stages
* Reproducible evaluation framework for representation comparison

## 🌐 Documentation

Complete project documentation, notebook walkthroughs, architecture diagrams, and experimental methodology are available at:

https://pgailinas.github.io/videoqa-representation-comparison/

## 👤 Author

**Phil Gailinas**

* M.S. Computer Engineering Candidate
* University of New Mexico

## 📄 License

This project is intended for academic and research use.

