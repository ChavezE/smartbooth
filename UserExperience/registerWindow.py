from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
import sys
import pyrebase

config = {
    "apiKey": "AIzaSyAq9xA-sjwtOmye3j_xzURxacHP6qknLOg",
    "authDomain": "photoboot-e2b33.firebaseapp.com",
    "databaseURL": "https://photoboot-e2b33.firebaseio.com",
    "storageBucket": "photoboot-e2b33.appspot.com",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

class registerWindow(QDialog):
	def __init__(self, parent):
		super(registerWindow, self).__init__()
		loadUi("register.ui", self)
		self.registerButton.clicked.connect(self.registerUsers)
		parent.hide()

	@pyqtSlot()
	def registerUsers(self):
		print(self.studentId.text())
		print(self.carrera.text())
		data = {"RFID": "00000000", "matricula": self.studentId.text(), "carrera": self.carrera.text()}
		db.child("Students").push(data)
		
