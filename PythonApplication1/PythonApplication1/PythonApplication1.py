import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QImage("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
            QPoint( 70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),
        ])

        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        p.drawPolygon([
            QPoint(50, 200), QPoint(150, 200), QPoint(100, 400),
        ])

        p.drawImage(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        'self.rabbit = QImage("images/rabbit.png")'

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(255, 204, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)
        p.end()

class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        'self.rabbit = QImage("images/rabbit.png")'

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(127, 84, 23))
        p.drawPolygon([
        QPoint(50, 200), QPoint(150, 200), QPoint(100, 400),
        ])


        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(235, 119, 166))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        p.end()


class Simple_drawing_window3(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing3")
        'self.rabbit = QImage("images/rabbit.png")'

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(19, 161, 203))
        p.drawPolygon([
        QPoint(150, 0), QPoint(50, 200), QPoint(150, 200), QPoint(200, 150), QPoint(100, 400),
        ])


        p.end()

def main():
    app = QApplication(sys.argv)

    w1 = Simple_drawing_window1()
    w1.show()

    w2 = Simple_drawing_window2()
    w2.show()

    w3 = Simple_drawing_window3()
    w3.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())