import random

from Individual import Individual
from EA_Population import EA_Population


class EA:
    def __init__(self, indiv_size, pop_size, prob, nrIter):
        self.__prob = prob
        self.__setS = [i for i in range(1, indiv_size + 1)]
        self.__setT = [i for i in range(1, indiv_size + 1)]
        self.__pop_size = pop_size
        self.__indiv_size = indiv_size
        self.__crtIter = 0
        self.__nrIter = nrIter
        self.__pop = EA_Population(pop_size, indiv_size, self.__setS, self.__setT)

    def iteration(self):
        pop = self.__pop.getPop()
        i1 = random.randint(0, len(pop) - 1)
        i2 = random.randint(0, len(pop) - 1)
        if i1 != i2:
            c = Individual.crossover(pop[i1], pop[i2])
            c.mutate(self.__prob)
            f1 = pop[i1].fitness()
            f2 = pop[i2].fitness()
            fc = c.fitness()
            if (f1 > f2) and (f1 > fc):
                pop[i1] = c
            if (f2 > f1) and (f2 > fc):
                pop[i2] = c
        self.__pop.setPop(pop)

    def run(self):
        while self.__crtIter in range(self.__nrIter) and self.__pop.bestIndiv().fitness() != 0:
            self.iteration()
            self.__crtIter += 1
            # if self.__crtIter % 1000 == 0: print(self.__crtIter)
            # print(str(self.__pop.bestIndiv()) + "Fitness: "+str(self.__pop.bestIndiv().fitness()))
        # print(self.__pop.bestIndiv(), self.__pop.bestIndiv().fitness())
        return self.__pop.bestIndiv()
