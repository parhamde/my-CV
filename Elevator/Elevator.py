
"""IMPORT LIBRARY PYQT5"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyQt5.QtCore import pyqtSignal
import sys
"""END IMPORT LIBRARY"""

# class page - constructor -> label (seld.label = label) -> def clicked : label.
""" START WINDOW"""    
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500, 500, 500, 500)
    win.setWindowTitle("Elevator")
    
    # page = Page(label)
    label = QtWidgets.QLabel(win)
    label.setText("travel")
    label.move(180,10)




    """START BUTTON""" 

    p1 = QtWidgets.QPushButton(win)
    p1.setText("p")
    p1.setStyleSheet("background-color: black; color:aqua; border-radius:10px;")
    p1.setFixedSize(40,30)
    p = lambda: label.move(180,10)
    p1.clicked.connect(p)
    p1.move(381,5)


    b1 = QtWidgets.QPushButton(win)
    b1.setText("1")
    b1.setStyleSheet("background-color: black; color:aqua; border-radius:10px;")
    b1.setFixedSize(40,30)
    clicked = lambda: label.move(180,50)
    b1.clicked.connect(clicked)
    b1.move(405,40)
    
    b2 = QtWidgets.QPushButton(win)
    b2.setText("2")
    b2.setStyleSheet("background-color: black; color:aqua; border-radius:10px;")
    b2.setFixedSize(40,30)
    clicked2 = lambda: label.move(180,100)
    b2.clicked.connect(clicked2)
    b2.move(360,40)

    b3 = QtWidgets.QPushButton(win)
    b3.setText("3")
    b3.setStyleSheet("background-color: black; color:aqua; border-radius:10px;")
    b3.setFixedSize(40,30)
    clicked3 = lambda: label.move(180,150)
    b3.clicked.connect(clicked3)
    b3.move(405,80)

    b4 = QtWidgets.QPushButton(win)
    b4.setStyleSheet("background-color: black; color:aqua; border-radius:10px;")
    b4.setFixedSize(40,30)
    b4.setText("4")
    clicked4 = lambda: label.move(180,200)
    b4.clicked.connect(clicked4)
    b4.move(360,80)

    b5 = QtWidgets.QPushButton(win)
    b5.setText("5")
    b5.setStyleSheet("background-color: black; color:aqua; border-radius:10px;")
    b5.setFixedSize(40,30)
    clicked5 = lambda: label.move(180,250)
    b5.clicked.connect(clicked5)
    b5.move(405,120)

    b6 = QtWidgets.QPushButton(win)
    b6.setStyleSheet("background-color: black; color:aqua; border-radius:10px;")
    b6.setFixedSize(40,30)
    b6.setText("6")
    clicked6 = lambda: label.move(180,300)
    b6.clicked.connect(clicked6)
    b6.move(360,120)
    
    


    
    
    win.show()
    sys.exit(app.exec_())
    
window()
