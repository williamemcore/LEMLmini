# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import  *
from PyQt5.QtWidgets import  *
import sys
from PyQt5.QtGui import *


from tcTable import tcTable
from fcTable import fcTable


from Ui_boardInfo import Ui_Dialog
import codecs
import struct, array
import os
#-------------------------------------------------------------------------------------------------------------------
# Global Variables
password='123'
ser = 0
SOT = 0x7E
inbuflen =122
inmsg= bytearray(122)

countSubResendBo=0

boM=os.getcwd()+'\\boM'   
boS=os.getcwd()+'\\boS'   

info=[]

#-------------------------------------------------------------------------------------------


class boardInfo(QDialog, Ui_Dialog):

    def __init__(self, parent=None):

        super(boardInfo, self).__init__(parent)
        self.setupUi(self)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.readUart)
        self.timer.start(500)

        global info
        info =[0 for i in range(6)]
        info[0]=self.ModelNumberEd
        info[1]=self.UnitSerialEd
        info[2]=self.LaserSerialEd
        info[3]=self.ManufactureDateEd
        info[4]=self.PCBNumberEd
        info[5]=self.FirmwareRevisionEd

        self.on_getFromBoardBu_clicked()

  #----------------------------------------------------
    def readUart(self):
        global  inmsg
        if  os.path.exists(boS)==True: 
            with open(boS, 'rb') as f:
                f.readinto(inmsg)
            f.close()

            boSSize=os.path.getsize(boS)


            value1=bytearray(inmsg)
            try:
                os.remove(boS)

            except:
                print('\n\nremove error 11')
 

            if(sys.getsizeof(value1)<6):return
            print('read routine2---',value1[0],value1[1],value1[2],value1[3],value1[4],value1[5]) 
            if (value1[0]==0x7e):
                value1[0]=0
                if((value1[5]==0x51)or(value1[5]==0x53)):   
                     
                    if(value1[5]==0x51):#save board info to board ACK
                        QMessageBox.question(self, 'Save  Status', "Save Board Info Successful.", QMessageBox.Ok)
                        return


                    if(value1[5]==0x53):#get board info from board
                        for i in range(6):
                            s2=bytearray(18)
                            for j in range(0,18):    #<18
                                s=value1[8+i*18+j]

                                if((s>33) and (s <126)):
                                    s2[j]=value1[8+i*18+j]

                            info[i].setText(s2.decode('utf-8'))
                            
                        QMessageBox.question(self, 'Get Board Info Status', "Get Board Info Successful.", QMessageBox.Ok)
                        return
                    
                                   
                        
 

                    
 #====================================Save/Get=======================================================                       
        
    @pyqtSlot()
    def on_saveToBoardBu_clicked(self):

    #check_password:
        if(self.passwordEd.text()!=password):
            QMessageBox.question(self, "Password", "Password not correct")
            return

    #save:    
        outmsg = bytearray(121)

        
        outmsg = bytearray()
        outmsg.append(SOT)
        
        outmsg.append(110) #packet len low byte
        
        outmsg.append(0) #packet len high byte
        

        outmsg.append(0) #SRC ADDR
        

        outmsg.append(0) #DEST ADDR
        

        outmsg.append(0x50) #MSG TYPE


        outmsg.append(8) #MSG ID low byte
        

        outmsg.append(0) #MSG ID high byte
        

#value:
        for i in range(6):

            s1 = bytearray()
            s1.extend(map(ord, info[i].text()))

            s = bytearray(18)
            k=0
            for j in range(0,len(s1)):    #<18

                if((s1[j]>31) and (s1[j] <126)):
                    s[k]=s1[j]

                    k+=1
            
            #print('len(s',info[i].text(),len(s),len(info[i].text()) )
    
            if(len(s)<=18):
                for j in range(0,len(s)):
                    outmsg.append(s[j]) 
                if(len(s)<18):
                    for j in range(len(s),18):
                        outmsg.append(0) #dummy
                        
                    
            else:       
                QMessageBox.question(self, "Save board info", "Value is over: "+info[i].text())


        outmsg.append(0)
        
        outmsg.append(0) 
        
        bChkSum=0
        value1=bytearray(outmsg)
        for i in range(3,len(outmsg)):
            bChkSum+=value1[i]
        outmsg.append(bChkSum&0xff)  # CRC8
        outmsg.append(0x74) 
        outmsg.append(0x03)

        value1=bytearray(outmsg)
        try:
            f = open(boM  ,'wb')    
            f.write(outmsg)
            f.close()
            
  
        except:
            print('\n save to board error5' )


        
    @pyqtSlot()
    def on_getFromBoardBu_clicked(self):
        
        outmsg = bytearray()
        outmsg.append(SOT)
        
        outmsg.append(9) #packet len low byte

        outmsg.append(0) #packet len high byte
        

        outmsg.append(0) #SRC ADDR
        

        outmsg.append(0) #DEST ADDR
        

        outmsg.append(0x52) #MSG TYPE


        outmsg.append(8) #MSG ID low byte
        

        outmsg.append(0) #MSG ID high byte
        
        
    #value:
        outmsg.append(0)    #dummy
        
          
        outmsg.append(0)   #dummy
        
        
        outmsg.append(0)   #dummy
        
        bChkSum=0
        value1=bytearray(outmsg)
        for i in range(3,len(outmsg)):
            bChkSum+=value1[i]
        outmsg.append(bChkSum&0xff)  # CRC8

        
        outmsg.append(0x74) 
        outmsg.append(0x03)
        
        try:
            f = open(boM  ,'wb') 
            f.write(outmsg)


            f.close()
    
        except:
            print('\n\n get from board error6' )
#=================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = boardInfo()

    ui.show()
    sys.exit(app.exec_()) 
