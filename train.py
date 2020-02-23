import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
import numpy as np
import pickle
WIDTH=80
HEIGHT=60
d=np.load("gdrive/My Drive/SELFCRASH/tr.npy",allow_pickle=True)
x=np.array(x)
X=x.reshape(10684,80,60,1)
X = np.array(X).reshape(-1, 80,60, 1)
print(X.shape)
model = Sequential()
model.add(Conv2D(256, (3, 3), input_shape=(80,60,1)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors

model.add(Dense(64))

model.add(Dense(4))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit([X], [y], batch_size=32, epochs=10, validation_split=0.3)
