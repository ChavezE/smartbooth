from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from validation import validateMatricule, validateCareer
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
		self.RFID = parent.rdif
		self.registerButton.clicked.connect(self.registerUsers)
		parent.hide()

	@pyqtSlot()
	def registerUsers(self):
		print("register")
		print(self.RFID)
		self.mat_error.setText("")
		self.car_error.setText("")
		print(self.studentId.text())
		print(self.carrera.text())
		mat = self.studentId.text()
		career = self.carrera.text()
		print("Matricula: ",validateMatricule(mat))
		print("Carrera: ",validateCareer(career))
		validateMat = validateMatricule(mat)
		validateCar = validateCareer(career)
		if(validateMat and validateCar):
			data = {"RFID": self.RFID, "maatricula": mat, "carrera": career}
			db.child("Students").push(data)
			#to do: mandar a captura
		else:
			if(not(validateMat)):
				self.mat_error.setText("Matrícula inválida")
			if(not(validateCar)):
				self.car_error.setText("Carrera inválida")
		
