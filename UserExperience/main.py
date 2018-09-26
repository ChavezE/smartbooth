#main.py --pyqt5
#mainwindow.ui
#pushbutton
#text1

import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
from registerWindow import registerWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QMovie
from cardReader import scanForRDIF

import threading 



class Main(QMainWindow):
	def __init__(self):
		super(Main, self).__init__()
		loadUi("mainwindow.ui", self)

		movie = QMovie ("welcome.gif")
		
		self.label.setMovie(movie)
		movie.start()

	def scanRfid(self):
		print("scan")
		rf, self.rdif = scanForRDIF()
		register = registerWindow(self)
		register.exec_()


app = QApplication(sys.argv)
main = Main()
main.show()
threading.Thread(target=main.scanRfid).start()
# threading.Thread(target=runReader).start()
# beginProgram()


# main.scanRfid()

sys.exit(app.exec_())


#py main.py