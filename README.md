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

The objective of this project is to compare pretrained and self-supervised video representations for downstream multiple-choice VideoQA. Learned `autoencoder_video` representations are evaluated against pretrained `clip_video` representations using shared `clip_text` representations, a common Fusion MLP classifier, and an identical evaluation framework.

## Experimental Framework

The project implements three complementary VideoQA pipelines:

* **Baseline VideoQA** using Qwen2-VL and the original videos.
* **Representation-Based VideoQA** using pretrained `clip_video` representations together with shared `clip_text` representations.
* **Representation-Based VideoQA** using self-supervised `autoencoder_video` representations together with the same shared `clip_text` representations.

Development-mode execution supports rapid experimentation, debugging, and parameter tuning before full-dataset evaluation. The two representation-based pipelines use an identical Fusion MLP classifier, multiple-choice prediction workflow, and evaluation methodology, allowing differences in performance to be attributed primarily to the quality of the video representations.

Shared CLIP text and CLIP video representations are generated once and reused across experiments, while autoencoder video representations remain experiment-specific.

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

> Self-supervised `autoencoder_video` representations can provide more effective downstream multiple-choice VideoQA performance than pretrained `clip_video` representations when both are evaluated using identical `clip_text` representations, the same Fusion MLP classifier, and a common evaluation framework.

The project further investigates whether self-supervised representation learning can produce video embeddings that improve downstream VideoQA performance while maintaining a consistent multimodal classification pipeline.

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
