# DIP-Based AI Image Detection

This project presents a complete **Digital Image Processing (DIP) and machine learning framework** for detecting AI-generated images using engineered image statistics and classical machine learning.

Rather than relying entirely on end-to-end deep learning, the project uses interpretable handcrafted DIP features derived from gradient, spatial, and frequency-domain analysis to capture meaningful and generalizable differences between real and synthetic images.

## 🚀 Project Summary

- Each image is represented by a **26-dimensional DIP feature vector**
- Features are extracted from:
  - Gradient-domain statistics
  - Spatial-domain statistics
  - Frequency-domain statistics
- Multiple classical machine learning models are evaluated
- Final experiments include:
  - Classifier comparison
  - Hyperparameter tuning
  - Feature-level analysis
  - Feature-group analysis
  - Cross-source robustness experiments
  - ROC/AUC evaluation

<p align="center">
  <img src="docs/images/overview-pipeline.png" width="900">
</p>

## 📘 Full Tutorial and Documentation

The complete step-by-step pipeline, including notebook walkthroughs and explanations, is available here:

👉 https://pgailinas.github.io/dip-ai-image-detection/

## 📂 Repository Structure

- `docs/` — GitHub Pages tutorial and documentation  
- `notebooks/` — Google Colab notebooks for each pipeline stage  
- `src/` — reusable Python code and configuration  
- `metadata/` — CSV-based pipeline artifacts (features, splits, models)  

## ⚙️ Execution Notes

- Designed primarily for **Google Colab execution**
- Tutorial notebooks can be viewed directly through GitHub without an account
- Public dataset download support is integrated into the workflow
- Uses a metadata-driven modular pipeline architecture
- Intermediate CSV artifacts enable reproducible staged execution
- All notebooks can be executed independently using provided repository artifacts and metadata files

## 👤 Author

Phil Gailinas  
M.S. Computer Engineering candidate  
University of New Mexico

