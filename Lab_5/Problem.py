class Problem:
    # def __init__(self, n, iter, nrPop, trace, alpha, beta, q0, rho):
    #     self.__n = n
    #     self.__setS = [i for i in range(1, n + 1)]
    #     self.__setT = [i for i in range(1, n + 1)]
    #     self.__iter = iter
    #     self.__nrPop = nrPop
    #     self.__trace = trace
    #     self.__alpha = alpha
    #     self.__beta = beta
    #     self.__q0 = q0
    #     self.__rho = rho

    def __init__(self):
        f = open("problem.txt", "r")
        values = []
        for line in f:
            line = line.strip('\n').split('=')
            values.append(line[1])
        self.__n = int(values[0])
        self.__setS = [i for i in range(1, self.__n + 1)]
        self.__setT = [i for i in range(1, self.__n + 1)]
        self.__iter = int(values[1])
        self.__nrPop = int(values[2])
        self.__trace = int(values[3])
        self.__alpha = float(values[4])
        self.__beta = float(values[5])
        self.__q0 = float(values[6])
        self.__rho = float(values[7])
        f.close()

    @property
    def nrPop(self):
        return self.__nrPop

    @property
    def n(self):
        return self.__n

    @property
    def alpha(self):
        return self.__alpha

    @property
    def beta(self):
        return self.__beta

    @property
    def trace(self):
        return self.__trace

    @property
    def q0(self):
        return self.__q0

    @property
    def rho(self):
        return self.__rho

    @property
    def length(self):
        return self.__n

    @property
    def setS(self):
        return self.__setS

    @property
    def setT(self):
        return self.__setT

    @property
    def iterations(self):
        return self.__iter

    @property
    def nrPop(self):
        return self.__nrPop
