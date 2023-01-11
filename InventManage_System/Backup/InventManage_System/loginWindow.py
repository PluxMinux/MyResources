import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QFont, QFontDatabase
import os


class mainWindow(QWidget):
	def __init__(self):
		super(mainWindow,self).__init__()
		
		self.title = "Inventory Management System"
		self.setWindowIcon(QtGui.QIcon('Images/inventoryIcon.png'))
		self.setWindowTitle(self.title) 						 
		self.setGeometry(100,100,1000,700)
		self.setFixedSize(self.size())

		self.image = QLabel(self)
		self.imageLoc = QPixmap('Images/loginBG.png')
		self.image.setPixmap(self.imageLoc)
		self.image.move(0,0)
		self.image.resize(1000,700)
		self.image.setScaledContents(True)
  
		self.InitWindow()
		self.center()
		self.show()
    
	def InitWindow(self):
		QFontDatabase.addApplicationFont('Font/Roboto/Roboto-Light.ttf')
		QFontDatabase.addApplicationFont('Font/Roboto/Roboto-Bold.ttf')
		QFontDatabase.addApplicationFont('Font/Roboto/Roboto-Medium.ttf')
		light = QFont("Roboto Light", 11)
		bold = QFont("Roboto Bold", 30)
		medium = QFont("Roboto Medium", 11)	
		self.username = QLineEdit(self)
		self.username.move(110,316)
		self.username.resize(315,50)
		self.username.setMaxLength(15)
		self.username.setPlaceholderText("Username")
		self.username.setFont(light)
		self.username.setAlignment(QtCore.Qt.AlignLeft)
		self.username.setStyleSheet("QLineEdit {padding: 10px; background-color: rgba(255, 255, 255, 6%); border-radius: 9px; color: white}")

		self.password = QLineEdit(self)
		self.password.move(110,391)
		self.password.resize(315,50)
		self.password.setEchoMode(QLineEdit.Password)
		self.password.setMaxLength(15)	
		self.password.setFont(light)
		self.password.setPlaceholderText("Password")
		self.password.setAlignment(QtCore.Qt.AlignLeft)
		self.password.setStyleSheet("QLineEdit {padding: 10px ; background-color: rgba(255, 255, 255, 6%); border-radius: 9px; color: white}")

		self.loginButton = QPushButton('LOGIN',self)
		self.loginButton.move(275,459)
		self.loginButton.resize(150,50)
		self.loginButton.setDefault(True)
		self.loginButton.setFont(medium)
		self.loginButton.clicked.connect(self.loginFunction)
		self.loginButton.setStyleSheet("QPushButton{background: rgba(255, 255, 255, 6%);border: 5px solid #00F0FF; border-radius: 25px ; color: 						#00F0FF; }"
                                     		"QPushButton:hover{color: white; background-color: #00F0FF}")

		self.cancelButton = QPushButton('CANCEL',self)
		self.cancelButton.move(111,459)
		self.cancelButton.resize(150,50)
		self.cancelButton.setDefault(True)
		self.cancelButton.setFont(medium)
		self.cancelButton.clicked.connect(self.loginFunction)
		self.cancelButton.setStyleSheet("QPushButton{background: rgba(255, 255, 255, 6%);border: 5px solid #00F0FF; border-radius: 25px ; color: 						#00F0FF; }"
                                     		"QPushButton:hover{color: white; background-color: #00F0FF}")







		

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
		
	def loginFunction(self):
		import HomeWindow
		self.newWindow = HomeWindow.Home()
		self.newWindow.show()
		self.hide()
		# user_acc = self.username.text()
		# pass_acc = self.password.text()
  
		# NoEmptyField = True
		# if (len(user_acc) == 0 or len(pass_acc) == 0):
			
		# 	NoEmptyField = False 
		# 	self.messagebox = QMessageBox()
		# 	self.messagebox.setText("Please fill up the username or password entry.")
		# 	self.messagebox.setWindowTitle("Message!")
		# 	self.messagebox.setIcon(QMessageBox.Information)
		# 	self.messagebox.show()
			

		# if (NoEmptyField):
		# 	connection = pymysql.connect(host='localhost',
        #                     user='root',
        #                     password='',
        #                     db='ws_db',
        #                     charset='utf8mb4',
        #                     cursorclass=pymysql.cursors.DictCursor)
		# 	with connection.cursor() as cursor:
		# 		result = cursor.execute("select * from account where user = %s and password = %s",(user_acc,pass_acc))	# Connect to the database
			
		# 	if(result == 0):
		# 		self.messagebox = QMessageBox()
		# 		self.messagebox.setText("Invalid account!, incorrect username or password")
		# 		self.messagebox.setWindowTitle("Message!")
		# 		self.messagebox.setIcon(QMessageBox.Information)
		# 		self.messagebox.show()
		# 	else:
		# 		print("Successfully login!")
		# 		self.newWindow = mainWindow()
		# 		self.newWindow.show()
		# 		self.hide()

	
  
if __name__ == '__main__':
	App = QApplication(sys.argv)
	window = mainWindow()
	window.show()
	sys.exit(App.exec_())