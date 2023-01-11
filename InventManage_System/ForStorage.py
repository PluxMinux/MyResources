import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
import pymysql.cursors

def Storage(self):
    self.GBAvailable = QGroupBox("",self)
    self.GBAvailable.move(350,220)
    self.GBAvailable.resize(252,150)
    self.GBAvailable.setStyleSheet("QGroupBox {border-image : url(Images/Available.png);border-radius: 18px ;}")
    
    self.LAvailable = QLabel("AVAILABLE CONTAINER",self.GBAvailable)
    self.LAvailable.move(10,10)
    self.LAvailable.setFont(QFont('Arial',13,QFont.Bold))
    self.LAvailable.setStyleSheet("QLabel {color: white;}")
    
    try:
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            cursor.execute('select available from in_storage')
        connection.commit()
        AValues = cursor.fetchone()
        getAValues = list(AValues.values())
        AValues = ' '.join(map(str,getAValues))
    except:
        AValues = 0
        
    self.LAValues = QLabel(str(AValues),self.GBAvailable)
    self.LAValues.move(110,40)
    self.LAValues.resize(50,30)
    self.LAValues.setFont(QFont('Arial',23,QFont.Bold))
    self.LAValues.setStyleSheet("QLabel {color: white;}")
    
    self.LEValue = QLineEdit(self.GBAvailable)
    self.LEValue.move(10,80)
    self.LEValue.resize(230,22)
    self.LEValue.setFont(QFont('Arial',11,QFont.Light))
    self.LEValue.setPlaceholderText("Enter a value")
    self.LEValue.setStyleSheet("QLineEdit {background: rgb(255, 255, 255, 40%);border: 1px solid white;color: white}")
    
    self.PBAdd = QPushButton("Add",self.GBAvailable)
    self.PBAdd.move(10,115)
    self.PBAdd.resize(110,20)
    self.PBAdd.setStyleSheet("QPushButton {background: rgb(255, 255, 255);border: 1px solid white;border-radius: 10px;}"
                                "QPushButton:hover{background: rgb(0, 255, 255);}")
    self.PBAdd.clicked.connect(self.clickedAdd)
    
    self.PBDelete = QPushButton("Delete",self.GBAvailable)
    self.PBDelete.move(130,115)
    self.PBDelete.resize(110,20)
    self.PBDelete.setStyleSheet("QPushButton {background: rgb(255, 255, 255);border: 1px solid white;border-radius: 10px;}"
                                "QPushButton:hover{background: rgb(0, 255, 255);}")
    self.PBDelete.clicked.connect(self.clickedDelete)
    
    self.GBBorrow = QGroupBox("",self)
    self.GBBorrow.move(630,220)
    self.GBBorrow.resize(252,150)
    self.GBBorrow.setStyleSheet("QGroupBox {border-image : url(Images/Borrow.png);border-radius: 18px ;}")
    
    self.LBorrow = QLabel("BORROWED CONTAINER",self.GBBorrow)
    self.LBorrow.move(10,10)
    self.LBorrow.setFont(QFont('Arial',13,QFont.Bold))
    self.LBorrow.setStyleSheet("QLabel {color: white;}")
    
    connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        borrowRow = cursor.execute('select * from list_borrowed')
    connection.commit()
    
    self.LBValues = QLabel(str(borrowRow),self.GBBorrow)
    self.LBValues.move(90,40)
    self.LBValues.resize(100,100)
    self.LBValues.setFont(QFont('Arial',53,QFont.Bold))
    self.LBValues.setStyleSheet("QLabel {color: white;}")
    
    self.GBTotal = QGroupBox("",self)
    self.GBTotal.move(910,220)
    self.GBTotal.resize(252,150)
    self.GBTotal.setStyleSheet("QGroupBox {border-image : url(Images/Total.png);border-radius: 18px ;}")
    
    self.LTotal = QLabel("TOTAL CONTAINER",self.GBTotal)
    self.LTotal.move(10,10)
    self.LTotal.setFont(QFont('Arial',13,QFont.Bold))
    self.LTotal.setStyleSheet("QLabel {color: white;}")
    
    Total = int(AValues) + borrowRow
    connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        borrowRow2 = cursor.execute('select * from list_borrowed')
    connection.commit()    

    self.LTValues = QLabel(str(Total),self.GBTotal)
    self.LTValues.move(80,40)
    self.LTValues.resize(100,100)
    self.LTValues.setFont(QFont('Arial',53,QFont.Bold))
    self.LTValues.setStyleSheet("QLabel {color: white;}")

    #Borrowed Container List
    self.GBList = QGroupBox("",self)
    self.GBList.move(350,400)
    self.GBList.resize(820,250)
    self.GBList.setStyleSheet("QGroupBox {background-color:  rgb(255, 255, 255);}")
    
    self.layoutList = QVBoxLayout(self.GBList)
    
    self.LList = QLabel("BORROWED CONAINER LIST ",self.GBList)
    self.LList.setFont(QFont('Arial',15,QFont.Light))
    
    connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        RowBorrowedTable = cursor.execute("select * from list_borrowed")
    
    self.TWLTable = QTableWidget(self.GBList)
    self.TWLTable.setColumnCount(5)
    self.TWLTable.setRowCount(5 + RowBorrowedTable)
    self.TWLTable.setContentsMargins(30,30,30,30)
    self.TWLTable.setAlternatingRowColors(True)
    self.TWLTable.setHorizontalHeaderLabels(['Quantity','Types','Name','Mobile','Address'])
    self.TWLTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.TWLTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    self.TWLTable.setEditTriggers(QAbstractItemView.NoEditTriggers)    
    self.header2 = self.TWLTable.horizontalHeader()
    self.header2.setDefaultSectionSize(153)
    
    self.layoutList.addWidget(self.LList)
    self.layoutList.addWidget(self.TWLTable)

    self.GBList.setLayout(self.layoutList)
    
    #Container Rate
    self.GBRate = QGroupBox("",self)
    self.GBRate.move(350,670)
    self.GBRate.resize(820,200)
    self.GBRate.setStyleSheet("QGroupBox {background-color:  rgb(255, 255, 255);}")
    
    self.layoutRate = QVBoxLayout(self.GBRate)
    
    self.LRate = QLabel("CONTAINER RATE ",self.GBRate)
    self.LRate.setFont(QFont('Arial',15,QFont.Light))
    

    
    self.TWRRTable = QTableWidget(self.GBRate)
    self.TWRRTable.setColumnCount(3)
    self.TWRRTable.setRowCount(10)
    self.TWRRTable.setContentsMargins(30,30,30,30)
    self.TWRRTable.setAlternatingRowColors(True)
    self.TWRRTable.setHorizontalHeaderLabels(['ID','Types','Rate'])
    self.TWRRTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.TWRRTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    self.TWRRTable.setEditTriggers(QAbstractItemView.NoEditTriggers)    
    self.header2 = self.TWRRTable.horizontalHeader()
    self.header2.setDefaultSectionSize(255)
    
    self.layoutRate.addWidget(self.LRate)
    self.layoutRate.addWidget(self.TWRRTable)

    self.GBRate.setLayout(self.layoutRate)