import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
 
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.paint = False
        self.pushButton.clicked.connect(self.draw_circle)
 
    def draw_circle(self):
        self.paint = True
        self.update()
 
    def paintEvent(self, event):
        if self.paint:
            qp = QPainter(self)
            qp.begin(self)
            self.draw_random_circle(qp)
            qp.end()
 
    def draw_random_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        qp.drawEllipse(x, y, diameter, diameter)
        self.paint = False
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
