__author__ = '804'

from PyQt4.QtCore import QRegExp, SIGNAL, Qt, SLOT
from PyQt4.QtGui import QWidget, QLabel, QRegExpValidator, QLineEdit, QPushButton, qApp, QGridLayout, QMessageBox
from ExtraMath import is_prime
from Solver import FieldEnquationSolver

class InputEnquation(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.msgBox = None
        self.solver = None
        self.resize(350, 100)
        self.setWindowTitle('Field equation')

        self.image = QLabel('ax^2 + bx + c = 0')

        self.l_a = QLabel('a = ')
        self.l_b = QLabel('b = ')
        self.l_c = QLabel('c = ')
        self.l_q = QLabel('q = ')

        self.rx = QRegExp("[0-9]*")
        self.a_validator = QRegExpValidator(self.rx, self)
        self.a = QLineEdit()
        self.a.setValidator(self.a_validator)

        self.rx = QRegExp("[0-9]*")
        self.b_validator = QRegExpValidator(self.rx, self)
        self.b = QLineEdit()
        self.b.setValidator(self.b_validator)

        self.rx = QRegExp("[0-9]*")
        self.c_validator = QRegExpValidator(self.rx, self)
        self.c = QLineEdit()
        self.c.setValidator(self.c_validator)

        self.rx = QRegExp("[0-9]*")
        self.q_validator = QRegExpValidator(self.rx, self)
        self.q = QLineEdit()
        self.q.setValidator(self.q_validator)

        self.calculate = QPushButton('Calculate', self)
        self.calculate.setFocusPolicy(Qt.NoFocus)
        self.connect(self.calculate, SIGNAL('clicked()'), self.click_calculate)

        self.exit = QPushButton('Exit', self)
        self.exit.setFocusPolicy(Qt.NoFocus)
        self.connect(self.exit, SIGNAL('clicked()'), qApp, SLOT('quit()'))

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.image, 1, 0, 1, 4)

        grid.addWidget(self.l_a, 2, 0)
        grid.addWidget(self.a, 2, 1)

        grid.addWidget(self.l_b, 3, 0)
        grid.addWidget(self.b, 3, 1)

        grid.addWidget(self.l_c, 2, 2)
        grid.addWidget(self.c, 2, 3)

        grid.addWidget(self.l_q, 3, 2)
        grid.addWidget(self.q, 3, 3)

        grid.addWidget(self.calculate, 4, 2, 1, 2)
        grid.addWidget(self.exit, 4, 0, 1, 2)

        self.setLayout(grid)

    def click_calculate(self):
        self.msgBox = QMessageBox()
        if (str(self.a.text()) == '') or (str(self.b.text()) == '') or (str(self.c.text()) == '') or (str(self.q.text()) == ''):
            self.msgBox.setWindowTitle('Error')
            self.msgBox.setText('Not all fields are filled')
            self.msgBox.exec_()
        else:
            if int(self.a.text()) == 0:
                self.msgBox.setWindowTitle('Error')
                self.msgBox.setText('\'a\' equal zero')
                self.msgBox.exec_()
            else:
                if (int(self.a.text()) >= int(self.q.text())) or (int(self.b.text()) >= int(self.q.text())) or (int(self.c.text()) >= int(self.q.text())):
                    self.msgBox.setWindowTitle('Error')
                    self.msgBox.setText('Coefficients not in the field')
                    self.msgBox.exec_()
                else:
                    if not is_prime(int(self.q.text())):
                        self.msgBox.setWindowTitle('Error')
                        self.msgBox.setText('Field power is not prime')
                        self.msgBox.exec_()
                    else:
                        self.solver = FieldEnquationSolver(int(self.a.text()), int(self.b.text()), int(self.c.text()), int(self.q.text()))
                        result = self.solver.solve()
                        if result[0] != result[1]:
                            self.msgBox.setWindowTitle('Result')
                            self.msgBox.setText('Two solutions: x1 = ' + str(result[0]) + ', x2 = ' + str(result[1]))
                            self.msgBox.exec_()
                        else:
                            self.msgBox.setWindowTitle('Result')
                            self.msgBox.setText('One solution: x = ' + str(result[0]))
                            self.msgBox.exec_()