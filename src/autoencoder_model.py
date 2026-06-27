import torch
import torch.nn as nn


class ConvAutoencoder(nn.Module):
    """
    THIS IS THE REAL MODEL USED IN TRAINING.

    Despite the name, it is NOT convolutional.
    It is a fully connected autoencoder operating on flattened frames.
    """

    def __init__(self, input_dim=32768, latent_dim=256):
        super().__init__()

        # --------------------------------------------------------
        # Encoder (MLP)
        # --------------------------------------------------------
        self.to_latent = nn.Sequential(
            nn.Linear(input_dim, 1024),
            nn.ReLU(),
            nn.Linear(1024, latent_dim)
        )

        # --------------------------------------------------------
        # Decoder (MLP)
        # --------------------------------------------------------
        self.from_latent = nn.Sequential(
            nn.Linear(latent_dim, 1024),
            nn.ReLU(),
            nn.Linear(1024, input_dim)
        )

    def encode(self, x):
        x = x.view(x.size(0), -1)
        return self.to_latent(x)

    def decode(self, z):
        return self.from_latent(z)

    def forward(self, x):
        x = x.view(x.size(0), -1)
        z = self.to_latent(x)
        out = self.from_latent(z)
        return out, z

  
