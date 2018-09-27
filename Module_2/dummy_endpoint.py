import sys
import cv2
import pyrebase
import os
import time
from PyQt5.QtCore import pyqtSlot, QTimer, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsOpacityEffect, QDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtCore

photo = '/photo.png'

config = {
	"apiKey": "AIzaSyAq9xA-sjwtOmye3j_xzURxacHP6qknLOg",
	"authDomain": "photoboot-e2b33.firebaseapp.com",
	"databaseURL": "https://photoboot-e2b33.firebaseio.com",
	"storageBucket": "photoboot-e2b33.appspot.com",
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
db = firebase.database()
cwd = '/home/pi/Desktop/smartbooth/smartbooth/Module_1'

globalParent = ""

class PhotoMain(QDialog):
	def __init__(self, parent, mat):
		super(PhotoMain, self).__init__()
		self.globalParent = parent
		self.globalParent.hide()
		self.studentID_mat = mat
		self.load_main_layout()

	def load_main_layout(self):
		self.cont = 3

		#Carga main layout
		loadUi("../UserExperience/views/dialog.ui", self)

		#Hace que al correr el código, se despliegue el fondo con la cámara
		self.start_recorder()
		
		#Esconde los componentes de funcionalidades fuera del main
		self.hide_confirm()
		self.hide_countdown()

		#Funcionalidad de botones
		self.newPhotoBtn.clicked.connect(self.take_photo)
		self.logoutBtn.clicked.connect(self.stop_timer)
		self.cancelBtn.clicked.connect(self.delete_photo)
		self.saveBtn.clicked.connect(self.upload_photo)

		#Icono para boton de tomar foto
		rMyIcon = QtGui.QPixmap("../UserExperience/img/new_photo_icon.png");
		self.newPhotoBtn.setIcon(QtGui.QIcon(rMyIcon))
		self.newPhotoBtn.setIconSize(QSize(65, 65))

		op2 = QGraphicsOpacityEffect(self)
		op2.setOpacity(0.7)
		self.newPhotoBtn.setGraphicsEffect(op2)
		self.newPhotoBtn.setAutoFillBackground(True)

		#Icono para boton de logout
		rMyIcon = QtGui.QPixmap("../UserExperience/img/logout_icon.png");
		self.logoutBtn.setIcon(QtGui.QIcon(rMyIcon))
		self.logoutBtn.setIconSize(QSize(50, 50)) 

		op2 = QGraphicsOpacityEffect(self)
		op2.setOpacity(0.7)
		self.logoutBtn.setGraphicsEffect(op2)
		self.logoutBtn.setAutoFillBackground(True)

		op2 = QGraphicsOpacityEffect(self)
		op2.setOpacity(0.7)
		self.cancelBtn.setGraphicsEffect(op2)
		self.cancelBtn.setAutoFillBackground(True)

		op2 = QGraphicsOpacityEffect(self)
		op2.setOpacity(0.7)
		self.saveBtn.setGraphicsEffect(op2)
		self.saveBtn.setAutoFillBackground(True)

	def stop_timer(self):
		self.timer.stop()
		self.load_login_layout()

	def load_login_layout(self):
		self.close()
		self.globalParent.show()
		self.globalParent.initialize_reader()

	def update_frame(self):
		ret, self.image=self.capture.read()
		self.image = cv2.flip(self.image,1)
		self.displayImage(self.image,1)

	def take_photo(self):
		self.start_timer()

	def delete_photo(self):
		self.start_recorder()
		self.show_main()	

	def upload_photo(self):
		mat = self.studentID_mat
		print("estoy en upload_photo")
		photo_name = time.asctime()
		

		# Upload photo in firebase storage
		storage.child("images/" + mat + "/" + photo_name).put(cwd + photo)

		# Get url from  given image firebase storage
		url = storage.child("images/" + mat + "/" + photo_name).get_url(None)

		# Update database with url
		data = {"url":url}
		db.child("Students").child(mat).child("photos").push(data)
		print("voy a start_recorder")
		self.start_recorder()
		self.show_main()

	def start_recorder(self):
		self.capture = cv2.VideoCapture(0)
		self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
		self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

		self.timer=QTimer(self)
		self.timer.timeout.connect(self.update_frame)
		self.timer.start(1)

	def show_main(self):
		self.cont = 3
		self.countdownLabel.setText("3")
		self.timer.stop()
		self.start_recorder()
		self.newPhotoBtn.show()
		self.logoutBtn.show()
		self.hide_confirm()
	
	def hide_main(self):
		self.newPhotoBtn.hide()
		self.logoutBtn.hide()

	def show_confirm(self):
		self.cancelBtn.show()
		self.saveBtn.show()
		self.hide_countdown()

	def hide_confirm(self):
		self.cancelBtn.hide()
		self.saveBtn.hide()

	def show_countdown(self):
		self.countdownLabel.show()
		self.hide_main()

	def hide_countdown(self):
		self.countdownLabel.hide()

	def update_label(self):
		if(self.cont == -1):
			self.countdown.stop()
			self.timer.stop()
			cv2.imwrite('photo.png', self.image)
			self.show_confirm()
		
		else:
			print('tick')
			self.countdownLabel.setText(str(self.cont))
			self.cont -= 1;

	def start_timer(self):
		self.show_countdown()
		self.countdown = QtCore.QTimer()
		self.countdown.timeout.connect(self.update_label)
		self.countdown.start(1000)  # every 10,000 milliseconds

	def displayImage(self, img, window=1):
		qformat=QImage.Format_Indexed8
		if len(img.shape) == 3:
			if img.shape[2] == 4:
				qformat=QImage.Format_RGBABB88
			else:
				qformat=QImage.Format_RGB888

		outImage=QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
		outImage=outImage.rgbSwapped()

		if window==1:
			self.imgLabel.setPixmap(QPixmap.fromImage(outImage))
			self.imgLabel.setScaledContents(True)

#app = QApplication(sys.argv)
#photoMain = PhotoMain()
#photoMain.show()
#sys.exit(app.exec())
