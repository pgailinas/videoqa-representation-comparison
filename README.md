# Investigating Self-Supervised Autoencoder Learning for VideoQA

This project investigates self-supervised autoencoder learning for Video
Question Answering (VideoQA) using the NExT-QA benchmark dataset
together with pretrained CLIP representations and the Qwen2-VL-7B
multimodal foundation model.

The project evaluates three complementary VideoQA pipelines:

- **Baseline VideoQA Pipeline** using Qwen2-VL and the original videos.
- **CLIP Representation Pipeline** using pretrained `clip_video` representations.
- **Autoencoder Representation Pipeline** using learned `autoencoder_video` representations.

The representation-based framework also supports hybrid CLIP–autoencoder video representations for investigating whether pretrained semantic and reconstruction-based representations provide complementary information.

Both representation-based approaches use shared CLIP question-answer representations, the same configurable downstream prediction framework, and identical evaluation methodology. This design enables controlled comparison of different video representation sources while evaluating multiple prediction methods under a common experimental framework.

## Research Objective

The objective of this project is to compare pretrained, hybrid, and self-supervised video representations for downstream multiple-choice VideoQA. By evaluating all representation sources using shared CLIP question-answer representations, common prediction methods, and a standardized evaluation framework, the project isolates the influence of video representation quality on downstream VideoQA performance.

## Dataset

The primary benchmark dataset is **NExT-QA**, containing:

-   5,440 videos
-   47,692 question-answer pairs
-   Official training, validation, and test splits
-   Temporal, causal, and descriptive reasoning tasks

The videos are used for baseline VideoQA inference, pretrained CLIP representation generation, self-supervised autoencoder training, and learned video representation generation. NExT-QA questions and answer choices are encoded as a reusable shared CLIP question-answer representation dataset for downstream representation-based VideoQA evaluation.

## Experimental Results

The completed experiments produced the following best accuracies under the common evaluation framework:

| Approach | Best Accuracy |
|----------|--------------:|
| **Qwen2-VL Baseline** | **79.84%** |
| **Pretrained CLIP Representations** | **46.42%** |
| **Hybrid CLIP + Autoencoder Representations** | **31.29%** |
| **Self-Supervised Autoencoder Representations** | **21.78%** |

The experiments demonstrate that pretrained semantic representations substantially outperform reconstruction-based representations for downstream VideoQA. Although the hybrid representation improved upon the autoencoder-only approach, it did not surpass pretrained CLIP representations, indicating that semantic representation quality is the primary determinant of representation-based VideoQA performance.

## Execution Notes

- Google Colab and Jupyter supported
- Development and full-dataset execution modes
- GPU acceleration where appropriate
- Shared CLIP representations generated once and reused
- Experiment-specific autoencoder artifacts stored by experiment

## Documentation

Complete project documentation, notebook tutorials, architecture diagrams, experimental results, and implementation details are available at:

https://pgailinas.github.io/videoqa-representation-comparison/

## Author

**Phil Gailinas**

-   M.S. Computer Engineering Candidate
-   University of New Mexico

## 📄 License

This project is intended for academic and research use.
