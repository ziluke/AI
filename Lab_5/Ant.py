from random import random, choice


class Ant:
    def __init__(self, size, setS, setT, graph, alpha, beta, trace, q0):
        self.__n = size
        self.__row_s = size
        self.__setS = setS
        self.__setT = setT
        self.__graph = graph
        self.__path = [choice(self.__graph.get_nodes())]
        self.__alpha = alpha
        self.__beta = beta
        self.__q0 = q0
        self.__trace = trace

    def getPath(self):
        return self.__path

    def repeated(self, path):
        score = 0
        for i in range(self.__n):
            visited = []
            for j in range(len(path)):
                if path[j][i] not in visited:
                    visited.append(path[j][i])
                else:
                    score += 1
        return score

    def next_moves(self, curr_path):
        if len(curr_path) == self.__n:
            return []

        last_n = curr_path[-1]
        poss_p = []

        for neighbour in self.__graph.get_neighbours(last_n):
            path = curr_path[:]
            path.append(neighbour)
            poss_p.append(path)

        valid_p = []
        for p in poss_p:
            if self.repeated(p) == 0:
                valid_p.append(p)

        return valid_p

    def fitness(self, trace, path):
        ln = len(self.next_moves(path))
        return trace ** self.__alpha * ln ** self.__beta

    def done(self):
        return len(self.__path) == self.__n

    def addMove(self):
        if self.done():
            return
        paths = self.next_moves(self.__path)
        paths = sorted(paths, key=lambda x: self.fitness(self.__graph[self.__path[-1], x[-1]], x), reverse=True)

        if random() < self.__q0:
            path = paths[0]
        else:
            path = choice(paths)

        self.__graph[self.__path[-1], path[-1]] += self.__trace
        self.__path = path
