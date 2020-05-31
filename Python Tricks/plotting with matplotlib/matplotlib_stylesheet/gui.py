from PyQt5.QtWidgets import QApplication, QMainWindow
from main2 import Ui_MainWindow
import numpy as np


class My_App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_canv1_1.clicked.connect(self.plotsin)


        t = np.arange(0,10,0.1)
        self.ui.canvas_widget1.canvas.axes1.plot(t,np.sin(t), label = 'sin')

        self.ui.canvas_widget1.canvas.axes1.plot(t, np.cos(t))


    def plotsin(self):
        t = np.arange(0,10,0.1)
        self.ui.canvas_widget1.canvas.axes1.clear()
        self.ui.canvas_widget1.canvas.axes1.plot(t,np.cos(t+2))
        #self.ui.canvas1.axes1.text(0.5,0.5,'Amir Hossien')
        self.ui.canvas_widget1.canvas.draw()




if __name__ == "__main__":
    app = QApplication([])
    window = My_App()
    window.show()
    app.exec_()
