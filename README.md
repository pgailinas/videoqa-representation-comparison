# Investigating Self-Supervised Autoencoder Learning for VideoQA

This project investigates self-supervised autoencoder learning for Video
Question Answering (VideoQA) using the NExT-QA benchmark dataset
together with pretrained CLIP representations and the Qwen2-VL-7B
multimodal foundation model.

The project evaluates three complementary VideoQA pipelines:

- **Baseline VideoQA Pipeline** using Qwen2-VL and the original videos.
- **CLIP Representation Pipeline** using pretrained `clip_video` representations.
- **Autoencoder Representation Pipeline** using learned `autoencoder_video` representations.

Both representation-based approaches use a shared CLIP text embedding dataset, the same downstream classifier, and identical evaluation methodology, allowing differences in VideoQA performance to be attributed primarily to the quality of the video representations.

## Research Objective

The objective of this project is to compare pretrained and self-supervised video representations for downstream multiple-choice VideoQA. Pretrained `clip_video` and learned `autoencoder_video` representations are evaluated using shared `clip_text` question-answer representations, identical prediction methods, and a common evaluation framework.

## Dataset

The primary benchmark dataset is **NExT-QA**, containing:

-   5,440 videos
-   47,692 question-answer pairs
-   Official training, validation, and test splits
-   Temporal, causal, and descriptive reasoning tasks

The videos are used for baseline VideoQA inference, pretrained CLIP video representation generation, self-supervised autoencoder training, and autoencoder latent representation generation. NExT-QA questions and answer choices are encoded as a reusable shared CLIP text embedding dataset for downstream representation-based VideoQA evaluation.

## Execution Notes

- Google Colab and Jupyter supported
- Development and full-dataset execution modes
- GPU acceleration where appropriate
- Shared CLIP representations generated once and reused
- Experiment-specific autoencoder artifacts stored by experiment

## Documentation

Complete project documentation, notebook walkthroughs, architecture
diagrams, and experimental methodology are available at:

https://pgailinas.github.io/videoqa-representation-comparison/

## Author

**Phil Gailinas**

-   M.S. Computer Engineering Candidate
-   University of New Mexico

## 📄 License

This project is intended for academic and research use.
