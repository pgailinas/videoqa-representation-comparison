# Project Decisions

## 2026-06-11 — Transition from RAG to Representation Comparison

### Decision

Refocused the project from RAG-based VideoQA experiments to a comparison of pretrained and autoencoder-based video representations.

### Rationale

The instructor recommended increasing the machine learning emphasis of the project. Autoencoder-based representation learning provides a stronger ML component and enables comparison between learned and pretrained video features.

---

## 2026-06-13 — Motion Score Computation Made Optional

### Decision

Motion score generation was removed from the standard evidence-generation workflow and retained as an optional feature.

### Rationale

Motion analysis significantly increased processing time while providing limited value for the baseline workflow. The capability remains available for future experimentation.

---

## 2026-06-15 — Adopt Combined Dataset Archive

### Decision

Replaced multipart ZIP distribution with a single NExTVideo_combined.zip archive.

### Rationale

Simplifies dataset management, reduces setup complexity, and avoids repeated archive reconstruction steps.

