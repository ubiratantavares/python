"""
How to Develop Multilayer Perceptron Models for Time Series Forecasting
https://machinelearningmastery.com/how-to-develop-multilayer-perceptron-models-for-time-series-forecasting/
"""

# univariate data preparation
from numpy import array

# split a univariate sequence into samples
def split_sequence(sequence, number_steps):
    """
    sequence:
    number_steps
    """
    x_input, y_output = [], []

    for i in range(len(sequence)):
        # find the end of this pattern
        end_ix = i + number_steps

        # check if we are beyound the sequence
        if end_ix > (len(sequence) - 1):
            break

        # gather input and output parts of the pattern
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
        x_input.append(seq_x)
        y_output.append(seq_y)
    return array(x_input), array(y_output)


def main():
    """
    função principal
    """
    # define input sequence
    serie = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    # choose a number of time steps = [1, 2, 3, 4, 5, 6, 7, 8]
    n_steps = 1

    # split into samples
    x_input, y_output = split_sequence(serie, n_steps)

    # summarize the data
    for i, _ in enumerate(x_input):
        print(x_input[i], y_output[i])

if __name__ == "__main__":
    main()
