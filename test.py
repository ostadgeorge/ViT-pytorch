import torch
import torch.nn.functional as F

a = torch.tensor([1.]).detach()
b = torch.tensor([1, 2])
c = torch.tensor([1, 2])

a.requires_grad_()

y = a * a + 2 * a