# if __name__ == '__main__':
#     ea = EA(3, 100, 0.01, 10000)
#     hc = HC(3, 10000)
#     pso = PSO(3, 100, 20, 1.5, 2.5, 1.0, 10000)
#
#     choice = 3
#
#     algs = {1: ea, 2: hc, 3: pso}
#     fct = algs.get(choice)
#     fct.run()
#
import sys
from PyQt5.QtWidgets import QApplication
from GUI import GUI
from Test import Test

if __name__ == '__main__':
    try:
        test = Test()
        test.runTests()
        app = QApplication(sys.argv)
        g = GUI()
        sys.exit(app.exec_())
    except Exception as er:
        print(er)
