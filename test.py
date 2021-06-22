import torch
import torch.nn.functional as F

a = torch.tensor([1, 2])
b = torch.tensor([1, 2])
c = torch.tensor([1, 2])

torch.stack([a, b, c])