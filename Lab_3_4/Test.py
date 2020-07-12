from EA import EA
from HC import HC
from PSO import PSO
from statistics import mean, stdev

import matplotlib.pyplot as pl


class Test:
    def __init__(self):
        self.__nr_runs = 30
        self.__iter = 1000
        self.__pop_s = 40
        self.__ea = EA(4, self.__pop_s, 0.01, self.__iter)
        self.__hc = HC(3, self.__iter)
        self.__pso = PSO(4, self.__pop_s, 10, 1.5, 2.5, 1.0, self.__iter)
        self.__bestEA = []
        self.__bestHC = []
        self.__bestPSO = []

    def __runTestEA(self):
        for _ in range(self.__nr_runs):
            self.__bestEA.append(self.__ea.run().fitness())
            self.__ea = EA(4, self.__pop_s, 0.01, self.__iter)

    def __runTestHC(self):
        for _ in range(self.__nr_runs):
            self.__bestHC.append(self.__hc.run().fitness())
            self.__hc = HC(3, self.__iter)

    def __runTestPSO(self):
        for _ in range(self.__nr_runs):
            self.__bestPSO.append(self.__pso.run().fitness)
            self.__pso = PSO(3, self.__pop_s, 10, 1.5, 2.5, 1.0, self.__iter)

    def runTests(self):
        self.__runTestEA()
        self.__runTestHC()
        self.__runTestPSO()
        avgEA, avgHC, avgPSO = self.getAvg()
        stdEA, stdHC, stdPSO = self.getSTD()
        print('Average:\n EA: {}, Average HC: {}, Average PSO: {}'.format(avgEA, avgHC, avgPSO))
        print('Standard Dev:\n EA: {}, HC: {}, PSO: {}'.format(stdEA, stdHC, stdPSO))
        self.getPlot()

    def getAvg(self):
        avgEA = mean(self.__bestEA)
        avgHC = mean(self.__bestHC)
        avgPSO = mean(self.__bestPSO)

        return avgEA, avgHC, avgPSO

    def getSTD(self):
        stdEA = stdev(self.__bestEA)
        stdHC = stdev(self.__bestHC)
        stdPSO = stdev(self.__bestPSO)

        return stdEA, stdHC, stdPSO

    def getPlot(self):
        pl.plot(range(1, len(self.__bestEA) + 1), self.__bestEA, 'r', label="EA")
        pl.plot(range(1, len(self.__bestHC) + 1), self.__bestHC, 'bs', label="HC")
        pl.plot(range(1, len(self.__bestPSO) + 1), self.__bestPSO, 'g^', label="PSO")
        pl.legend()
        pl.savefig('best_indiv_plot.png')
        pl.show()
