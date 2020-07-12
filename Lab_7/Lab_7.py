from Problem import Problem
from Controller import Controller

if __name__ == "__main__":
    split_ratio = float(input("Input slit ratio (btw. 0.1-1.0): "))
    prob = Problem("bdate2.txt", split_ratio)
    controller = Controller(prob)
    err = controller.run()
    print("The error of the regression is: {0:2f}".format(err))
