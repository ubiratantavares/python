"""
How to Develop Multilayer Perceptron Models for Time Series Forecasting
https://machinelearningmastery.com/how-to-develop-multilayer-perceptron-models-for-time-series-forecasting/
"""

# multivariate data preparation
from numpy import array, hstack
from keras.models import Sequential
from keras.layers import Dense

# split a univariate sequence into samples
def split_sequences(sequences, number_steps):
    """
    sequence:
    number_steps
    """
    x_input, y_output = [], []

    for i in range(len(sequences)):
        # find the end of this pattern
        end_ix = i + number_steps

        # check if we are beyound the sequence
        if end_ix > (len(sequences) - 1):
            break

        # gather input and output parts of the pattern
        seq_x, seq_y = sequences[i:end_ix, :-1], sequences[end_ix - 1, -1]
        x_input.append(seq_x)
        y_output.append(seq_y)
    return array(x_input), array(y_output)

def main():
    """
    função principal
    """
    # define input sequence
    serie1_input = array([10, 20, 30, 40, 50, 60, 70, 80, 90])
    serie2_input = array([15, 25, 35, 45, 55, 65, 75, 85, 95])
    serie3_output = array([serie1_input[i] + serie2_input[i] for i, _ in enumerate(serie1_input)])

    # convert to [rows, columns] structure
    serie1_input = serie1_input.reshape((len(serie1_input), 1))
    serie2_input = serie2_input.reshape((len(serie2_input), 1))
    serie3_output = serie3_output.reshape((len(serie3_output), 1))

    # horizontally stack columns
    series = hstack((serie1_input, serie2_input, serie3_output))
    print(series)

    # choose a number of time steps = [1, 2, 3, 4, 5, 6, 7, 8]
    n_steps = 3

    # convert into input/output
    x_input, y_output = split_sequences(series, n_steps)
    print(x_input.shape, y_output.shape)

    # summarize the data
    for i, _ in enumerate(x_input):
        print(x_input[i], y_output[i])

    # flatten input
    number_input = x_input.shape[1] * x_input.shape[2]
    print(number_input)

    x_input = x_input.reshape((x_input.shape[0], number_input))
    print(x_input)

    # define model
    model = Sequential()
    model.add(Dense(100, activation='relu', input_dim = number_input))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')

    # fit model
    model.fit(x_input, y_output, epochs=2000, verbose=0)

    # demonstrate prediction
    x_input = array([[70, 75], [80, 85], [90, 95]])
    x_input = x_input.reshape((1, number_input))
    yhat = model.predict(x_input, verbose=0)
    print(yhat)

if __name__ == "__main__":
    main()
