

import sys
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure

from PyQt5 import QtCore, QtGui, QtWidgets


class Canvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=50, height=20, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.patch.set_facecolor('#19232D')
        self.axes1 = self.fig.add_subplot(111)
        self.axes1.tick_params(axis='x', colors='#5e6f80')
        self.axes1.tick_params(axis='y', colors='#5e6f80')
        self.axes1.set_facecolor("#c6c9cc")
        super().__init__(self.fig)


class canvas_widget(QtWidgets.QWidget):
    def __init__(self, centralwidget):
        super(QtWidgets.QWidget, self).__init__(centralwidget)

        self.canvas = Canvas()

        layout = QtWidgets.QVBoxLayout()
        toolbar = NavigationToolbar2QT(self.canvas, self)
        layout.addWidget(toolbar)
        layout.addWidget(self.canvas)

        self.setGeometry(QtCore.QRect(349, 180, 300, 400))
        self.setObjectName("widget")
        self.setLayout(layout)
