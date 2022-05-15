
import torch


def _KL_Divergence(mu, logvar):

    """KL-Divergence = 0.5 * sum(1 + log(sigma^2) - mu^2 - sigma^2)

    Parameters:
    -----------
    mu
        the mean from the latent vector

    logvar
        log variance from the latent vector
    """

    return -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())