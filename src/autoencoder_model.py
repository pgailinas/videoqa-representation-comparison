import torch
import torch.nn as nn


class ConvAutoencoder(nn.Module):
    """
    EXACT MATCH to Notebook 03 trained model.

    Structure:
        encoder (Sequential)
        to_latent (Linear)
        from_latent (Linear)
        decoder (Sequential)
    """

    def __init__(self):
        super().__init__()

        # --------------------------------------------------------
        # Encoder (Conv stack)
        # --------------------------------------------------------
        self.encoder = nn.Sequential(
            nn.Conv2d(3, 32, 4, stride=2, padding=1),  # encoder.0
            nn.ReLU(),

            nn.Conv2d(32, 64, 4, stride=2, padding=1),  # encoder.2
            nn.ReLU(),

            nn.Conv2d(64, 128, 4, stride=2, padding=1), # encoder.4
            nn.ReLU(),
        )

        # --------------------------------------------------------
        # Bottleneck (MLP)
        # --------------------------------------------------------
        self.to_latent = nn.Linear(128 * 16 * 16, 256)
        self.from_latent = nn.Linear(256, 128 * 16 * 16)

        # --------------------------------------------------------
        # Decoder (ConvTranspose stack)
        # --------------------------------------------------------
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(128, 64, 4, stride=2, padding=1),  # decoder.1
            nn.ReLU(),

            nn.ConvTranspose2d(64, 32, 4, stride=2, padding=1),   # decoder.3
            nn.ReLU(),

            nn.ConvTranspose2d(32, 3, 4, stride=2, padding=1),    # decoder.5
            nn.Sigmoid(),
        )

    def forward(self, x):
        x = self.encoder(x)

        b = x.shape[0]
        x = x.view(b, -1)

        z = self.to_latent(x)
        x = self.from_latent(z)

        x = x.view(b, 128, 16, 16)

        x = self.decoder(x)

        return x, z

    def encode(self, x):
        x = self.encoder(x)
        b = x.shape[0]
        x = x.view(b, -1)
        return self.to_latent(x)

