import torch
import torch.nn as nn


class ConvAutoencoder(nn.Module):
    """
    Convolutional autoencoder matching the Notebook 03 trained model.

    Structure:
        named encoder layers
        to_latent (Linear)
        from_latent (Linear)
        named decoder layers
    """

    def __init__(self):
        super().__init__()

        self.latent_dim = 256
        self.encoded_feature_shape = (128, 16, 16)
        self.encoded_feature_size = 128 * 16 * 16

        # --------------------------------------------------------
        # Encoder
        # --------------------------------------------------------
        self.encoder_conv1 = nn.Conv2d(
            in_channels=3,
            out_channels=32,
            kernel_size=4,
            stride=2,
            padding=1,
        )
        self.encoder_relu1 = nn.ReLU()

        self.encoder_conv2 = nn.Conv2d(
            in_channels=32,
            out_channels=64,
            kernel_size=4,
            stride=2,
            padding=1,
        )
        self.encoder_relu2 = nn.ReLU()

        self.encoder_conv3 = nn.Conv2d(
            in_channels=64,
            out_channels=128,
            kernel_size=4,
            stride=2,
            padding=1,
        )
        self.encoder_relu3 = nn.ReLU()

        self.encoder_flatten = nn.Flatten()

        self.to_latent = nn.Linear(
            in_features=self.encoded_feature_size,
            out_features=self.latent_dim,
        )

        # --------------------------------------------------------
        # Decoder
        # --------------------------------------------------------
        self.from_latent = nn.Linear(
            in_features=self.latent_dim,
            out_features=self.encoded_feature_size,
        )

        self.decoder_unflatten = nn.Unflatten(
            dim=1,
            unflattened_size=self.encoded_feature_shape,
        )

        self.decoder_conv1 = nn.ConvTranspose2d(
            in_channels=128,
            out_channels=64,
            kernel_size=4,
            stride=2,
            padding=1,
        )
        self.decoder_relu1 = nn.ReLU()

        self.decoder_conv2 = nn.ConvTranspose2d(
            in_channels=64,
            out_channels=32,
            kernel_size=4,
            stride=2,
            padding=1,
        )
        self.decoder_relu2 = nn.ReLU()

        self.decoder_conv3 = nn.ConvTranspose2d(
            in_channels=32,
            out_channels=3,
            kernel_size=4,
            stride=2,
            padding=1,
        )
        self.decoder_output = nn.Sigmoid()

    def encode(self, x):
        x = self.encoder_conv1(x)
        x = self.encoder_relu1(x)

        x = self.encoder_conv2(x)
        x = self.encoder_relu2(x)

        x = self.encoder_conv3(x)
        x = self.encoder_relu3(x)

        x = self.encoder_flatten(x)
        latent = self.to_latent(x)

        return latent

    def decode(self, latent):
        x = self.from_latent(latent)
        x = self.decoder_unflatten(x)

        x = self.decoder_conv1(x)
        x = self.decoder_relu1(x)

        x = self.decoder_conv2(x)
        x = self.decoder_relu2(x)

        x = self.decoder_conv3(x)
        reconstruction = self.decoder_output(x)

        return reconstruction

    def forward(self, x):
        latent = self.encode(x)
        reconstruction = self.decode(latent)

        return reconstruction, latent
