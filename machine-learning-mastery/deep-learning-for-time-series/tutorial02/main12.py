"""
How to Develop Multilayer Perceptron Models for Time Series Forecasting
https://machinelearningmastery.com/how-to-develop-multilayer-perceptron-models-for-time-series-forecasting/
"""

# multivariate multi-step mlp example
from numpy import array, hstack
from keras.models import Sequential
from keras.layers import Dense


# split a multivariate sequence into samples
def split_sequences(sequences, number_steps_in, number_steps_out):
    """
    sequence:
    number_steps_in:
    number_steps_out:
    """
    x_input, y_output = [], []

    for i in range(len(sequences)):
        # find the end of this pattern
        end_ix = i + number_steps_in
        out_end_ix = end_ix + number_steps_out

        # check if we are beyound the sequence
        if out_end_ix > len(sequences):
            break

        # gather input and output parts of the pattern
        seq_x, seq_y = sequences[i:end_ix, :], sequences[end_ix:out_end_ix, :]
        x_input.append(seq_x)
        y_output.append(seq_y)

    return array(x_input), array(y_output)

def main():
    """
    função principal
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
    number_steps_in, number_steps_out = 3, 2

    # convert into input/output
    x_input, y_output = split_sequences(dataset, number_steps_in, number_steps_out)
    print(x_input.shape, y_output.shape)

    # summarize the data
    for i, _ in enumerate(x_input):
        print(x_input[i], end="\n\n")
        print(y_output[i])
        print("\n\n")

    # flatten input
    number_input = x_input.shape[1] * x_input.shape[2]

    x_input = x_input.reshape((x_input.shape[0], number_input))

    # flatten output
    number_output = y_output.shape[1] * y_output.shape[2]
    y_output = y_output.reshape((y_output.shape[0], number_output))

    # define model
    model = Sequential()
    model.add(Dense(100, activation='relu', input_dim=number_input))
    model.add(Dense(number_output))
    model.compile(optimizer='adam', loss='mse')

    # fit model
    model.fit(x_input, y_output, epochs=2000, verbose=0)

    # demonstrate prediction
    x_input = array([[60, 65, 125], [70, 75, 145], [80, 85, 165]])
    x_input = x_input.reshape((1, number_input))
    yhat = model.predict(x_input, verbose=0)
    #print(yhat)

    yhat = yhat.reshape((2, 3))
    print(yhat)


if __name__ == "__main__":
    main()
