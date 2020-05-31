import sys
import random
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4,dpi=100):
        fig = Figure(figsize=(width, height), dpi = dpi )
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.canvas = MplCanvas(self)
        self.setCentralWidget(self.canvas)


        n_data  =50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0,10) for i in range(n_data)]


        self._plot_ref = None
        self.update_plot()
        self.show()


        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        self.ydata = self.ydata[1:] + [random.randint(0,10)]

        if self._plot_ref is None:
            plot_refs = self.canvas.axes.plot(self.xdata, self.ydata, 'g')
            self._plot_ref = plot_refs[0]

        else:
            self._plot_ref.set_ydata(self.ydata)

        self.canvas.draw()



app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
