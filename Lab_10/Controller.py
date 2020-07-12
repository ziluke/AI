from System import FuzzySystem


class Controller:
    def __init__(self, temp, hum, time, rules):
        self.__system = FuzzySystem(rules)
        self.__system.add_description('temperature', temp)
        self.__system.add_description('humidity', hum)
        self.__system.add_description('time', time, out=True)

    def compute(self, inputs):
        return "If we have the humidity: " + str(inputs['humidity']) + \
               " and temperature: " + str(inputs['temperature']) + \
               ", the operating time will probably be: " + str(self.__system.compute(inputs)) + "\n"
