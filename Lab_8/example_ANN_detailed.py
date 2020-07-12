from random import random
from math import exp, sin, floor
from copy import deepcopy
import matplotlib as mpl


def identical(x):
    return x


def dIdentical(x):
    return 1


def ReLU(x):
    return max(0, x)


def dReLU(x):
    if x > 0:
        return 1
    else:
        return 0


def threshold(x):
    if x > 0.2:
        return 1
    return 0


def dThreshold(x):
    # is just to have some function when we train the network
    return 1


def sigmoid(x):
    return (1.0 / (1.0 + exp(-x)))


def dSigmoid(x):
    return x * (1.0 - x)


class Neuron:
    def __init__(self, noOfInputs, activationFunction):
        self.noOfInputs = noOfInputs
        self.activationFunction = activationFunction
        self.weights = [random() for i in range(self.noOfInputs)]
        self.output = 0

    def setWeights(self, newWeights):
        self.weights = newWeights

    def fireNeuron(self, inputs):
        u = sum([x * y for x, y in zip(inputs, self.weights)])
        self.output = self.activationFunction(u)
        return self.output

    def __str__(self):
        return str(self.weights)


class Layer:
    def __init__(self, noOfInputs, activationFunction, noOfNeurons):
        self.noOfNeurons = noOfNeurons
        self.neurons = [Neuron(noOfInputs, activationFunction) for i in
                        range(self.noOfNeurons)]

    def forward(self, inputs):
        for x in self.neurons:
            x.fireNeuron(inputs)
        return ([x.output for x in self.neurons])

    def __str__(self):
        s = ''
        for i in range(self.noOfNeurons):
            s += ' n ' + str(i) + ' ' + str(self.neurons[i]) + '\n'
        return s


class FirstLayer(Layer):
    def __init__(self, noOfNeurons, bias=False):
        if bias:
            noOfNeurons = noOfNeurons + 1
        Layer.__init__(self, 1, identical, noOfNeurons)
        for x in self.neurons:
            x.setWeights([1])

    def forward(self, inputs):
        for i in range(len(self.neurons)):
            self.neurons[i].fireNeuron([inputs[i]])
        return ([x.output for x in self.neurons])
        # return inputs


class Network:
    def __init__(self, structure, activationFunction, derivate, bias=False):
        self.activationFunction = activationFunction
        self.derivate = derivate
        self.bias = bias
        self.structure = structure[:]
        self.noLayers = len(self.structure)
        self.layers = [FirstLayer(self.structure[0], bias)]
        for i in range(1, len(self.structure)):
            self.layers = self.layers + [Layer(self.structure[i - 1], activationFunction, self.structure[i])]

    def feedForward(self, inputs):
        self.signal = inputs[:]
        if self.bias:
            self.signal.append(1)
        for l in self.layers:
            self.signal = l.forward(self.signal)
        return self.signal

    def backPropag(self, loss, learnRate):
        err = loss[:]
        delta = []
        currentLayer = self.noLayers - 1
        newConfig = Network(self.structure, self.activationFunction, self.derivate, self.bias)
        # last layer
        for i in range(self.structure[-1]):
            delta.append(err[i] * self.derivate(self.layers[-1].neurons[i].output))
            for r in range(self.structure[currentLayer - 1]):
                newConfig.layers[-1].neurons[i].weights[r] = self.layers[-1].neurons[i].weights[r] + learnRate * delta[
                    i] * self.layers[currentLayer - 1].neurons[r].output

        # propagate the errors layer by layer
        for currentLayer in range(self.noLayers - 2, 0, -1):

            currentDelta = []
            for i in range(self.structure[currentLayer]):
                currentDelta.append(self.derivate(self.layers[currentLayer].neurons[i].output) * sum(
                    [self.layers[currentLayer + 1].neurons[j].weights[i] * delta[j] for j in
                     range(self.structure[currentLayer + 1])]))

            delta = currentDelta[:]
            for i in range(self.structure[currentLayer]):
                for r in range(self.structure[currentLayer - 1]):
                    newConfig.layers[currentLayer].neurons[i].weights[r] = self.layers[currentLayer].neurons[i].weights[
                                                                               r] + learnRate * delta[i] * \
                                                                           self.layers[currentLayer - 1].neurons[
                                                                               r].output
        self.layers = deepcopy(newConfig.layers)

    def computeLoss(self, u, t):
        loss = []
        out = self.feedForward(u)
        for i in range(len(t)):
            loss.append(t[i] - out[i])
        return loss[:]

    def __str__(self):
        s = ''
        for i in range(self.noLayers):
            s += ' l ' + str(i) + ' :' + str(self.layers[i])
        return s


