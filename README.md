flexinet
---

Flexible torch neural network API.

Current test implementation: vanilla linear VAE

[/docs/img/flexinet.LinearVAE.svg]

## Example

```python
import flexinet as fn
import torch

X = torch.load("X_data.pt")
X_data = fn.pp.random_split(X)
X_data.keys()
```
>`dict_keys(['test', 'valid', 'train'])`

```python
model = fn.models.LinearVAE(X_data, latent_dim=20, hidden_layers=5, lr=1e-4)
```
<img width="541" alt="Screen Shot 2022-05-15 at 12 38 22 PM" src="https://user-images.githubusercontent.com/47393421/168488664-e7918416-8ae8-4369-a6ef-b73449c42b5f.png">

```python
model.train(epochs=10_000, print_frequency=25, lr=1e-5)
```
