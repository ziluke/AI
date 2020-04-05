from itertools import product

from Ant import Ant
from Graph import gen_graph


class Controller:
    def __init__(self, problem):
        self.__prob = problem
        self.__nrIter = problem.iterations
        self.__trace = problem.trace
        self.__alpha = problem.alpha
        self.__beta = problem.beta
        self.__rho = problem.rho
        self.__q0 = problem.q0
        self.__n = problem.n
        self.__nrPop = problem.nrPop

    def run(self):
        i = 0

        graph1 = gen_graph(self.__n)
        graph2 = gen_graph(self.__n)

        setS = [i for i in range(self.__n)]
        setT = [i for i in range(self.__n)]

        pop1 = [Ant(self.__n, setS, setT, graph1, self.__alpha, self.__beta, self.__trace, self.__q0) for _ in
                range(self.__nrPop)]
        pop2 = [Ant(self.__n, setS, setT, graph2, self.__alpha, self.__beta, self.__trace, self.__q0) for _ in
                range(self.__nrPop)]

        while i < self.__nrIter and (not pop1[0].done() or not pop2[0].done()):
            for a in pop1:
                a.addMove()
            for a in pop2:
                a.addMove()
            i += 1

        sol1 = [a.getPath() for a in pop1]
        sol2 = [a.getPath() for a in pop2]

        sols = []

        for s1, s2 in product(sol1, sol2):
            sol = s1 + s2
            sols.append(sol)

        sols = sorted(sols, key=lambda x: fitness(x))

        sol = sols[0]

        aux = ""
        for i in range(len(sol) // 2):
            for j in range(len(sol) // 2):
                h = len(sol) // 2
                aux = aux + str(sol[i][j]) + "," + str(sol[i + h][j]) + " "
            aux += '\n'

        print("The best solution found is:\n{} \nWith fitness: {}".format(aux, str(fitness(sol))))


def toSquares(sol):
    list = []
    h = len(sol) // 2
    for i in range(h):
        for j in range(h):
            aux = [sol[i][j], sol[i + h][j]]
            list.append(aux)
    return list


def fitness(sol):
    score = 0
    h = len(sol) // 2
    for i in range(len(sol)):
        visitedR = []
        visitedC = []
        for j in range(h):
            if sol[i][j] not in visitedR:
                visitedR.append(sol[i][j])
            else:
                score = score + 1
            if i >= h:
                if sol[j + h][i // 2] not in visitedC:
                    visitedC.append(sol[j + h][i // 2])
                else:
                    score = score + 1
            else:
                if sol[j][i // 2] not in visitedC:
                    visitedC.append(sol[j][i // 2])
                else:
                    score = score + 1

    geno = toSquares(sol)
    n = len(geno)
    for i in range(n):
        if geno[i] in geno[i + 1:]:
            score += 1

        return score
