# ============================================================
# Autoencoder Model Definition for VideoQA Project
# ============================================================

import torch
import torch.nn as nn

class ConvAutoencoder(nn.Module):
    """
    NOTE:
    This matches the ORIGINAL training architecture used in Notebook 03.
    It is NOT a convolutional autoencoder.
    It is a fully connected latent projection model.
    """

    def __init__(self, input_dim=1024, latent_dim=256):
        super().__init__()

        # ----------------------------
        # Encoder: flatten -> latent
        # ----------------------------
        self.to_latent = nn.Linear(input_dim, latent_dim)

        # ----------------------------
        # Decoder: latent -> reconstruct
        # ----------------------------
        self.from_latent = nn.Linear(latent_dim, input_dim)

    def encode(self, x):
        x = x.view(x.size(0), -1)
        return self.to_latent(x)

    def decode(self, z):
        return self.from_latent(z)

    def forward(self, x):
        x = x.view(x.size(0), -1)
        z = self.to_latent(x)
        out = self.from_latent(z)
        return out

  
