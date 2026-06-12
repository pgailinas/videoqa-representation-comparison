# Comparing Autoencoder-Based and Pretrained Video Representations for VideoQA

This project investigates self-supervised representation learning for Video Question Answering (VideoQA) using the NExT-QA benchmark dataset and the Qwen2-VL-7B multimodal foundation model.

Rather than training a VideoQA model from scratch, the project explores how different video representations influence downstream VideoQA performance. Specifically, the study compares representations learned through self-supervised autoencoder training against pretrained video representations while maintaining a fixed VideoQA model across all experiments.

Qwen2-VL-7B serves as the common VideoQA inference model, allowing performance differences to be attributed primarily to the quality of the underlying video representations rather than changes in model architecture.

The experimental framework compares three VideoQA workflows:

1. **Baseline VideoQA** — Direct VideoQA inference using sampled video evidence and Qwen2-VL-7B.
2. **Pretrained Representation VideoQA** — Evidence selection using pretrained video representations followed by Qwen2-VL-7B inference.
3. **Autoencoder Representation VideoQA** — Evidence selection using latent representations learned through self-supervised autoencoder training followed by Qwen2-VL-7B inference.

The project focuses on:

* Video Question Answering (VideoQA)
* Self-Supervised Learning
* Autoencoders
* Representation Learning
* Latent Feature Extraction
* Video Embeddings
* Temporal Reasoning
* Evidence-Based Video Retrieval
* Multimodal Foundation Models
* Downstream Task Evaluation

## Dataset

The primary benchmark dataset is **NExT-QA**, containing:

* 5,440 videos
* 47,692 question-answer pairs
* Official training, validation, and test splits
* Temporal, causal, and descriptive reasoning tasks

Video evidence is segmented into structured evidence units that serve as inputs for representation learning, retrieval, and VideoQA experimentation.

## Experimental Hypothesis

The primary research hypothesis is:

> Self-supervised video representations learned through autoencoder training can provide evidence representations that are competitive with or superior to pretrained video representations for downstream VideoQA tasks.

The project further investigates whether learned latent representations improve evidence selection and ultimately influence VideoQA answer quality when compared with pretrained representations and direct baseline inference.

## ⚙️ Execution Notes

* Designed primarily for Google Colab
* Supports local Jupyter execution
* Notebook-driven workflow
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

