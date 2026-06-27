# ============================================================
# Autoencoder Model Definition for VideoQA Project
# ============================================================

import torch
import torch.nn as nn


# ------------------------------------------------------------
# Conv Autoencoder (simple, stable baseline architecture)
# Designed for video frame / segment embeddings
# ------------------------------------------------------------

class ConvAutoencoder(nn.Module):
    def __init__(self, in_channels=3, latent_dim=256):
        super(ConvAutoencoder, self).__init__()

        # ========================================================
        # Encoder
        # ========================================================
        self.encoder = nn.Sequential(
            nn.Conv2d(in_channels, 32, kernel_size=4, stride=2, padding=1),
            nn.ReLU(),

            nn.Conv2d(32, 64, kernel_size=4, stride=2, padding=1),
            nn.ReLU(),

            nn.Conv2d(64, 128, kernel_size=4, stride=2, padding=1),
            nn.ReLU(),

            nn.Conv2d(128, latent_dim, kernel_size=4, stride=2, padding=1),
            nn.ReLU()
        )

        # ========================================================
        # Decoder
        # ========================================================
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(latent_dim, 128, kernel_size=4, stride=2, padding=1),
            nn.ReLU(),

            nn.ConvTranspose2d(128, 64, kernel_size=4, stride=2, padding=1),
            nn.ReLU(),

            nn.ConvTranspose2d(64, 32, kernel_size=4, stride=2, padding=1),
            nn.ReLU(),

            nn.ConvTranspose2d(32, in_channels, kernel_size=4, stride=2, padding=1),
            nn.Sigmoid()  # assumes normalized input [0,1]
        )

    # ------------------------------------------------------------
    # Forward pass (reconstruction)
    # ------------------------------------------------------------
    def forward(self, x):
        latent = self.encoder(x)
        reconstructed = self.decoder(latent)
        return reconstructed

    # ------------------------------------------------------------
    # Encode only (USED in Notebook 04)
    # ------------------------------------------------------------
    def encode(self, x):
        return self.encoder(x)

    # ------------------------------------------------------------
    # Decode only (optional)
    # ------------------------------------------------------------
    def decode(self, z):
        return self.decoder(z)

  
