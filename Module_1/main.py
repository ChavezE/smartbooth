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

import pyrebase

import threading 

# Module 2
sys.path.insert(0, '../Module_2')
import dummy_endpoint

config = {
    "apiKey": "AIzaSyAq9xA-sjwtOmye3j_xzURxacHP6qknLOg",
    "authDomain": "photoboot-e2b33.firebaseapp.com",
    "databaseURL": "https://photoboot-e2b33.firebaseio.com",
    "storageBucket": "photoboot-e2b33.appspot.com",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def userExists(rfid):
	try:
		dumy = db.child("Students").order_by_child("RFID").equal_to(rfid).get().val()
		return True
	except IndexError:
		return False

class Main(QMainWindow):
	def __init__(self):
		super(Main, self).__init__()
		loadUi("../UserExperience/views/mainwindow.ui", self)

		movie = QMovie ("../UserExperience/img/welcome.gif")
		self.rfid = 0
		self.label.setMovie(movie)
		movie.start()

	def scanRfid(self):
		print("scan")
		self.rfid, text = scanForRDIF()

		if (not(userExists(self.rfid))):
			register = registerWindow(self)
			register.exec_()
		else:
			Module_2 = dummy_endpoint.endpoint()
			print(Module_2)


app = QApplication(sys.argv)
main = Main()
main.show()
threading.Thread(target=main.scanRfid).start()


sys.exit(app.exec_())


#py main.py