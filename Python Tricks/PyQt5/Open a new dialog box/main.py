from PyQt5 import QtWidgets as Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog


class new_dialog(QDialog):
    def __init__(self):
        super().__init__()

        label = Qt.QLabel(self)
        label.setText('This is the new dilog!')

        #self.setCentralWidget(label)




class my_app(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = Qt.QVBoxLayout()


        push = Qt.QPushButton('press me!')
        layout.addWidget(push)

        widget = Qt.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


        push.clicked.connect(self.open_new_dialog)


    def open_new_dialog(self):
        new_dial = new_dialog()

        new_dial.exec_()






app = QApplication([])
my_app = my_app()
my_app.show()

app.exec_()
