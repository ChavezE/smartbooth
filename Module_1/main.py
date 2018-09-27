#main.py --pyqt5
#mainwindow.ui
#pushbutton
#text1

import sys

from PyQt5.QtCore import (pyqtSlot, pyqtSignal)
from PyQt5.QtWidgets import QApplication, QMainWindow
from registerWindow import registerWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QMovie
from cardReader import scanForRDIF

import pyrebase

import threading 

# Module 2
sys.path.insert(0, '../Module_2')
from dummy_endpoint import PhotoMain

config = {
	"apiKey": "AIzaSyAq9xA-sjwtOmye3j_xzURxacHP6qknLOg",
	"authDomain": "photoboot-e2b33.firebaseapp.com",
	"databaseURL": "https://photoboot-e2b33.firebaseio.com",
	"storageBucket": "photoboot-e2b33.appspot.com",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def userExists(rfid):
	mat = 0
	students = db.child("Students").order_by_child("RFID").equal_to(int(rfid)).get()
	try:
		students_values = students.val()

		for i in students_values:
			# this retrieves the key
			mat = i

		print ("User does exists")
		return True, mat

	except IndexError:
		print ("User does not exists")
		return False, mat

class Main(QMainWindow):

	scanRDIFE = pyqtSignal(str, name="scanRDIFE")

	def __init__(self):
		super(Main, self).__init__()
		loadUi("../UserExperience/views/mainwindow.ui", self)

		movie = QMovie ("../UserExperience/img/welcome.gif")
		self.rfid = 0
		self.label.setMovie(movie)
		movie.start()
		self.scanRDIFE.connect(self.onSuccessRead)

	@pyqtSlot(str)
	def onSuccessRead(self, id):
		print(id)
		check, mat = userExists(id)
		if (not(check)):
			register = registerWindow(self)
			register.exec_()
		else:
			module2 = PhotoMain(self, mat)
			module2.exec_()

	def scanRfid(self):
		print("scan")
		self.rfid, text = scanForRDIF()
		print("readed")
		self.scanRDIFE.emit(str(self.rfid))
		print("emited")


		


app = QApplication(sys.argv)
main = Main()
main.show()

threading.Thread(target=main.scanRfid).start()

sys.exit(app.exec_())


#py main.py