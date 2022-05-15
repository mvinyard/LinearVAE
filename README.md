flexinet
---

A flexible API for instantiating pytorch neural networks.

## Current test implementation: vanilla linear VAE

<img width="400" alt="FlexiLinearAVE" src="/docs/img/flexinet.LinearVAE.svg">

### Example

```python
import flexinet as fn
import torch

X = torch.load("X_data.pt")
X_data = fn.pp.random_split(X)
X_data.keys()
```
>`dict_keys(['test', 'valid', 'train'])`

```python
model = fn.models.LinearVAE(X_data,
                            latent_dim=20, 
                            hidden_layers=5, 
                            power=2,
                            dropout=0.1,
                            activation_function_dict={'LeakyReLU': LeakyReLU(negative_slope=0.01)},
                            optimizer=torch.optim.Adam
                            reconstruction_loss_function=torch.nn.BCELoss(),
                            reparameterization_loss_function=torch.nn.KLDivLoss(),
                            device="cuda:0",
                           )
```
<img width="541" alt="from_nb.linear_VAE" src="https://user-images.githubusercontent.com/47393421/168488664-e7918416-8ae8-4369-a6ef-b73449c42b5f.png">

```python
model.train(epochs=10_000, print_frequency=50, lr=1e-4)
```

```python
model.plot_loss()
```

## Contact

If you have suggestions, questions, or comments, please reach out to Michael Vinyard via [email](mailto:mvinyard@broadinstitute.org)
