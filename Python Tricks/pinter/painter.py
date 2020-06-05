import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
import numpy as np
import matplotlib.pyplot as plt
import imageio


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel()
        self.canvas = QtGui.QPixmap(800, 600)
        self.label.setPixmap(self.canvas)
        self.label.pixmap().fill(QtGui.QColor('black'))
        layout.addWidget(self.label)


        butt = QtWidgets.QPushButton('Save and Show')
        layout.addWidget(butt)


        widget = QtWidgets.QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.last_x, self.last_y = None, None

        butt.clicked.connect(self.save)

    def save(self):
        #bytes = QtCore.QByteArray()
        #buffer = QtCore.QBuffer()
        #buffer.open(QtCore.QIODevice.WriteOnly)
        #self.canvas.save(buffer,'PNG')
        pixmap = self.label.pixmap()
        pixmap.save('ppp.png')
        image = imageio.imread('ppp.png')
        #b = image.bits()
        #b.setsize(300*400)
        #arr = np.frombuffer(b, np.uint8).reshape((300,400))
        #state = self.canvas.save('Alii.jpg')
        #pixmap = self.label.pixmap()
        #pixmap.save('Ali.png')
        plt.imshow(image)
        plt.show()

        #self.canvas.save('Ali','PNG')
        #mat = O

    def mouseMoveEvent(self, e):
        if self.last_x is None: # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return # Ignore the first time.

        pen = QtGui.QPen()
        pen.setWidth(2)
        pen.setColor(QtGui.QColor('gray'))


        painter = QtGui.QPainter(self.label.pixmap())
        painter.setPen(pen)
        #painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        #painter.drawPoint(e.x(), e.y())
        x = e.x()
        y = e.y()
        painter.drawRect(x,y,30,30)
        painter.end()
        self.update()

        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
