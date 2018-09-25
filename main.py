from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)
 
import sys
import pyrebase

class Dialog(QDialog):
    def __init__(self):
        super(Dialog, self).__init__()
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
        
        button = QPushButton('Guardar', self)
        button.clicked.connect(self.on_click)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(button)
        self.setLayout(mainLayout)
        self.setWindowTitle("Registro")
        
 
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Registro")
        layout = QFormLayout()
        
        self.studentId = QLineEdit()
        self.studentId.setObjectName("studentId")

        self.carrera = QLineEdit()
        self.carrera.setObjectName("studentId")

        layout.addRow(QLabel("Matrícula:"))
        layout.addRow(self.studentId)
        layout.addRow(QLabel("Carrera:")) 
        layout.addRow(self.carrera) 

        self.formGroupBox.setLayout(layout)
    
    @pyqtSlot()
    def on_click(self):
        print(self.studentId.text())
        print(self.carrera.text())
        data = {"RFID": "00000000", "matricula": self.studentId.text(), "carrera": self.carrera.text()}
        self.db.child("Students").push(data)
        #print(self.db.child("Students").order_by_child("RFID").equal_to('A0051212').get().val())
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
sys.exit(dialog.exec_())