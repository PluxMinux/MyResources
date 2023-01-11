import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
import pymysql.cursors

def Reports(self):
    self.GBToday = QGroupBox("",self)
    self.GBToday.move(350,220)
    self.GBToday.resize(320,150)
    self.GBToday.setStyleSheet("QGroupBox {border-image : url(Images/Today.png);border-radius: 18px ;}")
    
    self.LBToday = QLabel("TOTAL OF TODAY'S INQUIRY",self.GBToday)
    self.LBToday.move(10,20)
    self.LBToday.setFont(QFont('Arial',15,QFont.Bold))
    
    self.LBToday.setStyleSheet("QLabel {color: white;}")

    # try:
    #     connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    #     with connection.cursor() as cursor:
    #         values=cursor.execute('select time_stamp,d_mode,t_payment,ownership,p_mode from today_inquiry order by 1 desc')
    #         cursor.execute('select d_mode = "Door delivery" from today_inquiry;')
    #         D_values = cursor.fetchone()
    #         D_values = list(D_values.values())
    #         D_values = ' '.join(map(str,D_values))
    #         cursor.execute('select d_mode = "Self pick-up" from today_inquiry;')
    #         ND_values = cursor.fetchone()
    #         ND_values = list(ND_values.values())
    #         ND_values = ' '.join(map(str,ND_values))
    #     connection.commit()
        
    #     print("try")

    # except:
    #     D_values = 0
    #     ND_values = 0
    # print("ex")

    self.LBTodayValues = QLabel("0",self.GBToday)
    self.LBTodayValues.move(140,60)
    self.LBTodayValues.setFont(QFont('Arial',40,QFont.Bold))
    self.LBTodayValues.setStyleSheet("QLabel {color: rgb(0,255,255);}")
    
    self.GBNumberDelivery = QGroupBox("",self)
    self.GBNumberDelivery.move(700,220)
    self.GBNumberDelivery.resize(470,70)
    self.GBNumberDelivery.setStyleSheet("QGroupBox {border-image : url(Images/DeliveryInquiry.png);border-radius: 18px ;}")
    
    self.LDTotal = QLabel("TOTAL INQUIRIES FOR DELIVERY\t\t:",self.GBNumberDelivery)
    self.LDTotal.move(10,25)
    self.LDTotal.setFont(QFont('Arial',13,QFont.Bold))
    self.LDTotal.setStyleSheet("QLabel {color: white;}")
    
    self.LDValues = QLabel('0',self.GBNumberDelivery)
    self.LDValues.move(400,10)
    self.LDValues.setFont(QFont('Arial',30,QFont.Bold))
    self.LDValues.setStyleSheet("QLabel {color: rgb(0,255,255);}")
    
    self.GBNumberNonDelivery = QGroupBox("",self)
    self.GBNumberNonDelivery.move(700,300)
    self.GBNumberNonDelivery.resize(470,70)
    self.GBNumberNonDelivery.setStyleSheet("QGroupBox {border-image : url(Images/NonDeliveryInquiry.png);border-radius: 18px ;}")
    
    self.LNDTotal = QLabel("TOTAL INQUIRIES FOR NON-DELIVERY\t: ",self.GBNumberNonDelivery)
    self.LNDTotal.move(10,25)
    self.LNDTotal.setFont(QFont('Arial',13,QFont.Bold))
    self.LNDTotal.setStyleSheet("QLabel {color: white;}")

    self.LNDValues = QLabel("0",self.GBNumberNonDelivery)
    self.LNDValues.move(400,10)
    self.LNDValues.setFont(QFont('Arial',30,QFont.Bold))
    self.LNDValues.setStyleSheet("QLabel {color: rgb(0,255,255);}")
    


    #Iquiries List
    self.GBTodayList = QGroupBox("",self)
    self.GBTodayList.move(350,400)
    self.GBTodayList.resize(820,250)
    self.GBTodayList.setStyleSheet("QGroupBox {background-color:  rgb(255, 255, 255);}")

    self.layoutTodayList = QVBoxLayout(self.GBTodayList)
    
    self.LTodayList = QLabel("TODAY'S INQUERIES ",self.GBTodayList)
    self.LTodayList.setFont(QFont('Arial',15,QFont.Light))
    
    connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        myrow=cursor.execute('select * from today_inquiry')
    
    self.TWTodayTable = QTableWidget(self.GBTodayList)
    self.TWTodayTable.setColumnCount(6)
    self.TWTodayTable.setRowCount(5 + myrow)
    self.TWTodayTable.setContentsMargins(30,30,30,30)
    self.TWTodayTable.setAlternatingRowColors(True)
    self.TWTodayTable.setHorizontalHeaderLabels(['Customer ID','Timestamp','Delivery mode','Total payment','Ownership','Payment mode'])
    self.TWTodayTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.TWTodayTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    self.TWTodayTable.setEditTriggers(QAbstractItemView.NoEditTriggers)    
    self.header2 = self.TWTodayTable.horizontalHeader()
    self.header2.setDefaultSectionSize(128)
    

    self.layoutTodayList.addWidget(self.LTodayList)
    self.layoutTodayList.addWidget(self.TWTodayTable)

    self.GBTodayList.setLayout(self.layoutTodayList)
    
    #Container Rate
    self.GBHistory = QGroupBox("",self)
    self.GBHistory.move(350,670)
    self.GBHistory.resize(820,200)
    self.GBHistory.setStyleSheet("QGroupBox {background-color:  rgb(255, 255, 255);}")
    
    self.layoutHistory = QVBoxLayout(self.GBHistory)
    
    self.LHistory = QLabel("HISTORY INQUIRY ",self.GBHistory)
    self.LHistory.setFont(QFont('Arial',15,QFont.Light))
    
    connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        HistoryInquiry=cursor.execute('select times_stamp,d_mode,t_payment,ownership,p_mode from history_inquiry order by 1 desc')
    connection.commit()
    

    
    self.TWHistoryTable = QTableWidget(self.GBHistory)
    self.TWHistoryTable.setColumnCount(6)
    self.TWHistoryTable.setRowCount(5 + HistoryInquiry)
    self.TWHistoryTable.setContentsMargins(30,30,30,30)
    self.TWHistoryTable.setAlternatingRowColors(True)
    self.TWHistoryTable.setHorizontalHeaderLabels(['Customer ID','Timestamp','Delivery mode','Total payment','Ownership','Payment mode'])
    self.TWHistoryTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.TWHistoryTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    self.TWHistoryTable.setEditTriggers(QAbstractItemView.NoEditTriggers)    
    self.header2 = self.TWHistoryTable.horizontalHeader()
    self.header2.setDefaultSectionSize(128)
    
    self.layoutHistory.addWidget(self.LHistory)
    self.layoutHistory.addWidget(self.TWHistoryTable)

    self.GBTodayList.setLayout(self.layoutHistory)
    
    for i in range(HistoryInquiry):
        myBorrowList=cursor.fetchone()
        self.TWHistoryTable.setItem(i,0,QTableWidgetItem('{}'.format(myBorrowList['times_stamp'])))
        self.TWHistoryTable.setItem(i,1,QTableWidgetItem('{}'.format(myBorrowList['d_mode'])))
        self.TWHistoryTable.setItem(i,2,QTableWidgetItem('{}'.format(myBorrowList['t_payment'])))
        self.TWHistoryTable.setItem(i,3,QTableWidgetItem('{}'.format(myBorrowList['ownership'])))
        self.TWHistoryTable.setItem(i,4,QTableWidgetItem('{}'.format(myBorrowList['p_mode'])))
