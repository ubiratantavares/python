"""
How to Develop Multilayer Perceptron Models for Time Series Forecasting
https://machinelearningmastery.com/how-to-develop-multilayer-perceptron-models-for-time-series-forecasting/
"""

# multivariate data preparation
from numpy import array, hstack

def main():
    """
    função principal
    """
    # define input sequence
    serie1 = array([10, 20, 30, 40, 50, 60, 70, 80, 90])
    serie2 = array([15, 25, 35, 45, 55, 65, 75, 85, 95])
    serie3 = array([serie1[i] + serie2[i] for i, _ in enumerate(serie1)])
    # convert to [rows, columns] structure
    serie1 = serie1.reshape((len(serie1), 1))
    serie2 = serie2.reshape((len(serie2), 1))
    serie3 = serie3.reshape((len(serie3), 1))

    # horizontally stack columns
    dataset = hstack((serie1, serie2, serie3))
    print(dataset)

if __name__ == "__main__":
    main()
