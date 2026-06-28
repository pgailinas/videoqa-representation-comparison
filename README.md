# Investigating Self-Supervised Autoencoder Learning for VideoQA

This project investigates self-supervised autoencoder learning for Video
Question Answering (VideoQA) using the NExT-QA benchmark dataset
together with pretrained CLIP representations and the Qwen2-VL-7B
multimodal foundation model.

The project compares three complementary approaches:

-   **Baseline VideoQA** using Qwen2-VL and the original videos.
-   **Representation-Based VideoQA** using pretrained CLIP video
    embeddings.
-   **Representation-Based VideoQA** using self-supervised autoencoder
    latent representations.

Both representation-based approaches use common CLIP text
representations and the same downstream classifier, allowing differences
in VideoQA performance to be attributed primarily to the quality of the
video representations.

## Research Objective

The objective of this project is to compare pretrained and
self-supervised video representations for downstream multiple-choice
VideoQA. Learned autoencoder representations are evaluated against
pretrained CLIP video representations using a common text representation
and evaluation framework.

## Experimental Framework

The experimental framework consists of three pipelines:

- Baseline VideoQA using Qwen2-VL
- Representation-Based VideoQA using pretrained CLIP video representations
- Representation-Based VideoQA using self-supervised autoencoder latent representations

Development-subset experiments are used for parameter optimization
before full-dataset evaluation. The representation-based pipelines share
identical text representations, classifier, and evaluation methodology,
isolating the impact of the video representation.

The project focuses on:

-   Video Question Answering (VideoQA)
-   Self-Supervised Learning
-   Autoencoders
-   Video Representation Learning
-   Multimodal Representation Learning
-   CLIP Representations
-   Latent Feature Learning
-   Multiple-Choice VideoQA
-   Experimental Performance Analysis

## Dataset

The primary benchmark dataset is **NExT-QA**, containing:

-   5,440 videos
-   47,692 question-answer pairs
-   Official training, validation, and test splits
-   Temporal, causal, and descriptive reasoning tasks

The videos are used for baseline VideoQA inference, pretrained CLIP video representation generation, self-supervised autoencoder training, and autoencoder latent representation generation. NExT-QA questions and answer choices are encoded as common CLIP text representations for downstream representation-based VideoQA evaluation.

## Experimental Hypothesis

The primary research hypothesis is:

> Self-supervised autoencoder learning can produce compact latent video
> representations that preserve sufficient semantic and temporal
> information to support effective downstream VideoQA.

The project further investigates whether learned autoencoder representations can provide meaningful latent structure for downstream VideoQA evaluation when compared with
pretrained CLIP video representations under a common evaluation
framework.

## ⚙️ Execution Notes

-   Designed primarily for Google Colab
-   Supports local Jupyter execution
-   Notebook-driven workflow
- Experiment artifacts stored by experiment name in Google Drive
-   Development and full-dataset execution modes
-   GPU acceleration where appropriate
-   Modular and reproducible experimental framework

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
