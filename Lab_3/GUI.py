from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import *

from EA import EA
from HC import HC
from PSO import PSO


class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("mainWindow")
        self.setWindowTitle("Euler Square")
        self.resize(324, 374)
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QRect(50, 90, 221, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.btnEA = QPushButton(self.verticalLayoutWidget)
        self.btnEA.setObjectName("btnEA")
        self.verticalLayout.addWidget(self.btnEA)
        self.btnEA.setText("EA")

        self.btnHC = QPushButton(self.verticalLayoutWidget)
        self.btnHC.setObjectName("btnHC")
        self.verticalLayout.addWidget(self.btnHC)
        self.btnHC.setText("HC")

        self.btnPSO = QPushButton(self.verticalLayoutWidget)
        self.btnPSO.setObjectName("btnPSO")
        self.verticalLayout.addWidget(self.btnPSO)
        self.btnPSO.setText("PSO")

        self.btnEA.clicked.connect(self.ea_clicked)
        self.btnHC.clicked.connect(self.hc_clicked)
        self.btnPSO.clicked.connect(self.pso_clicked)

        self.show()

    def ea_clicked(self):
        ea = EA_GUI(self)

    def hc_clicked(self):
        hc = HC_GUI(self)

    def pso_clicked(self):
        pso = PSO_GUI(self)


class EA_GUI(QMainWindow):
    def __init__(self, parent=None):
        super(EA_GUI, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setObjectName("window")
        self.resize(798, 572)
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QRect(40, 20, 651, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.probabilityLabel = QLabel(self.verticalLayoutWidget)
        self.probabilityLabel.setObjectName("probabilityLabel")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.probabilityLabel)
        self.probabilityLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.probabilityLineEdit.setObjectName("probabilityLineEdit")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.probabilityLineEdit)
        self.populationSizeLabel = QLabel(self.verticalLayoutWidget)
        self.populationSizeLabel.setObjectName("populationSizeLabel")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.populationSizeLabel)
        self.populationSizeLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.populationSizeLineEdit.setObjectName("populationSizeLineEdit")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.populationSizeLineEdit)
        self.individualSizeLabel = QLabel(self.verticalLayoutWidget)
        self.individualSizeLabel.setObjectName("individualSizeLabel")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.individualSizeLabel)
        self.individualSizeLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.individualSizeLineEdit.setObjectName("individualSizeLineEdit")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.individualSizeLineEdit)
        self.nrOfGenerationsLabel = QLabel(self.verticalLayoutWidget)
        self.nrOfGenerationsLabel.setObjectName("nrOfGenerationsLabel")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.nrOfGenerationsLabel)
        self.nrOfGenerationsLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.nrOfGenerationsLineEdit.setObjectName("nrOfGenerationsLineEdit")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.nrOfGenerationsLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.solutionLabel = QLabel(self.verticalLayoutWidget)
        self.solutionLabel.setText("")
        self.solutionLabel.setObjectName("solutionLabel")
        self.horizontalLayout.addWidget(self.solutionLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.runBtn = QPushButton(self)
        self.runBtn.setGeometry(QRect(340, 510, 75, 23))
        self.runBtn.setObjectName("runBtn")

        self.setWindowTitle("EA")
        self.probabilityLabel.setText("Probability")
        self.populationSizeLabel.setText("Population size")
        self.individualSizeLabel.setText("Individual size")
        self.nrOfGenerationsLabel.setText("Nr. of generations")
        self.label.setText("Best solution:")
        self.runBtn.setText("Run")

        self.runBtn.clicked.connect(self.run_clicked)

        self.show()

    def run_clicked(self):
        prob = float(self.probabilityLineEdit.text())
        pop_s = int(self.populationSizeLineEdit.text())
        nr_gen = int(self.nrOfGenerationsLineEdit.text())
        indiv_s = int(self.individualSizeLineEdit.text())

        ea = EA(indiv_s, pop_s, prob, nr_gen)

        sol = ea.run()

        self.label.setText("The best solution we found has fitness {}".format(sol.fitness()))
        self.solutionLabel.setText(str(sol))


class HC_GUI(QMainWindow):
    def __init__(self, parent=None):
        super(HC_GUI, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setObjectName("window")
        self.resize(798, 572)
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QRect(40, 20, 651, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.individualSizeLabel = QLabel(self.verticalLayoutWidget)
        self.individualSizeLabel.setObjectName("individualSizeLabel")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.individualSizeLabel)
        self.individualSizeLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.individualSizeLineEdit.setObjectName("individualSizeLineEdit")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.individualSizeLineEdit)
        self.nrOfGenerationsLabel = QLabel(self.verticalLayoutWidget)
        self.nrOfGenerationsLabel.setObjectName("nrOfGenerationsLabel")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.nrOfGenerationsLabel)
        self.nrOfGenerationsLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.nrOfGenerationsLineEdit.setObjectName("nrOfGenerationsLineEdit")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.nrOfGenerationsLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.solutionLabel = QLabel(self.verticalLayoutWidget)
        self.solutionLabel.setText("")
        self.solutionLabel.setObjectName("solutionLabel")
        self.horizontalLayout.addWidget(self.solutionLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.runBtn = QPushButton(self)
        self.runBtn.setGeometry(QRect(340, 510, 75, 23))
        self.runBtn.setObjectName("runBtn")

        self.setWindowTitle("HC")
        self.individualSizeLabel.setText("Individual size")
        self.nrOfGenerationsLabel.setText("Nr. of generations")
        self.label.setText("Best solution:")
        self.runBtn.setText("Run")

        self.runBtn.clicked.connect(self.run_clicked)

        self.show()

    def run_clicked(self):
        nr_gen = int(self.nrOfGenerationsLineEdit.text())
        indiv_s = int(self.individualSizeLineEdit.text())

        ea = HC(indiv_s, nr_gen)

        sol = ea.run()

        self.label.setText("The best solution we found has fitness {}".format(sol.fitness()))
        self.solutionLabel.setText(str(sol))


class PSO_GUI(QMainWindow):
    def __init__(self, parent=None):
        super(PSO_GUI, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setObjectName("window")
        self.resize(798, 572)
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QRect(40, 20, 651, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")

        self.probabilityLabel = QLabel(self.verticalLayoutWidget)
        self.probabilityLabel.setObjectName("probabilityLabel")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.probabilityLabel)
        self.probabilityLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.probabilityLineEdit.setObjectName("probabilityLineEdit")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.probabilityLineEdit)
        self.wLabel = QLabel(self.verticalLayoutWidget)
        self.wLabel.setObjectName("wLabel")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.wLabel)
        self.wLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.wLineEdit.setObjectName("wLineEdit")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.wLineEdit)
        self.populationSizeLabel = QLabel(self.verticalLayoutWidget)
        self.populationSizeLabel.setObjectName("populationSizeLabel")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.populationSizeLabel)
        self.populationSizeLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.populationSizeLineEdit.setObjectName("populationSizeLineEdit")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.populationSizeLineEdit)
        self.individualSizeLabel = QLabel(self.verticalLayoutWidget)
        self.individualSizeLabel.setObjectName("individualSizeLabel")
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.individualSizeLabel)
        self.individualSizeLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.individualSizeLineEdit.setObjectName("individualSizeLineEdit")
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.individualSizeLineEdit)
        self.nrOfGenerationsLabel = QLabel(self.verticalLayoutWidget)
        self.nrOfGenerationsLabel.setObjectName("nrOfGenerationsLabel")
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.nrOfGenerationsLabel)
        self.nrOfGenerationsLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.nrOfGenerationsLineEdit.setObjectName("nrOfGenerationsLineEdit")
        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.nrOfGenerationsLineEdit)
        self.c2Label = QLabel(self.verticalLayoutWidget)
        self.c2Label.setObjectName("c2Label")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.c2Label)
        self.c2LineEdit = QLineEdit(self.verticalLayoutWidget)
        self.c2LineEdit.setObjectName("c2LineEdit")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.c2LineEdit)
        self.neighbourhoodSizeLabel = QLabel(self.verticalLayoutWidget)
        self.neighbourhoodSizeLabel.setObjectName("neighbourhoodSizeLabel")
        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.neighbourhoodSizeLabel)
        self.neighbourhoodSizeLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.neighbourhoodSizeLineEdit.setObjectName("neighbourhoodSizeLineEdit")
        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.neighbourhoodSizeLineEdit)

        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.solutionLabel = QLabel(self.verticalLayoutWidget)
        self.solutionLabel.setText("")
        self.solutionLabel.setObjectName("solutionLabel")
        self.horizontalLayout.addWidget(self.solutionLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.runBtn = QPushButton(self)
        self.runBtn.setGeometry(QRect(340, 510, 75, 23))
        self.runBtn.setObjectName("runBtn")

        self.setWindowTitle("PSO")
        self.probabilityLabel.setText("c1")
        self.wLabel.setText("w")
        self.populationSizeLabel.setText("Population size")
        self.individualSizeLabel.setText("Individual size")
        self.nrOfGenerationsLabel.setText("Nr. of generations")
        self.c2Label.setText("c2")
        self.neighbourhoodSizeLabel.setText("Neighbourhood size")
        self.label.setText("Best solution:")
        self.runBtn.setText("Run")

        self.runBtn.clicked.connect(self.run_clicked)

        self.show()

    def run_clicked(self):
        self.label.setText("Best solution:")
        c1 = float(self.probabilityLineEdit.text())
        c2 = float(self.c2LineEdit.text())
        w = float(self.wLineEdit.text())
        nr_gen = int(self.nrOfGenerationsLineEdit.text())
        indiv_s = int(self.individualSizeLineEdit.text())
        n_s = int(self.neighbourhoodSizeLineEdit.text())
        pop_s = int(self.populationSizeLineEdit.text())

        pso = PSO(indiv_s, pop_s, n_s, c1, c2, w, nr_gen)

        sol = pso.run()

        self.label.setText("The best solution we found has fitness {}".format(sol.fitness))
        self.solutionLabel.setText(str(sol))
