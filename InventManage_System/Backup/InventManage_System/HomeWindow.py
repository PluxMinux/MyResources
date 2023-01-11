import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
import pymysql.cursors

#Data
typeList = []
typeList_N = []
ownershipList = []
deliveryList = []
paymentList = []
paymentList_N = []
stateList = []
a = []

class Home(QWidget):

    def __init__(self):
        super(Home,self).__init__()
        
        self.InitWindow()

        import ForReports
        ForReports.Reports(self)
        import ForRecords
        ForRecords.Records(self)
        import ForStorage
        ForStorage.Storage(self)
        import ForOverview
        ForOverview.OverviewWindow(self)
        import ForInquiry
        ForInquiry.Delivery(self)

        self.show()
		
    def InitWindow(self):
        self.setWindowIcon(QIcon('Images/inventoryIcon.png'))
        self.setWindowTitle("QUALIPURE: Inventory Management System") 						 
        self.setGeometry(100,100,1200,900)
        self.setFixedSize(self.size())
        
        self.image_NI = QLabel(self)
        self.imageLoc_NI = QPixmap('Images/NewInquiryBanner.png')
        self.image_NI.setPixmap(self.imageLoc_NI)
        self.image_NI.move(0,-360)
        self.image_NI.resize(1200,900)
        
        
        self.image_OV = QLabel(self)
        self.imageLoc_OV = QPixmap('Images/OverviewBanner.png')
        self.image_OV.setPixmap(self.imageLoc_OV)
        self.image_OV.move(0,-360)
        self.image_OV.resize(1200,900)
        self.image_OV.setHidden(True)
        
        self.image_S = QLabel(self)
        self.imageLoc_S = QPixmap('Images/StorageBanner.png')
        self.image_S.setPixmap(self.imageLoc_S)
        self.image_S.move(0,-360)
        self.image_S.resize(1200,900)
        self.image_S.setHidden(True)
        
        self.image_R = QLabel(self)
        self.imageLoc_R = QPixmap('Images/RecordsBanner.png')
        self.image_R.setPixmap(self.imageLoc_R)
        self.image_R.move(0,-360)
        self.image_R.resize(1200,900)
        self.image_R.setHidden(True)

        self.image_RR = QLabel(self)
        self.imageLoc_RR = QPixmap('Images/ReportsBanner.png')
        self.image_RR.setPixmap(self.imageLoc_RR)
        self.image_RR.move(0,-360)
        self.image_RR.resize(1200,900)
        self.image_RR.setHidden(True)

        self.PBNewInqury = QPushButton("NEW INQUIRY",self)
        self.PBNewInqury.move(0,180)
        self.PBNewInqury.resize(321,144)
        self.PBNewInqury.setFont(QFont('Arial',20,QFont.Bold))
        self.PBNewInqury.setStyleSheet("""QPushButton {border-image : url(Images/New Inquiry Button1.png);color: white;}
                                       QPushButton:hover {border-image : url(Images/New Inquiry Button.png);color: yellow;}""")
        self.PBNewInqury.clicked.connect(self.clickedInquiry)

        self.PBOverview = QPushButton("OVERVIEW",self)
        self.PBOverview.move(0,324)
        self.PBOverview.resize(321,144)
        self.PBOverview.setFont(QFont('Arial',20,QFont.Bold)) 
        self.PBOverview.setStyleSheet("""QPushButton {border-image : url(Images/PBOverview2.jpg);color: white;}
                                       QPushButton:hover {border-image : url(Images/PBOverview1.jpg);color: yellow;}""")
        self.PBOverview.clicked.connect(self.clickedOverview)

        self.PBStorage = QPushButton("STORAGE",self)
        self.PBStorage.move(0,468)
        self.PBStorage.resize(321,144)
        self.PBStorage.setFont(QFont('Arial',20,QFont.Bold)) 
        self.PBStorage.setStyleSheet("""QPushButton {border-image : url(Images/Storage Button1.png);color: white;}
                                       QPushButton:hover {border-image : url(Images/Storage Button.png);color: yellow;}""")
        self.PBStorage.clicked.connect(self.clickedStorage)
        
        self.PBRecords = QPushButton("RECORDS",self)
        self.PBRecords.move(0,612)
        self.PBRecords.resize(321,144)
        self.PBRecords.setFont(QFont('Arial',20,QFont.Bold)) 
        self.PBRecords.setStyleSheet("""QPushButton {border-image : url(Images/Records Button1.png);color: white;}
                                       QPushButton:hover {border-image : url(Images/Records Button.png);color: yellow;}""")
        self.PBRecords.clicked.connect(self.clickedRecords)

        self.PDReports = QPushButton("REPORTS",self)
        self.PDReports.move(0,756)
        self.PDReports.resize(321,144)
        self.PDReports.setFont(QFont('Arial',20,QFont.Bold)) 
        self.PDReports.setStyleSheet("""QPushButton {border-image : url(Images/Reports Button1.png);color: white;}
                                       QPushButton:hover {border-image : url(Images/Reports Button.png);color: yellow;}""")
        self.PDReports.clicked.connect(self.clickedReports)

        self.LogoutButton = QPushButton('Log out',self)
        self.LogoutButton.move(116,107)
        self.LogoutButton.resize(181,30)
        self.LogoutButton.setDefault(True)
        #self.LogoutButton.setFont(light)
        self.LogoutButton.setStyleSheet("QPushButton{background: rgba(255, 255, 255, 6%);border: 1px solid white; border-radius: 0px ; color: white; }"
                                     		"QPushButton:hover{color: white; background-color: #00F0FF; border: 1px solid #00F0FF}")
        self.LogoutButton.clicked.connect(self.clickedLogout)
    
        
    def clickedInquiry(self):
        self.image_NI.setHidden(False)
        self.image_OV.setHidden(True)
        self.image_S.setHidden(True)
        self.image_R.setHidden(True)
        self.image_RR.setHidden(True)
        self.GBDOI_N.setHidden(True)
        
        from ForReports import Reports
        self.GBToday.setHidden(True)
        self.GBNumberDelivery.setHidden(True)
        self.GBNumberNonDelivery.setHidden(True)
        self.GBTodayList.setHidden(True)
        self.GBHistory.setHidden(True)
        
        from ForRecords import Records
        self.GBDeliveryOption.setHidden(True)
        
        
        from ForStorage import Storage
        self.GBAvailable.setHidden(True)
        self.GBBorrow.setHidden(True)
        self.GBTotal.setHidden(True)
        self.GBList.setHidden(True)
        self.GBRate.setHidden(True)
        
        from ForOverview import OverviewWindow    
        self.GBQueueBox.setHidden(True)
        self.GBReady.setHidden(True)
        
        from ForInquiry import Delivery
        self.GBType.setHidden(False)
        self.GBCI.setHidden(False)
        self.GBDOI.setHidden(False)
        self.GBSubmitCancel.setHidden(False)

    # def clickedOverview(self):
    #     connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    #     with connection.cursor() as cursor:
    #         numberofrows2=cursor.execute('select * from queue_order')
            
    #     connection.commit()
    #     for i in range(numberofrows2):
    #         customers2=cursor.fetchone()
    #         #i -= 1
    #         self.TWQTable.setItem(i,0,QTableWidgetItem('{}'.format(customers2['order_type'])))
    #         self.TWQTable.setItem(i,1,QTableWidgetItem('{}'.format(customers2['quantity'])))
    #         self.TWQTable.setItem(i,2,QTableWidgetItem('{}'.format(customers2['wc_types'])))
    #         self.TWQTable.setItem(i,3,QTableWidgetItem('{}'.format(customers2['address'])))
    #         self.TWQTable.setItem(i,4,QTableWidgetItem('{}'.format(customers2['c_name'])))
    #         self.TWQTable.setItem(i,5,QTableWidgetItem('{}'.format(customers2['t_payment'])))
        

    #     connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    #     with connection.cursor() as cursor:
    #         ready=cursor.execute('select * from rdy_togo')
            
    #     for ii in range(ready,0,-1):
    #         customers1=cursor.fetchone()
    #         ii -= 1
    #         self.TWRTable.setItem(ii,0,QTableWidgetItem('{}'.format(customers1['order_type'])))
    #         self.TWRTable.setItem(ii,1,QTableWidgetItem('{}'.format(customers1['quantity'])))
    #         self.TWRTable.setItem(ii,2,QTableWidgetItem('{}'.format(customers1['wc_types'])))
    #         self.TWRTable.setItem(ii,3,QTableWidgetItem('{}'.format(customers1['address'])))
    #         self.TWRTable.setItem(ii,4,QTableWidgetItem('{}'.format(customers1['c_name'])))
    #         self.TWRTable.setItem(ii,5,QTableWidgetItem('{}'.format(customers1['t_payment'])))
        
        
        
    #     self.image_NI.setHidden(True)
    #     self.image_OV.setHidden(False)
    #     self.image_S.setHidden(True)
    #     self.image_R.setHidden(True)
    #     self.image_RR.setHidden(True)
    #     self.GBDOI_N.setHidden(True)
        
    #     from ForReports import Reports
    #     self.GBToday.setHidden(True)
    #     self.GBNumberDelivery.setHidden(True)
    #     self.GBNumberNonDelivery.setHidden(True)
    #     self.GBTodayList.setHidden(True)
    #     self.GBHistory.setHidden(True)
        
    #     from ForRecords import Records
    #     self.GBDeliveryOption.setHidden(True)
        
        
    #     from ForStorage import Storage
    #     self.GBAvailable.setHidden(True)
    #     self.GBBorrow.setHidden(True)
    #     self.GBTotal.setHidden(True)
    #     self.GBList.setHidden(True)
    #     self.GBRate.setHidden(True)
        
    #     from ForOverview import OverviewWindow    
    #     self.GBQueueBox.setHidden(False)
    #     self.GBReady.setHidden(False)
        
    #     from ForInquiry import Delivery
    #     self.GBType.setHidden(True)
    #     self.GBCI.setHidden(True)
    #     self.GBDOI.setHidden(True)
    #     self.GBSubmitCancel.setHidden(True)
        
        
    def clickedStorage(self):
        #Display WC_PRICING table
        spaces = " "
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            num_borrowed=cursor.execute('select * from wc_pricing')
        connection.commit()
        for i in range(num_borrowed):
            myBorrowList=cursor.fetchone()
            self.TWRRTable.setItem(i,0,QTableWidgetItem('{}{}'.format(spaces*40,myBorrowList['wc_id'])))
            self.TWRRTable.setItem(i,1,QTableWidgetItem('{}'.format(myBorrowList['wc_types'])))
            self.TWRRTable.setItem(i,2,QTableWidgetItem('{}'.format(myBorrowList['price'])))
        
        
        #Display the borrowed list
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            num_borrowed=cursor.execute('select * from list_borrowed')
        connection.commit()
        for i in range(num_borrowed,0,-1):
            myBorrowList=cursor.fetchone()
            i -= 1
            self.TWLTable.setItem(i,0,QTableWidgetItem('{}{}'.format(spaces*22,myBorrowList['num_c'])))
            self.TWLTable.setItem(i,1,QTableWidgetItem('{}'.format(myBorrowList['type_c'])))
            self.TWLTable.setItem(i,2,QTableWidgetItem('{}'.format(myBorrowList['c_name'])))
            self.TWLTable.setItem(i,3,QTableWidgetItem('{}'.format(myBorrowList['m_num'])))
            self.TWLTable.setItem(i,4,QTableWidgetItem('{}'.format(myBorrowList['address'])))
            
        self.image_NI.setHidden(True)
        self.image_OV.setHidden(True)
        self.image_S.setHidden(False)
        self.image_R.setHidden(True)
        self.image_RR.setHidden(True)
        self.GBDOI_N.setHidden(True)
        
        from ForReports import Reports
        self.GBToday.setHidden(True)
        self.GBNumberDelivery.setHidden(True)
        self.GBNumberNonDelivery.setHidden(True)
        self.GBTodayList.setHidden(True)
        self.GBHistory.setHidden(True)
        
        from ForRecords import Records
        self.GBDeliveryOption.setHidden(True)
        

        from ForInquiry import Delivery
        self.GBType.setHidden(True)
        self.GBCI.setHidden(True)
        self.GBDOI.setHidden(True)
        self.GBSubmitCancel.setHidden(True)
        
        from ForOverview import OverviewWindow    
        self.GBQueueBox.setHidden(True)
        self.GBReady.setHidden(True)

        from ForStorage import Storage
        self.GBAvailable.setHidden(False)
        self.GBBorrow.setHidden(False)
        self.GBTotal.setHidden(False)
        self.GBList.setHidden(False)
        self.GBRate.setHidden(False)
        

    def clickedRecords(self):
        #Display customer info
        
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            num_borrowed=cursor.execute('select * from customer_info')
        connection.commit()
        spaces = " "
        for i in range(num_borrowed):
            myBorrowList=cursor.fetchone()
            self.TWDOTable.setItem(i,0,QTableWidgetItem(spaces*24+'{}'.format(myBorrowList['d_order_id'])))
            self.TWDOTable.setItem(i,1,QTableWidgetItem('{}'.format(myBorrowList['f_name'])))
            self.TWDOTable.setItem(i,2,QTableWidgetItem('{}'.format(myBorrowList['l_name'])))
            self.TWDOTable.setItem(i,3,QTableWidgetItem('{}'.format(myBorrowList['m_number'])))
            self.TWDOTable.setItem(i,4,QTableWidgetItem('{}'.format(myBorrowList['h_number'])))
            self.TWDOTable.setItem(i,5,QTableWidgetItem('{}'.format(myBorrowList['s_name'])))
            self.TWDOTable.setItem(i,6,QTableWidgetItem('{}'.format(myBorrowList['b_name'])))
            self.TWDOTable.setItem(i,7,QTableWidgetItem('{}'.format(myBorrowList['c_name'])))
        
        self.image_NI.setHidden(True)
        self.image_OV.setHidden(True)
        self.image_S.setHidden(True)
        self.image_R.setHidden(False)
        self.image_RR.setHidden(True)
        self.GBDOI_N.setHidden(True)
        
        from ForReports import Reports
        self.GBToday.setHidden(True)
        self.GBNumberDelivery.setHidden(True)
        self.GBNumberNonDelivery.setHidden(True)
        self.GBTodayList.setHidden(True)
        self.GBHistory.setHidden(True)
        
        from ForInquiry import Delivery
        self.GBType.setHidden(True)
        self.GBCI.setHidden(True)
        self.GBDOI.setHidden(True)
        self.GBSubmitCancel.setHidden(True)
        
        from ForOverview import OverviewWindow    
        self.GBQueueBox.setHidden(True)
        self.GBReady.setHidden(True)

        from ForStorage import Storage
        self.GBAvailable.setHidden(True)
        self.GBBorrow.setHidden(True)
        self.GBTotal.setHidden(True)
        self.GBList.setHidden(True)
        self.GBRate.setHidden(True)
        
        from ForRecords import Records
        self.GBDeliveryOption.setHidden(False)
        
        
    def clickedReports(self):
        # connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        # with connection.cursor() as cursor:
        #     cursor.execute('select max(d_order_id) from d_order_info')
        # connection.commit()
        # AValues = cursor.fetchone()
        # getAValues = list(AValues.values())
        # AValues = ' '.join(map(str,getAValues))
        
        # connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        # with connection.cursor() as cursor:
        #     cursor.execute('select max(d_order_id) from d_order_info')
        # connection.commit()

    
        #Display the todays inquiries by SORTED
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            data=cursor.execute('select custo_id,time_stamp,d_mode,t_payment,ownership,p_mode from today_inquiry order by 1 desc')
            #today = cursor.execute('select date_format(time_stamp, '%d) as `today` from today_inquiry')
            
        connection.commit()
        
        for i in range(data):
            myBorrowList=cursor.fetchone()
            self.TWTodayTable.setItem(i,0,QTableWidgetItem('{}'.format(myBorrowList['custo_id'])))
            self.TWTodayTable.setItem(i,1,QTableWidgetItem('{}'.format(myBorrowList['time_stamp'])))
            self.TWTodayTable.setItem(i,2,QTableWidgetItem('{}'.format(myBorrowList['d_mode'])))
            self.TWTodayTable.setItem(i,3,QTableWidgetItem('{}'.format(myBorrowList['t_payment'])))
            self.TWTodayTable.setItem(i,4,QTableWidgetItem('{}'.format(myBorrowList['ownership'])))
            self.TWTodayTable.setItem(i,5,QTableWidgetItem('{}'.format(myBorrowList['p_mode'])))
        
    
        try:
            connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                #latest=cursor.execute('select time_stamp,d_mode,t_payment,ownership,p_mode from today_inquiry order by 1 desc')
                cursor.execute('SELECT time_stamp FROM today_inquiry ORDER BY time_stamp desc limit 1;')
            connection.commit()
            AValues = cursor.fetchone()
            getAValues = list(AValues.values())
            Frow = ' '.join(map(str,getAValues))
            Frow = list(Frow)
            Frow = Frow[8:10]
            Frow = "".join(Frow)
            
            
        except:
            print("No Data")
            pass

        # for i in range(latest):
        #     myBorrowList=cursor.fetchone()
        #     self.TWTodayTable.setItem(i,0,QTableWidgetItem('{}'.format(myBorrowList['time_stamp'])))
        #     self.TWTodayTable.setItem(i,1,QTableWidgetItem('{}'.format(myBorrowList['d_mode'])))
        #     self.TWTodayTable.setItem(i,2,QTableWidgetItem('{}'.format(myBorrowList['t_payment'])))
        #     self.TWTodayTable.setItem(i,3,QTableWidgetItem('{}'.format(myBorrowList['ownership'])))
        #     self.TWTodayTable.setItem(i,4,QTableWidgetItem('{}'.format(myBorrowList['p_mode'])))


        
    

    #Get date of latest row
        try:
            from datetime import date
            today = date.today()
            TodayDate = today.strftime("%d")
    
            if int(Frow) != int(TodayDate):
                connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
                with connection.cursor() as cursor:
                    cursor.execute('insert into history_inquiry select * from today_inquiry')
                    cursor.execute('truncate today_inquiry')
                    TodayInquiry=cursor.execute('select custo_id,time_stamp,d_mode,t_payment,ownership,p_mode from today_inquiry order by 1 desc')
                    HistoryInquiry=cursor.execute('select * from history_inquiry')
                connection.commit()

                for i in range(TodayInquiry):
                    myBorrowList=cursor.fetchone()
                    self.TWTodayTable.setItem(i,0,QTableWidgetItem('{}'.format(myBorrowList['custo_id'])))
                    self.TWTodayTable.setItem(i,1,QTableWidgetItem('{}'.format(myBorrowList['time_stamp'])))
                    self.TWTodayTable.setItem(i,2,QTableWidgetItem('{}'.format(myBorrowList['d_mode'])))
                    self.TWTodayTable.setItem(i,3,QTableWidgetItem('{}'.format(myBorrowList['t_payment'])))
                    self.TWTodayTable.setItem(i,4,QTableWidgetItem('{}'.format(myBorrowList['ownership'])))
                    self.TWTodayTable.setItem(i,5,QTableWidgetItem('{}'.format(myBorrowList['p_mode'])))
                
                for i in range(HistoryInquiry):
                    myBorrowList=cursor.fetchone()
                    self.TWHistoryTable.setItem(i,0,QTableWidgetItem('{}'.format(myBorrowList['custo_id'])))
                    self.TWHistoryTable.setItem(i,1,QTableWidgetItem('{}'.format(myBorrowList['times_stamp'])))
                    self.TWHistoryTable.setItem(i,2,QTableWidgetItem('{}'.format(myBorrowList['d_mode'])))
                    self.TWHistoryTable.setItem(i,3,QTableWidgetItem('{}'.format(myBorrowList['t_payment'])))
                    self.TWHistoryTable.setItem(i,4,QTableWidgetItem('{}'.format(myBorrowList['ownership'])))
                    self.TWHistoryTable.setItem(i,5,QTableWidgetItem('{}'.format(myBorrowList['p_mode'])))
                
                
        except:
            print("No Data 2")
            pass
        
        
        # connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        # with connection.cursor() as cursor:
        #     #latest=cursor.execute('select time_stamp,d_mode,t_payment,ownership,p_mode from today_inquiry order by 1 desc')
        #     total = cursor.execute('SELECT * from today_inquiry')
        #     self.LBTodayValues.setText(str(total))
        #     print(total)
        #     d="Door delivery"
        #     t_delivery = cursor.execute('SELECT COUNT(1) FROM today_inquiry WHERE d_mode = %s',(d))
        #     self.LDValues.setText(str(t_delivery))
        #     print(t_delivery)
        #     s="Self pick-up"
        #     t_pickup = cursor.execute('SELECT COUNT(1) FROM today_inquiry WHERE d_mode = %s',(s))
        #     self.LNDValues.setText(str(t_pickup))
        #     print(t_pickup)
        # connection.commit()
        
        
        
        #Display the number of Delivery and Self Pickup
        d="Door delivery"
        s="Self pick-up"
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            #latest=cursor.execute('select time_stamp,d_mode,t_payment,ownership,p_mode from today_inquiry order by 1 desc')
            total = cursor.execute('SELECT * from today_inquiry')
            self.LBTodayValues.setText(str(total))
            print(total)
            
            cursor.execute("""SELECT COUNT(1) FROM today_inquiry WHERE d_mode = %s""",(d))
            t_delivery =  cursor.fetchone()
            t_delivery = list(t_delivery.values())
            t_delivery = ' '.join(map(str, t_delivery))
            self.LDValues.setText(str(t_delivery))

            cursor.execute("""SELECT COUNT(1) FROM today_inquiry WHERE d_mode = %s""",(s))
            t_pickup =  cursor.fetchone()
            t_pickup = list(t_pickup.values())
            t_pickup = ' '.join(map(str, t_pickup))
            self.LNDValues.setText(str(t_pickup))
        connection.commit() 
        
        self.image_NI.setHidden(True)
        self.image_OV.setHidden(True)
        self.image_S.setHidden(True)
        self.image_R.setHidden(True)
        self.image_RR.setHidden(False)
        self.GBDOI_N.setHidden(True)
        
        from ForReports import Reports
        self.GBToday.setHidden(False)
        self.GBNumberDelivery.setHidden(False)
        self.GBNumberNonDelivery.setHidden(False)
        self.GBTodayList.setHidden(False)
        self.GBHistory.setHidden(False)
        
        from ForOverview import OverviewWindow    
        self.GBQueueBox.setHidden(True)
        self.GBReady.setHidden(True)
        
        from ForInquiry import Delivery
        self.GBType.setHidden(True)
        self.GBCI.setHidden(True)
        self.GBDOI.setHidden(True)
        self.GBSubmitCancel.setHidden(True)
        
        from ForStorage import Storage
        self.GBAvailable.setHidden(True)
        self.GBBorrow.setHidden(True)
        self.GBTotal.setHidden(True)
        self.GBList.setHidden(True)
        self.GBRate.setHidden(True)
        
        from ForRecords import Records
        self.GBDeliveryOption.setHidden(True)
        

    def clickedSlim(self):
        self.LOther.setDisabled(True)
        self.LESize.setDisabled(True)
        self.CBUnit.setDisabled(True)
        typeList.clear()
        if self.RBSlim.isChecked() == True:
            typeList.append(self.RBSlim.text())
            typeList.append(self.RBSlim.text())

    def clickedRound(self):
        self.LOther.setDisabled(True)
        self.LESize.setDisabled(True)
        self.CBUnit.setDisabled(True)
        typeList.clear()
        if self.RBRound.isChecked() == True:
            typeList.append(self.RBRound.text())
            typeList.append(self.RBRound.text())

    def clickedOther(self):
        self.LOther.setDisabled(True)
        self.LESize.setDisabled(True)
        self.CBUnit.setDisabled(True)
        typeList.clear()
        if self.RBOther.isChecked() == True:
            self.LOther.setDisabled(False)
            self.LESize.setDisabled(False)
            self.CBUnit.setDisabled(False)
        
            typeList.append(self.RBOther.text())

    def clickedOwn(self):
        ownershipList.clear()
        if self.RBOwn.isChecked() == True:
            ownershipList.append(self.RBOwn.text())

    def clickedLend(self):
        ownershipList.clear()
        if self.RBLend.isChecked() == True:
            ownershipList.append(self.RBLend.text())
            
    def clickedDelivery(self):
        deliveryList.clear()
        if self.RBDelivery.isChecked() == True:
            deliveryList.append(self.RBDelivery.text())

    def clickedPick(self):
        deliveryList.clear()
        if self.RBPick.isChecked() == True:
            deliveryList.append(self.RBPick.text())
            
    def clickedCDelivery(self):
        paymentList.clear()
        if self.RBCDelivery.isChecked() == True:
            paymentList.append(self.RBCDelivery.text())

    def clickedUpfront(self):
        paymentList.clear()
        if self.RBUpfront.isChecked() == True:
            paymentList.append(self.RBUpfront.text())
        
    def clickedForDelivery(self):
        self.GBCI.setDisabled(False)
        self.GBDOI.setDisabled(False)
        self.GBDOI_N.setDisabled(True)
        self.GBDOI_N.setHidden(True)
        stateList.clear()
        stateList.append("For Deliver")
        
    def clickedForNonDelivery(self):
        self.GBCI.setDisabled(True)
        self.GBDOI.setDisabled(True)
        self.GBDOI_N.setDisabled(False)
        self.GBDOI_N.setHidden(False)
        stateList.clear()
        stateList.append("For Pickup")
        
    def clickedSlim_N(self):
        self.LOther_N.setDisabled(True)
        self.LESize_N.setDisabled(True)
        self.CBUnit_N.setDisabled(True)
        typeList_N.clear()
        if self.RBSlim_N.isChecked() == True:
            typeList_N.append(self.RBSlim_N.text())
            typeList_N.append(self.RBSlim_N.text())

    def clickedRound_N(self):
        self.LOther_N.setDisabled(True)
        self.LESize_N.setDisabled(True)
        self.CBUnit_N.setDisabled(True)
        typeList_N.clear()
        if self.RBRound_N.isChecked() == True:
            typeList_N.append(self.RBRound_N.text())
            typeList_N.append(self.RBRound_N.text())
            
    def clickedOther_N(self):
        self.LOther_N.setDisabled(True)
        self.LESize_N.setDisabled(True)
        self.CBUnit_N.setDisabled(True)
        typeList_N.clear()
        if self.RBOther_N.isChecked() == True:
            self.LOther_N.setDisabled(False)
            self.LESize_N.setDisabled(False)
            self.CBUnit_N.setDisabled(False)
        
            typeList_N.append(self.RBOther_N.text())


    def clickedSubmit(self):
        #For Deliver Option
        order_type = " ".join(stateList)
        if ("For Deliver" in stateList):
            #Customer Data 
            f_name = self.LEFname.text()
            l_name = self.LELname.text()
            m_number = int(self.LENumber.text())
            h_number = self.LEHnumber.text()
            s_name = self.LEStreet.text()
            b_name = self.LEBrgy.text()
            c_name = self.LECity.text()
            data = (f_name,l_name,str(m_number),h_number,s_name,b_name,c_name)
            
    
            
            self.otherList = []
            if ("Other" in typeList):
                self.otherList.append(self.LESize.text())
                self.otherList.append(self.CBUnit.currentText())
                typeList.append("".join(self.otherList))

            self.WCIDList = []
            if ("Slim" in typeList):
                self.WCIDList.clear
                self.WCIDList.append("1")
            if ("Round" in typeList):
                self.WCIDList.clear
                self.WCIDList.append("2")
            if ("Other" in typeList):
                self.WCIDList.clear
                self.WCIDList.append("3")

            connection = pymysql.connect(host='localhost', user='root', password='', db='ws_db', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                cursor.execute('select price from wc_pricing where wc_id = %s',(' '.join(self.WCIDList)))
            connection.commit()
            ThePrice = cursor.fetchone()
            priceList = list(ThePrice.values())
            price = ' '.join(map(str,priceList))
            
    
            
            #Order Data
            wc_id = ' '.join(self.WCIDList)
            
            c_type = ''.join(typeList[1])
            quantity = self.LEQuantity.text()
            t_payment = int(price) * int(quantity)
            ownership = ' '.join(ownershipList)
            delivery = ' '.join(deliveryList)
            payment = ' '.join(paymentList)

            D_address = (h_number + ", " + s_name + ", " + b_name + ", " + c_name)
            D_name = (l_name + ", " + f_name)
        
            NoEmptyField1 = False
            for i in data:
                if(len(i) == 0):
                    NoEmptyField1 = True
                    break

            if(NoEmptyField1):
                self.messagebox = QMessageBox()
                self.messagebox.setText("Please complete the entry.")
                self.messagebox.setWindowTitle("Message!")
                self.messagebox.setIcon(QMessageBox.Information)
                self.messagebox.show()

            else:
                connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
                with connection.cursor() as cursor:
                    cursor.execute("insert into customer_info(f_name,l_name,m_number,h_number,s_name,b_name,c_name) values (%s,%s,%s,%s,%s,%s,%s)",(f_name,l_name,int(m_number),h_number,s_name,b_name,c_name))	
                    cursor.execute("insert into d_order_info(water_container_id,total_payment,c_type,quantity,ownership,d_mode,p_mode) values (%s,%s,%s,%s,%s,%s,%s)",(wc_id,t_payment,c_type,quantity,ownership,delivery,payment))
                    cursor.execute("insert into queue_order(order_type,quantity,wc_types,address,c_name,t_payment) values (%s,%s,%s,%s,%s,%s)",(delivery,quantity,c_type,D_address,D_name,t_payment))
                    
                    connection.commit()
                    self.messagebox = QMessageBox()
                    self.messagebox.setText("Inquiry Successfuly Added")
                    self.messagebox.setWindowTitle("Message!")
                    self.messagebox.setIcon(QMessageBox.Information)
                    self.messagebox.show()
                    
                    self.LEFname.clear()
                    self.LELname.clear()
                    self.LENumber.clear()
                    self.LEHnumber.clear()
                    self.LEStreet.clear()
                    self.LEBrgy.clear()
                    self.LECity.clear()


            #List Borrowed
            #For those customer who borrowed water container
            if self.RBLend.isChecked():
                connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
                with connection.cursor() as cursor:
                    cursor.execute('insert into list_borrowed(num_c,type_c,c_name,m_num,address) values(%s,%s,%s,%s,%s)',(quantity,c_type,D_name,m_number,D_address))
                    #num_borrowed=cursor.execute('select * from list_borrowed')
                    cursor.execute('select * from list_borrowed')
                connection.commit()
                # for i in range(num_borrowed,0,-1):
                #     myBorrowList=cursor.fetchone()
                #     self.TWLTable.setItem(i,0,QTableWidgetItem('\t{}'.format(myBorrowList['num_c'])))
                #     self.TWLTable.setItem(i,1,QTableWidgetItem('{}'.format(myBorrowList['type_c'])))
                #     self.TWLTable.setItem(i,2,QTableWidgetItem('{}'.format(myBorrowList['c_name'])))
                #     self.TWLTable.setItem(i,3,QTableWidgetItem('{}'.format(myBorrowList['m_num'])))
                #     self.TWLTable.setItem(i,4,QTableWidgetItem('{}'.format(myBorrowList['address'])))

                # spaces = ' '
                # for i in range(num_borrowed,0,-1):
                #     myBorrowList=cursor.fetchone()
                #     i -= 1
                #     self.TWLTable.setItem(i,0,QTableWidgetItem('{}{}'.format(spaces*22,myBorrowList['num_c'])))
                #     self.TWLTable.setItem(i,1,QTableWidgetItem('{}'.format(myBorrowList['type_c'])))
                #     self.TWLTable.setItem(i,2,QTableWidgetItem('{}'.format(myBorrowList['c_name'])))
                #     self.TWLTable.setItem(i,3,QTableWidgetItem('{}'.format(myBorrowList['m_num'])))
                #     self.TWLTable.setItem(i,4,QTableWidgetItem('{}'.format(myBorrowList['address'])))

                connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
                with connection.cursor() as cursor:
                    borrowRow = cursor.execute('select * from list_borrowed')
                    cursor.execute('update in_storage set borrowed = %s where id = 1',borrowRow)
                    cursor.execute('select available from in_storage where id = 1')
                connection.commit()
                
                AValues = cursor.fetchone()
                getAValues = list(AValues.values())
                AValues = ' '.join(map(str,getAValues))
                Total = int(AValues) + borrowRow
                self.LBValues.setText(str(borrowRow))
                
                
                connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
                with connection.cursor() as cursor:
                    cursor.execute('update in_storage set total = %s where id = 1',Total)
                connection.commit()                
                self.LTValues.setText(str(Total))
                
        
                
            # else:
            #     connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
            #     with connection.cursor() as cursor:
            #         #updateBorrowedTable = cursor.execute("select * from list_borrowed")
            #         cursor.execute("select * from list_borrowed")
            #     #spaces = " "    
            #     # for i in range(updateBorrowedTable):
            #     #     customers2=cursor.fetchone()
            #     #     #i -= 1
            #     #     self.TWLTable.setItem(i,0,QTableWidgetItem('\t{}'.format(customers2['num_c'])))
            #     #     self.TWLTable.setItem(i,1,QTableWidgetItem('{}'.format(customers2['type_c'])))
            #     #     self.TWLTable.setItem(i,2,QTableWidgetItem('{}'.format(customers2['c_name'])))
            #     #     self.TWLTable.setItem(i,3,QTableWidgetItem('{}'.format(customers2['m_num'])))
            #     #     self.TWLTable.setItem(i,4,QTableWidgetItem('{}'.format(customers2['address'])))
                    
                    
            #     # for i in range(updateBorrowedTable,0,-1):
            #     #     myBorrowList=cursor.fetchone()
            #     #     i -= 1
            #     #     self.TWLTable.setItem(i,0,QTableWidgetItem('{}{}'.format(spaces*22,myBorrowList['num_c'])))
            #     #     self.TWLTable.setItem(i,1,QTableWidgetItem('{}'.format(myBorrowList['type_c'])))
            #     #     self.TWLTable.setItem(i,2,QTableWidgetItem('{}'.format(myBorrowList['c_name'])))
            #     #     self.TWLTable.setItem(i,3,QTableWidgetItem('{}'.format(myBorrowList['m_num'])))
            #     #     self.TWLTable.setItem(i,4,QTableWidgetItem('{}'.format(myBorrowList['address'])))
                    
                    

            if ("Other" in typeList):
                self.otherList.append(self.LESize.text())
                self.otherList.append(self.CBUnit.currentText())
                typeList.pop(1)
                
            self.RBSlim.setAutoExclusive(False) 
            self.RBSlim.setChecked(False)
            self.RBRound.setAutoExclusive(False) 
            self.RBRound.setChecked(False)
            self.RBOther.setAutoExclusive(False) 
            self.RBOther.setChecked(False)
            self.RBOwn.setAutoExclusive(False) 
            self.RBOwn.setChecked(False)
            self.RBLend.setAutoExclusive(False) 
            self.RBLend.setChecked(False)
            self.RBDelivery.setAutoExclusive(False) 
            self.RBDelivery.setChecked(False)
            self.RBPick.setAutoExclusive(False) 
            self.RBPick.setChecked(False)
            self.RBCDelivery.setAutoExclusive(False) 
            self.RBCDelivery.setChecked(False)
            self.RBUpfront.setAutoExclusive(False) 
            self.RBUpfront.setChecked(False)
            self.LESize.setText("")
            self.LEQuantity.setText("")
            
            connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                updateQueueTable = cursor.execute("select * from queue_order")
                
                
            connection.commit()
            for i in range(updateQueueTable):
                customers2=cursor.fetchone()
                #i -= 1
                self.TWQTable.setItem(i,0,QTableWidgetItem('{}'.format(customers2['order_type'])))
                self.TWQTable.setItem(i,1,QTableWidgetItem('{}'.format(customers2['quantity'])))
                self.TWQTable.setItem(i,2,QTableWidgetItem('{}'.format(customers2['wc_types'])))
                self.TWQTable.setItem(i,3,QTableWidgetItem('{}'.format(customers2['address'])))
                self.TWQTable.setItem(i,4,QTableWidgetItem('{}'.format(customers2['c_name'])))
                self.TWQTable.setItem(i,5,QTableWidgetItem('{}'.format(customers2['t_payment'])))
            
            

            
        #For Self pickup option
        else:
            
            if ("Other" in typeList_N):
                self.otherList_N.append(self.LESize_N.text())
                self.otherList_N.append(self.CBUnit_N.currentText())
                typeList_N.append("".join(self.otherList_N))
                
            self.WCIDList_N = []
            if ("Slim" in typeList_N):
                self.WCIDList_N.clear
                self.WCIDList_N.append("1")
            if ("Round" in typeList_N):
                self.WCIDList_N.clear
                self.WCIDList_N.append("2")
            if ("Other" in typeList_N):
                self.WCIDList_N.clear
                self.WCIDList_N.append("3")
            
            
            connection = pymysql.connect(host='localhost', user='root', password='', db='ws_db', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                cursor.execute('select price from wc_pricing where wc_id = %s',(' '.join(self.WCIDList_N)))
                #cursor.execute("insert into queue_order(order_type,quantity,wc_types,address,c_name,t_payment) values (%s,%s,%s,%s,%s,%s)",(order_type,quantity,c_type,address,name,t_payment_N))
            connection.commit()
            ThePrice = cursor.fetchone()
            priceList = list(ThePrice.values())
            price = ' '.join(map(str,priceList))
                
            
            
            
            wc_id_N = ' '.join(self.WCIDList_N)
            
            c_type_N = ''.join(typeList_N[1])
            quantity_N = self.LEQuantity_N.text()
            t_payment_N = int(price) * int(quantity_N)
            ownership_N = self.RBOwn_N.text()
            delivery_N = self.RBPick_N.text()
            payment_N = self.RBUpfront_N.text()
            
            address = "N/A"
            name = "N/A"
            

            # connection = pymysql.connect(host='localhost', user='root', password='', db='ws_db', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            # with connection.cursor() as cursor:
            #     #cursor.execute('select price from wc_pricing where wc_id = %s',(' '.join(self.WCIDList_N)))
            #     cursor.execute("insert into queue_order(order_type,quantity,wc_types,address,c_name,t_payment) values (%s,%s,%s,%s,%s,%s)",(order_type,quantity_N,c_type_N,address,name,t_payment_N))    
            # connection.commit()
            # ThePrice = cursor.fetchone()
            # priceList = list(ThePrice.values())
            # price = ' '.join(map(str,priceList))
                
            #Order Data
            

            
        
            if((self.RBSlim_N.isChecked() or self.RBRound_N.isChecked() or self.RBOther_N.isChecked()) and int(quantity_N)>0):
                connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
                with connection.cursor() as cursor:
                    cursor.execute("insert into nd_order_info(water_container_id,total_payment,c_type,quantity,ownership,d_mode,p_mode) values (%s,%s,%s,%s,%s,%s,%s)",(wc_id_N,t_payment_N,c_type_N,quantity_N,ownership_N,delivery_N,payment_N))
                    cursor.execute("insert into queue_order(order_type,quantity,wc_types,address,c_name,t_payment) values (%s,%s,%s,%s,%s,%s)",(order_type,quantity_N,c_type_N,address,name,t_payment_N))
                    connection.commit()
                    self.messagebox = QMessageBox()
                    self.messagebox.setText("Inquiry Successfuly Added")
                    self.messagebox.setWindowTitle("Message!")
                    self.messagebox.setIcon(QMessageBox.Information)
                    self.messagebox.show()
            

            else:
                self.messagebox = QMessageBox()
                self.messagebox.setText("Please complete the entry.")
                self.messagebox.setWindowTitle("Message!")
                self.messagebox.setIcon(QMessageBox.Information)
                self.messagebox.show()
                


            if ("Other" in typeList_N):
                self.otherList_N.append(self.LESize_N.text())
                self.otherList_N.append(self.CBUnit_N.currentText())
                typeList_N.pop(1)
                
            self.RBSlim_N.setAutoExclusive(False) 
            self.RBSlim_N.setChecked(False)
            self.RBRound_N.setAutoExclusive(False) 
            self.RBRound_N.setChecked(False)
            self.RBOther_N.setAutoExclusive(False) 
            self.RBOther_N.setChecked(False)
            self.LESize_N.setText("")
            self.LEQuantity_N.setText("")
            
            connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                numberofrows2=cursor.execute('select * from queue_order')
                
            #connection.commit()
            for i in range(numberofrows2):
                customers2=cursor.fetchone()
                #i -= 1
                self.TWQTable.setItem(i,0,QTableWidgetItem('{}'.format(customers2['order_type'])))
                self.TWQTable.setItem(i,1,QTableWidgetItem('{}'.format(customers2['quantity'])))
                self.TWQTable.setItem(i,2,QTableWidgetItem('{}'.format(customers2['wc_types'])))
                self.TWQTable.setItem(i,3,QTableWidgetItem('{}'.format(customers2['address'])))
                self.TWQTable.setItem(i,4,QTableWidgetItem('{}'.format(customers2['c_name'])))
                self.TWQTable.setItem(i,5,QTableWidgetItem('{}'.format(customers2['t_payment'])))

        #Update the table of REACORDS
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            ForRecords = cursor.execute('select * from customer_info')

        for i in range(ForRecords):
                customers2=cursor.fetchone()
                #i -= 1
                self.TWDOTable.setItem(i,0,QTableWidgetItem('{}'.format(customers2['d_order_id'])))
                self.TWDOTable.setItem(i,1,QTableWidgetItem('{}'.format(customers2['f_name'])))
                self.TWDOTable.setItem(i,2,QTableWidgetItem('{}'.format(customers2['l_name'])))
                self.TWDOTable.setItem(i,3,QTableWidgetItem('{}'.format(customers2['m_number'])))
                self.TWDOTable.setItem(i,4,QTableWidgetItem('{}'.format(customers2['h_number'])))
                self.TWDOTable.setItem(i,5,QTableWidgetItem('{}'.format(customers2['s_name'])))
                self.TWDOTable.setItem(i,5,QTableWidgetItem('{}'.format(customers2['b_name'])))
                self.TWDOTable.setItem(i,5,QTableWidgetItem('{}'.format(customers2['c_name'])))


        #REPORT
        #Join two tables of delevery and non-delivery
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            cursor.execute('truncate today_inquiry')
            cursor.execute('insert into today_inquiry (custo_id,time_stamp,d_mode, t_payment,ownership,p_mode) select d_order_id, date_time,d_mode,total_payment,ownership,p_mode from d_order_info')
            cursor.execute('insert into today_inquiry (custo_id,time_stamp,d_mode, t_payment,ownership,p_mode) select d_order_id, date_time,d_mode,total_payment,ownership,p_mode from nd_order_info')
            data=cursor.execute('select custo_id,time_stamp,d_mode,t_payment,ownership,p_mode from today_inquiry order by 1 desc')
        connection.commit()


        for i in range(data):
            myBorrowList=cursor.fetchone()
            self.TWTodayTable.setItem(i,0,QTableWidgetItem('{}'.format(myBorrowList['custo_id'])))
            self.TWTodayTable.setItem(i,1,QTableWidgetItem('{}'.format(myBorrowList['time_stamp'])))
            self.TWTodayTable.setItem(i,2,QTableWidgetItem('{}'.format(myBorrowList['d_mode'])))
            self.TWTodayTable.setItem(i,3,QTableWidgetItem('{}'.format(myBorrowList['t_payment'])))
            self.TWTodayTable.setItem(i,4,QTableWidgetItem('{}'.format(myBorrowList['ownership'])))
            self.TWTodayTable.setItem(i,5,QTableWidgetItem('{}'.format(myBorrowList['p_mode'])))

        #Display the number of Delivery and Self Pickup
        d="Door delivery"
        s="Self pick-up"
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            #latest=cursor.execute('select time_stamp,d_mode,t_payment,ownership,p_mode from today_inquiry order by 1 desc')
            total = cursor.execute('SELECT * from today_inquiry')
            self.LBTodayValues.setText(str(total))
            print(total)
            
            cursor.execute("""SELECT COUNT(1) FROM today_inquiry WHERE d_mode = %s""",(d))
            t_delivery =  cursor.fetchone()
            t_delivery = list(t_delivery.values())
            t_delivery = ' '.join(map(str, t_delivery))
            self.LDValues.setText(str(t_delivery))

            cursor.execute("""SELECT COUNT(1) FROM today_inquiry WHERE d_mode = %s""",(s))
            t_pickup =  cursor.fetchone()
            t_pickup = list(t_pickup.values())
            t_pickup = ' '.join(map(str, t_pickup))
            self.LNDValues.setText(str(t_pickup))
        connection.commit() 

        


    def clickedUpdateRecords(self,row,column):
        
        

        try:
        
            Info = self.TWDOTable.item(row,column).text()
            custo_id = self.TWDOTable.item(row,0).text()
            f_name = self.TWDOTable.item(row,1).text()
            l_name = self.TWDOTable.item(row,2).text()
            m_number = self.TWDOTable.item(row,3).text()
            h_number = self.TWDOTable.item(row,4).text()
            s_name = self.TWDOTable.item(row,5).text()
            b_name = self.TWDOTable.item(row,6).text()
            c_name = self.TWDOTable.item(row,7).text()


                
            if (len(Info) == 0):
                self.messagebox = QMessageBox()
                self.messagebox.setText("Don't leave any cell blank.")
                self.messagebox.setWindowTitle("Message!")
                self.messagebox.setIcon(QMessageBox.Information)
                self.messagebox.show()
                
                
                connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
                with connection.cursor() as cursor:
                    myrow=cursor.execute('select * from customer_info')
                spaces = " "
                
                for i in range(myrow):
                    myBorrowList=cursor.fetchone()
                    self.TWDOTable.setItem(i,0,QTableWidgetItem(spaces*24+'{}'.format(myBorrowList['d_order_id'])))
                    self.TWDOTable.setItem(i,1,QTableWidgetItem('{}'.format(myBorrowList['f_name'])))
                    self.TWDOTable.setItem(i,2,QTableWidgetItem('{}'.format(myBorrowList['l_name'])))
                    self.TWDOTable.setItem(i,3,QTableWidgetItem('{}'.format(myBorrowList['m_number'])))
                    self.TWDOTable.setItem(i,4,QTableWidgetItem('{}'.format(myBorrowList['h_number'])))
                    self.TWDOTable.setItem(i,5,QTableWidgetItem('{}'.format(myBorrowList['s_name'])))
                    self.TWDOTable.setItem(i,6,QTableWidgetItem('{}'.format(myBorrowList['b_name'])))
                    self.TWDOTable.setItem(i,7,QTableWidgetItem('{}'.format(myBorrowList['c_name'])))

            
        
            else:
                connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
                with connection.cursor() as cursor:																		
                    cursor.execute('update customer_info set f_name = %s,l_name= %s,m_number= %s,h_number= %s,s_name = %s,b_name= %s,c_name= %s where d_order_id = %s ',(f_name,l_name,m_number,h_number,s_name,b_name,c_name,custo_id))

                connection.commit()
        
        except:
            print("xxx")
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
            

    def clickedPushLatest(self):
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            cursor.execute('select min(q_id) from queue_order')
        connection.commit()
        maxID = cursor.fetchone()
        getMaxId = list(maxID.values())
        maxID = ' '.join(map(str,getMaxId))
        print(maxID)
        
        
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO rdy_togo SELECT * FROM queue_order WHERE q_id=%s',int(maxID))
            
            
            ready=cursor.execute('select * from rdy_togo')
        connection.commit()
        for ii in range(ready,0,-1):
            customers1=cursor.fetchone()
            ii -= 1
            self.TWRTable.setItem(ii,0,QTableWidgetItem('{}'.format(customers1['order_type'])))
            self.TWRTable.setItem(ii,1,QTableWidgetItem('{}'.format(customers1['quantity'])))
            self.TWRTable.setItem(ii,2,QTableWidgetItem('{}'.format(customers1['wc_types'])))
            self.TWRTable.setItem(ii,3,QTableWidgetItem('{}'.format(customers1['address'])))
            self.TWRTable.setItem(ii,4,QTableWidgetItem('{}'.format(customers1['c_name'])))
            self.TWRTable.setItem(ii,5,QTableWidgetItem('{}'.format(customers1['t_payment'])))
            
            
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM queue_order WHERE q_id = %s',maxID)
        connection.commit()
        
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            numberofrows2=cursor.execute('select * from queue_order')
            
        connection.commit()
        
        for i in range(numberofrows2):
            customers2=cursor.fetchone()
            
            self.TWQTable.setItem(i,0,QTableWidgetItem('{}'.format(customers2['order_type'])))
            self.TWQTable.setItem(i,1,QTableWidgetItem('{}'.format(customers2['quantity'])))
            self.TWQTable.setItem(i,2,QTableWidgetItem('{}'.format(customers2['wc_types'])))
            self.TWQTable.setItem(i,3,QTableWidgetItem('{}'.format(customers2['address'])))
            self.TWQTable.setItem(i,4,QTableWidgetItem('{}'.format(customers2['c_name'])))
            self.TWQTable.setItem(i,5,QTableWidgetItem('{}'.format(customers2['t_payment'])))
            
        self.TWQTable.setRowCount(numberofrows2)
    
    def clickedAdd(self):
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            num_borrowed=cursor.execute('select available from in_storage where id = 1')
        connection.commit()
        AValues = cursor.fetchone()
        getAValues = list(AValues.values())
        AValues = ' '.join(map(str,getAValues))
        
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            num_borrowed=cursor.execute('update in_storage set available = %s where id = 1',(int(self.LEValue.text()) + int(AValues)))
        connection.commit()
        
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            cursor.execute('select available from in_storage where id=1')
        connection.commit()
        AValues = cursor.fetchone()
        getAValues = list(AValues.values())
        AValues = ' '.join(map(str,getAValues))
        self.LAValues.setText(AValues)
        
        self.LEValue.setText("")
        
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            borrowRow = cursor.execute('select * from list_borrowed')
            cursor.execute('update in_storage set borrowed = %s where id = 1',borrowRow)
            cursor.execute('select available from in_storage where id = 1')
        connection.commit()
        
        AValues = cursor.fetchone()
        getAValues = list(AValues.values())
        AValues = ' '.join(map(str,getAValues))
        print(getAValues)
        print(borrowRow)
        Total = int(AValues) + borrowRow
        self.LBValues.setText(str(borrowRow))
        self.LTValues.setText(str(Total))
        
    def clickedDelete(self):
        #self.LAValues.text()
        #self.LBValues.text()
        #self.LTValues.text()
        #self.LEValue.text()
        
        #Get the total value of available
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            cursor.execute('select available from in_storage where id = 1')
        connection.commit()
        AValues = cursor.fetchone()
        getAValues = list(AValues.values())
        AValues = ' '.join(map(str,getAValues))
        
        AValues = int(AValues) - int(self.LEValue.text())
        
        #Get the total value of total
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            cursor.execute('select total from in_storage where id = 1')
        connection.commit()
        AValues1 = cursor.fetchone()
        getAValues1 = list(AValues1.values())
        AValues1 = ' '.join(map(str,getAValues1))
        
        AValues1 = int(AValues1) - int(self.LEValue.text())
        
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            borrowRow = cursor.execute('select * from list_borrowed')
            cursor.execute('update in_storage set available = %s, total = %s where id = 1',(AValues, AValues1))
            cursor.execute('select available from in_storage where id = 1')
        connection.commit()
        
        self.LAValues.setText(str(AValues))
        self.LTValues.setText(str(AValues1))
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def clickedLogout(self):
        import loginWindow
        self.newWindow = loginWindow.mainWindow()
        self.newWindow.show()
        self.hide()



    def clickedOverview(self):
        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            numberofrows2=cursor.execute('select * from queue_order')
            
        connection.commit()
        for i in range(numberofrows2):
            customers2=cursor.fetchone()
            #i -= 1
            self.TWQTable.setItem(i,0,QTableWidgetItem('{}'.format(customers2['order_type'])))
            self.TWQTable.setItem(i,1,QTableWidgetItem('{}'.format(customers2['quantity'])))
            self.TWQTable.setItem(i,2,QTableWidgetItem('{}'.format(customers2['wc_types'])))
            self.TWQTable.setItem(i,3,QTableWidgetItem('{}'.format(customers2['address'])))
            self.TWQTable.setItem(i,4,QTableWidgetItem('{}'.format(customers2['c_name'])))
            self.TWQTable.setItem(i,5,QTableWidgetItem('{}'.format(customers2['t_payment'])))
        

        connection = pymysql.connect(host='localhost',user='root',password='',db='ws_db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            ready=cursor.execute('select * from rdy_togo')
            
        for ii in range(ready,0,-1):
            customers1=cursor.fetchone()
            ii -= 1
            self.TWRTable.setItem(ii,0,QTableWidgetItem('{}'.format(customers1['order_type'])))
            self.TWRTable.setItem(ii,1,QTableWidgetItem('{}'.format(customers1['quantity'])))
            self.TWRTable.setItem(ii,2,QTableWidgetItem('{}'.format(customers1['wc_types'])))
            self.TWRTable.setItem(ii,3,QTableWidgetItem('{}'.format(customers1['address'])))
            self.TWRTable.setItem(ii,4,QTableWidgetItem('{}'.format(customers1['c_name'])))
            self.TWRTable.setItem(ii,5,QTableWidgetItem('{}'.format(customers1['t_payment'])))
        
        
        
        self.image_NI.setHidden(True)
        self.image_OV.setHidden(False)
        self.image_S.setHidden(True)
        self.image_R.setHidden(True)
        self.image_RR.setHidden(True)
        self.GBDOI_N.setHidden(True)
        
        from ForReports import Reports
        self.GBToday.setHidden(True)
        self.GBNumberDelivery.setHidden(True)
        self.GBNumberNonDelivery.setHidden(True)
        self.GBTodayList.setHidden(True)
        self.GBHistory.setHidden(True)
        
        from ForRecords import Records
        self.GBDeliveryOption.setHidden(True)
        
        
        from ForStorage import Storage
        self.GBAvailable.setHidden(True)
        self.GBBorrow.setHidden(True)
        self.GBTotal.setHidden(True)
        self.GBList.setHidden(True)
        self.GBRate.setHidden(True)
        
        from ForOverview import OverviewWindow    
        self.GBQueueBox.setHidden(False)
        self.GBReady.setHidden(False)
        
        from ForInquiry import Delivery
        self.GBType.setHidden(True)
        self.GBCI.setHidden(True)
        self.GBDOI.setHidden(True)
        self.GBSubmitCancel.setHidden(True)



        

if __name__ == '__main__':
	App = QApplication(sys.argv)
	window = Home()
	window.show()
	sys.exit(App.exec_())

