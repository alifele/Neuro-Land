from PyQt5 import QtWidgets
from imports import *

class Dynamical_Systems_tab:
    def __init__(self, ribbon, mainwindow):
        dynamic = ribbon.add_ribbon_tab("Neurons")
        ### Actions ###

        self.huxly_model = QtWidgets.QAction(QIcon('icons/icon.png'),"Huxly", mainwindow)
        self.Fithz = QtWidgets.QAction(QIcon('icons/icon.png'),"Fithz", mainwindow)
        self.custom = QtWidgets.QAction(QIcon('icons/icon.png'),"custom", mainwindow)
        self._brain_action = QtWidgets.QAction(QIcon('icons/icon.png'),"Brain", mainwindow)

        file_pane = dynamic.add_ribbon_pane("Neuronal models")
        file_pane.add_ribbon_widget(RibbonButton(mainwindow, self.huxly_model, True))
        file_pane.add_ribbon_widget(RibbonButton(mainwindow, self.Fithz, True))
        file_pane.add_ribbon_widget(RibbonButton(mainwindow, self.custom, True))

        zoom_pane = dynamic.add_ribbon_pane("Synapses")
        zoom_pane.add_ribbon_widget(RibbonButton(mainwindow, self._brain_action, True))


class Neural_Networks_tab:
    def __init__(self, ribbon, mainwindow):

        neural = ribbon.add_ribbon_tab("Neural Networks and Artificial Intelligence")
        ### Actions ###
        self.model = QtWidgets.QAction(QIcon('icons/icon.png'),"perceptro", mainwindow)
        self.multi = QtWidgets.QAction(QIcon('icons/icon.png'),"Multi", mainwindow)
        self.hop = QtWidgets.QAction(QIcon('icons/icon.png'),"Hoppfild", mainwindow)
        self.heb = QtWidgets.QAction(QIcon('icons/icon.png'),"Hebb", mainwindow)
        self.som = QtWidgets.QAction(QIcon('icons/icon.png'),"self orga. map", mainwindow)


        plot_pane = neural.add_ribbon_pane("models")
        plot_pane.add_ribbon_widget(RibbonButton(mainwindow, self.model, True))
        plot_pane.add_ribbon_widget(RibbonButton(mainwindow, self.multi, True))
        plot_pane = neural.add_ribbon_pane("learning")
        plot_pane.add_ribbon_widget(RibbonButton(mainwindow, self.hop, True))
        plot_pane.add_ribbon_widget(RibbonButton(mainwindow, self.heb, True))
        plot_pane.add_ribbon_widget(RibbonButton(mainwindow, self.som, True))




class Artificial_Intelligence_tab:
    def __init__(self, ribbon, mainwindow):


        self.class_ = QtWidgets.QAction(QIcon('icons/icon.png'),"classifi", mainwindow)
        self.reg = QtWidgets.QAction(QIcon('icons/icon.png'),"Regress", mainwindow)
        self.gan = QtWidgets.QAction(QIcon('icons/icon.png'),"GAN", mainwindow)
        self.cnn = QtWidgets.QAction(QIcon('icons/icon.png'),"CNN", mainwindow)
        self.rnn = QtWidgets.QAction(QIcon('icons/icon.png'),"RNN", mainwindow)
        self.maze = QtWidgets.QAction(QIcon('icons/icon.png'),"maze", mainwindow)
        self.snake = QtWidgets.QAction(QIcon('icons/icon.png'),"snake", mainwindow)
        self.pingpong = QtWidgets.QAction(QIcon('icons/icon.png'),"pingpong", mainwindow)
        self.genet = QtWidgets.QAction(QIcon('icons/icon.png'),"toward goal", mainwindow)
        self.mona = QtWidgets.QAction(QIcon('icons/icon.png'),"Monaliza", mainwindow)
        self.car = QtWidgets.QAction(QIcon('icons/icon.png'),"car", mainwindow)
        self.cond = QtWidgets.QAction(QIcon('icons/icon.png'),"Conditioning", mainwindow)


        AI = ribbon.add_ribbon_tab("Metaheuristics")
        Ann = AI.add_ribbon_pane("ANN")
        Ann.add_ribbon_widget(RibbonButton(mainwindow, self.class_, True))
        Ann.add_ribbon_widget(RibbonButton(mainwindow, self.reg, True))
        Ann.add_ribbon_widget(RibbonButton(mainwindow, self.gan, True))
        Ann.add_ribbon_widget(RibbonButton(mainwindow, self.cnn, True))
        Ann.add_ribbon_widget(RibbonButton(mainwindow, self.rnn, True))
        rl = AI.add_ribbon_pane("Rienforcment")
        rl.add_ribbon_widget(RibbonButton(mainwindow, self.maze, True))
        rl.add_ribbon_widget(RibbonButton(mainwindow, self.pingpong, True))
        rl.add_ribbon_widget(RibbonButton(mainwindow, self.snake, True))
        rl.add_ribbon_widget(RibbonButton(mainwindow, self.cond, True))
        gen = AI.add_ribbon_pane("Genetic")
        gen.add_ribbon_widget(RibbonButton(mainwindow, self.genet, True))
        gen.add_ribbon_widget(RibbonButton(mainwindow, self.mona, True))
        gen.add_ribbon_widget(RibbonButton(mainwindow, self.car, True))





