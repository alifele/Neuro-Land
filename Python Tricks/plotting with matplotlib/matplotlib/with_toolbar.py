import sys
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore, QtGui, QtWidgets


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = plt.Figure(figsize=(width, height), dpi = dpi)
        self. axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        sc = MplCanvas(self)
        sc.axes.plot([0,1,2,3,4],[1,3,4,1,2])

        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        widget =QtWidgets.QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.show()



app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
