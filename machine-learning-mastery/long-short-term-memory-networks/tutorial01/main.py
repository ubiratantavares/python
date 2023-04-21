"""
How to use an Encoder-Decoder LSTM to Echo Sequences of Random Integers
https://machinelearningmastery.com/how-to-use-an-encoder-decoder-lstm-to-echo-sequences-of-random-integers/
"""

from random import randint
from numpy import array, argmax
from pandas import DataFrame, concat
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import TimeDistributed

# generate a sequence of random numbers in [0, 99]
def generate_sequence(length=15):
    """
    input: lenght -> especifica a quantidade numeros aleatorios ([1, 25]) a ser gerados.
    output: retorna uma lista contendo a sequência ordenada dos números aleatórios gerados.
    """
    conjunto = set()
    indice = 1
    while indice <= length:
        numero_sorteado = randint(1, 25)
        if numero_sorteado not in conjunto:
            conjunto.add(numero_sorteado)
            indice += 1
    return list(conjunto)

# one hot encode sequence
def one_hot_encode(sequence, n_unique=25):
    """
    input: sequence -> lista contendo a sequência ordenada dos números aleatórios gerados.
    output: uma matriz contendo o one hot encode da lista
    """
    encoding = list()
    for value in sequence:
        vector = [0 for _ in range(n_unique)]
        vector[value-1] = 1
        encoding.append(vector)
    return array(encoding)

# decode a one hot encoded string
def one_hot_decode(encoded_seq):
    """
    input: encoded_seq -> sequência codificada
    output: sequência decodificada
    """
    return [argmax(vector)+1 for vector in encoded_seq]

# convert encoded sequence to supervised learning
def to_supervised(sequence, n_in, n_out):
    """
    input: sequence -> lista contendo a sequência ordenada dos números aleatórios gerados.
    input: n_in -> 
    input: n_out ->
    output: x_values, y_values
    """
    #create lag copies of the sequence
    data = DataFrame(sequence)
    data = concat([data.shift(n_in - i - 1) for i in range(n_in)], axis=1)
    # drop rows with missing values
    data.dropna(inplace=True)
    # specify columns for input and output pairs
    values = data.values
    width = sequence.shape[1]
    x_values = values.reshape(len(values), n_in, width)
    y_values = values[:, 0:(n_out*width)].reshape(len(values), n_out, width)
    return x_values, y_values


# prepare data for the LSTM
def get_data(n_in, n_out):
    # generate random sequence
    sequence = generate_sequence()
    # one hot encode
    encoded = one_hot_encode(sequence)
    # convert to X,y pairs
    x_values, y_values = to_supervised(encoded, n_in, n_out)
    return x_values, y_values


# define model
def define_model(n_in, encoded_length, batch_size, n_neurons):
    model = Sequential()
    model.add(LSTM(n_neurons, batch_input_shape=(batch_size, n_in, encoded_length), return_sequences=True, stateful=True))
    model.add(TimeDistributed(Dense(encoded_length, activation='softmax')))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# train model
def train_model(n_in, n_out, encoded_length, batch_size, n_neurons, number_of_samples):
    model = define_model(n_in, encoded_length, batch_size, n_neurons)
    for _ in range(number_of_samples):
        # generate new random sequence
        x_values, y_values = get_data(n_in, n_out)
        # fit model for one epoch on this sequence
        model.fit(x_values, y_values, epochs=1, batch_size=batch_size, verbose=2, shuffle=False)
        model.reset_states()
    return model


# evaluate LSTM
def evaluate_model(model, n_in, n_out, batch_size):
    x_values, y_values = get_data(n_in, n_out)
    yhat = model.predict(x_values, batch_size=batch_size, verbose=0)
    # decode all pairs
    for i in range(len(x_values)):
        print('Expected:', one_hot_decode(y_values[i]), 'Predicted', one_hot_decode(yhat[i]))

def main():
    """
    Função principal para a execução de todo o processo.
    """
    # generate random sequence
    sequence = generate_sequence()
    print(sequence)
    # one hot encode
    encoded = one_hot_encode(sequence)
    # convert to X,y pairs
    x_input, y_output = to_supervised(encoded, 15, 15)
    # decode all pairs
    for i in range(len(x_input)):
        print(one_hot_decode(x_input[i]), '=>', one_hot_decode(y_output[i]))
    
    n_in = 15
    n_out = 15
    encoded_length = 25
    batch_size = 21
    n_neurons = 60
    number_of_samples = 1000
    lstm_train = train_model(n_in, n_out, encoded_length, batch_size, n_neurons, number_of_samples)
    evaluate_model(lstm_train, n_in, n_out, batch_size)

if __name__ == "__main__":
    main()
