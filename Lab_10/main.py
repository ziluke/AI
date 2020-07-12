from Controller import Controller
from Description import FuzzyDescription
from Rule import FuzzyRule


def trap_reg(a, b, c, d):
    return lambda x: max(0, min((x - a) / (b - a), 1, (d - x) / (d - c)))


def tri_reg(a, b, c):
    return trap_reg(a, b, b, c)


def inv_line(a, b):
    return lambda val: val * (b - a) + a


def inv_tri(a, b, c):
    return lambda val: (inv_line(a, b)(val) + inv_line(c, b)(val)) / 2


# def getDescr(line: str):
#     vals = line.strip(',')
#     outs = []
#     for val in vals[1:]:
#         outs.append(int(val))
#
#     function = None
#     if len(outs) == 4:
#         function = trap_reg(outs[0], outs[1], outs[2], outs[3])
#     else:
#         function = tri_reg(outs[0], outs[1], outs[2])
#
#     return vals[0], function
#
#
# def readProblemData():
#     file = open("problem.in", 'r')
#     temperature = FuzzyDescription()
#     humidity = FuzzyDescription()
#     time = FuzzyDescription()
#     rules = []
#     descriptions = {'temperature': temperature, 'humidity': humidity, 'time': time}
#
#     desc = ""
#     for line in file:
#         if line in {"temperature", "humidity", "time", "rules"}:
#             desc = line
#         elif desc != "rules":
#             if desc != "time":
#                 name, fct = getDescr(line)
#                 descriptions[desc].add_region(name, fct)
#             else:
#                 name, fct = getDescr(line)
#                 descriptions[desc].add_region(name, fct, )

def readInput():
    file = open("input.in", "r")
    inputs = []
    for line in file:
        vals = line.split(',')
        vals[0] = int(vals[0])
        vals[1] = int(vals[1])
        inputs.append(vals)

    file.close()
    return inputs


if __name__ == "__main__":
    temperature = FuzzyDescription()
    humidity = FuzzyDescription()
    time = FuzzyDescription()
    rules = []

    temperature.add_region('very cold', trap_reg(-1000, -30, -20, 5))
    temperature.add_region('cold', tri_reg(-5, 0, 10))
    temperature.add_region('normal', trap_reg(5, 10, 15, 20))
    temperature.add_region('warm', tri_reg(15, 20, 25))
    temperature.add_region('hot', trap_reg(25, 30, 35, 1000))

    humidity.add_region('dry', tri_reg(-1000, 0, 50))
    humidity.add_region('normal', tri_reg(0, 50, 100))
    humidity.add_region('wet', tri_reg(50, 100, 1000))

    time.add_region('short', tri_reg(-1000, 0, 50), inv_line(50, 0))
    time.add_region('medium', tri_reg(0, 50, 100), inv_tri(0, 50, 100))
    time.add_region('long', tri_reg(50, 100, 1000), inv_line(50, 100))

    rules.append(FuzzyRule({'temperature': 'very cold', 'humidity': 'wet'},
                           {'time': 'short'}))
    rules.append(FuzzyRule({'temperature': 'cold', 'humidity': 'wet'},
                           {'time': 'short'}))
    rules.append(FuzzyRule({'temperature': 'normal', 'humidity': 'wet'},
                           {'time': 'short'}))
    rules.append(FuzzyRule({'temperature': 'warm', 'humidity': 'wet'},
                           {'time': 'short'}))
    rules.append(FuzzyRule({'temperature': 'hot', 'humidity': 'wet'},
                           {'time': 'medium'}))

    rules.append(FuzzyRule({'temperature': 'very cold', 'humidity': 'normal'},
                           {'time': 'short'}))
    rules.append(FuzzyRule({'temperature': 'cold', 'humidity': 'normal'},
                           {'time': 'medium'}))
    rules.append(FuzzyRule({'temperature': 'normal', 'humidity': 'normal'},
                           {'time': 'medium'}))
    rules.append(FuzzyRule({'temperature': 'warm', 'humidity': 'normal'},
                           {'time': 'medium'}))
    rules.append(FuzzyRule({'temperature': 'hot', 'humidity': 'normal'},
                           {'time': 'long'}))

    rules.append(FuzzyRule({'temperature': 'very cold', 'humidity': 'dry'},
                           {'time': 'medium'}))
    rules.append(FuzzyRule({'temperature': 'cold', 'humidity': 'dry'},
                           {'time': 'long'}))
    rules.append(FuzzyRule({'temperature': 'normal', 'humidity': 'dry'},
                           {'time': 'long'}))
    rules.append(FuzzyRule({'temperature': 'warm', 'humidity': 'dry'},
                           {'time': 'long'}))
    rules.append(FuzzyRule({'temperature': 'hot', 'humidity': 'dry'},
                           {'time': 'long'}))

    ctrl = Controller(temperature, humidity, time, rules)

    inputs = readInput()

    out = open("output.out", "w")

    for inp in inputs:
        out.write(ctrl.compute({'humidity': inp[0], 'temperature': inp[1]}))

    out.close()
