from ACO_Controller import Controller
from Problem import Problem

if __name__ == '__main__':
    prob = Problem()
    aco = Controller(prob)
    aco.run()
