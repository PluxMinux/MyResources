from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys, time

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi("New form of code/design.ui", self)
        
        self.setWindowTitle("Login Interface")
        self.pushButton.clicked.connect(self.clickedDisplay)
        
        self.show()
        
    def clickedDisplay(self):
        print(self.lineEdit.text())
        QApplication.setOverrideCursor(Qt.WaitCursor)
        time.sleep(5)
        QApplication.restoreOverrideCursor()
        

if __name__ == '__main__':
	App = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(App.exec_())
