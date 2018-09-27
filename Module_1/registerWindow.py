from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from validation import validateMatricule, validateCareer
import sys
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

class registerWindow(QDialog):
	def __init__(self, parent):
		super(registerWindow, self).__init__()
		loadUi("../UserExperience/views/register.ui", self)
		self.globalParent = parent
		self.RFID = parent.rfid
		print(parent.rfid)
		self.registerButton.clicked.connect(self.registerUsers)
		parent.hide()

	def initialize_reader(self):
		self.globalParent.show()
		threading.Thread(target=self.globalParent.scanRfid).start()

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
		
		# Call validation
		validateMat = validateMatricule(mat)
		validateCar = validateCareer(career)
		if(validateMat and validateCar):
			data = {"RFID": self.RFID,  "carrera": career, "matricula": mat}
			
			db.child("Students").child(mat).set(data)

			# Call module 2 after registration
			print (self.studentId)
			module2 = PhotoMain(self, mat)
			module2.exec_()
		else:
			if(not(validateMat)):
				self.mat_error.setText("Matrícula inválida")
			if(not(validateCar)):
				self.car_error.setText("Carrera inválida")
		
