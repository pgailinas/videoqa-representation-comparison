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

### 3) Use Qwen2-VL-7B as the Common VideoQA Foundation Model

**Decision:** -- Selected Qwen2-VL-7B as the downstream VideoQA inference model for all experimental workflows.

**Rationale:** -- Using a single multimodal foundation model across all experiments allows performance differences to be attributed primarily to the quality of video representations rather than differences in VideoQA model architecture.

### 4) Maintain a Fixed Downstream VideoQA Model

**Decision:** -- Maintained a single downstream VideoQA inference model across all experimental workflows.

**Rationale:** -- The objective of the project is to evaluate the impact of different video representations rather than compare VideoQA model architectures. Keeping the downstream inference model fixed isolates the effects of representation quality and enables direct comparison between baseline video evidence, pretrained representations, and autoencoder-based latent representations.

---

## Architecture Development (June 2026)

### 1) Separate Video Preparation and Evidence Generation

**Decision:** -- Established a dedicated preprocessing workflow responsible for generating structured video evidence resources prior to VideoQA experimentation.

**Rationale:** -- Separating preprocessing from downstream experimentation improves modularity, reduces redundant processing, and allows generated evidence resources to be reused across multiple experimental workflows.

### 2) Standardize on Evidence Segments Rather Than Full Videos

**Decision:** -- Established structured video evidence segments as the primary unit of processing throughout the experimental pipeline.

**Rationale:** -- Processing videos as evidence segments improves scalability, enables consistent metadata generation, supports representation learning workflows, and provides a common input format for baseline inference, pretrained representations, and autoencoder-based representations.

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

### 1) Transition from Representation Comparison to Autoencoder-Centered Research (06/18)

**Decision:** Refined the project scope from comparison of pretrained and autoencoder-based video representations to a focused investigation of self-supervised autoencoder learning for Video Question Answering (VideoQA).

**Rationale:** While representation comparison provided a useful experimental framework, the revised direction places greater emphasis on machine-learning methodology, self-supervised learning, representation learning, and downstream task evaluation. The new scope more closely aligns with the project's primary research objective of determining whether compact representations learned from unlabeled video data preserve sufficient information for VideoQA reasoning.

### 2) Remove Pretrained Representation Workflow from the Experimental Pipeline (06/18)

**Decision:** Removed the pretrained-representation experimental branch from the project architecture and notebook workflow.

**Rationale:** Eliminating the pretrained-representation workflow simplifies the experimental design and allows the project to focus on the relationship between self-supervised representation learning, video reconstruction, compression, and downstream VideoQA performance.

### 3) Retain Baseline VideoQA as the Control Condition (06/18)

**Decision:** Retained the baseline VideoQA workflow using original video evidence while establishing autoencoder-based VideoQA as the primary experimental workflow.

**Rationale:** The baseline workflow provides a consistent reference point for evaluating the effects of representation learning, reconstruction quality, and information compression. Comparing reconstructed video evidence against original video evidence enables direct assessment of information preservation and downstream reasoning performance.

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

