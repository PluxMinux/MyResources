from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic, QtCore
import sys, timeit, pyautogui, time, ctypes




class LoginInterface(QWidget):
    def __init__(self):
        super(LoginInterface,self).__init__()
        uic.loadUi("Login Interface/Design.ui", self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowIcon(QIcon('Login Interface/Drawer/systemIcon.png'))
        self.setWindowTitle("One Piece") 

        
        myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        

        
        self.minWin.setIcon(QIcon('Login Interface/Drawer/minus.svg'))
        self.minWin.clicked.connect(self.showMinimized)
        self.maxWin.setIcon(QIcon('Login Interface/Drawer/square.svg'))
        self.maxWin.clicked.connect(self.clickedFullscreen)
        self.closeWin.setIcon(QIcon('Login Interface/Drawer/x.svg'))
        self.closeWin.clicked.connect(self.close)
        
        
        self.label_3.setStyleSheet("image: url(Login Interface/Drawer/systemIcon.png);")
        self.image.setStyleSheet("image: url(Login Interface/Drawer/logo.png);")
        

        self.newAccount.clicked.connect(self.clickedNewAccount)

        self.labelMovie.setHidden(True)
        
        iconUsername = QIcon("Login Interface/Drawer/user.svg")
        self.usernameEntry.addAction(iconUsername, QLineEdit.LeadingPosition)
        
        iconPassword = QIcon("Login Interface/Drawer/lock.svg")
        self.passwordEntry.addAction(iconPassword, QLineEdit.LeadingPosition)
        
        
        self.show()
        
    def clickedFullscreen(self):
        x = int(pyautogui.size()[0])
        y = int(pyautogui.size()[1])
        self.setGeometry(0,0,x,y)
        self.widget.setGeometry(0,0,x,y)

    def clickedNewAccount(self):
        self.loginLabel.setHidden(True)
        self.usernameEntry.setHidden(True)
        self.passwordEntry.setHidden(True)
        self.rememberMe.setHidden(True)
        self.forgetPassword.setHidden(True)
        self.Login.setHidden(True)
        self.newAccount.setHidden(True)
        self.labelMovie.setHidden(False)
        
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.duration)
        self.timer.start(5000)
        
        self.movie = QMovie("Login Interface/Drawer/loading.gif")
        self.labelMovie.setMovie(self.movie)
        self.movie.setScaledSize(QtCore.QSize(300,120))
        self.movie.start()
        
    def duration(self):
        self.movie.stop()
        self.labelMovie.setHidden(True)
        self.timer.stop()
        
        self.loginLabel.setHidden(False)
        self.usernameEntry.setHidden(False)
        self.passwordEntry.setHidden(False)
        self.rememberMe.setHidden(False)
        self.forgetPassword.setHidden(False)
        self.Login.setHidden(False)
        self.newAccount.setHidden(False)
            
            
    #START
    #Make the window movable.        
    def mousePressEvent(self, event):                             
        self.clickPosition = event.globalPos()

    def mouseMoveEvent(self, event):                                  # !!!
        delta = QtCore.QPoint(event.globalPos() - self.clickPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.clickPosition = event.globalPos()
    #END



if __name__ == '__main__':
	App = QApplication(sys.argv)
	window = LoginInterface()
	window.show()
	sys.exit(App.exec_())
