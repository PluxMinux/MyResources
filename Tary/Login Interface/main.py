from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5 import uic, QtCore, QtGui, QtWidgets
import sys, time

class LoginInterface(QWidget):
    def __init__(self):
        super(LoginInterface,self).__init__()
        uic.loadUi("Login Interface/Design.ui", self)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.label_3.setStyleSheet("image: url(Login Interface/Drawer/systemIcon.png);")
        self.image.setStyleSheet("image: url(Login Interface/Drawer/logo.png);")
        
        self.show()
        


if __name__ == '__main__':
	App = QApplication(sys.argv)
	window = LoginInterface()
	window.show()
	sys.exit(App.exec_())
