# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle.style_rc
from plot import canvas_widget

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

        self.canvas_widget1 = canvas_widget(self.centralwidget)
        self.canvas_widget1.setGeometry(QtCore.QRect(20, 60, 320, 270))
        self.canvas_widget1.setObjectName("canvas_widget1")
        self.pushButton_canv1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_canv1_1.setGeometry(QtCore.QRect(28, 350, 80, 25))
        self.pushButton_canv1_1.setObjectName("pushButton_canv1_1")
        self.pushButton_canv1_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_canv1_3.setGeometry(QtCore.QRect(116, 350, 80, 25))
        self.pushButton_canv1_3.setObjectName("pushButton_canv1_3")
        self.pushButton_canv1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_canv1_2.setGeometry(QtCore.QRect(202, 350, 80, 25))
        self.pushButton_canv1_2.setObjectName("pushButton_canv1_2")
        self.canvas_widget2 = canvas_widget(self.centralwidget)
        self.canvas_widget2.setGeometry(QtCore.QRect(360, 60, 320, 270))
        self.canvas_widget2.setObjectName("canvas_widget2")
        self.pushButton_canv2_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_canv2_1.setGeometry(QtCore.QRect(378, 350, 80, 25))
        self.pushButton_canv2_1.setObjectName("pushButton_canv2_1")
        self.pushButton_canv2_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_canv2_3.setGeometry(QtCore.QRect(464, 350, 80, 25))
        self.pushButton_canv2_3.setObjectName("pushButton_canv2_3")
        self.pushButton_canv2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_canv2_2.setGeometry(QtCore.QRect(550, 350, 80, 25))
        self.pushButton_canv2_2.setObjectName("pushButton_canv2_2")
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
