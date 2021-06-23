import torch

def compute_input_gradient(func, inp, **kwargs):
	# inp.requires_grad = True
	# inp.grad.data = 0.
	loss = func(inp, **kwargs)
	loss.backward(retain_graph=True)
	# inp.requires_grad = False
	
	return inp.grad.data