def test1():
    nn = Network([3, 4, 1], ReLU, dReLU)  # sigmoid, dSigmoid)#
    u = [[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
    t = [[0], [1], [1], [20]]
    errors = []
    iterations = []
    for i in range(1500):
        iterations.append(i)
        e = []
        for j in range(len(u)):
            e.append(nn.computeLoss(u[j], t[j])[0])
            nn.backPropag(nn.computeLoss(u[j], t[j]), 0.01)
        errors.append(sum([x ** 2 for x in e]))
    for j in range(len(u)):
        print(u[j], t[j], nn.feedForward(u[j]))
    print(str(nn))
    mpl.pyplot.plot(iterations, errors, label='loss value vs iteration')
    mpl.pyplot.xlabel('Iterations')
    mpl.pyplot.ylabel('loss function')
    mpl.pyplot.legend()
    mpl.pyplot.show()


def test2():
    nn = Network([2, 1], sigmoid, dSigmoid)
    u = [[1, 1], [0, 1], [1, 0], [0, 0]]
    t = [[0], [1], [1], [0]]
    errors = []
    iterations = []
    for i in range(10):
        iterations.append(i)
        e = []
        for j in range(len(u)):
            e.append(nn.computeLoss(u[j], t[j])[0])
            nn.backPropag(nn.computeLoss(u[j], t[j]), 1)
        errors.append(sum([x ** 2 for x in e]))
    for j in range(len(u)):
        print(u[j], t[j], nn.feedForward(u[j]))
    mpl.pyplot.plot(iterations, errors, label='loss value vs iteration')
    mpl.pyplot.xlabel('Iterations')
    mpl.pyplot.ylabel('loss function')
    mpl.pyplot.legend()
    mpl.pyplot.show()


def readData(fileName):
    f = open(fileName, "r")
    data = []
    first = True
    for line in f:
        if first:
            first = False
            continue
        line = line.strip('\n')
        if len(line) == 0:
            continue
        line = line.split()
        line = [float(i) for i in line]
        data.append(line)
    f.close()
    return data


def split_data(data, split_ratio):
    if split_ratio == 1:
        return data, data

    split = floor(len(data) * split_ratio)
    return data[:split], data[split:]


def model_data(fileName, split_r):
    data = readData(fileName)
    training, test = split_data(data, split_r)
    X = [[] for _ in training]
    Y = [[] for _ in training]
    index = 0
    for d in training:
        X[index] = X[index] + d[:-1]
        Y[index].append(d[-1])
        index += 1
    minsX, maxsX = getMinMax(X)
    minsY, maxsY = getMinMax(Y)
    X = normalization(X, minsX, maxsX)
    Y = normalization(Y, minsY, maxsY)
    return X, Y, test


def getMinMax(X):
    mins = [9999 for _ in X[0]]
    maxs = [-1 for _ in X[0]]
    for x in X:
        for i in range(len(x)):
            mins[i] = min(mins[i], x[i])
            maxs[i] = max(maxs[i], x[i])
    return mins, maxs


def normalization(list, mins, maxs):
    data = list[:]
    for x in data:
        for i in range(len(x)):
            x[i] = (x[i] - mins[i]) / (maxs[i] - mins[i])
    return data


def test3():
    net = Network([5, 4, 1], identical, dIdentical)
    inputs, outputs, testData = model_data("bdate2.txt", 0.4)
    errors = []
    iterations = []
    for i in range(10):
        iterations.append(i)
        e = []
        for j in range(len(inputs)):
            e.append(net.computeLoss(inputs[j], outputs[j])[0])
            net.backPropag(net.computeLoss(inputs[j], outputs[j]), 0.1)
        errors.append(sum([x ** 2 for x in e]))

    for j in range(len(inputs)):
        print(inputs[j], outputs[j], net.feedForward(inputs[j]))
    mpl.pyplot.plot(iterations, errors, label='loss value vs iteration')
    mpl.pyplot.xlabel('Iterations')
    mpl.pyplot.ylabel('loss function')
    mpl.pyplot.legend()
    mpl.pyplot.show()


test3()
# test1()
# test2()
