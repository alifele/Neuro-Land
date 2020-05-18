from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from main import *
from dialog import *
import dialog2
import sys


class new_dialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

class new_dialog2(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = dialog2.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.show_name)
    def show_name(self):

        text = self.ui.lineEdit.text()
        self.ui.label_2.setText('Your name is ' + text)
class my_app(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.open_dialog)
        self.ui.pushButton.clicked.connect(self.open_dialog2)

    def open_dialog(self):
        new_dlg = new_dialog()
        new_dlg.exec_()

    def open_dialog2(self):
        new_dlg = new_dialog2()
        new_dlg.exec_()








if __name__ == "__main__":


    app = QApplication(sys.argv)
    window = my_app()
    window.show()
    sys.exit(app.exec_())
