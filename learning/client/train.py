import configparser
from tensorflow.keras.datasets import cifar10
# from tensorflow.keras.applications.mobilenet import MobileNet
import model
from tensorflow.keras.utils import to_categorical
import random
import numpy as np
import sys

num_of_round = int(sys.argv[1])

config = configparser.ConfigParser()
config.read('../config.ini')
print(config.sections())

def load_dataset():
    (X_train, Y_train), (X_test, Y_test) = cifar10.load_data()
    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')
    X_train = X_train / 255.0
    X_test = X_test / 255.0
    Y_train = to_categorical(Y_train)
    Y_test = to_categorical(Y_test)
    return (X_train, Y_train), (X_test, Y_test)

def sampling_data():
    (x_train, y_train), (x_test, y_test) = load_dataset()
    print(len(x_train))
    # num_of_each_dataset = int(x_train.shape[0] / NUMOFCLIENTS)
    num_of_each_dataset = int(config['learning']['data_per_epoch'])
    split_data_index = []
    while len(split_data_index) < num_of_each_dataset:
        item = random.choice(range(x_train.shape[0]))
        if item not in split_data_index:
            split_data_index.append(item)
    new_x_train = np.asarray([x_train[k] for k in split_data_index])
    new_y_train = np.asarray([y_train[k] for k in split_data_index])
    return new_x_train, new_y_train

x_train, y_train = sampling_data()

m = model.init()

LOCAL_EPOCHS = int(config['learning']['local_epoch'])
BATCH_SIZE = int(config['learning']['batch_size'])

if num_of_round != 0:
    m.load_weights('./server/models/round_'+str(num_of_round)+'.h5')
m.fit(x_train, y_train, epochs=LOCAL_EPOCHS, batch_size=BATCH_SIZE, verbose=1, validation_split=0.2)
m.save_weights('./client/models/round_'+str(num_of_round+1)+'.h5')
