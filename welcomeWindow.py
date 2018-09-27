#main.py --pyqt5
#mainwindow.ui
#pushbutton
#text1

import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
from secondWindow import secondWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QMovie

class Main(QMainWindow):
	def __init__(self):
		super(Main, self).__init__()
		loadUi("mainwindow.ui", self)
		self.pushButton.clicked.connect(self.on_button_click)
		
		movie = QMovie ("welcome.gif")
		
		self.label.setMovie(movie)
		movie.start()
		

	def on_button_click(self):
	#	self.label.setText("Hola")
		second = secondWindow(self)
		second.exec_()

app = QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())


#py main.py