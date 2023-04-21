"""
How to Develop Multilayer Perceptron Models for Time Series Forecasting
https://machinelearningmastery.com/how-to-develop-multilayer-perceptron-models-for-time-series-forecasting/
"""

# multivariate output mlp example
from numpy import array, hstack
from keras.models import Model
from keras.layers import Input, Dense


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
        seq_x, seq_y = sequences[i:end_ix, :], sequences[end_ix, :]
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
    number_steps = 3

    # convert into input/output
    x_input, y_output = split_sequences(series, number_steps)
    print(x_input.shape, y_output.shape)

    # summarize the data
    for i, _ in enumerate(x_input):
        print(x_input[i], y_output[i])

    # flatten input
    number_input = x_input.shape[1] * x_input.shape[2]
    x_input = x_input.reshape((x_input.shape[0], number_input))

    # separate output
    y1_output = y_output[:, 0].reshape((y_output.shape[0], 1))
    y2_output = y_output[:, 1].reshape((y_output.shape[0], 1))
    y3_output = y_output[:, 2].reshape((y_output.shape[0], 1))

    # define model
    visible = Input(shape = (number_input,))
    dense = Dense(100, activation='relu')(visible)

    # define output 1
    output1 = Dense(1)(dense)

    # define output 2
    output2 = Dense(1)(dense)

    # define output 3
    output3 = Dense(1)(dense)

    # tie together
    model = Model(inputs = visible, outputs = [output1, output2, output3])
    model.compile(optimizer='adam', loss='mse')

    # fit model
    model.fit(x_input, [y1_output, y2_output, y3_output], epochs = 2000, verbose = 0)

    # demonstrate prediction
    x_input = array([[70, 75, 145], [80, 85, 165], [90, 95, 185]])
    x_input = x_input.reshape((1, number_input))

    yhat = model.predict(x_input, verbose=0)
    print(yhat)

    lista = []
    for i in range(3):
        lista.append(int(yhat[i][0][0]))

    print(lista)

if __name__ == "__main__":
    main()
