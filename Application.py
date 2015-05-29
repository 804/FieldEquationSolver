__author__ = '804'

from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QApplication
from MainWindow import InputEnquation

class App(QApplication):
    def __init__(self, *args):
        QApplication.__init__(self, *args)
        self.main = InputEnquation()
        self.connect(self, SIGNAL("lastWindowClosed()"), self.close_app)
        self.main.show()

    def close_app(self):
        self.exit(0)