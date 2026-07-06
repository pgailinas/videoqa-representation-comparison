---
title: Project Decisions
nav_order: 13
has_toc: false
---

# Project Decisions

This document records significant project decisions, implementation direction changes, and architectural milestones for the VideoQA representation-learning project. Only major decisions that materially affect project design, workflow, methodology, or outcomes are recorded.

Dates are provided when known or when a decision corresponds to a significant project milestone. For some decisions, only the approximate development period is recorded.

---

## Project Formation (May 2026)

### 1) Initiate VideoQA Research Project (05/20)

**Decision:** Established a research project and GitHub repository to investigate Video Question Answering (VideoQA) using multimodal foundation models, public benchmark datasets, and reproducible notebook-driven experimentation.

**Rationale:** The project was created to support ECE-551 (Problems in Machine Learning) at the University of New Mexico and to provide a structured environment for exploring machine-learning approaches to video understanding, multimodal reasoning, and experimental evaluation. The repository serves as the authoritative source for project documentation, implementation, results, and research artifacts.

### 2) Adopt NExT-QA as the Primary Benchmark Dataset

**Decision:** -- Selected the NExT-QA benchmark dataset as the foundation for all VideoQA experiments.

**Rationale:** -- NExT-QA provides a widely used benchmark containing video-question-answer pairs designed to evaluate causal, temporal, and descriptive reasoning. The dataset offers sufficient scale and diversity to support representation-learning experiments and downstream VideoQA evaluation.

### 3) Use Qwen2-VL-7B as the Baseline VideoQA Model

**Decision:** Selected Qwen2-VL-7B as the baseline VideoQA model for evaluating original NExT-QA video evidence.

**Rationale:** The baseline workflow provides a strong multimodal reference for comparison with representation-based VideoQA pipelines. Using a single baseline model enables downstream evaluation of whether pretrained CLIP representations and self-supervised autoencoder representations preserve information useful for VideoQA reasoning.

### 4) Standardize the Downstream Representation-Based Classifier

**Decision:** Standardized on a common Fusion MLP classifier for all representation-based VideoQA methods while retaining Qwen2-VL as the baseline reference method.

**Rationale:** The objective of the project is to compare video representations rather than downstream classifier architectures. Both representation-based methods use the same Fusion MLP classifier, prediction workflow, and evaluation methodology, isolating the contribution of the video representation. The Qwen2-VL baseline provides the reference method using the original videos.

---

## Architecture Development (June 2026)

### 1) Separate Video Preparation and Evidence Generation

**Decision:** -- Established a dedicated preprocessing workflow responsible for generating structured video evidence resources prior to VideoQA experimentation.

**Rationale:** -- Separating preprocessing from downstream experimentation improves modularity, reduces redundant processing, and allows generated evidence resources to be reused across multiple experimental workflows.

### 2) Standardize on Evidence Segments for Autoencoder Training

**Decision:** Established structured video evidence segments as the primary unit of processing for self-supervised autoencoder training while retaining complete videos for baseline VideoQA and pretrained CLIP representation generation.

**Rationale:** Evidence segments improve the efficiency and scalability of self-supervised representation learning by allowing the autoencoder to learn from shorter temporal sequences. Baseline VideoQA and pretrained CLIP representations continue to operate on complete NExT-QA videos, ensuring each experimental pipeline uses the most appropriate representation source.

### 3) Adopt Evidence Metadata as the Central Intermediate Representation

**Decision:** -- Standardized on evidence metadata and structured video evidence records as the primary intermediate data representation used throughout the project.

**Rationale:** -- Evidence metadata provides a reusable abstraction between raw video assets and downstream experiments. This approach supports baseline VideoQA, pretrained representation generation, autoencoder training, and final evaluation using a common evidence framework.

### 4) Adopt Combined Archive Distribution Strategy

**Decision:** -- Replaced multipart video archive management with a single combined dataset archive.

**Rationale:** -- A single archive simplifies dataset management, reduces setup complexity, eliminates archive reconstruction steps, and improves reproducibility within Google Colab environments.

---

## Project Redesign (June 2026)

### 1) Transition from Retrieval-Augmented Generation to Representation Learning (06/11)

**Decision:** -- Refocused the project from Retrieval-Augmented Generation (RAG)-based VideoQA workflows to a comparative study of pretrained and autoencoder-based video representations.

**Rationale:** -- The revised direction increases emphasis on machine-learning concepts and self-supervised learning while providing a stronger alignment with course objectives centered on machine learning methodology and representation learning.

### 2) Introduce Autoencoder-Based Representation Learning (06/11)

**Decision:** -- Added self-supervised autoencoder training as a primary experimental workflow.

**Rationale:** -- Autoencoders provide a mechanism for learning compact latent video representations without requiring additional labels. These learned representations can be evaluated through downstream VideoQA performance and compared directly against pretrained representations.

### 3) Retain Baseline, Pretrained, and Autoencoder Experimental Pipelines

**Decision:** -- Organized the project around three comparative experimental workflows:

1. Baseline VideoQA
2. Pretrained Representation VideoQA
3. Autoencoder Representation VideoQA

