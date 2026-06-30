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

The objective of this project is to compare pretrained and
self-supervised video representations for downstream multiple-choice
VideoQA. Learned autoencoder video representations are evaluated
against pretrained CLIP video representations using a shared CLIP text
embedding dataset, a common downstream classifier, and an identical
evaluation framework.

## Experimental Framework

The experimental framework consists of three complementary pipelines:

- Baseline VideoQA using Qwen2-VL
- Representation-Based VideoQA using pretrained CLIP video and shared CLIP text embeddings
- Representation-Based VideoQA using self-supervised autoencoder video embeddings and shared CLIP text embeddings

Development-mode execution is used to validate notebook functionality and tune experiment parameters before full-dataset evaluation. The representation-based pipelines share identical text representations, classifier, and evaluation methodology, isolating the impact of the video representation.

Shared CLIP text and pretrained CLIP video embeddings are generated once and stored as reusable shared artifacts. These artifacts are reused across all downstream representation-based VideoQA experiments, while autoencoder-generated video representations remain experiment-specific.

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

The videos are used for baseline VideoQA inference, pretrained CLIP video representation generation, self-supervised autoencoder training, and autoencoder latent representation generation. NExT-QA questions and answer choices are encoded as a reusable shared CLIP text embedding dataset for downstream representation-based VideoQA evaluation.

## Experimental Hypothesis

The primary research hypothesis is:

> Self-supervised autoencoder video representations can provide more effective downstream VideoQA performance than pretrained CLIP video representations when both are evaluated using identical CLIP text embeddings and the same downstream classifier.

The project further investigates whether learned autoencoder representations can provide meaningful latent structure for downstream VideoQA evaluation when compared with
pretrained CLIP video representations under a common evaluation
framework.

## ⚙️ Execution Notes

- Designed primarily for Google Colab
- Supports local Jupyter execution
- Notebook-driven workflow
- Shared CLIP text and pretrained CLIP video embedding datasets generated once and stored independently of experiments
- Experiment-specific autoencoder artifacts stored by experiment name
- Development and full-dataset execution modes
- GPU acceleration where appropriate
- Modular and reproducible experimental framework
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
