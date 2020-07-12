from random import random, shuffle


class Particle:
    def __init__(self, length, setS, setT):
        self.__size = 2 * length
        self.__setS = setS
        self.__setT = setT

        self.__position = self.createPos(setS, setT)
        self.__velocity = [[0 for _ in range(length)] for _ in range(self.__size)]
        self.evaluate()
        self.__bestPos = self.__position
        self.__bestFit = self.__fitness

    def toSquares(self):
        list = []
        h = self.__size // 2
        for i in range(h):
            for j in range(h):
                aux = [self.__position[i][j], self.__position[i + h][j]]
                list.append(aux)
        return list

    def fit(self):
        score = 0
        h = self.__size // 2
        for i in range(self.__size):
            visitedR = []
            visitedC = []
            for j in range(self.__size // 2):
                if self.__position[i][j] not in visitedR and (
                        self.__position[i][j] in self.__setS and self.__position[i][j] in self.__setT):
                    visitedR.append(self.__position[i][j])
                else:
                    score = score + 1
                if i >= h:
                    if self.__position[j + h][i // 2] not in visitedC and (
                            self.__position[i][j] in self.__setS and self.__position[i][j] in self.__setT):
                        visitedC.append(self.__position[j + h][i // 2])
                    else:
                        score = score + 1
                else:
                    if self.__position[j][i // 2] not in visitedC and (
                            self.__position[i][j] in self.__setS and self.__position[i][j] in self.__setT):
                        visitedC.append(self.__position[j][i // 2])
                    else:
                        score = score + 1
        geno = self.toSquares()
        n = len(geno)
        for i in range(n):
            if geno[i] in geno[i + 1:]:
                score += 1

            return score

    def evaluate(self):
        self.__fitness = self.fit()

    def createPos(self, setS, setT):
        position = []
        for _ in range(self.__size // 2):
            aux = setS[:]
            shuffle(aux)
            position.append(aux)
        for _ in range(self.__size // 2):
            aux = setT[:]
            shuffle(aux)
            position.append(aux)
        return position

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, newV):
        self.__velocity = newV

    @property
    def position(self):
        return self.__position

    @property
    def fitness(self):
        return self.__fitness

    @property
    def bestPosition(self):
        return self.__bestPos

    @property
    def bestFitness(self):
        return self.__bestFit

    @position.setter
    def position(self, newPosition):
        self.__position = newPosition.copy()
        self.evaluate()

        if self.__fitness < self.__bestFit:
            self.__bestPos = self.__position
            self.__bestFit = self.__fitness

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness

    def __str__(self):
        aux = ""
        h = self.__size // 2
        for i in range(h):
            for j in range(h):
                aux = aux + str(self.__position[i][j]) + "," + str(self.__position[i + h][j]) + " "
            aux = aux + '\n'
        return aux
