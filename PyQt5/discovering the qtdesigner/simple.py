# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_edit.setGeometry(QtCore.QRect(150, 110, 113, 25))
        self.name_edit.setObjectName("name_edit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 67, 21))
        self.label_2.setObjectName("label_2")
        self.show_button = Newbot(self.centralwidget)
        self.show_button.setGeometry(QtCore.QRect(150, 180, 89, 25))
        self.show_button.setObjectName("show_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 240, 131, 61))
        self.label.setObjectName("label")
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
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.show_button.setText(_translate("MainWindow", "Show"))
        self.label.setText(_translate("MainWindow", "your name is ..."))
from newbot import Newbot
