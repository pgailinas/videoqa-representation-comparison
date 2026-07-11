# Investigating Self-Supervised Autoencoder Learning for VideoQA

This project investigates self-supervised autoencoder learning for Video
Question Answering (VideoQA) using the NExT-QA benchmark dataset
together with pretrained CLIP representations and the Qwen2-VL-7B
multimodal foundation model.

The project evaluates three complementary VideoQA approaches:

-   **Baseline VideoQA** using Qwen2-VL and the original videos.
-   **Representation-Based VideoQA** using pretrained CLIP video
    embeddings.
-   **Representation-Based VideoQA** using self-supervised autoencoder
    latent representations.

Both representation-based approaches use a shared CLIP text embedding dataset, the same downstream classifier, and identical evaluation methodology, allowing differences in VideoQA performance to be attributed primarily to the quality of the video representations.

## Research Objective

The objective of this project is to compare pretrained and self-supervised video representations for downstream multiple-choice VideoQA. Learned `autoencoder_video` representations are evaluated against pretrained `clip_video` representations using shared `clip_text` question-answer representations, configurable representation-based prediction methods, and a common evaluation framework.

## Experimental Framework

The project implements three complementary VideoQA pipelines:

* **Baseline VideoQA** using Qwen2-VL and the original videos.
* **Representation-Based VideoQA** using pretrained `clip_video` representations together with shared `clip_text` representations.
* **Representation-Based VideoQA** using self-supervised `autoencoder_video` representations together with the same shared `clip_text` representations.

Development-mode execution supports rapid experimentation, debugging, and parameter tuning before full-dataset evaluation.

Both representation-based pipelines use the same shared `clip_text` question-answer representations, identical multiple-choice prediction workflow, and common evaluation methodology. The active experiment may use cosine similarity or one of several learned multimodal fusion classifiers, allowing both the video representation source and the prediction method to be evaluated independently.

Shared CLIP text representations are generated once and reused across all representation-based experiments. Shared CLIP video representations are likewise generated once and reused, while autoencoder video representations remain experiment-specific.

The project focuses on:

* Video Question Answering (VideoQA)
* Self-Supervised Learning
* Autoencoders
* Video Representation Learning
* Multimodal Representation Learning
* CLIP Representations
* Latent Feature Learning
* Multiple-Choice VideoQA
* Experimental Performance Analysis

## Dataset

The primary benchmark dataset is **NExT-QA**, containing:

-   5,440 videos
-   47,692 question-answer pairs
-   Official training, validation, and test splits
-   Temporal, causal, and descriptive reasoning tasks

The videos are used for baseline VideoQA inference, pretrained CLIP video representation generation, self-supervised autoencoder training, and autoencoder latent representation generation. NExT-QA questions and answer choices are encoded as a reusable shared CLIP text embedding dataset for downstream representation-based VideoQA evaluation.

## Experimental Hypothesis

The primary research hypothesis is:

> Self-supervised `autoencoder_video` representations can provide more effective downstream multiple-choice VideoQA performance than pretrained `clip_video` representations when both are evaluated using identical shared `clip_text` question-answer representations, the same representation-based prediction method, and a common evaluation framework.

The project further investigates whether self-supervised representation learning can produce video embeddings that improve downstream VideoQA performance while maintaining a consistent multimodal classification pipeline.

## ⚙️ Execution Notes

- Designed primarily for Google Colab
- Supports local Jupyter execution
- Notebook-driven workflow
- Shared CLIP question-answer text and pretrained CLIP video representation datasets generated once and reused across experiments
- Experiment-specific autoencoder artifacts stored by experiment name
- Development and full-dataset execution modes
- GPU acceleration where appropriate
- Modular experimental framework supporting multiple representation sources and prediction methods
- Local-first artifact generation with optional promotion to shared Google Drive storage

## 🌐 Documentation

Complete project documentation, notebook walkthroughs, architecture
diagrams, and experimental methodology are available at:

https://pgailinas.github.io/videoqa-representation-comparison/

## 👤 Author

**Phil Gailinas**

-   M.S. Computer Engineering Candidate
-   University of New Mexico

## 📄 License

This project is intended for academic and research use.
