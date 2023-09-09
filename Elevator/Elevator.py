
"""IMPORT LIBRARY PYQT5"""
from backend import*
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyQt5.QtCore import pyqtSignal
import sys
"""END IMPORT LIBRARY"""


""" START WINDOW"""    
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500, 500, 500, 500)
    win.setWindowTitle("Elevator")
    
    
    label = QtWidgets.QLabel(win)
    label.setText("travel")
    label.move(50,50)


    """START BUTTON""" 

    
    b1 = QtWidgets.QPushButton(win)
    b1.setText("1")
    b1.setStyleSheet("background-color: black; color:aqua; border-radius:10px;")
    b1.setFixedSize(40,30)
    b1.clicked.connect(clicked)
    b1.move(405,40)
    
    b2 = QtWidgets.QPushButton(win)
    b2.setText("2")
    b2.setStyleSheet("background-color: black; color:aqua; border-radius:10px;")
    b2.setFixedSize(40,30)
    b2.clicked.connect(clicked2)
    b2.move(360,40)

    b3 = QtWidgets.QPushButton(win)
    b3.setText("3")
    b3.setStyleSheet("background-color: black; color:aqua; border-radius:10px;")
    b3.setFixedSize(40,30)
    b3.clicked.connect(clicked3)
    b3.move(405,80)

    b4 = QtWidgets.QPushButton(win)
    b4.setStyleSheet("background-color: black; color:aqua; border-radius:10px;")
    b4.setFixedSize(40,30)
    b4.setText("4")
    b4.clicked.connect(clicked4)
    b4.move(360,80)

    b5 = QtWidgets.QPushButton(win)
    b5.setText("5")
    b5.setStyleSheet("background-color: black; color:aqua; border-radius:10px;")
    b5.setFixedSize(40,30)
    b5.clicked.connect(cilcked5)
    b5.move(405,120)

    b6 = QtWidgets.QPushButton(win)
    b6.setStyleSheet("background-color: black; color:aqua; border-radius:10px;")
    b6.setFixedSize(40,30)
    b6.setText("6")
    b6.clicked.connect(cilcked6)
    b6.move(360,120)
    
    


    
    
    win.show()
    sys.exit(app.exec_())
    
window()
