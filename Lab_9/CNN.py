# -*- coding: utf-8 -*-
"""
Created on Sun May 17 13:17:16 2020

@author: lukas
"""
import tensorflow as tf
import numpy as np

class CNN:
    def __init__(self):
        self.__model = tf.keras.models.Sequential()
        self.__model.add(tf.keras.layers.Flatten())
        self.__model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu))
        self.__model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu))
        self.__model.add(tf.keras.layers.Dense(10, activation = tf.nn.softmax))
        self.__model.compile(optimizer='adam',
                             loss='sparse_categorical_crossentropy',
                             metrics=['accuracy'])
        
    def train(self, x, y, epochs):
        self.__model.fit(x, y, epochs=epochs)
    
    def loss(self,  x_test, y_test):
        return self.__model.evaluate(x_test, y_test)
    
    def predict(self, x_test):
        predictions = self.__model.predict([x_test])
        predicted = [np.argmax(element) for element in predictions]
        return predicted
        