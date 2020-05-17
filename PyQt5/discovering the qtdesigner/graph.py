# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets as Qt
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = PlotWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(120, 120, 241, 211))
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

from pyqtgraph import PlotWidget
#import pyqtgraph as pg


class new_win(Qt.QMainWindow):
    def __init__(self):
        super().__init__()
        t = np.arange(0,1000,0.1)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.widget.plot(t,np.sin(t))




app = Qt.QApplication([])
window = new_win()
window.show()
app.exec_()
