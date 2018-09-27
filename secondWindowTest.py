from PyQt5.QtWidgets import QDialog, QgroupBox
from PyQt5.uic import loadUi

class secondWindow(QDialog):
	def __init__(self, parent):
		super(secondWindow, self).__init__()
		loadUi("dialog.ui", self)
		#self.pushButton.clicked.connect(self.on_button_click)
		parent.hide()
		self.config = {
        "apiKey": "AIzaSyAq9xA-sjwtOmye3j_xzURxacHP6qknLOg",
        "authDomain": "photoboot-e2b33.firebaseapp.com",
        "databaseURL": "https://photoboot-e2b33.firebaseio.com",
        #"projectId": "photoboot-e2b33",
        "storageBucket": "photoboot-e2b33.appspot.com",
        #"messagingSenderId": "193395117022"
        }

        self.firebase = pyrebase.initialize_app(self.config)
        self.db = self.firebase.database()

		self.createFormGroupBox()
		self.guardar.clicked.connect(self.on_button_click)

	def createFormGroupBox(self):

	def on_button_click(self):
		
	
	#def on_button_click(self):
	#	self.label.setText("Hola")

