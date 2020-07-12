from PSO_Population import PSO_Population
from random import random


class PSO:
    def __init__(self, part_size, pop_size, neighSize, c1, c2, w, nrIter):
        self.__setS = [i for i in range(1, part_size + 1)]
        self.__setT = [i for i in range(1, part_size + 1)]
        self.__pop_size = pop_size
        self.__part_size = part_size
        self.__crtIter = 0
        self.__nrIter = nrIter
        self.__c1 = c1
        self.__c2 = c2
        self.__w = w
        self.__pop = PSO_Population(pop_size, part_size, neighSize, self.__setS, self.__setT)

    def getBestNeighbours(self):
        neighbours = self.__pop.getNeighbors()
        bestNeighbours = []
        for i in range(self.__pop_size):
            bestNeighbours.append(neighbours[i][0])
            for j in range(1, len(neighbours[i])):
                if self.__pop.getPop()[bestNeighbours[i]] > self.__pop.getPop()[neighbours[i][j]]:
                    bestNeighbours[i] = neighbours[i][j]
        return bestNeighbours

    def updateVelocity(self, bestNeighbors):
        pop = self.__pop.getPop()
        for i in range(self.__pop_size):
            for j in range(len(pop[0].velocity)):
                for x in range(len(pop[0].velocity[j])):
                    newV = self.__w * pop[i].velocity[j][x]
                    newV = newV + self.__c1 * random() * (pop[bestNeighbors[i]].position[j][x] - pop[i].position[j][x])
                    newV = newV + self.__c2 * random() * (pop[i].bestPosition[j][x] - pop[i].position[j][x])
                    pop[i].velocity[j][x] = newV
        return pop

    def updatePos(self, pop):
        for i in range(self.__pop_size):
            newPos = []
            for j in range(len(pop[0].velocity)):
                part = []
                for x in range(len(pop[0].velocity[j])):
                    var = pop[i].position[j][x] + pop[i].velocity[j][x]
                    if var > self.__part_size:
                        var = self.__part_size
                    else:
                        if var < 1:
                            var = 1
                    part.append(int(var))
                newPos.append(part)
            pop[i].position = newPos

        return pop

    def iteration(self):
        bestNeighbours = self.getBestNeighbours()
        pop = self.updateVelocity(bestNeighbours)
        pop = self.updatePos(pop)

        self.__pop.setPop(pop)

    def run(self):
        while self.__crtIter in range(self.__nrIter) and self.__pop.bestIndiv().fitness != 0:
            self.__w = self.__w / (self.__crtIter + 1)
            self.iteration()
            self.__crtIter += 1
            # if self.__crtIter % 1000 == 0: print(self.__crtIter)
            # print(str(self.__pop.bestIndiv()) + "Fitness: "+str(self.__pop.bestIndiv().fitness()))

        #print(self.__pop.bestIndiv(), self.__pop.bestIndiv().fitness)
        return self.__pop.bestIndiv()