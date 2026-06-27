import torch
import torch.nn as nn


class ConvAutoencoder(nn.Module):
    """
    Hybrid Conv + MLP Autoencoder used in Notebook 03.

    Architecture:
        Conv Encoder
            ↓
        Flatten
            ↓
        Linear bottleneck (to_latent)
            ↓
        Linear expansion (from_latent)
            ↓
        Conv Decoder

    Outputs:
        reconstructed_image, latent_vector
    """

    def __init__(self, latent_dim=256):
        super().__init__()

        # --------------------------------------------------------
        # Convolutional encoder
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
        # Latent projection (MLP bottleneck)
        # NOTE: input size is dynamic → initialized at runtime
        # --------------------------------------------------------
        self.to_latent = None
        self.from_latent = None

        self.latent_dim = latent_dim
        self._enc_shape = None  # stores conv feature map shape

        # --------------------------------------------------------
        # Decoder (conv transpose)
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

    # ------------------------------------------------------------
    # Lazy initialization of linear layers (IMPORTANT FIX)
    # ------------------------------------------------------------
    def _build_latent_layers(self, flattened_dim):
        self.to_latent = nn.Linear(flattened_dim, self.latent_dim)
        self.from_latent = nn.Linear(self.latent_dim, flattened_dim)

    # ------------------------------------------------------------
    # Forward pass
    # ------------------------------------------------------------
    def forward(self, x):
        # Conv encoding
        x = self.encoder(x)

        # Store shape for reconstruction
        b = x.shape[0]
        self._enc_shape = x.shape[1:]  # (C, H, W)

        # Flatten
        x = x.view(b, -1)
        flat_dim = x.shape[1]

        # Lazy init linear layers (fixes checkpoint mismatch issues)
        if self.to_latent is None:
            self._build_latent_layers(flat_dim)

        # Latent bottleneck
        z = self.to_latent(x)

        # Expand back
        x = self.from_latent(z)

        # Restore conv shape
        x = x.view(b, *self._enc_shape)

        # Decode
        x = self.decoder(x)

        return x, z

    # ------------------------------------------------------------
    # Encode-only (used in Notebook 04 / 06)
    # ------------------------------------------------------------
    def encode(self, x):
        x = self.encoder(x)

        b = x.shape[0]
        x = x.view(b, -1)
        flat_dim = x.shape[1]

        if self.to_latent is None:
            self._build_latent_layers(flat_dim)

        z = self.to_latent(x)
        return z

