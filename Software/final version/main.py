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

from Tabs.Dynamical_systems.neuron_models.Huxly.Implementation.gui import huxly_dialog

from appear import UI_elemts





class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_elemts()
        self.ui.Setup_UI(self)

        self.init_signals()





    def init_signals(self):
        self.ui.dynamic_tab.huxly_model.triggered.connect(self.test)


    def test(self):
        self.new_window1 = huxly_dialog(self.ui)





def start():
    app = QApplication([])
    main = mainwindow()
    #main.test()
    main.show()
    sys.exit(app.exec_())

start()
