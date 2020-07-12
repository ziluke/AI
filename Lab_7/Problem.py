from math import floor


class Problem:
    def __init__(self, filename, ratio):
        self.__split_ratio = ratio
        self.__training, self.__testing = self.__split_data(self.__readData(filename))

    def __readData(self, fileName):
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
        return data

    def __split_data(self, data):
        if self.__split_ratio == 1:
            return data, data

        split = floor(len(data) * self.__split_ratio)
        return data[:split], data[split:]

    def get_Training(self):
        return self.__training

    def get_Test(self):
        return self.__testing
