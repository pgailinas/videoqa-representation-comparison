# ============================================================
# Autoencoder Model Definition for VideoQA Project
# ============================================================

import torch
import torch.nn as nn


class ConvAutoencoder(nn.Module):
    """
    Exact architecture matching Notebook 03 training script.
    Conv encoder + Conv decoder using Sequential blocks.
    Returns (reconstruction, latent).
    """

    def __init__(self):
        super().__init__()

        # --------------------------------------------------------
        # Encoder
        # --------------------------------------------------------
        self.encoder = nn.Sequential(
            nn.Conv2d(3, 32, 4, stride=2, padding=1),   # 32 x 16 x 16
            nn.ReLU(),

            nn.Conv2d(32, 64, 4, stride=2, padding=1),  # 64 x 8 x 8
            nn.ReLU(),

            nn.Conv2d(64, 128, 4, stride=2, padding=1), # 128 x 4 x 4
            nn.ReLU(),

            nn.Conv2d(128, 256, 4, stride=2, padding=1), # 256 x 2 x 2
            nn.ReLU(),
        )

        # --------------------------------------------------------
        # Decoder
        # --------------------------------------------------------
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(256, 128, 4, stride=2, padding=1),
            nn.ReLU(),

            nn.ConvTranspose2d(128, 64, 4, stride=2, padding=1),
            nn.ReLU(),

            nn.ConvTranspose2d(64, 32, 4, stride=2, padding=1),
            nn.ReLU(),

            nn.ConvTranspose2d(32, 3, 4, stride=2, padding=1),
            nn.Sigmoid(),
        )

    def forward(self, x):
        latent = self.encoder(x)
        reconstructed = self.decoder(latent)
        return reconstructed, latent

  
