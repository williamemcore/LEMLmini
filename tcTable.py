# -*- coding: utf-8 -*-

from PyQt5 import  QtCore, QtGui

from PyQt5.QtCore import  *
from PyQt5.QtWidgets import  *
import sys
from PyQt5.QtGui import *
from tcEnable import tcEnable
from Ui_tcTable import Ui_Dialog
#import codecs
import struct, array
#-------------------------------------------------------------------------------------------------------------------
# Global Variables


SOT = 0x7E

inmsg= bytearray(61)
vRef=3.3
import os
tcM=os.getcwd()+'\\tcM'    
tcS=os.getcwd()+'\\tcS'    
tcE=os.getcwd()+'\\tcE'   
#-----------------------------------------------------
class tcTable(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(tcTable, self).__init__(parent)
        self.setupUi(self)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.readUart)
        self.timer.start(500)
        self.on_getFromBoardBu_clicked()


      


   
 #----------------------------------------------------
    def readUart(self):
        global  inmsg
        if  os.path.exists(tcS)==True:  #received from UART
            with open(tcS, 'rb') as f:
                #value1 = f.read()
                f.readinto(inmsg)
            f.close()

            tcSSize=os.path.getsize(tcS)


            value1=bytearray(inmsg)
            try:
                os.remove(tcS)
                print("\nremoved  ",tcS)
            except:
                print('\n\nremove error 11')
 
            if(sys.getsizeof(value1)<6):return

            if (value1[0]==0x7e):

                if((value1[5]==0x11)or(value1[5]==0x13)or(value1[5]==0x15)or(value1[5]==0x17)):   

                       
                    if(value1[5]==0x11):

                        QMessageBox.question(self, 'Save TC Table Status', "Save TC Table Successful.", QMessageBox.Ok)
                        return


                    if(value1[5]==0x13):
                        channel=value1[8]

                        if((channel>=0)and(channel<23)):
                            self.selChannelTC.setCurrentIndex(channel)

                            s2=struct.unpack('h', bytes([value1[10], value1[9]]))[0]       
                            s=409.6*(s2)/1024
                            s=round(s)
 
                            self.tcpd_0.setText(str(s))

                            s2=struct.unpack('h', bytes([value1[12], value1[11]]))[0]       #point1
                            s=409.6*(s2)/1024
                            s=round(s)
                            self.tcpd_1.setText(str(s))

                            s2=struct.unpack('h', bytes([value1[14], value1[13]]))[0]       #point2
                            s=409.6*(s2)/1024
                            s=round(s)
                            self.tcpd_2.setText(str(s))

                            s2=struct.unpack('h', bytes([value1[16], value1[15]]))[0]       #point3
                            s=409.6*(s2)/1024
                            s=round(s)
                            self.tcpd_3.setText(str(s))

                            s2=struct.unpack('h', bytes([value1[18], value1[17]]))[0]       #point4
                            s=409.6*(s2)/1024
                            s=round(s)
                            self.tcpd_4.setText(str(s))

                            s2=struct.unpack('h', bytes([value1[20], value1[19]]))[0]       #point5
                            s=409.6*(s2)/1024
                            s=round(s)
                            self.tcpd_5.setText(str(s))

                            s2=struct.unpack('h', bytes([value1[22], value1[21]]))[0]       #point6
                            s=409.6*(s2)/1024
                            s=round(s)
                            self.tcpd_6.setText(str(s))

                            s2=struct.unpack('h', bytes([value1[24], value1[23]]))[0]       #point7
                            s=409.6*(s2)/1024
                            s=round(s)
                            self.tcpd_7.setText(str(s))

                            s2=struct.unpack('h', bytes([value1[26], value1[25]]))[0]       #point8
                            s=409.6*(s2)/1024
                            s=round(s)
                            self.tcpd_8.setText(str(s))


                            if(value1[27]==1):                                              #enable
                                self.channelEnaCheck.setChecked(True)
                            else:
                                self.channelEnaCheck.setChecked(False)

                            QMessageBox.question(self, 'Get TC TableStatus', "Get TC Table Successful.", QMessageBox.Ok)
                            return
                        
                    if(value1[5]==0x15):#get data from board ACK
                        channel=value1[8]

                        if((channel>=0)and(channel<23)):
                            self.selChannelTC.setCurrentIndex(channel)
                            
                            tmv=(vRef*(value1[9]*256+value1[10]))/0x1000               #temp
                            t=(tmv*1000-500)/10
                            if(t<-15):

                                return
                            self.moduleTemEdit.setText( "{:3.1f}".format(t))
      
                            s2=struct.unpack('h', bytes([value1[12], value1[11]]))[0] 

                            s=409.6*(s2)/1024
                            s=round(s)
                            if((s<0) or (s>4096)):
                                QMessageBox.question(self, 'DAC(mv) @ 25 C', "DAC(mv) @ 25 C  over.", QMessageBox.Ok)
                                self.dac25Edit.setText('')
                            else:

                                self.dac25Edit.setText(str(s))
                            

                            
                            s2=struct.unpack('h', bytes([value1[14], value1[13]]))[0]       #TC compensated
                            s=409.6*(s2)/1024
                            s=round(s)
                            self.tcCorrectionEdit.setText(str(s)) 

                            
                            QMessageBox.question(self, 'Get TC Data  Status', "Get TC Data  Successful.", QMessageBox.Ok)
                            value1[5]=0
                            return
        else:  
            if  os.path.exists(tcE)==True: 
                with open(tcE, 'rb') as f:
                    f.readinto(inmsg)
                f.close()
                value1=bytearray(inmsg)
                s=value1[8+self.selChannelTC.currentIndex()]
                
                if((s==1) and (self.channelEnaCheck.isChecked()==False)):
                    self.channelEnaCheck.setChecked(True)
                    return
                if((s==0) and self.channelEnaCheck.isChecked()==True):
                    self.channelEnaCheck.setChecked(False)
                    return 
 #===========================================================================================                   

    @pyqtSlot()
    def on_exitBu_clicked(self):
        self.timer.stop()
    

    
    @pyqtSlot(int)
    def on_selChannelTC_currentIndexChanged(self, index):
        self.on_getFromBoardBu_clicked()

 #-------------------------------------------------------------------   
    @pyqtSlot()
    def on_saveToBoardBu_clicked(self):
        outmsg = bytearray()

        outmsg = bytearray()
        outmsg.append(SOT)
        outmsg.append(0) #packet len high byte
        outmsg.append(26) #packet len low byte
        
        outmsg.append(0) #SRC ADDR
        outmsg.append(0) #DEST ADDR
        outmsg.append(0x10) #MSG TYPE
        outmsg.append(8) #MSG ID low byte
        outmsg.append(0) #MSG ID high byte
        

    #value:
        channel=self.selChannelTC.currentIndex()              #channel

        if(channel<0):
            return
        outmsg.append(channel)
        

        try:
            s=(int(self.tcpd_0.text()))*1024/409.6               

            if(s>10240 or s<-10240):
                msgbx.showinfo(title="Save TC Table", message="Value is over: "+ str(s))
                return 
        except:
            QMessageBox.about(self, "Save TC Table", "Value is not correct in channel   "+ str(channel))
            return
        s1=struct.pack('h',int(s))
        outmsg.append(s1[1])
        outmsg.append(s1[0])


 
        try:
            s=(int(self.tcpd_1.text()))*1024/409.6                  #point 1
            if(s>10240 or s<-10240):
                msgbx.showinfo(title="Save TC Table", message="Value is over: "+ str(s))
                return 
        except:
            QMessageBox.about(self, "Save TC Table", "Value is not correct in channel   "+ '2')
            return
        s1=struct.pack('h',int(s))
        outmsg.append(s1[1])
        outmsg.append(s1[0])
        


        try:
            s=(int(self.tcpd_2.text()))*1024/409.6                  #point 2
            if(s>10240 or s<-10240):
                msgbx.showinfo(title="Save TC Table", message="Value is over: "+ str(s))
                return 
        except:
            QMessageBox.about(self, "Save TC Table", "Value is not correct in channel   "+ '3')
            return
        s1=struct.pack('h',int(s))
        outmsg.append(s1[1])
        outmsg.append(s1[0])
        

        
        try:
            s=(int(self.tcpd_3.text()))*1024/409.6                  #point 3
            if(s>10240 or s<-10240):
                msgbx.showinfo(title="Save TC Table", message="Value is over: "+ str(s))
                return 
        except:
            QMessageBox.about(self, "Save TC Table", "Value is not correct in channel   "+ '4')
            return
        s1=struct.pack('h',int(s))
        outmsg.append(s1[1])
        outmsg.append(s1[0])
        


        try:
            s=(int(self.tcpd_4.text()))*1024/409.6                  #point 4
            if(s>10240 or s<-10240):
                msgbx.showinfo(title="Save TC Table", message="Value is over: "+ str(s))
                return 
        except:
            QMessageBox.about(self, "Save TC Table", "Value is not correct in channel   "+ '5')
            return
        s1=struct.pack('h',int(s))
        outmsg.append(s1[1])
        outmsg.append(s1[0])
        

        try:
            s=(int(self.tcpd_5.text()))*1024/409.6                  #point 5
            if(s>10240 or s<-10240):
                msgbx.showinfo(title="Save TC Table", message="Value is over: "+ str(s))
                return 
        except:
            QMessageBox.about(self, "Save TC Table", "Value is not correct in channel   "+ '6')
            return
        s1=struct.pack('<h',int(s))
        outmsg.append(s1[1])
        outmsg.append(s1[0])
        


        try:
            s=(int(self.tcpd_6.text()))*1024/409.6                  #point 6
            if(s>10240 or s<-10240):
                msgbx.showinfo(title="Save TC Table", message="Value is over: "+ str(s))
                return 
        except:
            QMessageBox.about(self, "Save TC Table", "Value is not correct in channel   "+ '7')
            return
        s1=struct.pack('h',int(s))
        outmsg.append(s1[1])
        outmsg.append(s1[0])
        


        try:
            s=(int(self.tcpd_7.text()))*1024/409.6                  #point 7
            if(s>10240 or s<-10240):
                msgbx.showinfo(title="Save TC Table", message="Value is over: "+ str(s))
                return 
        except:
            QMessageBox.about(self, "Save TC Table", "Value is not correct in channel   "+ '8')
            return
        s1=struct.pack('h',int(s))
        outmsg.append(s1[1])
        outmsg.append(s1[0])
        

        try:
            s=(int(self.tcpd_8.text()))*1024/409.6                  #point 8
            if(s>10240 or s<-10240):
                msgbx.showinfo(title="Save TC Table", message="Value is over: "+ str(s))
                return 
        except:
            QMessageBox.about(self, "Save TC Table", "Value is not correct in channel   "+ '9')
            return
        s1=struct.pack('h',int(s))
        outmsg.append(s1[1])
        outmsg.append(s1[0])
        

    #channelEnaCheck:
        enaCheck=bytearray(1)
        if(self.channelEnaCheck.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0

        outmsg.append(enaCheck[0])
        bChkSum=0
        value1=bytearray(outmsg)
        for i in range(3,len(outmsg)):
            bChkSum+=value1[i]
        outmsg.append(bChkSum&0xff)  # CRC8
        outmsg.append(0x74) 
        outmsg.append(0x03)

        try:
            f = open(tcM  ,'wb')     #under current folder
            f.write(outmsg)

            f.close()
    
        except:
            print('\n\n save to board error5' )

  #------------------------------------------------------------
    @pyqtSlot()
    def on_getFromBoardBu_clicked(self):#get table

        outmsg = bytearray()
        outmsg.append(SOT)
        
        outmsg.append(9) #packet len low byte

        outmsg.append(0) #packet len high byte
        

        outmsg.append(0) #SRC ADDR
        

        outmsg.append(0) #DEST ADDR
        

        outmsg.append(0x12) #MSG TYPE
        

        outmsg.append(8) #MSG ID low byte
        

        outmsg.append(0) #MSG ID high byte
        
    #value:
        s=self.selChannelTC.currentIndex()              #channel
        print('s=',s)
        if(s<0):
            return
        outmsg.append(s) 
        
        
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
            f = open(tcM  ,'wb') 
            f.write(outmsg)


            f.close()
    
        except:
            print('\n\n save to board error6' )
 #-----------------------------------------------------------       
    @pyqtSlot()
    def on_getTcDateBu_clicked(self):

        outmsg = bytearray()
        outmsg.append(SOT)
        
        outmsg.append(9) #packet len low byte

        outmsg.append(0) #packet len high byte
        

        outmsg.append(0) #SRC ADDR
        

        outmsg.append(0) #DEST ADDR
        

        outmsg.append(0x14) #MSG TYPE
        

        outmsg.append(8) #MSG ID low byte
        

        outmsg.append(0) #MSG ID high byte
        
    #value:
        s=self.selChannelTC.currentIndex()              #channel

        if(s<0):
            return
        outmsg.append(s)
        
        
        outmsg.append(0)   
        
          
        outmsg.append(0) 
        
        
        outmsg.append(0)  
        bChkSum=0
        value1=bytearray(outmsg)
        for i in range(3,len(outmsg)):
            bChkSum+=value1[i]
        outmsg.append(bChkSum&0xff)  # CRC8

        
        outmsg.append(0x74) 
        outmsg.append(0x03)
        

        try:
            f = open(tcM  ,'wb') 

            f.write(outmsg)


            f.close()
    
        except:
            print('\n\n save to board error7' )

    @pyqtSlot()
    def on_TcConfigBu_clicked(self):
        self.tcEnable=tcEnable()
        self.tcEnable.show()

    @pyqtSlot()
    def on_channelEnaCheck_clicked(self):
        enaCheck=bytearray(1)
        if(self.channelEnaCheck.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(tcE)==False:     #TC enable <-> TC table
            f = open(tcE  ,'wb')     
        else:
            f = open(tcE  ,'rb+')   
        f.seek(8+self.selChannelTC.currentIndex(),0)
        f.write(enaCheck)
        f.close() 


        
        

#=================================================================
if __name__ == "__main__":          # self start
    app = QApplication(sys.argv)
    ui = tcTable()
    ui.show()
    sys.exit(app.exec_())  
    

