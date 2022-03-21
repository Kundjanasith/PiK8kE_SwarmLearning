import configparser
from tensorflow.keras.datasets import cifar10
# from tensorflow.keras.applications.mobilenet import MobileNet
import model
from tensorflow.keras.utils import to_categorical
import random
import numpy as np
import sys

config = configparser.ConfigParser()
config.read('./config.ini')
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

_, (X_test, Y_test) = load_dataset()
print(X_test.shape, Y_test.shape)

NUM_OF_ROUNDS = int(config['learning']['num_of_rounds'])

local_res = []
global_res = []
for i in range(NUM_OF_ROUNDS):
    print('Communication round: #',i)

    local_model = model.init()
    local_score = local_model.evaluate(X_test,Y_test)
    local_res.append(local_score)

    global_model = model.init()
    global_score = global_model.evaluate(X_test,Y_test)
    global_res.append(global_score)
    break

local_res = np.array(local_res)
global_res = np.array(global_res)

np.save('./evaluation/local_res.npy',local_res)
np.save('./evaluation/global_res.npy',global_res)