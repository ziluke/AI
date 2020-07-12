from Individual import Individual


class EA_Population:
    def __init__(self, count, length, setS, setT):
        self.__size = count
        self.__length = length
        self.__pop = [Individual(length, setS, setT) for _ in range(count)]

    def getPop(self):
        return self.__pop

    def setPop(self, pop):
        self.__pop = pop

    def __str__(self):
        aux = ""
        for i in self.__pop:
            aux = aux + str(i) + '\n'
        return aux

    def bestIndiv(self):
        return sorted(self.__pop)[0]
