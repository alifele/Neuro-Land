from PyQt5 import QtWidgets
from Tabs.Dynamical_systems.neuron_models.Huxly.Implementation.main import Ui_Dialog


class huxly(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        self.ui  = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.verticalSlider.valueChanged.connect(self.test)
        self.ui.lineEdit.textEdited.connect(self.lineEditChanged)

        self.ui.verticalSlider.setMaximum(30)
        self.ui.verticalSlider.setMinimum(-30)
        self.ui.verticalSlider.setSingleStep(0.1)

        self.ui.widget.canvas.line5.set_xdata([1,2,3])
        self.ui.widget.canvas.line5.set_ydata([2,3,1])
        self.ui.widget.canvas.draw()
        self.ui.widget.canvas.ax5.set_ylim(0,10)
        self.ui.widget.canvas.ax5.set_xlim(0,10)


        self.ui.lineEdit.setText(str(self.ui.verticalSlider.value()))


    def test(self, value):
        self.ui.lineEdit.setText(str(value))

    def lineEditChanged(self, value):
        self.ui.verticalSlider.setValue(float(value))





class huxly_dialog(huxly):
    def __init__(self, ui):
        super().__init__()
        self.setWindowTitle('Sin plotter')
        ui.mdiArea.addSubWindow(self)
        self.exec_()


if __name__ == '__main__':
    from main import Ui_Dialog
    app = QtWidgets.QApplication([])
    window = huxly()
    window.show()
    app.exec_()
