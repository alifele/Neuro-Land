# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dia.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(140, 140, 26, 24))
        self.toolButton.setObjectName("toolButton")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 60, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(380, 200, 112, 23))
        self.radioButton.setObjectName("radioButton")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(190, 90, 92, 23))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(70, 260, 92, 23))
        self.checkBox_2.setObjectName("checkBox_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.radioButton.setText(_translate("Dialog", "RadioButton"))
        self.checkBox.setText(_translate("Dialog", "CheckBox"))
        self.checkBox_2.setText(_translate("Dialog", "CheckBox"))
