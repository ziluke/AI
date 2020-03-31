from itertools import product
from copy import deepcopy

from Individual import Individual


class HC:
    def __init__(self, size, nrIter):
        self.__setS = [i for i in range(1, size + 1)]
        self.__setT = [i for i in range(1, size + 1)]
        self.__size = size
        self.__crtIter = 0
        self.__nrIter = nrIter

    def getNeighbours(self, state):
        geno = state.getGeno()
        neighbors = []
        for i in range(self.__size):
            for j in range(self.__size):
                for v in product(self.__setS, self.__setT):
                    geno[i][j] = v[0]
                    geno[i + self.__size][j] = v[1]
                    indiv = Individual(self.__size, self.__setS, self.__setT)
                    indiv.setGeno(geno)
                    neighbors.append(indiv)
        return neighbors

    def bestNeighbor(self, neighbors):
        return sorted(neighbors)[0]

    def run(self):
        state = Individual(self.__size, self.__setS, self.__setT)
        final = deepcopy(state)
        while self.__crtIter in range(self.__nrIter) and state.fitness() != 0:
            neighbors = self.getNeighbours(state)
            bestN = self.bestNeighbor(neighbors)
            if state.fitness() > bestN.fitness():
                state = bestN
            else:
                state = Individual(self.__size, self.__setS, self.__setT)
            self.__crtIter += 1
            # if self.__crtIter % 1000 == 0: print(self.__crtIter)
        final = state
        return final
