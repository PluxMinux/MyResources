import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
import pymysql.cursors

def Records(self):
    #QUEUE ORDER
    self.GBDeliveryOption = QGroupBox("",self)
    self.GBDeliveryOption.move(350,220)
    self.GBDeliveryOption.resize(820,650)
    self.GBDeliveryOption.setStyleSheet("QGroupBox {background-color:  rgb(255, 255, 255);}")
    
    self.layoutDeliveryOption = QVBoxLayout(self.GBDeliveryOption)
    
    self.LDeliveryOption = QLabel("\nCUSTOMER LIST FOR DELIVERY OPTION \n",self.GBDeliveryOption)
    self.LDeliveryOption.setFont(QFont('Arial',15,QFont.Light))
    
    connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        myrow=cursor.execute('select * from customer_info')
    
    self.TWDOTable = QTableWidget(self.GBDeliveryOption)
    self.TWDOTable.setColumnCount(8)
    self.TWDOTable.setRowCount(20+myrow)
    self.TWDOTable.setContentsMargins(30,30,30,30)
    self.TWDOTable.setAlternatingRowColors(True)
    self.TWDOTable.setHorizontalHeaderLabels(['Customer ID','First name','Last Name','Mobile Number','House Number','Street Name','Barangay','City'])

    self.TWDOTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    #self.TWDOTable.setEditTriggers(QAbstractItemView.NoEditTriggers)    
    self.headerDeliveryOption = self.TWDOTable.horizontalHeader()
    self.headerDeliveryOption.setDefaultSectionSize(153)
    
    self.layoutDeliveryOption.addWidget(self.LDeliveryOption)
    self.layoutDeliveryOption.addWidget(self.TWDOTable)

    # connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    # with connection.cursor() as cursor:
    #     num_borrowed=cursor.execute('select * from customer_info')
    # connection.commit()
    # spaces = " "
    # for i in range(num_borrowed):
    #     myBorrowList=cursor.fetchone()
    #     self.TWDOTable.setItem(i,0,QTableWidgetItem(spaces*24+'{}'.format(myBorrowList['d_order_id'])))
    #     self.TWDOTable.setItem(i,1,QTableWidgetItem('{}'.format(myBorrowList['f_name'])))
    #     self.TWDOTable.setItem(i,2,QTableWidgetItem('{}'.format(myBorrowList['l_name'])))
    #     self.TWDOTable.setItem(i,3,QTableWidgetItem('{}'.format(myBorrowList['m_number'])))
    #     self.TWDOTable.setItem(i,4,QTableWidgetItem('{}'.format(myBorrowList['h_number'])))
    #     self.TWDOTable.setItem(i,5,QTableWidgetItem('{}'.format(myBorrowList['s_name'])))
    #     self.TWDOTable.setItem(i,6,QTableWidgetItem('{}'.format(myBorrowList['b_name'])))
    #     self.TWDOTable.setItem(i,7,QTableWidgetItem('{}'.format(myBorrowList['c_name'])))
    
        
    # self.GBDeliveryOption.setLayout(self.layoutDeliveryOption)
    
    self.TWDOTable.cellChanged.connect(self.clickedUpdateRecords)
    


    