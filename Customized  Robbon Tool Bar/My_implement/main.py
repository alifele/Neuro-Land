from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
import PyQt5.QtWidgets as MYQT
from PyQt5.QtGui import QKeySequence as QKSec
from GUI.RibbonButton import RibbonButton
from GUI.Icons import get_icon
from GUI.RibbonTextbox import RibbonTextbox
from GUI.RibbonWidget import *
import qdarkstyle
from PyQt5.QtGui import QIcon



class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800,600)
        self.setWindowTitle("My Application")

        layout = MYQT.QVBoxLayout()

        push = MYQT.QPushButton('press me')
        layout.addWidget(push)

        lineedit = MYQT.QLineEdit("Hello there ")
        layout.addWidget(lineedit)

        hwidget = MYQT.QWidget()
        hlayout = MYQT.QHBoxLayout()
        push1 = MYQT.QPushButton("hey")
        push2 = MYQT.QPushButton('Mey')
        hlayout.addWidget(push1)
        hlayout.addWidget(push2)
        hwidget.setLayout(hlayout)
        layout.addWidget(hwidget)


        analwidget = MYQT.QWidget()
        analwidgetlayout = MYQT.QHBoxLayout()
        for i in range(3):
            anal = MYQT.QDial()
            analwidgetlayout.addWidget(anal)
        analwidget.setLayout(analwidgetlayout)
        layout.addWidget(analwidget)


        widget = MYQT.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


        #---------- Actions ----------------
        self._open_action = MYQT.QAction(QIcon('icons/about.png'),"Open", self)
        self._zoom_action = MYQT.QAction(QIcon('icons/zoom.png'), "Zoom", self)
        self._brain_action = MYQT.QAction(QIcon('icons/icon.png'),"Brain", self)
        self.pres = MYQT.QAction(QIcon('icons/icon.png'),'Plot', self)

        self._ribbon = RibbonWidget(self)
        self.addToolBar(self._ribbon)

        home_tab = self._ribbon.add_ribbon_tab("edit")
        file_pane = home_tab.add_ribbon_pane("File")
        file_pane.add_ribbon_widget(RibbonButton(self, self._open_action, True))
        file_pane.add_ribbon_widget(RibbonButton(self, self._zoom_action, True))
        zoom_pane = home_tab.add_ribbon_pane("Zoom")
        zoom_pane.add_ribbon_widget(RibbonButton(self, self._brain_action, True))

        plot_tab = self._ribbon.add_ribbon_tab("Plot")
        plot_pane = plot_tab.add_ribbon_pane("Plot Uitls")
        plot_pane.add_ribbon_widget(RibbonButton(self, self.pres, True))




        Plotts_tab = self._ribbon.add_ribbon_tab("Plotter")







app = QApplication([])
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
# or in new API
app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
main = mainwindow()
main.show()


app.exec_()
