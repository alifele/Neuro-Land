import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMainWindow
from PyQt5.QtWidgets import QPushButton, QTabWidget




app = QApplication(sys.argv)


label = QtWidgets.QLabel('Hello there How Are You?')
label.setAlignment(Qt.AlignCenter)
window = QtWidgets.QMainWindow()
window.setCentralWidget(label)
#window.setCentralWidget(label)

window.show()


app.exec_()
