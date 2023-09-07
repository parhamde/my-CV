from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyQt5.QtCore import pyqtSignal
import sys

def clicked():
    print("clicked")
    
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500, 500, 500, 500)
    win.setWindowTitle("first")
    
    
    label = QtWidgets.QLabel(win)
    label.setText("travel")
    label.move(50,50)
    
    
    b1 = QtWidgets.QPushButton(win)
    b1.setText("1")
    b1.setStyleSheet("background-color: yellow; color:aqua;")
    b1.setFixedSize(40,30)
    b1.clicked.connect(clicked)
    b1.move(405,10)
    
    b2 = QtWidgets.QPushButton(win)
    b2.setText("2")
    b2.setFixedSize(40,30)
    b2.move(360,10)

    b3 = QtWidgets.QPushButton(win)
    b3.setText("3")
    b3.move(380,40)

    b4 = QtWidgets.QPushButton(win)
    b4.setText("4")
    b4.move(360,40)

    
    
    win.show()
    sys.exit(app.exec_())
    
window()