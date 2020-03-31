from Particle import Particle
from random import randint


class PSO_Population:
    def __init__(self, count, length, n_Size, setS, setT):
        self.__size = count
        self.__length = length
        self.__nSize = n_Size
        self.__pop = [Particle(length, setS, setT) for _ in range(count)]
        self.__neighbors = self.selectNeighbours()

    def getPop(self):
        return self.__pop

    def setPop(self, pop):
        self.__pop = pop

    def getNeighbors(self):
        return self.__neighbors

    def selectNeighbours(self):
        if self.__nSize > self.__size:
            self.__nSize = self.__size

        neighbors = []
        for i in range(self.__size):
            localNeighbor = []
            for j in range(self.__nSize):
                x = randint(0, self.__size - 1)
                while x in localNeighbor:
                    x = randint(0, self.__size - 1)
                localNeighbor.append(x)
            neighbors.append(localNeighbor.copy())
        return neighbors


    def bestIndiv(self):
        return sorted(self.__pop)[0]

    def __str__(self):
        aux = ""
        for i in self.__pop:
            aux = aux + str(i) + '\n'
        return aux
