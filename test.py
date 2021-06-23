import torch
import torch.nn.functional as F

a = torch.tensor([1.]).detach()
b = torch.tensor([1, 2])
c = torch.tensor([1, 2])

a.requires_grad_()
a = a * a 
a