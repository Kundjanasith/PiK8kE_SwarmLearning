from tensorflow.keras.applications.mobilenet import MobileNet
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.layers import Input, Dense, BatchNormalization, Flatten
from tensorflow.keras import Model
from tensorflow.keras.optimizers import SGD

def init():
    model = MobileNet(include_top=True,input_tensor=Input(shape=(32,32,3)))
    x = model.output
    x = Flatten()(x)
    # x = Dense(512,activation='relu')(x)
    # x = BatchNormalization()(x)
    x = Dense(10,activation='softmax')(x)
    model = Model(model.input,x)
    LOSS = 'categorical_crossentropy' 
    # lr = 0.000025
    # OPTIMIZER = SGD(learning_rate=lr, momentum=0.9, nesterov=False)
    model.compile(optimizer='adam', loss=LOSS, metrics=['accuracy'])
    return model