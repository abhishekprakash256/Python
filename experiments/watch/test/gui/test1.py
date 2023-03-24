"""
make the test app
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow
import sys

def clicked():
	print("clicked")



def window():
	app = QApplication(sys.argv)
	win = QMainWindow()  #make the app window 
	win.setGeometry(700,400,300,300)  #set the app location and size
	win.setWindowTitle("My App")

	label = QtWidgets.QLabel(win) #where it is gonna shown
	label.setText("label text")   #make the label text
	label.move(130,140)   #label location 

	b1 = QtWidgets.QPushButton(win)   #button inside the app 
	b1.move(100,100)
	b1.setText("Click me")   #button text
	b1.clicked.connect(clicked)  #mapped to the button


	win.show()
	sys.exit(app.exec_())


window()