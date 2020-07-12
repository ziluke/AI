import numpy as np


class Controller:
    def __init__(self, prob):
        self.__prob = prob
        self.__data = self.__prob.get_Training()
        self.__x, self.__y = self.__model_data(self.__data)
        self.__beta = self.__beta_coeff()

    def __beta_coeff(self):
        Xt = self.__x.transpose()
        Xi = np.linalg.inv(Xt @ self.__x)
        beta = (Xi @ Xt) @ self.__y
        return beta

    def __model_data(self, data):
        X = [[1] for _ in data]
        Y = []
        index = 0
        for d in data:
            X[index] = X[index] + d[:-1]
            Y.append(d[-1])
            index += 1
        return np.array(X), np.array(Y)

    def __predict(self, x):
        sum = 0
        for i in range(len(self.__beta)):
            sum += self.__beta[i] * x[i]
        return sum

    def run(self):
        x, y = self.__model_data(self.__prob.get_Test())
        err = 0
        for i in range(len(x)):
            predict = self.__predict(x[i])
            print("Predicted: {0:.2f}  ->  Actual: {1:.2f}".format(predict, y[i]))
            curr_err = (y[i] - predict) ** 2
            err += curr_err
        return err
