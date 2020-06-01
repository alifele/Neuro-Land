from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import QKeySequence as QKSec
from GUI.RibbonButton import RibbonButton
from GUI.Icons import get_icon
from GUI.RibbonTextbox import RibbonTextbox
from GUI.RibbonWidget import *
import qdarkstyle
from PyQt5.QtGui import QIcon
import ribbon_actions
import qdarkstyle.style_rc
from  plotter.gui import sin_window

f = open("qdarkstyle/style.qss")
style = f.read()
f.close()


class Mdi_Area(QtWidgets.QMdiArea):
    def __init__(self):
        super().__init__()
        self.setViewMode(QtWidgets.QMdiArea.TabbedView)
        self.setTabsClosable(True)
        self.setTabsMovable(True)


class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800,600)
        self.setWindowTitle("My Application")
        self.setStyleSheet(style)

        layout = QtWidgets.QVBoxLayout()

        self.mdiArea = Mdi_Area()
        layout.addWidget(self.mdiArea)


        self.new_window = sin_window()
        self.new_window.setWindowTitle("Huxly Model")
        self.mdiArea.addSubWindow(self.new_window)

        self.new_window1 = QtWidgets.QWidget()
        self.new_window1.setWindowTitle("Neural Network")
        self.mdiArea.addSubWindow(self.new_window1)



        self._ribbon = RibbonWidget(self)
        self.addToolBar(self._ribbon)


        self.dynamic_tab = ribbon_actions.Dynamical_Systems_tab(self._ribbon, self)
        self.neural_networks_tab = ribbon_actions.Neural_Networks_tab(self._ribbon, self)
        self.artificial_intelligence_tab = ribbon_actions.Artificial_Intelligence_tab(self._ribbon, self)
        self.cellular_automata_tab = ribbon_actions.Cellular_Automata_tab(self._ribbon, self)
        self.lab_tab = ribbon_actions.Lab_tab(self._ribbon, self)


        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)










app = QApplication([])
#app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
# or in new API
#app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
main = mainwindow()
main.show()


app.exec_()
