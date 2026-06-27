import torch
import torch.nn as nn


class ConvAutoencoder(nn.Module):
    """
    HYBRID MODEL USED IN NOTEBOOK 03:

    Conv Encoder
    ↓
    Flatten
    ↓
    Linear bottleneck (to_latent)
    ↓
    Linear expansion (from_latent)
    ↓
    Conv Decoder
    """

    def __init__(self, latent_dim=256):
        super().__init__()

        # --------------------------------------------------------
        # Convolutional encoder (feature extraction)
        # --------------------------------------------------------
        self.encoder = nn.Sequential(
            nn.Conv2d(3, 32, 4, stride=2, padding=1),
            nn.ReLU(),

            nn.Conv2d(32, 64, 4, stride=2, padding=1),
            nn.ReLU(),

            nn.Conv2d(64, 128, 4, stride=2, padding=1),
            nn.ReLU(),

            nn.Conv2d(128, 256, 4, stride=2, padding=1),
            nn.ReLU(),
        )

        # --------------------------------------------------------
        # Bottleneck projection (MLP)
        # --------------------------------------------------------
        self.to_latent = nn.Linear(256 * 2 * 2, latent_dim)
        self.from_latent = nn.Linear(latent_dim, 256 * 2 * 2)

        # --------------------------------------------------------
        # Decoder (mirror conv)
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
        # encoder conv
        x = self.encoder(x)

        # flatten
        b = x.shape[0]
        x = x.view(b, -1)

        # latent bottleneck
        z = self.to_latent(x)
        x = self.from_latent(z)

        # reshape back to conv feature map
        x = x.view(b, 256, 2, 2)

        # decode
        out = self.decoder(x)

        return out, z

  
