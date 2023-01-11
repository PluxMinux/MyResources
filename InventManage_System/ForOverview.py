import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5 import QtGui
import pymysql.cursors

def OverviewWindow(self):
    #QUEUE ORDER
    self.GBQueueBox = QGroupBox("",self)
    self.GBQueueBox.move(350,220)
    self.GBQueueBox.resize(820,300)
    self.GBQueueBox.setStyleSheet("QGroupBox {background-color:  rgb(255, 255, 255);}")
    
    self.layout1 = QVBoxLayout(self.GBQueueBox)
    
    self.LQueue = QLabel("\nQUEUE ORDER \n",self.GBQueueBox)
    self.LQueue.setFont(QFont('Arial',15,QFont.Light))
    
    connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        myrow=cursor.execute('select * from queue_order')

    self.TWQTable = QTableWidget(self.GBQueueBox)
    self.TWQTable.setColumnCount(6)
    self.TWQTable.setRowCount(5+myrow)
    self.TWQTable.setContentsMargins(30,30,30,30)
    self.TWQTable.setAlternatingRowColors(True)
    self.TWQTable.setHorizontalHeaderLabels(['Order Type','Quantity','Types','Address','Name','Total Payment'])
    self.TWQTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.TWQTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    self.TWQTable.setEditTriggers(QAbstractItemView.NoEditTriggers)    
    self.header = self.TWQTable.horizontalHeader()
    self.header.setDefaultSectionSize(130)
    
    self.PBPush = QPushButton("LATEST ORDER QUEUE COMPLETE",self.GBQueueBox)
    self.PBPush.setFont(QFont('Arial',9,QFont.Light))
    self.PBPush.clicked.connect(self.clickedPushLatest)
    
    self.layout1.addWidget(self.LQueue)
    self.layout1.addWidget(self.TWQTable)
    self.layout1.addWidget(self.PBPush)
    
    self.GBQueueBox.setLayout(self.layout1)
    

    #Ready to go
    self.GBReady = QGroupBox("",self)
    self.GBReady.move(350,560)
    self.GBReady.resize(820,300)
    self.GBReady.setStyleSheet("QGroupBox {background-color:  rgb(255, 255, 255);}")
    
    self.layout2 = QVBoxLayout(self.GBReady)
    
    self.LReady = QLabel("\nREADY TO GO \n",self.GBReady)
    self.LReady.setFont(QFont('Arial',15,QFont.Light))
    
    self.TWRTable = QTableWidget(self.GBReady)
    self.TWRTable.setColumnCount(6)
    self.TWRTable.setRowCount(20 + myrow)
    self.TWRTable.setContentsMargins(30,30,30,30)
    self.TWRTable.setAlternatingRowColors(True)
    self.TWRTable.setHorizontalHeaderLabels(['Order Type','Quantity','Types','Address','Name','Total Payment'])
    self.TWRTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.TWRTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    self.TWRTable.setEditTriggers(QAbstractItemView.NoEditTriggers)    
    self.header2 = self.TWRTable.horizontalHeader()
    self.header2.setDefaultSectionSize(130)
    
    self.layout2.addWidget(self.LReady)
    self.layout2.addWidget(self.TWRTable)

    self.GBReady.setLayout(self.layout2)