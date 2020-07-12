class FuzzyDescription:
    def __init__(self):
        self.__reg = {}
        self.__inv = {}

    def add_region(self, name, membership_funct, inverse=None):
        self.__reg[name] = membership_funct
        self.__inv[name] = inverse

    def fuzzify(self, value):
        return {name: membership_funct(value) for name, membership_funct in self.__reg.items()}

    def defuzzify(self, name, value):
        return self.__inv[name](value)