class Cellular_Automata_tab:
    def __init__(self, ribbon, mainwindow):

        self._brain_action = QtWidgets.QAction(QIcon('icons/icon.png'),"Brain", mainwindow)


        cell = ribbon.add_ribbon_tab("Signal Processing")
        p1 = cell.add_ribbon_pane('Game of Life')
        p1.add_ribbon_widget(RibbonButton(mainwindow, self._brain_action, True))
        p1.add_ribbon_widget(RibbonButton(mainwindow, self._brain_action, True))
        p1.add_ribbon_widget(RibbonButton(mainwindow, self._brain_action, True))



class Lab_tab:
    def __init__(self, ribbon, mainwindow):

        self._brain_action = QtWidgets.QAction(QIcon('icons/icon.png'),"Brain", mainwindow)


        self.heart_sig = QtWidgets.QAction(QIcon('icons/icon.png'),"heart sig", mainwindow)
        self.brain_sig = QtWidgets.QAction(QIcon('icons/icon.png'),"brain sig", mainwindow)
        self.eyetrack = QtWidgets.QAction(QIcon('icons/icon.png'),"Eye Track", mainwindow)
        self.soundstim = QtWidgets.QAction(QIcon('icons/icon.png'),"Sound", mainwindow)
        self.visstim = QtWidgets.QAction(QIcon('icons/icon.png'),"Visual", mainwindow)
        self.sensestim = QtWidgets.QAction(QIcon('icons/icon.png'),"Sensial", mainwindow)
        self.odorstim = QtWidgets.QAction(QIcon('icons/icon.png'),"Odor", mainwindow)
        self.tastestim = QtWidgets.QAction(QIcon('icons/icon.png'),"Taste", mainwindow)

        lab = ribbon.add_ribbon_tab("Laboratory")
        body = lab.add_ribbon_pane("Body Signals")
        body.add_ribbon_widget(RibbonButton(mainwindow, self.heart_sig, True))
        body.add_ribbon_widget(RibbonButton(mainwindow, self.brain_sig, True))
        body.add_ribbon_widget(RibbonButton(mainwindow, self.eyetrack, True))
        stimulus = lab.add_ribbon_pane("Stimulus")
        stimulus.add_ribbon_widget(RibbonButton(mainwindow, self.soundstim, True))
        stimulus.add_ribbon_widget(RibbonButton(mainwindow, self.visstim, True))
        stimulus.add_ribbon_widget(RibbonButton(mainwindow, self.sensestim, True))
        stimulus.add_ribbon_widget(RibbonButton(mainwindow, self.odorstim, True))
        stimulus.add_ribbon_widget(RibbonButton(mainwindow, self.tastestim, True))
