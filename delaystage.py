# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Polarizer.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# run in base conda environment
#
# Magnus H. Berntsen


from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import numpy as np

zero_pos = 0#-65549
preset1_pos = 86.3355 # 
preset2_pos = 85 # 
#

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 439)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 80, 160, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
       
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 200, 160, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(420, 160, 300, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 60, 300, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lcdNumber = QtWidgets.QLCDNumber(10,self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(420, 90, 250, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        #self.lcdNumber_2 = QtWidgets.QLCDNumber(10,self.centralwidget)
        #self.lcdNumber_2.setGeometry(QtCore.QRect(420, 190, 250, 41))
        #self.lcdNumber_2.setObjectName("lcdNumber2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 350, 41))
        font = QtGui.QFont()
        font.setFamily("aakar")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        #self.label_6 = QtWidgets.QLabel(self.centralwidget)
        #self.label_6.setGeometry(QtCore.QRect(250, 80, 82, 71))
        #font = QtGui.QFont()
        #font.setPointSize(10)
        #self.label_6.setFont(font)
        #self.label_6.setObjectName("label_6")
        #self.label_7 = QtWidgets.QLabel(self.centralwidget)
        #self.label_7.setGeometry(QtCore.QRect(250, 115, 82, 71))
        #font = QtGui.QFont()
        #font.setPointSize(10)
        #self.label_7.setFont(font)
        #self.label_7.setObjectName("label_7")
        #self.widget = QtWidgets.QWidget(self.centralwidget)
        #self.widget.setGeometry(QtCore.QRect(180, 240, 61, 111))
        #self.widget.setObjectName("widget")
        #self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        #self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        #self.verticalLayout.setObjectName("verticalLayout")
        #self.lineEdit = QtWidgets.QLineEdit(self.widget)
        #self.lineEdit.setObjectName("lineEdit")
        #self.verticalLayout.addWidget(self.lineEdit)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(120, 100, 200, 50))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)


        #self.widget2 = QtWidgets.QWidget(self.centralwidget)
        #self.widget2.setGeometry(QtCore.QRect(170, 110, 51, 30))
        #self.widget2.setObjectName("widget2")
        #self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget2)
        #self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        #self.verticalLayout_3.setObjectName("verticalLayout_3")
        #self.pushButton_4 = QtWidgets.QPushButton(self.widget2)
        #self.pushButton_4.setObjectName("pushButton_4")
        #self.verticalLayout_3.addWidget(self.pushButton_4)

        #self.widget5 = QtWidgets.QWidget(self.centralwidget)
        #self.widget5.setGeometry(QtCore.QRect(170, 190, 51, 30))
        #self.widget5.setObjectName("widget5")
        #self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget5)
        #self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        #self.verticalLayout_5.setObjectName("verticalLayout_5")
        #self.pushButton_8 = QtWidgets.QPushButton(self.widget5)
        #self.pushButton_8.setObjectName("pushButton_8")
        #self.verticalLayout_5.addWidget(self.pushButton_8)


        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(120, 210, 150, 75))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout.addWidget(self.pushButton_9)
        #self.widget4 = QtWidgets.QWidget(self.centralwidget)
        #self.widget4.setGeometry(QtCore.QRect(150, 100, 82, 71))
        #self.widget4.setObjectName("widget4")
        #self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget4)
        #self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        #self.verticalLayout_4.setObjectName("verticalLayout_4")
        #self.pushButton = QtWidgets.QPushButton(self.widget4)
        #self.pushButton.setObjectName("pushButton")
        #self.verticalLayout_4.addWidget(self.pushButton)
        #self.pushButton_2 = QtWidgets.QPushButton(self.widget4)
        #self.pushButton_2.setObjectName("pushButton_2")
        #self.verticalLayout_4.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Relative motion (mm)"))
        self.label_2.setText(_translate("MainWindow", "Absolute position"))
        self.label_4.setText(_translate("MainWindow", "Current position"))
        #self.label_8.setText(_translate("MainWindow", "Current vertical position"))
        self.label_5.setText(_translate("MainWindow", "Delay-stage controller"))
        self.pushButton_3.setText(_translate("MainWindow", "-"))
        self.pushButton_3.clicked.connect(lambda: self.move('rn'))
        self.pushButton_7.setText(_translate("MainWindow", "+"))
        self.pushButton_7.clicked.connect(lambda: self.move('rp'))
        #self.pushButton_4.setText(_translate("MainWindow", "+"))
        #self.pushButton_4.clicked.connect(lambda: self.move('rVp'))
        #self.pushButton_8.setText(_translate("MainWindow", "-"))
        #self.pushButton_8.clicked.connect(lambda: self.move('rVn'))
        self.pushButton_9.setText(_translate("MainWindow", "Move"))
        self.pushButton_9.clicked.connect(lambda: self.move('abs'))
        #self.pushButton.setText(_translate("MainWindow", "Vertical"))
        #self.label_6.setText(_translate("MainWindow", "(15600)"))
        #self.pushButton.clicked.connect(lambda: self.move_to_preset('vertical'))
        #self.pushButton_2.setText(_translate("MainWindow", "Horizontal"))
        #self.label_7.setText(_translate("MainWindow", "(18475)"))
        #self.pushButton_2.clicked.connect(lambda: self.move_to_preset('horizontal'))
       

    def do_at_startup(self, MainWindow):
        """
        Query current position when program is started, 
        and add preset relative step sizes.
        """
        # Initiate connection
        with serial.Serial('COM3') as ser:
            ser.baudrate = 921600
            ser.bytesize = 8
            ser.parity = 'N'
            ser.xonxoff = 1
            ser.rtscts = 1
            ser.timeout = 5
            
            
            # Ask for current position
            ser.write(b'1TP'+b'\r\n')
            answ = ser.readline()
            print(answ)
            curr_pos_U = answ.decode('utf-8')#.split('1TP')
            print('Current position: ',curr_pos_U)

            #ser.write(b'1TPV?'+b'\r\n')
            #answ = ser.readline()
            #curr_pos_V = answ.decode('utf-8').split('1TPV')
            #print('Current position: ',curr_pos_V)
            # Update LDC display with current horizontal and vertical positions
            self.lcdNumber.display(curr_pos_U)
            #self.lcdNumber_2.display(curr_pos_V[1])
            # Set values for relative movements
            self.lineEdit.setText("0.1")
            self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)

        
        # Dev dummy number
        #self.lcdNumber.display(10000)

    def move(self,mode):
        """
        Move with the number of relative steps given in one of the three input boxes
        or go to the given absolute position.
        """
        with serial.Serial('COM3') as ser:
            ser.baudrate = 921600
            ser.bytesize = 8
            ser.parity = 'N'
            ser.xonxoff = 1
            ser.rtscts = 1
            ser.timeout = 3
        
            # Construnct command
            if mode == 'rp': # relative 1, positive
                # Get step size
                to_move = self.lineEdit.text()
                tmp_str = '1PR'
            elif mode == 'rn': # relative 1, negative
                # Get step size
                to_move = self.lineEdit.text()
                tmp_str = '1PR-'
            elif mode == 'abs': # absolute movement
                to_move = self.lineEdit_4.text()
                tmp_str = '1PA'
            else:
                print('error')
            
            # Construct command string
            move_string = bytes(tmp_str+'{}'.format(to_move),'utf-8')
            # Move
            ser.write(move_string+b'\r\n')
            answ = ser.readline()
            print(answ)
            
            # Ask for current position
            ser.write(bytes('1TP','utf-8')+b'\r\n')
            answ = ser.readline()
            print(answ)
            
            # Update LCD display
            self.lcdNumber.display(answ.decode('utf-8'))
            


    def get_home(self, MainWindow):
        """
        Query home position.
        """
        # Initiate connection
        with serial.Serial('COM6') as ser:
            ser.baudrate = 19200
            ser.bytesize = 8
            ser.parity = 'N'
            ser.xonxoff = 1
            ser.rtscts = 1
            ser.timeout = 5
            
            # Ask for home position
            ser.write(b'0OR?'+b'\r\n')
            answ = ser.readline()
            home_pos = answ.decode('utf-8').split()[1]
            print(home_pos)
        
    def move_to_preset(self, pos):
        """
        Send command to move to preset position of vertical or horizontal polarization
        """
        # Initiate connection
        with serial.Serial('COM6') as ser:
            ser.baudrate = 19200
            ser.bytesize = 8
            ser.parity = 'N'
            ser.xonxoff = 1
            ser.rtscts = 1
            ser.timeout = 5
            
            if pos == 'vertical':
                tmp_pos = preset1_pos
            elif pos == 'horizontal':
                tmp_pos = preset2_pos
            else:
                print('error')
            
            # Move
            pos_string = bytes('0PA{}'.format(tmp_pos),'utf-8')
            ser.write(pos_string+b'\r\n')
            answ = ser.readline()
            # Ask for current position
            ser.write(b'0PA?'+b'\r\n')
            answ = ser.readline()
            curr_pos = answ.decode('utf-8').split()
            # Update LDC display with current position
            self.lcdNumber.display(int(curr_pos[1])-zero_pos)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.do_at_startup(MainWindow)
    sys.exit(app.exec_())