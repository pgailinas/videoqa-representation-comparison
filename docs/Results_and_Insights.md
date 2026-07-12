---
title: Results and Insights
nav_order: 11
has_toc: false
---

# Results and Insights

This page summarizes the experimental results obtained throughout the project and highlights the principal observations from comparing foundation-model, pretrained representation-based, and self-supervised representation-based VideoQA approaches.

---

## Baseline VideoQA Results

The Qwen2-VL baseline serves as the reference implementation for direct multimodal VideoQA reasoning. Unlike the representation-based methods, the baseline processes the original video frames directly and does not require additional representation learning or downstream classifier training.

| Experiment | Evaluation | Accuracy |
|------------|-----------:|---------:|
| Qwen2-VL Baseline | Development (100 videos) | **79.84%** |

The baseline substantially outperformed every representation-based method evaluated during this project and provides an approximate upper reference for the current experimental framework.

---

## Pretrained Representation Results

Shared CLIP text and video representations were generated once for the complete NExT-QA dataset and reused across all representation-based experiments.

### Development Experiments (100 Validation Videos)

| Method | Accuracy |
|--------|---------:|
| Cosine Similarity | **44.12%** |
| Interaction Fusion | 27.44% |
| Gated Fusion | 25.87% |
| Fusion MLP | 24.86% |
| Bilinear Fusion | 22.96% |

The development experiments were intentionally performed on a reduced dataset to validate the notebook workflow, compare prediction methods, and identify promising configurations for larger-scale evaluation.

### Full Validation Experiments

| Method | Accuracy |
|--------|---------:|
| **Bilinear Fusion** | **46.42%** |
| **Interaction Fusion** | **45.30%** |
| **Cosine Similarity** | **44.18%** |
| **Gated Fusion** | **41.61%** |
| **Fusion MLP** | **34.21%** |

Several important observations emerged from the full-validation experiments:

- Bilinear Fusion achieved the highest overall representation-based accuracy.
- Interaction Fusion also surpassed the zero-shot cosine similarity baseline.
- Cosine Similarity remained remarkably stable between development and full-validation experiments, demonstrating that the 100-video development subset provided a representative estimate of full-validation performance.
- Gated Fusion improved substantially with additional training data but did not exceed the cosine similarity baseline.
- The standard Fusion MLP produced the weakest learned classifier performance, indicating that simple multimodal concatenation is less effective than explicit cross-modal interaction modeling.

---

## Autoencoder Representation Results

The self-supervised autoencoder pipeline was evaluated using learned video representations combined with shared CLIP question-answer representations.

| Method | Accuracy |
|--------|---------:|
| Autoencoder + Fusion MLP (Development) | **23.46%** |

Although the autoencoder successfully learned compact latent video representations, these representations did not achieve competitive VideoQA performance within the current experimental configuration. Additional investigation into improved representation learning, larger training sets, or semantic alignment objectives may further improve downstream performance.

---

## Runtime Environment Observations

Experiments were conducted using Google Colab.

- Qwen2-VL inference executed reliably on NVIDIA L4 GPU runtimes.
- NVIDIA T4 runtimes occasionally experienced CUDA out-of-memory errors during Qwen2-VL inference.
- Representation-based classifier training benefited substantially from GPU acceleration.
- Shared CLIP representation generation required only a single execution and significantly reduced subsequent experimentation time.

---

## Runtime Performance Analysis

Separating representation generation from downstream VideoQA evaluation substantially improved experimentation efficiency.

Once the shared CLIP text and video representations had been generated, additional experiments required only selecting a prediction method and executing Notebook 07. This modular design enabled rapid comparison among multiple multimodal fusion strategies without regenerating representations.

---

## Representation Analysis

The experiments indicate that pretrained CLIP representations already provide a strong semantic embedding space for VideoQA.

Zero-shot cosine similarity achieved over 44% validation accuracy without any supervised classifier training, demonstrating that CLIP's pretrained alignment between visual and textual representations transfers effectively to multiple-choice VideoQA.

Learned multimodal fusion methods produced mixed results, indicating that architecture selection plays an important role when attempting to improve upon pretrained representations.

---

## Reasoning Category Analysis

Notebook 08 provides per-category evaluation metrics and error analysis across all completed experiments. These analyses help identify strengths and weaknesses for different VideoQA reasoning categories and provide insight into the types of questions that remain challenging for representation-based approaches.

---

## Representation Comparison

Overall representation-based performance ranked as follows:

| Rank | Method | Accuracy |
|-----:|--------|---------:|
| 1 | Bilinear Fusion | **46.42%** |
| 2 | Interaction Fusion | **45.30%** |
| 3 | Cosine Similarity | **44.18%** |
| 4 | Gated Fusion | **41.61%** |
| 5 | Fusion MLP | **34.21%** |
| 6 | Autoencoder + Fusion MLP (Development) | **23.46%** |

These results demonstrate that pretrained CLIP representations substantially outperform the current self-supervised autoencoder representations while also showing that learned multimodal fusion can improve upon simple cosine similarity when appropriate interaction mechanisms are used.

---

## Key Findings

- Qwen2-VL achieved the highest overall VideoQA accuracy.
- Cosine Similarity provided a strong zero-shot representation-based baseline requiring no classifier training.
- Bilinear Fusion achieved the highest accuracy among the evaluated representation-based prediction methods.
- Interaction Fusion also outperformed the cosine similarity baseline after training on the complete NExT-QA training split.
- Gated Fusion exhibited evidence of overfitting with extended training and did not surpass cosine similarity.
- The standard Fusion MLP substantially underperformed the interaction-based fusion architectures.
- Representation generation and downstream prediction were successfully separated into reusable notebook stages, enabling rapid experimentation across multiple prediction methods.

---

## Lessons Learned

Several architectural decisions proved particularly valuable:

- Generating shared CLIP representations only once dramatically reduced experimentation time.
- Standardized prediction artifacts enabled Notebook 08 to evaluate multiple experiments without modification.
- A modular notebook workflow allowed new representation-based experiments to be executed by changing only a small number of configuration parameters.
- Development-mode experiments effectively identified promising methods before committing to full-scale evaluation.

---

## Future Work

Potential directions for future investigation include:

- Improve self-supervised autoencoder representations through larger training datasets and additional training epochs.
- Investigate semantic alignment between learned autoencoder representations and pretrained CLIP representations.
- Evaluate additional multimodal fusion architectures and contrastive learning objectives.
- Extend evaluation to the complete NExT-QA test split.
- Explore larger pretrained vision-language models for direct comparison with representation-based approaches.

