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
        self.huxly_model = MYQT.QAction(QIcon('icons/icon.png'),"Huxly", self)
        self.Fithz = MYQT.QAction(QIcon('icons/icon.png'),"Fithz", self)
        self.custom = MYQT.QAction(QIcon('icons/icon.png'),"custom", self)
        self.model = MYQT.QAction(QIcon('icons/icon.png'),"perceptro", self)
        self.multi = MYQT.QAction(QIcon('icons/icon.png'),"Multi", self)
        self.hop = MYQT.QAction(QIcon('icons/icon.png'),"Hoppfild", self)
        self.heb = MYQT.QAction(QIcon('icons/icon.png'),"Hebb", self)
        self.som = MYQT.QAction(QIcon('icons/icon.png'),"self orga. map", self)

        self.class_ = MYQT.QAction(QIcon('icons/icon.png'),"classifi", self)
        self.reg = MYQT.QAction(QIcon('icons/icon.png'),"Regress", self)
        self.gan = MYQT.QAction(QIcon('icons/icon.png'),"GAN", self)
        self.cnn = MYQT.QAction(QIcon('icons/icon.png'),"CNN", self)
        self.rnn = MYQT.QAction(QIcon('icons/icon.png'),"RNN", self)
        self.maze = MYQT.QAction(QIcon('icons/icon.png'),"maze", self)
        self.snake = MYQT.QAction(QIcon('icons/icon.png'),"snake", self)
        self.pingpong = MYQT.QAction(QIcon('icons/icon.png'),"pingpong", self)
        self.genet = MYQT.QAction(QIcon('icons/icon.png'),"toward goal", self)
        self.mona = MYQT.QAction(QIcon('icons/icon.png'),"Monaliza", self)
        self.car = MYQT.QAction(QIcon('icons/icon.png'),"car", self)
        self.heart_sig = MYQT.QAction(QIcon('icons/icon.png'),"heart sig", self)
        self.brain_sig = MYQT.QAction(QIcon('icons/icon.png'),"brain sig", self)
        self.eyetrack = MYQT.QAction(QIcon('icons/icon.png'),"Eye Track", self)
        self.soundstim = MYQT.QAction(QIcon('icons/icon.png'),"Sound", self)
        self.visstim = MYQT.QAction(QIcon('icons/icon.png'),"Visual", self)
        self.sensestim = MYQT.QAction(QIcon('icons/icon.png'),"Sensial", self)
        self.odorstim = MYQT.QAction(QIcon('icons/icon.png'),"Odor", self)
        self.tastestim = MYQT.QAction(QIcon('icons/icon.png'),"Taste", self)











        self.pres = MYQT.QAction(QIcon('icons/icon.png'),'Plot', self)

        self._ribbon = RibbonWidget(self)
        self.addToolBar(self._ribbon)

        dynamic = self._ribbon.add_ribbon_tab("Dynalical System")
        file_pane = dynamic.add_ribbon_pane("Neurons models")
        file_pane.add_ribbon_widget(RibbonButton(self, self.huxly_model, True))
        file_pane.add_ribbon_widget(RibbonButton(self, self.Fithz, True))
        file_pane.add_ribbon_widget(RibbonButton(self, self.custom, True))

        zoom_pane = dynamic.add_ribbon_pane("Synapses")
        zoom_pane.add_ribbon_widget(RibbonButton(self, self._brain_action, True))


        neural = self._ribbon.add_ribbon_tab("Neural Networks")
        plot_pane = neural.add_ribbon_pane("models")
        plot_pane.add_ribbon_widget(RibbonButton(self, self.model, True))
        plot_pane.add_ribbon_widget(RibbonButton(self, self.multi, True))
        plot_pane = neural.add_ribbon_pane("learning")
        plot_pane.add_ribbon_widget(RibbonButton(self, self.hop, True))
        plot_pane.add_ribbon_widget(RibbonButton(self, self.heb, True))
        plot_pane.add_ribbon_widget(RibbonButton(self, self.som, True))






        AI = self._ribbon.add_ribbon_tab("Artificial Intelligence")
        Ann = AI.add_ribbon_pane("ANN")
        Ann.add_ribbon_widget(RibbonButton(self, self.class_, True))
        Ann.add_ribbon_widget(RibbonButton(self, self.reg, True))
        Ann.add_ribbon_widget(RibbonButton(self, self.gan, True))
        Ann.add_ribbon_widget(RibbonButton(self, self.cnn, True))
        Ann.add_ribbon_widget(RibbonButton(self, self.rnn, True))

        rl = AI.add_ribbon_pane("Rienforcment")
        rl.add_ribbon_widget(RibbonButton(self, self.maze, True))
        rl.add_ribbon_widget(RibbonButton(self, self.pingpong, True))
        rl.add_ribbon_widget(RibbonButton(self, self.snake, True))


        gen = AI.add_ribbon_pane("Genetic")
        gen.add_ribbon_widget(RibbonButton(self, self.genet, True))
        gen.add_ribbon_widget(RibbonButton(self, self.mona, True))
        gen.add_ribbon_widget(RibbonButton(self, self.car, True))





        cell = self._ribbon.add_ribbon_tab("Cellular Automata")
        p1 = cell.add_ribbon_pane('Game of Life')
        p1.add_ribbon_widget(RibbonButton(self, self._brain_action, True))
        p1.add_ribbon_widget(RibbonButton(self, self._brain_action, True))
        p1.add_ribbon_widget(RibbonButton(self, self._brain_action, True))


        lab = self._ribbon.add_ribbon_tab("Laboratory")
        body = lab.add_ribbon_pane("Body Signals")
        body.add_ribbon_widget(RibbonButton(self, self.heart_sig, True))
        body.add_ribbon_widget(RibbonButton(self, self.brain_sig, True))
        body.add_ribbon_widget(RibbonButton(self, self.eyetrack, True))
        stimulus = lab.add_ribbon_pane("Stimulus")
        stimulus.add_ribbon_widget(RibbonButton(self, self.soundstim, True))
        stimulus.add_ribbon_widget(RibbonButton(self, self.visstim, True))
        stimulus.add_ribbon_widget(RibbonButton(self, self.sensestim, True))
        stimulus.add_ribbon_widget(RibbonButton(self, self.odorstim, True))
        stimulus.add_ribbon_widget(RibbonButton(self, self.tastestim, True))











app = QApplication([])
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
# or in new API
app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
main = mainwindow()
main.show()


app.exec_()
