import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
import pymysql.cursors

def Delivery(self):
    #Type of order
    self.GBType = QGroupBox(self)
    self.GBType.move(350,220)
    self.GBType.resize(520,150)
    self.GBType.setStyleSheet("QGroupBox {background-color:  rgb(255, 255, 255);}")

    self.LType = QLabel("TYPE OF ORDER",self.GBType)
    self.LType.move(20,20)
    self.LType.setFont(QFont('Arial',15,QFont.Light))
    
    self.PBDelivery = QPushButton("DELIVERY", self.GBType)
    self.PBDelivery.move(20,60)
    self.PBDelivery.resize(230,70)
    self.PBDelivery.setFont(QFont('Arial',15,QFont.Bold))
    self.PBDelivery.setStyleSheet("""QPushButton {border-image : url(Images/Pick up button1.png);color: white;border-radius: 20;}
                                    QPushButton:hover {border-image : url(Images/Pick up button.png);color: yellow;}""")
    self.PBDelivery.clicked.connect(self.clickedForDelivery)
    
    self.PBSelf = QPushButton("SELF PICK-UP", self.GBType)
    self.PBSelf.move(270,60)
    self.PBSelf.resize(230,70)
    self.PBSelf.setFont(QFont('Arial',15,QFont.Bold))
    self.PBSelf.setStyleSheet("""QPushButton {border-image : url(Images/Delivery Button1.png);color: white;border-radius: 20;}
                                    QPushButton:hover {border-image : url(Images/Delivery Button.png);color: yellow;}""")
    self.PBSelf.clicked.connect(self.clickedForNonDelivery)
    
    #Customer information
    self.GBCI = QGroupBox(self)
    self.GBCI.move(350,390)
    self.GBCI.resize(520,480)
    self.GBCI.setStyleSheet("QGroupBox {background-color:  rgb(255, 255, 255);}")
    self.GBCI.setDisabled(True)
    
    self.LCI = QLabel("CUSTOMER INFORMATION",self.GBCI)
    self.LCI.move(30,20)
    self.LCI.setFont(QFont('Arial',15,QFont.Light))
    
    self.LEFname = QLineEdit(self.GBCI)
    self.LEFname.move(30,60)
    self.LEFname.resize(220,30)
    self.LEFname.setFont(QFont('Arial',11,QFont.Light))
    self.LEFname.setPlaceholderText("First Name")
    self.LEFname.setStyleSheet("QLineEdit {background-color:  rgb(240, 240, 240);border-radius: 5px;}")
    
    self.LELname = QLineEdit(self.GBCI)
    self.LELname.move(270,60)
    self.LELname.resize(220,30)
    self.LELname.setFont(QFont('Arial',11,QFont.Light))
    self.LELname.setPlaceholderText("Last Name")
    self.LELname.setStyleSheet("QLineEdit {background-color:  rgb(240, 240, 240);border-radius: 5px;}")
    
    self.LENumber = QLineEdit(self.GBCI)
    self.LENumber.move(30,100)
    self.LENumber.resize(460,30)
    self.LENumber.setFont(QFont('Arial',11,QFont.Light))
    self.LENumber.setPlaceholderText("Mobile Number")
    self.LENumber.setStyleSheet("QLineEdit {background-color:  rgb(240, 240, 240);border-radius: 5px;}")
    
    self.Line = QGroupBox(self.GBCI)
    self.Line.move(20, 160)
    self.Line.resize(480,3)
    
    self.LAI = QLabel("ADDRESS INFORMATION",self.GBCI)
    self.LAI.move(30,190)
    self.LAI.setFont(QFont('Arial',14,QFont.Light))

    self.LEHnumber = QLineEdit(self.GBCI)
    self.LEHnumber.move(30,230)
    self.LEHnumber.resize(460,30)
    self.LEHnumber.setFont(QFont('Arial',11,QFont.Light))
    self.LEHnumber.setPlaceholderText("House Number")
    self.LEHnumber.setStyleSheet("QLineEdit {background-color:  rgb(240, 240, 240);border-radius: 5px;}")
    
    self.LEStreet = QLineEdit(self.GBCI)
    self.LEStreet.move(30,280)
    self.LEStreet.resize(460,30)
    self.LEStreet.setFont(QFont('Arial',11,QFont.Light))
    self.LEStreet.setPlaceholderText("Street Name")
    self.LEStreet.setStyleSheet("QLineEdit {background-color:  rgb(240, 240, 240);border-radius: 5px;}")
    
    self.LEBrgy = QLineEdit(self.GBCI)
    self.LEBrgy.move(30,330)
    self.LEBrgy.resize(460,30)
    self.LEBrgy.setFont(QFont('Arial',11,QFont.Light))
    self.LEBrgy.setPlaceholderText("Barangay")
    self.LEBrgy.setStyleSheet("QLineEdit {background-color:  rgb(240, 240, 240);border-radius: 5px;}")
    
    self.LECity = QLineEdit(self.GBCI)
    self.LECity.move(30,380)
    self.LECity.resize(460,30)
    self.LECity.setFont(QFont('Arial',11,QFont.Light))
    self.LECity.setPlaceholderText("City")
    self.LECity.setStyleSheet("QLineEdit {background-color:  rgb(240, 240, 240);border-radius: 5px;}")
    
    #Customer order for delivery
    self.GBDOI = QGroupBox(self)
    self.GBDOI.move(890,220)
    self.GBDOI.resize(290,530)
    self.GBDOI.setStyleSheet("QGroupBox {background-color:  rgb(255, 255, 255);}")
    self.GBDOI.setDisabled(True)
    
    self.LDOI = QLabel("ORDER INFORMATION",self.GBDOI)
    self.LDOI.move(20,20)
    self.LDOI.setFont(QFont('Arial',15,QFont.Light))
    
    self.LCType = QLabel("WATER CONTAINER",self.GBDOI)
    self.LCType.move(20,60)
    self.LCType.setFont(QFont('Arial',12,QFont.Light))
    
    self.G1 = QGroupBox(self.GBDOI)
    self.G1.move(10,90)
    self.G1.resize(270,40)
    self.G1.setStyleSheet("QGroupBox {background-color:  rgb(255, 255, 255);border: 1px white;}")

    
    self.layoutG1 = QHBoxLayout(self.G1)
    
    self.RBSlim = QRadioButton("Slim",self.G1)
    self.RBSlim.setFont(QFont('Arial',11,QFont.Light))
    self.RBSlim.clicked.connect(self.clickedSlim)
    
    self.RBRound = QRadioButton("Round",self.G1)
    self.RBRound.setFont(QFont('Arial',11,QFont.Light))
    self.RBRound.clicked.connect(self.clickedRound)

    self.RBOther = QRadioButton("Other",self.G1)
    self.RBOther.setFont(QFont('Arial',11,QFont.Light))
    self.RBOther.clicked.connect(self.clickedOther)
    
    self.layoutG1.addWidget(self.RBSlim)
    self.layoutG1.addWidget(self.RBRound)
    self.layoutG1.addWidget(self.RBOther)
    
    self.G1.setLayout(self.layoutG1)
    
    self.LOther = QLabel("Other",self.GBDOI)
    self.LOther.move(20,140)
    self.LOther.setFont(QFont('Arial',11,QFont.Light))
    self.LOther.setDisabled(True)
    
    self.LESize = QLineEdit(self.GBDOI)
    self.LESize.move(20,160)
    self.LESize.resize(160,25)
    self.LESize.setPlaceholderText("Container Size")
    self.LESize.setFont(QFont('Arial',11,QFont.Light))
    self.LESize.setStyleSheet("QLineEdit {background-color:  rgb(240, 240, 240) ;border-radius: 5px;}")
    self.LESize.setDisabled(True)
    
    self.CBUnit = QComboBox(self.GBDOI)
    self.CBUnit.move(190,160)
    self.CBUnit.resize(80,25)
    self.CBUnit.addItem("L")
    self.CBUnit.addItem("mL")
    self.CBUnit.setFont(QFont('Arial',11,QFont.Light))
    self.CBUnit.setStyleSheet("QComboBox {background-color:  rgb(240, 240, 240) ;border-radius: 5px;}")
    self.CBUnit.setDisabled(True)

    self.LQuantity = QLabel("QUANTITY",self.GBDOI)
    self.LQuantity.move(20,220)
    self.LQuantity.setFont(QFont('Arial',12,QFont.Light))

    self.LEQuantity = QLineEdit(self.GBDOI)
    self.LEQuantity.setStyleSheet("QLineEdit {background-color:  rgb(240, 240, 240) ;border-radius: 5px;}")
    self.LEQuantity.move(20,250)
    self.LEQuantity.resize(250,30)
    self.LEQuantity.setPlaceholderText("Number of water container")
    self.LEQuantity.setFont(QFont('Arial',11,QFont.Light))

    
    
    self.LOwnership = QLabel("OWNERSHIP",self.GBDOI)
    self.LOwnership.move(20,300)
    self.LOwnership.setFont(QFont('Arial',12,QFont.Light))
    
    self.G2 = QGroupBox(self.GBDOI)
    self.G2.move(30,320)
    self.G2.resize(250,40)
    self.G2.setStyleSheet("QGroupBox {background-color:  rgb(255, 255, 255);border: 1px white}")
    
    self.layoutG2 = QHBoxLayout(self.G2)

    self.RBOwn = QRadioButton("Owned",self.G2)
    self.RBOwn.setFont(QFont('Arial',11,QFont.Light))    
    self.RBOwn.clicked.connect(self.clickedOwn)
    
    self.RBLend = QRadioButton("Lend",self.G2)
    self.RBLend.setFont(QFont('Arial',11,QFont.Light)) 
    self.RBLend.clicked.connect(self.clickedLend)
    
    self.layoutG2.addWidget(self.RBOwn)
    self.layoutG2.addWidget(self.RBLend)
    
    self.G2.setLayout(self.layoutG2)
    
    self.LDelivery = QLabel("DELIVERY",self.GBDOI)
    self.LDelivery.move(20,380)
    self.LDelivery.setFont(QFont('Arial',12,QFont.Light))
    
    self.G3 = QGroupBox(self.GBDOI)
    self.G3.move(20,400)
    self.G3.resize(260,40)
    self.G3.setStyleSheet("QGroupBox {background-color:  rgb(255, 255, 255);border: 1px white}")
    
    self.layoutG3 = QHBoxLayout(self.G3)

    self.RBDelivery = QRadioButton("Door delivery",self.G3)
    self.RBDelivery.setFont(QFont('Arial',11,QFont.Light))    
    self.RBDelivery.clicked.connect(self.clickedDelivery)
    
    self.RBPick = QRadioButton("Self pick-up",self.G3)
    self.RBPick.setFont(QFont('Arial',11,QFont.Light)) 
    self.RBPick.clicked.connect(self.clickedPick)
    
    self.layoutG3.addWidget(self.RBDelivery)
    self.layoutG3.addWidget(self.RBPick)
    
    self.G3.setLayout(self.layoutG3)
    
    
    
    self.LPayment = QLabel("PAYMENT",self.GBDOI)
    self.LPayment.move(20,460)
    self.LPayment.setFont(QFont('Arial',12,QFont.Light))
    
    self.G4 = QGroupBox(self.GBDOI)
    self.G4.move(20,480)
    self.G4.resize(260,40)
    self.G4.setStyleSheet("QGroupBox {background-color:  rgb(255, 255, 255);border: 1px white;}")
    
    self.layoutG4 = QHBoxLayout(self.G4)

    self.RBCDelivery = QRadioButton("Cash on delivery",self.G4)
    self.RBCDelivery.setFont(QFont('Arial',11,QFont.Light))    
    self.RBCDelivery.clicked.connect(self.clickedCDelivery)
    
    self.RBUpfront = QRadioButton("Pay upfront",self.G4)
    self.RBUpfront.setFont(QFont('Arial',11,QFont.Light)) 
    self.RBUpfront.clicked.connect(self.clickedUpfront)
    
    self.layoutG4.addWidget(self.RBCDelivery)
    self.layoutG4.addWidget(self.RBUpfront)
    
    self.G4.setLayout(self.layoutG4)
    
    
    #Customer order for NON-delivery
    self.GBDOI_N = QGroupBox(self)
    self.GBDOI_N.move(890,220)
    self.GBDOI_N.resize(290,530)
    self.GBDOI_N.setStyleSheet("QGroupBox {background-color:  rgb(102, 204, 226);}")
    self.GBDOI_N.setDisabled(True)
    self.GBDOI_N.setHidden(True)
    
    self.LDOI_N = QLabel("ORDER INFORMATION",self.GBDOI_N)
    self.LDOI_N.move(20,20)
    self.LDOI_N.setFont(QFont('Arial',15,QFont.Light))
    #self.LDOI_N.setStyleSheet("QLabel {color: white;}")
    
    self.LCType_N = QLabel("WATER CONTAINER",self.GBDOI_N)
    self.LCType_N.move(20,60)
    self.LCType_N.setFont(QFont('Arial',12,QFont.Light))
    
    self.G1_N = QGroupBox(self.GBDOI_N)
    self.G1_N.move(10,90)
    self.G1_N.resize(270,40)
    self.G1_N.setStyleSheet("QGroupBox {background-color:  rgb(102, 204, 226);border: 1px white;}")
    
    self.layoutG1_N = QHBoxLayout(self.G1_N)
    
    self.RBSlim_N = QRadioButton("Slim",self.G1_N)
    self.RBSlim_N.setFont(QFont('Arial',11,QFont.Light))
    self.RBSlim_N.clicked.connect(self.clickedSlim_N)
    
    self.RBRound_N = QRadioButton("Round",self.G1_N)
    self.RBRound_N.setFont(QFont('Arial',11,QFont.Light))
    self.RBRound_N.clicked.connect(self.clickedRound_N)

    self.RBOther_N = QRadioButton("Other",self.G1_N)
    self.RBOther_N.setFont(QFont('Arial',11,QFont.Light))
    self.RBOther_N.clicked.connect(self.clickedOther_N)
    
    self.layoutG1_N.addWidget(self.RBSlim_N)
    self.layoutG1_N.addWidget(self.RBRound_N)
    self.layoutG1_N.addWidget(self.RBOther_N)
    
    self.G1_N.setLayout(self.layoutG1_N)
    
    self.LOther_N = QLabel("Other",self.GBDOI_N)
    self.LOther_N.move(20,140)
    self.LOther_N.setFont(QFont('Arial',11,QFont.Light))
    self.LOther_N.setDisabled(True)
    
    self.LESize_N = QLineEdit(self.GBDOI_N)
    self.LESize_N.move(20,160)
    self.LESize_N.resize(160,25)
    self.LESize_N.setPlaceholderText("Container Size")
    self.LESize_N.setFont(QFont('Arial',11,QFont.Light))
    self.LESize_N.setStyleSheet("QLineEdit {background-color:  rgb(240, 240, 240);border-radius: 5px;}")
    self.LESize_N.setDisabled(True)
    
    self.CBUnit_N = QComboBox(self.GBDOI_N)
    self.CBUnit_N.move(190,160)
    self.CBUnit_N.resize(80,25)
    self.CBUnit_N.addItem("L")
    self.CBUnit_N.addItem("mL")
    self.CBUnit_N.setFont(QFont('Arial',11,QFont.Light))
    self.CBUnit_N.setStyleSheet("QComboBox {background-color:  rgb(240, 240, 240);border-radius: 5px;}")
    self.CBUnit_N.setDisabled(True)

    self.LQuantity_N = QLabel("QUANTITY",self.GBDOI_N)
    self.LQuantity_N.move(20,220)
    self.LQuantity_N.setFont(QFont('Arial',12,QFont.Light))
    

    self.LEQuantity_N = QLineEdit(self.GBDOI_N)
    self.LEQuantity_N.move(20,250)
    self.LEQuantity_N.resize(250,30)
    self.LEQuantity_N.setPlaceholderText("Number of water container")
    self.LEQuantity_N.setFont(QFont('Arial',11,QFont.Light))
    self.LEQuantity_N.setStyleSheet("QLineEdit {background-color:  rgb(240, 240, 240);border-radius: 5px;}")
    
    self.LOwnership_N = QLabel("OWNERSHIP",self.GBDOI_N)
    self.LOwnership_N.move(20,300)
    self.LOwnership_N.setFont(QFont('Arial',12,QFont.Light))
    self.LOwnership_N.setDisabled(True)
    
    self.G2_N = QGroupBox(self.GBDOI_N)
    self.G2_N.move(30,320)
    self.G2_N.resize(250,40)
    self.G2_N.setStyleSheet("QGroupBox {background-color:  rgb(102, 204, 226);border: 1px white}")
    
    self.layoutG2_N = QHBoxLayout(self.G2_N)

    self.RBOwn_N = QRadioButton("Owned",self.G2_N)
    self.RBOwn_N.setFont(QFont('Arial',11,QFont.Light))
    self.RBOwn_N.setChecked(True)
    self.RBOwn_N.setDisabled(True)
    #self.RBOwn_N.clicked.connect(self.clickedOwn)
    
    self.RBLend_N = QRadioButton("Lend",self.G2_N)
    self.RBLend_N.setFont(QFont('Arial',11,QFont.Light)) 
    self.RBLend_N.setDisabled(True)
    #self.RBLend_N.clicked.connect(self.clickedLend)
    
    self.layoutG2_N.addWidget(self.RBOwn_N)
    self.layoutG2_N.addWidget(self.RBLend_N)
    
    self.G2_N.setLayout(self.layoutG2_N)
    
    self.LDelivery_N = QLabel("DELIVERY",self.GBDOI_N)
    self.LDelivery_N.move(20,380)
    self.LDelivery_N.setFont(QFont('Arial',12,QFont.Light))
    self.LDelivery_N.setDisabled(True)
    
    self.G3_N = QGroupBox(self.GBDOI_N)
    self.G3_N.move(20,400)
    self.G3_N.resize(260,40)
    self.G3_N.setStyleSheet("QGroupBox {background-color:  rgb(102, 204, 226);border: 1px white}")
    
    self.layoutG3_N = QHBoxLayout(self.G3_N)

    self.RBDelivery_N = QRadioButton("Door delivery",self.G3_N)
    self.RBDelivery_N.setFont(QFont('Arial',11,QFont.Light))    
    self.RBDelivery_N.setDisabled(True)
    #self.RBDelivery_N.clicked.connect(self.clickedDelivery)
    
    self.RBPick_N = QRadioButton("Self pick-up",self.G3_N)
    self.RBPick_N.setFont(QFont('Arial',11,QFont.Light)) 
    self.RBPick_N.setChecked(True)
    self.RBPick_N.setDisabled(True)
    #self.RBPick_N.clicked.connect(self.clickedPick)
    
    self.layoutG3_N.addWidget(self.RBDelivery_N)
    self.layoutG3_N.addWidget(self.RBPick_N)
    
    self.G3_N.setLayout(self.layoutG3_N)
    

    self.LPayment_N = QLabel("PAYMENT",self.GBDOI_N)
    self.LPayment_N.move(20,460)
    self.LPayment_N.setFont(QFont('Arial',12,QFont.Light))
    self.LPayment_N.setDisabled(True)
    
    self.G4_N = QGroupBox(self.GBDOI_N)
    self.G4_N.move(20,480)
    self.G4_N.resize(260,40)
    self.G4_N.setStyleSheet("QGroupBox {background-color:  rgb(102, 204, 226);border: 1px white;}")
    
    self.layoutG4_N = QHBoxLayout(self.G4_N)

    self.RBCDelivery_N = QRadioButton("Cash on delivery",self.G4_N)
    self.RBCDelivery_N.setFont(QFont('Arial',11,QFont.Light))    
    self.RBCDelivery_N.setDisabled(True)
    
    self.RBUpfront_N = QRadioButton("Pay upfront",self.G4_N)
    self.RBUpfront_N.setFont(QFont('Arial',11,QFont.Light)) 
    self.RBUpfront_N.setChecked(True)
    self.RBUpfront_N.setDisabled(True)

    
    self.layoutG4_N.addWidget(self.RBCDelivery_N)
    self.layoutG4_N.addWidget(self.RBUpfront_N)
    
    self.G4_N.setLayout(self.layoutG4_N)
    
    
    #Buttons
    self.GBSubmitCancel = QGroupBox(self)
    self.GBSubmitCancel.move(890,770)
    self.GBSubmitCancel.resize(290,100)
    self.GBSubmitCancel.setStyleSheet("QGroupBox {border-image : url(Images/SubmitCancel.png);}")

    self.PBSubmit = QPushButton("SUBMIT",self.GBSubmitCancel)
    self.PBSubmit.move(10,30)
    self.PBSubmit.resize(120,40)
    self.PBSubmit.setFont(QFont('Arial',12,QFont.Bold)) 
    self.PBSubmit.setStyleSheet("QPushButton{background: rgba(255, 255, 255, 6%);border: 3px solid white; border-radius: 18px ; color: white; }"
                                     		"QPushButton:hover{color: white; background-color: #00F0FF; border: 3px solid #00F0FF }")
    #import ForInquiryData
    self.PBSubmit.clicked.connect(self.clickedSubmit)
    
    self.PBCancel = QPushButton("CANCEL",self.GBSubmitCancel)
    self.PBCancel.move(160,30)
    self.PBCancel.resize(120,40)
    self.PBCancel.setFont(QFont('Arial',12,QFont.Bold)) 
    self.PBCancel.setStyleSheet("QPushButton{background: rgba(255, 255, 255, 6%);border: 3px solid white; border-radius: 18px ; color: white; }"
                                     		"QPushButton:hover{color: white; background-color: #00F0FF; border: 3px solid #00F0FF }")
        
    #Overview    
    self.GBQueueBox.setHidden(True)
    self.GBReady.setHidden(True)

    #Storage
    self.GBAvailable.setHidden(True)
    self.GBBorrow.setHidden(True)
    self.GBTotal.setHidden(True)
    self.GBList.setHidden(True)
    self.GBRate.setHidden(True)
    
    #Records
    self.GBDeliveryOption.setHidden(True)

    
    #Reports
    self.GBToday.setHidden(True)
    self.GBNumberDelivery.setHidden(True)
    self.GBNumberNonDelivery.setHidden(True)
    self.GBTodayList.setHidden(True)
    self.GBHistory.setHidden(True)


