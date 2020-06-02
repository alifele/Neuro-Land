from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import QKeySequence as QKSec
from Ribbon.RibbonButton import RibbonButton
from Ribbon.Icons import get_icon
from Ribbon.RibbonTextbox import RibbonTextbox
from Ribbon.RibbonWidget import *
import qdarkstyle
from PyQt5.QtGui import QIcon
import ribbon_actions
import qdarkstyle.style_rc
import sys

from sin_plot.sin_widget import Sin_window

from appear import UI_elemts







class mainwindow(QMainWindow):
    def __init__(self,app):
        super().__init__()

        self.app = app

        self.ui = UI_elemts()
        self.ui.Setup_UI(self)


        self.new_window = Sin_window()
        self.new_window.setWindowTitle("Huxly Model")
        self.ui.mdiArea.addSubWindow(self.new_window)

        self.new_window1 = QDialog()
        self.new_window1.setWindowTitle("Neural Network")
        self.ui.mdiArea.addSubWindow(self.new_window1)

        #self.new_windowF = Sin_window()
        #self.new_windowF.setWindowTitle("Futz")
        #self.ui.mdiArea.addSubWindow(self.new_windowF)

        self.ui.dynamic_tab.Fithz.triggered.connect(self.test)


    def test(self):
        #self.app.exit()
        self.new_windowF = Sin_window()
        self.new_windowF.setWindowTitle("Futz")
        self.ui.mdiArea.addSubWindow(self.new_windowF)
        self.new_windowF.exec_()



def start():
    app = QApplication([])
    main = mainwindow(app)
    #main.test()
    main.show()
    app.exec_()

start()
