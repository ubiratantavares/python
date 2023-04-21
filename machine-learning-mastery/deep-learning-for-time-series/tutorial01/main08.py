"""
How to Develop LSTM Models for Time Series Forecasting
https://machinelearningmastery.com/how-to-develop-lstm-models-for-time-series-forecasting/
"""

# multivariate data preparation
from numpy import array, hstack
from keras.models import Sequential
from keras.layers import LSTM, Dense

# split a multivariate sequence into samples
def split_sequences(sequences, number_steps):
    """
    sequence:
    number_steps:
    """
    x_input, y_output = list(), list()
    for i in range(len(sequences)):
        # find the end of this pattern
        end_ix = i + number_steps
        # check if we are beyond the sequence
        if end_ix > len(sequences):
            break
        # gather input and output parts of the pattern
        seq_x, seq_y = sequences[i:end_ix, :-1], sequences[end_ix - 1, -1]
        x_input.append(seq_x)
        y_output.append(seq_y)
    return array(x_input), array(y_output)


def main():
    """
    funcao principal
    """
    # define input sequence
    in_seq1 = array([10, 20, 30, 40, 50, 60, 70, 80, 90])
    in_seq2 = array([15, 25, 35, 45, 55, 65, 75, 85, 95])
    out_seq = array([in_seq1[i]+in_seq2[i] for i in range(len(in_seq1))])

    # convert to [rows, columns] structure
    in_seq1 = in_seq1.reshape((len(in_seq1), 1))
    in_seq2 = in_seq2.reshape((len(in_seq2), 1))
    out_seq = out_seq.reshape((len(out_seq), 1))

    # horizontally stack columns
    dataset = hstack((in_seq1, in_seq2, out_seq))
    print(dataset)
    # choose a number of time steps
    number_steps = 3
    # convert into input/output
    x_input, y_output = split_sequences(dataset, number_steps)
    print(x_input.shape, y_output.shape)
	# the dataset knows the number of features, e.g. 2
    number_features = x_input.shape[2]
	# define model
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(number_steps, number_features)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
	# fit model
    model.fit(x_input, y_output, epochs=200, verbose=0)
	# demonstrate prediction
    x_input = array([[80, 85], [90, 95], [100, 105]])
    x_input = x_input.reshape((1, number_steps, number_features))
    yhat = model.predict(x_input, verbose=0)
    print(yhat)

if __name__ == "__main__":
    main()
