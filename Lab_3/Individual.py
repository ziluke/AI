import random


class Individual:
    def __init__(self, length, setS, setT):
        self.__length = 2 * length
        self.__genotype = self.createIndiv(setS, setT)
        self.__setS = setS
        self.__setT = setT

    def createIndiv(self, setS, setT):
        genotype = []
        for _ in range(self.__length // 2):
            aux = setS[:]
            random.shuffle(aux)
            genotype.append(aux)
        for _ in range(self.__length // 2):
            aux = setT[:]
            random.shuffle(aux)
            genotype.append(aux)
        return genotype

    def getSetS(self):
        return self.__setS

    def getSetT(self):
        return self.__setT

    def getGeno(self):
        return self.__genotype

    def setGeno(self, geno):
        self.__genotype = geno

    def getSize(self):
        return self.__length

    def toSquares(self):
        list = []
        h = self.__length // 2
        for i in range(h):
            for j in range(h):
                aux = [self.__genotype[i][j], self.__genotype[i + h][j]]
                list.append(aux)
        return list

    def fitness(self):
        score = 0
        h = self.__length // 2
        for i in range(self.__length):
            visitedR = []
            visitedC = []
            for j in range(self.__length // 2):
                if self.__genotype[i][j] not in visitedR:
                    visitedR.append(self.__genotype[i][j])
                else:
                    score = score + 1
                if i >= h:
                    if self.__genotype[j + h][i // 2] not in visitedC:
                        visitedC.append(self.__genotype[j + h][i // 2])
                    else:
                        score = score + 1
                else:
                    if self.__genotype[j][i // 2] not in visitedC:
                        visitedC.append(self.__genotype[j][i // 2])
                    else:
                        score = score + 1

        geno = self.toSquares()
        n = len(geno)
        for i in range(n):
            if geno[i] in geno[i + 1:]:
                score += 1

            return score

    @staticmethod
    def crossover(p1, p2):
        c_geno = []
        x = random.randint(0, p1.getSize())
        y = random.randint(0, p1.getSize())
        if x > y:
            x, y = y, x
        for i in range(p1.getSize()):
            if i in range(x, y + 1):
                c_geno.append(p2.getGeno()[i])
            else:
                c_geno.append(p1.getGeno()[i])
        child = Individual(p1.getSize() // 2, p1.getSetS(), p1.getSetT())
        child.setGeno(c_geno)
        return child

    def mutate(self, prob):
        if prob > random.uniform(0, 1):
            p = random.randint(0, self.__length - 1)
            random.shuffle(self.__genotype[p])

    def __lt__(self, other):
        return self.fitness() < other.fitness()

    def __gt__(self, other):
        return self.fitness() > other.fitness()

    def __str__(self):
        aux = ""
        h = self.__length // 2
        for i in range(h):
            for j in range(h):
                aux = aux + str(self.__genotype[i][j]) + "," + str(self.__genotype[i + h][j]) + " "
            aux = aux + '\n'
        return aux


