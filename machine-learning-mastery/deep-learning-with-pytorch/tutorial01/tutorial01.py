# PyTorch Tutorial: How to Develop Deep Learning Models with Python
# https://machinelearningmastery.com/pytorch-tutorial-develop-deep-learning-models/
# Last Updated on April 8, 2023

# PyTorch Installation Guide
# https://pytorch.org/get-started/locally/


from functions import prepare_data
from mlp import MLP


def main():
    # prepare the data
    path = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/ionosphere.csv'
    train_dl, test_dl = prepare_data(path)
    print(len(train_dl.dataset), len(test_dl.dataset))
    # define the network
    model = MLP(34)

    # train the model


    # evaluate the model


    #  make a single prediciton(expect class=1)
    

if __name__ == "__main__":
    main()

