# PyTorch Tutorial: How to Develop Deep Learning Models with Python
# https://machinelearningmastery.com/pytorch-tutorial-develop-deep-learning-models/
# Last Updated on April 8, 2023

# PyTorch Installation Guide
# https://pytorch.org/get-started/locally/


# check pytorch version
import torch
from torch.utils.data import DataLoader
from csvdataset import CSVDataset


# prepare the dataset
def prepare_data(path):
    # load the dataset
    dataset = CSVDataset(path)
    # calculate split
    train, test = dataset.get_splits()
    # prepare data loaders
    train_dl = DataLoader(train, batch_size=32, shuffle=True)
    test_dl = DataLoader(test, batch_size=1024, shuffle=False)
    return train_dl, test_dl


# train the model
def train_model(train_dl, model):
    pass


# evaluate the model
def evaluate_model(test_del, model):
    pass

# make a class prediciton for one row of data
def predict(row, model):
    pass
