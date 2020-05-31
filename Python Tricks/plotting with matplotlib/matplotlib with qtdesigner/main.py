import sys
import matplotlib.pyplot as plt
import matplotlib
from lay import Ui_MainWindow
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.canvas.axes1.plot([0,1,2,3,4],[10,1,20,3,40])
        self.ui.canvas.axes2.plot([1,2,3,4,5],[4,1,3,4,1])

        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