**Rationale:** -- Maintaining all three workflows enables direct comparison between raw video evidence, pretrained feature representations, and learned latent representations while using a common evaluation framework.

### 4) Evaluate Representation Quality Through Downstream VideoQA Performance

**Decision:** -- Selected downstream VideoQA performance as the primary method for evaluating learned and pretrained video representations.

**Rationale:** -- While representation quality can be measured through reconstruction metrics, embedding statistics, or compression characteristics, downstream task performance provides a practical assessment of whether a representation preserves information useful for multimodal reasoning and question answering.

---

## Project Refinement (June 2026)

### 1) Retain Baseline VideoQA as the Control Condition (06/18)

**Decision:** Retained the baseline VideoQA workflow using original NExT-QA videos as the control condition for all representation-learning experiments.

**Rationale:** The baseline workflow provides a consistent reference for evaluating both pretrained CLIP representations and self-supervised autoencoder representations. Comparing downstream VideoQA performance against the baseline isolates the effects of representation learning while maintaining a common evaluation methodology across all experimental pipelines.

---

## Experimental Methodology (June 2026)

### 1) Make Motion Score Generation Optional

**Decision:** -- Removed motion score computation from the standard evidence-generation workflow while retaining support for future experimentation.

**Rationale:** -- Motion analysis substantially increased processing time and resource consumption while providing limited immediate value for baseline experimentation. Retaining the capability as an optional feature preserves future research flexibility.

### 2) Adopt Development-Subset Optimization Prior to Full-Dataset Execution

**Decision:** -- Introduced a two-stage experimental methodology consisting of development-subset experimentation followed by full-dataset execution using optimized configurations.

**Rationale:** -- Development-subset experiments reduce computational cost during workflow validation and parameter optimization while ensuring final results are generated using consistent, frozen configurations.

### 3) Separate Development Experiments from Final Full-Dataset Experiments

**Decision:** -- Created dedicated workflows for development experimentation and final full-dataset execution.

**Rationale:** -- Separating exploratory experimentation from final evaluation improves reproducibility, reduces accidental configuration drift, and ensures that final results are generated using validated experimental settings.

### 4) Standardize on Multiple-Choice Evaluation for NExT-QA (06/19)

**Decision:** -- Adopted NExT-QA multiple-choice evaluation as the sole evaluation methodology for all VideoQA experiments.

**Rationale:** -- NExT-QA is a multiple-choice benchmark dataset. Restricting evaluation to answer-choice prediction provides a consistent and objective accuracy metric while isolating the effects of video representation learning, reconstruction quality, and compression. This approach eliminates variability introduced by open-ended language generation and ensures direct comparison between baseline and autoencoder-based VideoQA workflows.

## Shared Representation Architecture (June 2026)

### 1) Separate Shared Representation Generation from Experiment Execution (06/27)

**Decision:** Established dedicated notebooks to generate reusable pretrained CLIP text and video representations independently of downstream VideoQA experiments.

**Rationale:** Pretrained CLIP representations are independent of individual autoencoder experiments and therefore should be generated once and reused across all representation-based VideoQA workflows. Separating representation generation from experiment execution reduces redundant computation, simplifies experiment management, and improves reproducibility by ensuring every experiment consumes the same shared representation artifacts.

### 2) Distinguish Shared and Experiment-Specific Representations (06/27)

**Decision:** Adopted separate storage strategies for shared pretrained representations and experiment-specific autoencoder representations.

**Rationale:** Shared `clip_text` representations are generated once and reused by both representation-based methods. `clip_video` representations are reusable but are used only by the CLIP representation method. `autoencoder_video` representations depend on the autoencoder training configuration and remain experiment-specific. This distinction minimizes duplicated storage, simplifies experiment comparison, and supports efficient evaluation of multiple autoencoder configurations using a common set of pretrained representations.






---

## Final Architecture (July 2026)

### 1) Adopt a Shared Fusion MLP Classifier

**Decision:** Standardized all representation-based VideoQA methods on a common Fusion MLP classifier.

**Rationale:** Using the same classifier, prediction workflow, and multiple-choice objective isolates the effect of the video representation while minimizing architectural differences between the representation-based methods.

### 2) Replace Cosine Similarity with Learned Classification

**Decision:** Replaced cosine-similarity scoring with a learned Fusion MLP classifier trained using CrossEntropyLoss.

**Rationale:** The learned classifier provides a common multimodal prediction architecture for both representation-based methods while supporting direct comparison of `clip_video` and `autoencoder_video` representations.

### 3) Standardize Shared and Experiment-Specific Representations

**Decision:** Adopted shared `clip_text` representations together with experiment-specific video representations.

**Rationale:** Shared `clip_text` representations are reused by both representation-based methods, while `clip_video` and `autoencoder_video` remain method-specific. This isolates the contribution of the video representation.

### 4) Standardize on a Common Evaluation Framework

**Decision:** Evaluated all implemented methods using the same multiple-choice evaluation framework.

**Rationale:** Common metrics, reporting, and analysis enable fair comparison among the Qwen2-VL baseline, CLIP representation method, and autoencoder representation method.
