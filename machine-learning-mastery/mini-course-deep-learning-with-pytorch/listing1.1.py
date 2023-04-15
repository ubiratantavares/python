import torch

print(torch.__version__)

# declare two symbolic floating-point scalars
a = torch.tensor(1.5)
b = torch.tensor(2.5)

# create a simple symbolic expression using the add function
c = torch.add(a, b)
print(c)
