# -*- coding: utf-8 -*-
"""
Created on Sun May 17 13:13:40 2020

@author: lukas
"""


import tensorflow as tf
import matplotlib.pyplot as plt
from CNN import CNN

def split_data(mnist):
    return mnist.load_data()

def load_data():
    mnist = tf.keras.datasets.mnist
    return mnist

def normalize(x):
    return tf.keras.utils.normalize(x, axis=1)

if __name__=='__main__':
    data = load_data()
    (x_train, y_train), (x_test, y_test) = split_data(data)
    x_train = normalize(x_train)
    x_test = normalize(x_test)
    cnn = CNN()
    epochs = int(input("Enter number of epochs: "))
    cnn.train(x_train, y_train, epochs)
    loss = cnn.loss(x_test, y_test)
    print("The loss of the algorithm is {}".format(loss))
    predictions = cnn.predict(x_test)
    for i in range(len(predictions)):       
        print("The NN predicted for the {0} element the number {1}".format(i, predictions[i]))   
        plt.imshow(x_test[i])
        plt.title("The {} element".format(i))
        plt.show()
    
    
