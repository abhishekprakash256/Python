"""
using the main window
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow
import sys


class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow,self).__init__()
		self.setGeometry(700,400,300,300)  #set the app location and size
		self.setWindowTitle("My App")
		self.initUI()

	def initUI(self):
		self.label = QtWidgets.QLabel(self) #where it is gonna shown
		self.label.setText("label text")   #make the label text
		self.label.move(130,140)   #label location 

		self.b1 = QtWidgets.QPushButton(self)   #button inside the app 
		self.b1.move(100,100)
		self.b1.setText("Click me")   #button text
		self.b1.clicked.connect(self.clicked)  #mapped to the button
	
	def clicked(self):
		self.label.setText("button pressed")
		self.update()

	def update(self):
		self.label.adjustSize()


def window():
	app = QApplication(sys.argv)
	win = MyWindow()
	win.show()
	sys.exit(app.exec_())

window()