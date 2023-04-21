"""
How to Develop LSTM Models for Time Series Forecasting
https://machinelearningmastery.com/how-to-develop-lstm-models-for-time-series-forecasting/
"""

# univariate data preparation
from numpy import array
from keras.models import Sequential
from keras.layers import LSTM, Dense


# split a univariate sequence into samples
def split_sequence(sequence, number_steps):
    """
    sequence:
    number_steps:
    """
    x_input, y_output = list(), list()
    for i in range(len(sequence)):
        # find the end of this pattern
        end_ix = i + number_steps
        # check if we are beyond the sequence
        if end_ix > len(sequence)-1:
            break
        # gather input and output parts of the pattern
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
    x_input.append(seq_x)
    y_output.append(seq_y)
    return array(x_input), array(y_output)


def main():
    """
    funcao principal
    """
    # define input sequence
    serie = [10, 20, 30, 40, 50, 60, 70, 80, 90]


    # choose a number of time steps
    number_steps = 3

    # split into samples
    x_input, y_output = split_sequence(serie, number_steps)
    print(x_input.shape, y_output.shape)

    number_samples = x_input.shape[0]
    number_features = 1

    # reshape from [samples, timesteps] into [samples, timesteps, features]
    x_input = x_input.reshape((number_samples, number_steps, number_features))

	# define model
    model = Sequential()
    model.add(LSTM(50,
                   activation='relu',
                   return_sequences=True,
                   input_shape=(number_steps, number_features)))
    model.add(LSTM(50, activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    # fit model
    model.fit(x_input, y_output, epochs=200, verbose=0)
    # demonstrate prediction
    x_input = array([70, 80, 90])
    x_input = x_input.reshape((1, number_steps, number_features))
    yhat = model.predict(x_input, verbose=0)
    print(yhat)

if __name__ == "__main__":
    main()
