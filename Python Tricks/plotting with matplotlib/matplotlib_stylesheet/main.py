# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import sys
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure

from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle.style_rc




class Canvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=10, height=20, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes1 = fig.add_subplot(211)
        super().__init__(fig)


class canvas_widget(QtWidgets.QWidget):
    def __init__(self, centralwidget, canvas):
        super().__init__(centralwidget)
        layout = QtWidgets.QVBoxLayout()

        toolbar = NavigationToolbar2QT(canvas, self)
        layout.addWidget(toolbar)

        layout.addWidget(canvas)


        self.setGeometry(QtCore.QRect(349, 180, 300, 400))
        self.setObjectName("widget")
        self.setLayout(layout)




f = open("qdarkstyle/style.qss")
style = f.read()
f.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(style)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.canvas1 = Canvas()
        self.canvas2 = Canvas()

        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(20, 60, 321, 411))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.canvas_widget1 = canvas_widget(self.centralwidget, self.canvas1)
        self.canvas_widget1.setObjectName("canvas_widget1")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_canv1_1 = QtWidgets.QPushButton(self.widget)
        self.pushButton_canv1_1.setObjectName("pushButton_canv1_1")
        self.horizontalLayout.addWidget(self.pushButton_canv1_1)
        self.pushButton_canv1_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_canv1_3.setObjectName("pushButton_canv1_3")
        self.horizontalLayout.addWidget(self.pushButton_canv1_3)
        self.pushButton_canv1_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_canv1_2.setObjectName("pushButton_canv1_2")
        self.horizontalLayout.addWidget(self.pushButton_canv1_2)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(380, 60, 331, 411))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.canvas_widget2 = canvas_widget(self.centralwidget, self.canvas2)
        self.canvas_widget2.setObjectName("canvas_widget2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_canv2_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_canv2_1.setObjectName("pushButton_canv2_1")
        self.horizontalLayout_2.addWidget(self.pushButton_canv2_1)
        self.pushButton_canv2_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_canv2_3.setObjectName("pushButton_canv2_3")
        self.horizontalLayout_2.addWidget(self.pushButton_canv2_3)
        self.pushButton_canv2_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_canv2_2.setObjectName("pushButton_canv2_2")
        self.horizontalLayout_2.addWidget(self.pushButton_canv2_2)
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
        self.pushButton_canv1_1.setText(_translate("MainWindow", "plot sin"))
        self.pushButton_canv1_3.setText(_translate("MainWindow", "plot cos"))
        self.pushButton_canv1_2.setText(_translate("MainWindow", "update"))
        self.pushButton_canv2_1.setText(_translate("MainWindow", "plot sin"))
        self.pushButton_canv2_3.setText(_translate("MainWindow", "plot cos"))
        self.pushButton_canv2_2.setText(_translate("MainWindow", "update"))
