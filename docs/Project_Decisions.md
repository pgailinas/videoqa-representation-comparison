---
title: Project Decisions
nav_order: 3
has_children: true
has_toc: false
---
# Project Decisions

This document records significant project decisions, implementation direction changes, and architectural milestones for the VideoQA representation-learning project.

Only major decisions that materially affect project design, workflow, methodology, or outcomes are recorded.

Dates marked "XX" are approximate and will be refined from Git commit history when possible.

---

## 2026-05-XX — Adopt NExT-QA as the Primary Benchmark Dataset

### Decision

Selected the NExT-QA benchmark dataset as the foundation for all VideoQA experiments.

### Rationale

NExT-QA provides a widely used benchmark containing video-question-answer pairs designed to evaluate causal, temporal, and descriptive reasoning. The dataset offers sufficient scale and diversity to support representation-learning experiments and downstream VideoQA evaluation.

---

## 2026-05-XX — Use Qwen2-VL-7B as the Common VideoQA Foundation Model

### Decision

Selected Qwen2-VL-7B as the downstream VideoQA inference model for all experimental workflows.

### Rationale

Using a single multimodal foundation model across all experiments allows performance differences to be attributed primarily to the quality of video representations rather than differences in VideoQA model architecture.

---

## 2026-05-XX — Adopt a Notebook-Driven Experimental Framework

### Decision

Organized the project as a sequence of independently executable notebooks rather than a single monolithic workflow.

### Rationale

Notebook-based execution supports reproducibility, modular experimentation, incremental development, and compatibility with both Google Colab and local Jupyter environments.

---

## 2026-06-XX — Separate Video Preparation and Evidence Generation

### Decision

Established a dedicated preprocessing workflow responsible for generating structured video evidence resources prior to VideoQA experimentation.

### Rationale

Separating preprocessing from downstream experimentation improves modularity, reduces redundant processing, and allows generated evidence resources to be reused across multiple experimental workflows.

---

## 2026-06-XX — Adopt Evidence Metadata as the Central Intermediate Representation

### Decision

Standardized on evidence metadata and structured video evidence records as the primary intermediate data representation used throughout the project.

### Rationale

Evidence metadata provides a reusable abstraction between raw video assets and downstream experiments. This approach supports baseline VideoQA, pretrained representation generation, autoencoder training, and final evaluation using a common evidence framework.

---

## 2026-06-XX — Adopt Combined Archive Distribution Strategy

### Decision

Replaced multipart video archive management with a single combined dataset archive.

### Rationale

A single archive simplifies dataset management, reduces setup complexity, eliminates archive reconstruction steps, and improves reproducibility within Google Colab environments.

---

## 2026-06-11 — Transition from Retrieval-Augmented Generation to Representation Learning

### Decision

Refocused the project from Retrieval-Augmented Generation (RAG)-based VideoQA workflows to a comparative study of pretrained and autoencoder-based video representations.

### Rationale

The revised direction increases emphasis on machine-learning concepts and self-supervised learning while providing a stronger alignment with course objectives centered on machine learning methodology and representation learning.

---

## 2026-06-11 — Introduce Autoencoder-Based Representation Learning

### Decision

Added self-supervised autoencoder training as a primary experimental workflow.

### Rationale

Autoencoders provide a mechanism for learning compact latent video representations without requiring additional labels. These learned representations can be evaluated through downstream VideoQA performance and compared directly against pretrained representations.

---

## 2026-06-11 — Retain Baseline, Pretrained, and Autoencoder Experimental Pipelines

### Decision

Organized the project around three comparative experimental workflows:

1. Baseline VideoQA
2. Pretrained Representation VideoQA
3. Autoencoder Representation VideoQA

### Rationale

Maintaining all three workflows enables direct comparison between raw video evidence, pretrained feature representations, and learned latent representations while using a common evaluation framework.

---

## 2026-06-13 — Make Motion Score Generation Optional

### Decision

Removed motion score computation from the standard evidence-generation workflow while retaining support for future experimentation.

### Rationale

Motion analysis substantially increased processing time and resource consumption while providing limited immediate value for baseline experimentation. Retaining the capability as an optional feature preserves future research flexibility.

---

## 2026-06-XX — Adopt Development-Subset Optimization Prior to Full-Dataset Execution

### Decision

Introduced a two-stage experimental methodology consisting of development-subset experimentation followed by full-dataset execution using optimized configurations.

### Rationale

Development-subset experiments reduce computational cost during workflow validation and parameter optimization while ensuring final results are generated using consistent, frozen configurations.

---

## 2026-06-XX — Separate Development Experiments from Final Full-Dataset Experiments

### Decision

Created dedicated workflows for development experimentation and final full-dataset execution.

### Rationale

Separating exploratory experimentation from final evaluation improves reproducibility, reduces accidental configuration drift, and ensures that final results are generated using validated experimental settings.

