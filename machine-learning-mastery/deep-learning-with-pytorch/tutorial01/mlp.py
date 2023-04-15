# PyTorch Tutorial: How to Develop Deep Learning Models with Python
# https://machinelearningmastery.com/pytorch-tutorial-develop-deep-learning-models/
# Last Updated on April 8, 2023

# PyTorch Installation Guide
# https://pytorch.org/get-started/locally/

from torch.nn import Module
from torch.nn import Linear
from torch.nn.init import kaiming_uniform_
from torch.nn import ReLU
from torch.nn.init import xavier_uniform_
from torch.nn import Sigmoid


class MLP(Module):
    # define model elements
    def __init__(self, n_inputs):
        super(MLP, self).__init__()
        # input to first hidden layer
        self.hidden1 = Linear(n_inputs, 10)
        kaiming_uniform_(self.hidden1.weight, onlinearity = 'relu')
        # second hidden layer
        self.hidden2 = Linear(10, 8)
        kaiming_uniform_(self.hidden2.weight, onlinearity = 'relu')
        self.act2 = ReLU()
        # third hidden layer and output
        self.hidden3 = Linear(8, 1)
        xavier_uniform_(self.hidden3.weight)
        self.act3 = Sigmoid()

    # forward propagate input
    def forward(self, X):
        # input to first hidden layer
        X = self.hidden1(X)
        X = self.act1(X)
        # second hidden layer
        X = self.hidden2(X)
        X = self.act2(X)
        # third hidden layer and output
        X = self.hidden3(X)
        X = self.act3(X)
        return X