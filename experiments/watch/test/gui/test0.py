"""
test PyQt5
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow
import sys



def window():
	app = QApplication(sys.argv)
	win = QMainWindow()
	win.setGeometry(700,400,300,300)
	win.setWindowTitle("My App")

	label = QtWidgets.QLabel(win) #where it is gonna shown
	label.setText("label text")
	label.move(130,140)


	win.show()
	sys.exit(app.exec_())


window()