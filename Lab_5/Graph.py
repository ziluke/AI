from collections import defaultdict
from itertools import permutations, product


class Graph:

    def __init__(self):
        self.__graph = defaultdict(dict)

    def __getitem__(self, item):
        return self.__graph[item[0]][item[1]]

    def __setitem__(self, key, value):
        self.__graph[key[0]][key[1]] = value

    def addEdge(self, n1, n2):
        self.__graph[n1][n2] = 1
        self.__graph[n2][n1] = 1

    def get_nodes(self):
        return [i for i in self.__graph.keys()]

    def get_neighbours(self, node):
        return [n for n in self.__graph[node].keys()]


def gen_graph(n):
    vals = [i for i in range(1, n + 1)]
    perms = permutations(vals)
    g = Graph()
    for n1, n2 in product(perms, repeat=2):
        g.addEdge(n1, n2)

    return g
