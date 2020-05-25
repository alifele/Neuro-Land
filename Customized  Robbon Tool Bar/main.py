import sys
from PyQt5.QtWidgets import *
from GUI.MainWindow import MainWindow
import qdarkstyle



__author__ = 'mamj'


def main():
    a = QApplication(sys.argv)
    a.setQuitOnLastWindowClosed(True)
    a.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # or in new API
    a.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    main_window = MainWindow()
    main_window.show()
    sys.exit(a.exec_())


main()
