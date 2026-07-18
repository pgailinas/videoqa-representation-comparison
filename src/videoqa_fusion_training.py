"""Shared training utilities for learned representation-based VideoQA classifiers.

The notebook retains each fusion architecture so readers can study how video and
question-answer embeddings are combined. This module centralizes the repeated
PyTorch dataset, data-loader, training, validation, and output-validation logic.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence, Mapping, Any

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset


class GroupedFusionQADataset(Dataset):
    """Convert grouped QA dictionaries into validated PyTorch tensors."""

    def __init__(
        self,
        samples: Sequence[Mapping[str, Any]],
        *,
        video_embedding_dimension: int,
        text_embedding_dimension: int,
        num_choices: int,
    ) -> None:
        if not samples:
            raise RuntimeError("Grouped QA samples must not be empty.")
        self.samples = samples
        self.video_embedding_dimension = int(video_embedding_dimension)
        self.text_embedding_dimension = int(text_embedding_dimension)
        self.num_choices = int(num_choices)

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, index: int) -> dict[str, torch.Tensor]:
        sample = self.samples[index]
        qa_record_id = str(sample.get("qa_record_id", index))

        video_embedding = np.asarray(sample["video_embedding"], dtype=np.float32)
        question_answer_embeddings = np.asarray(
            sample["question_answer_embeddings"], dtype=np.float32
        )
        label = int(sample["label"])

        expected_video_shape = (self.video_embedding_dimension,)
        expected_text_shape = (self.num_choices, self.text_embedding_dimension)

        if video_embedding.shape != expected_video_shape:
            raise ValueError(
                f"Invalid video embedding shape for {qa_record_id}: "
                f"{video_embedding.shape}; expected {expected_video_shape}."
            )
        if question_answer_embeddings.shape != expected_text_shape:
            raise ValueError(
                f"Invalid question-answer embedding shape for {qa_record_id}: "
                f"{question_answer_embeddings.shape}; expected {expected_text_shape}."
            )
        if label not in range(self.num_choices):
            raise ValueError(f"Invalid label for {qa_record_id}: {label}")
        if not np.isfinite(video_embedding).all():
            raise ValueError(f"Non-finite video values found for {qa_record_id}.")
        if not np.isfinite(question_answer_embeddings).all():
            raise ValueError(f"Non-finite text values found for {qa_record_id}.")

        return {
            "video": torch.from_numpy(video_embedding),
            "question_answers": torch.from_numpy(question_answer_embeddings),
            "label": torch.tensor(label, dtype=torch.long),
        }


@dataclass
class FusionTrainingResult:
    """Standard outputs shared by all learned fusion classifiers."""

    model: nn.Module
    device: torch.device
    all_scores: np.ndarray
    training_history_df: pd.DataFrame
    training_epochs: int
    final_training_loss: float


def _set_random_seed(random_seed: int) -> None:
    np.random.seed(random_seed)
    torch.manual_seed(random_seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(random_seed)


def train_and_score_fusion_classifier(
    *,
    model: nn.Module,
    train_samples: Sequence[Mapping[str, Any]],
    validation_samples: Sequence[Mapping[str, Any]],
    video_embedding_dimension: int,
    text_embedding_dimension: int,
    num_choices: int,
    batch_size: int,
    learning_rate: float,
    weight_decay: float,
    epochs: int,
    random_seed: int,
    method_label: str,
) -> FusionTrainingResult:
    """Train one fusion model and return its validation candidate scores."""

    if batch_size <= 0 or epochs <= 0:
        raise ValueError("batch_size and epochs must be greater than zero.")
    if learning_rate <= 0 or weight_decay < 0:
        raise ValueError("Invalid optimizer configuration.")

    _set_random_seed(random_seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)

    train_dataset = GroupedFusionQADataset(
        train_samples,
        video_embedding_dimension=video_embedding_dimension,
        text_embedding_dimension=text_embedding_dimension,
        num_choices=num_choices,
    )
    validation_dataset = GroupedFusionQADataset(
        validation_samples,
        video_embedding_dimension=video_embedding_dimension,
        text_embedding_dimension=text_embedding_dimension,
        num_choices=num_choices,
    )

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    validation_loader = DataLoader(
        validation_dataset, batch_size=batch_size, shuffle=False
    )

    trainable_parameter_count = sum(
        parameter.numel() for parameter in model.parameters() if parameter.requires_grad
    )
    if trainable_parameter_count <= 0:
        raise RuntimeError(f"The {method_label} model has no trainable parameters.")

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(
        model.parameters(), lr=learning_rate, weight_decay=weight_decay
    )

    history: list[dict[str, float | int]] = []
    for epoch_index in range(epochs):
        model.train()
        epoch_losses: list[float] = []
        correct_predictions = 0
        processed_samples = 0

        for batch in train_loader:
            video_batch = batch["video"].to(device)
            question_answer_batch = batch["question_answers"].to(device)
            label_batch = batch["label"].to(device)

            optimizer.zero_grad(set_to_none=True)
            scores = model(video_batch, question_answer_batch)
            expected_shape = (video_batch.shape[0], num_choices)
            if tuple(scores.shape) != expected_shape:
                raise ValueError(
                    f"Unexpected {method_label} training score shape: "
                    f"{tuple(scores.shape)}; expected {expected_shape}."
                )

            loss = criterion(scores, label_batch)
            if not torch.isfinite(loss):
                raise ValueError(f"Non-finite loss encountered during {method_label} training.")

            loss.backward()
            optimizer.step()

            epoch_losses.append(float(loss.item()))
            correct_predictions += int((scores.argmax(dim=1) == label_batch).sum().item())
            processed_samples += int(label_batch.shape[0])

        if not epoch_losses or processed_samples == 0:
            raise RuntimeError(f"No batches were processed during epoch {epoch_index + 1}.")

        history.append(
            {
                "epoch": epoch_index + 1,
                "loss": float(np.mean(epoch_losses)),
                "accuracy": correct_predictions / processed_samples,
            }
        )

    training_history_df = pd.DataFrame(history)
    if len(training_history_df) != epochs:
        raise RuntimeError("Training history row count does not match configured epochs.")

    model.eval()
    validation_score_batches: list[np.ndarray] = []
    with torch.no_grad():
        for batch in validation_loader:
            video_batch = batch["video"].to(device)
            question_answer_batch = batch["question_answers"].to(device)
            scores = model(video_batch, question_answer_batch)
            expected_shape = (video_batch.shape[0], num_choices)
            if tuple(scores.shape) != expected_shape:
                raise ValueError(
                    f"Unexpected {method_label} validation score shape: "
                    f"{tuple(scores.shape)}; expected {expected_shape}."
                )
            if not torch.isfinite(scores).all():
                raise ValueError(f"Non-finite validation scores generated by {method_label}.")
            validation_score_batches.append(scores.cpu().numpy())

    if not validation_score_batches:
        raise RuntimeError(f"No validation batches were scored by {method_label}.")

    all_scores = np.vstack(validation_score_batches)
    expected_all_scores_shape = (len(validation_samples), num_choices)
    if all_scores.shape != expected_all_scores_shape:
        raise ValueError(
            f"Expected score matrix shape {expected_all_scores_shape}, "
            f"found {all_scores.shape}."
        )
    if not np.isfinite(all_scores).all():
        raise ValueError(f"{method_label} score matrix contains non-finite values.")

    final_training_loss = float(training_history_df["loss"].iloc[-1])
    return FusionTrainingResult(
        model=model,
        device=device,
        all_scores=all_scores,
        training_history_df=training_history_df,
        training_epochs=epochs,
        final_training_loss=final_training_loss,
    )
