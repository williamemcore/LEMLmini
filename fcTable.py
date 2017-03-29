# -*- coding: utf-8 -*-
from PyQt5 import  QtCore
from PyQt5.QtCore import  *
from PyQt5.QtWidgets import  *
import sys
from PyQt5.QtGui import *
from fcEnable import fcEnable
from Ui_fcTable import Ui_Dialog
#import codecs
import struct
#-------------------------------------------------------------------------------------------------------------------
# Global Variables


SOT = 0x7E

inmsg= bytearray(61)
dacRef=409.6
import os
fcM=os.getcwd()+'\\fcM'    
fcS=os.getcwd()+'\\fcS'    
fcE=os.getcwd()+'\\fcE'    
#-----------------------------------------------------
class fcTable(QDialog, Ui_Dialog):

    def __init__(self, parent=None):

        super(fcTable, self).__init__(parent)
        self.setupUi(self)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.readUart)
        self.timer.start(500)

        self.on_getFromBoardBu_clicked()


 #----------------------------------------------------
    def readUart(self):
        global  inmsg
        if  os.path.exists(fcS)==True:  #received from UART
            with open(fcS, 'rb') as f:
                f.readinto(inmsg)
            f.close()

            fcSSize=os.path.getsize(fcS)


            value1=bytearray(inmsg)
            try:
                os.remove(fcS)

            except:
                print('\n\nremove error 11')
 
            if(sys.getsizeof(value1)<6):return

            if (value1[0]==0x7e):

                if((value1[5]==0x21)or(value1[5]==0x23)or(value1[5]==0x25)or(value1[5]==0x27)):  
                       
                    if(value1[5]==0x21):#save FC table to board ACK

                        QMessageBox.question(self, 'Save FC Table Status', "Save FC Table Successful.", QMessageBox.Ok)
                        return


                    if(value1[5]==0x23):#get FC table from board
                        channel=value1[8]

                        if((channel>=0)and(channel<23)):
                            self.selChannelFC.setCurrentIndex(channel)

                            s2=struct.unpack('h', bytes([value1[10], value1[9]]))[0]      
                            s=(dacRef*s2)/1024
                            s=round(s)
 
                            self.fcpd_0.setText(str(s))

                            s2=struct.unpack('h', bytes([value1[12], value1[11]]))[0]       #point1
                            s=(dacRef*s2)/1024
                            s=round(s)
                            self.fcpd_1.setText(str(s))

                            s2=struct.unpack('h', bytes([value1[14], value1[13]]))[0]       #point2
                            s=(dacRef*s2)/1024
                            s=round(s)
                            self.fcpd_2.setText(str(s))

                            s2=struct.unpack('h', bytes([value1[16], value1[15]]))[0]       #point3
                            s=(dacRef*s2)/1024
                            s=round(s)
                            self.fcpd_3.setText(str(s))

                            s2=struct.unpack('h', bytes([value1[18], value1[17]]))[0]       #point4
                            s=(dacRef*s2)/1024
                            s=round(s)
                            self.fcpd_4.setText(str(s))

                            s2=struct.unpack('h', bytes([value1[20], value1[19]]))[0]       #point5
                            s=(dacRef*s2)/1024
                            s=round(s)
                            self.fcpd_5.setText(str(s))

                            s2=struct.unpack('h', bytes([value1[22], value1[21]]))[0]       #point6
                            s=(dacRef*s2)/1024
                            s=round(s)
                            self.fcpd_6.setText(str(s))

                            s2=struct.unpack('h', bytes([value1[24], value1[23]]))[0]       #point7
                            s=(dacRef*s2)/1024
                            s=round(s)
                            self.fcpd_7.setText(str(s))

                            s2=struct.unpack('h', bytes([value1[26], value1[25]]))[0]       #point8
                            s=(dacRef*s2)/1024
                            s=round(s)
                            self.fcpd_8.setText(str(s)) 

                            if(value1[27]==1):                                              #enable
                                self.channelEnaCheck.setChecked(True)
                                if(self.channelEnaCheck.isChecked()==False):
                                    self.on_channelEnaCheck_clicked()
                            else:
                                self.channelEnaCheck.setChecked(False)
                        
                                if(self.channelEnaCheck.isChecked()==True):
         
                                    self.on_channelEnaCheck_clicked()
    


                            s=struct.unpack('h', bytes([value1[29], value1[28]]))[0]     #fiber Len
                            if((s>0) and (s<5000)):
                                self.fibLenSli.setValue(s/10)
                                

                            QMessageBox.question(self, 'Get FC Table Status', "Get FC Table Successful.", QMessageBox.Ok)
                            return
                        
                    if(value1[5]==0x25):
                        channel=value1[8]
                        
                        if((channel>=0)and(channel<23)):
                            self.selChannelFC.setCurrentIndex(channel)
                            
                            fiLen=(value1[9]*256+value1[10])/10              #fiber len
   
                            if((fiLen<0) or (fiLen>500)):
                                print('\nfiLen ovre',fiLen)
                                fiLen=0
                                #return
                            self.FibLen.setText( "{:3.0f}".format(fiLen))
                            self.fibLenSli.setValue(fiLen)
      
                            s2=struct.unpack('h', bytes([value1[12], value1[11]]))[0]  #DAC @25 C
                            s=(dacRef*s2)/1024
                            s=round(s)
                            if((s<0) or (s>4096)):
                                QMessageBox.question(self, 'DAC(mv) @ 25 C', "DAC(mv) @ 25 C  over.", QMessageBox.Ok)
                                self.dac25Edit.setText('')
                            else:
 
                                self.dac25Edit.setText(str(s))

                            

                            
                            s2=struct.unpack('h', bytes([value1[14], value1[13]]))[0]       #FC compensated
                            s=(dacRef*s2)/1024
                            s=round(s)
                            self.fcCorrectionEdit.setText(str(s)) 

                            
                            QMessageBox.question(self, 'Get FC Data Status', "Get FC Data Successful.", QMessageBox.Ok)
                            value1[5]=0
                            return
        else:  
            if  os.path.exists(fcE)==True: 
                with open(fcE, 'rb') as f:
                    f.readinto(inmsg)
                f.close()
                value1=bytearray(inmsg)
                s=value1[8+self.selChannelFC.currentIndex()]
                
                if((s==1) and (self.channelEnaCheck.isChecked()==False)):
                    self.channelEnaCheck.setChecked(True)
                    return
                if((s==0) and self.channelEnaCheck.isChecked()==True):
                    self.channelEnaCheck.setChecked(False)
                    return 
 #=========save==================================================================================   

    @pyqtSlot()
    def on_saveToBoardBu_clicked(self):
        outmsg = bytearray()
        outmsg.append(SOT)
        outmsg.append(0) #packet len high byte
        outmsg.append(28) #packet len low byte
        

        outmsg.append(0) #SRC ADDR
        outmsg.append(0) #DEST ADDR

        outmsg.append(0x20) #MSG TYPE
        outmsg.append(8) #MSG ID low byte


        outmsg.append(0) #MSG ID high byte


    #value:
        channel=self.selChannelFC.currentIndex()              #channel
        print('on_saveToBoardBu_clicked: channel=',channel)
        if(channel<0):
            return
        outmsg.append(channel)


        try:
            s=(int(self.fcpd_0.text()))*1024/dacRef               

            if(s>10240 or s<-10240):
                QMessageBox.question(self, "Save FC Table", "Value is over: "+ self.fcpd_0.text())
                return 
        except:
            QMessageBox.about(self, "Save FC Table", "Value is not correct in channel   "+ str(channel))
            return
        s1=struct.pack('h',int(s))
        
        outmsg.append(s1[1])
        outmsg.append(s1[0])

 
        try:
            s=(int(self.fcpd_1.text()))*1024/dacRef                  #point 1
            if(s>10240 or s<-10240):
                QMessageBox.question(self, "Save FC Table", "Value is over: "+ self.fcpd_1.text())
                return 
        except:
            QMessageBox.about(self, "Save FC Table", "Value is not correct in channel   "+ '2')
            return
        s1=struct.pack('h',int(s))
        
        outmsg.append(s1[1])
        
        outmsg.append(s1[0])
        


        try:
            s=(int(self.fcpd_2.text()))*1024/dacRef                  #point 2
            if(s>10240 or s<-10240):
                QMessageBox.question(self, "Save FC Table", "Value is over: "+ self.fcpd_2.text())
                return 
        except:
            QMessageBox.about(self, "Save FC Table", "Value is not correct in channel   "+ '3')
            return
        s1=struct.pack('h',int(s))
        
        outmsg.append(s1[1])
        
        outmsg.append(s1[0])
        

        
        try:
            s=(int(self.fcpd_3.text()))*1024/dacRef                  #point 3
            if(s>10240 or s<-10240):
                QMessageBox.question(self, "Save FC Table", "Value is over: "+ self.fcpd_3.text())
                return 
        except:
            QMessageBox.about(self, "Save FC Table", "Value is not correct in channel   "+ '4')
            return
        s1=struct.pack('h',int(s))
        
        outmsg.append(s1[1])
        
        outmsg.append(s1[0])
        


        try:
            s=(int(self.fcpd_4.text()))*1024/dacRef                  #point 4
            if(s>10240 or s<-10240):
                QMessageBox.question(self, "Save FC Table", "Value is over: "+ self.fcpd_4.text())
                return 
        except:
            QMessageBox.about(self, "Save FC Table", "Value is not correct in channel   "+ '5')
            return
        s1=struct.pack('h',int(s))
        
        outmsg.append(s1[1])
        
        outmsg.append(s1[0])
        

        try:
            s=(int(self.fcpd_5.text()))*1024/dacRef                  #point 5
            if(s>10240 or s<-10240):
                QMessageBox.question(self, "Save FC Table", "Value is over: "+ self.fcpd_5.text())
                return 
        except:
            QMessageBox.about(self, "Save FC Table", "Value is not correct in channel   "+ '6')
            return
        s1=struct.pack('<h',int(s))
        
        outmsg.append(s1[1])
        
        outmsg.append(s1[0])
        


        try:
            s=(int(self.fcpd_6.text()))*1024/dacRef                  #point 6
            if(s>10240 or s<-10240):
                QMessageBox.question(self, "Save FC Table", "Value is over: "+ self.fcpd_6.text())
                return 
        except:
            QMessageBox.about(self, "Save FC Table", "Value is not correct in channel   "+ '7')
            return
        s1=struct.pack('h',int(s))
        
        outmsg.append(s1[1])
        
        outmsg.append(s1[0])
        


        try:
            s=(int(self.fcpd_7.text()))*1024/dacRef                  #point 7
            if(s>10240 or s<-10240):
                QMessageBox.question(self, "Save FC Table", "Value is over: "+ self.fcpd_7.text())
                return 
        except:
            QMessageBox.about(self, "Save FC Table", "Value is not correct in channel   "+ '8')
            return
        s1=struct.pack('h',int(s))
        
        outmsg.append(s1[1])
        
        outmsg.append(s1[0])
        

        try:
            s=(int(self.fcpd_8.text()))*1024/dacRef                  #point 8
            if(s>10240 or s<-10240):
                QMessageBox.question(self, "Save FC Table", "Value is over: "+ self.fcpd_8.text())
                return 
        except:
            QMessageBox.about(self, "Save FC Table", "Value is not correct in channel   "+ '9')
            return
        s1=struct.pack('h',int(s))
        
        outmsg.append(s1[1])
        
        outmsg.append(s1[0])
        

    #channelEnaCheck:
        enaCheck=bytearray(1)
        if(self.channelEnaCheck.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0

        outmsg.append(enaCheck[0])
 

     #fiber Len:
        fiber=self.fibLenSli.value()*10
        d1=int(fiber/256)
        outmsg.append(d1) 
        d2=int(fiber%256)
        outmsg.append(d2) 
        
        bChkSum=0
        value1=bytearray(outmsg)
        for i in range(3,len(outmsg)):
            bChkSum+=value1[i]
        outmsg.append(bChkSum&0xff)  # CRC8
    
        outmsg.append(0x74) 
        outmsg.append(0x03)

        try:
            f = open(fcM  ,'wb')   
            f.write(outmsg)


            f.close()
    
        except:
            print('\n\n save to board error5' )


  #------------------------------get------------------------------

    @pyqtSlot()
    def on_getFromBoardBu_clicked(self):#get table
        outmsg = bytearray()
        outmsg.append(SOT)
        outmsg.append(9) #packet len low byte
        outmsg.append(0) #packet len high byte
        

        outmsg.append(0) #SRC ADDR
        

        outmsg.append(0) #DEST ADDR
        

        outmsg.append(0x22) #MSG TYPE
        

        outmsg.append(8) #MSG ID low byte
        

        outmsg.append(0) #MSG ID high byte
        
    #value:
        s=self.selChannelFC.currentIndex()              #channel

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
            f = open(fcM  ,'wb') 
            f.write(outmsg)


            f.close()
    
        except:
            print('\n\n save to board error6' )
 #----------------------------------------------------------- 
    @pyqtSlot()
    def on_getFcDateBu_clicked(self):
        outmsg = bytearray()
        outmsg.append(SOT)
        outmsg.append(9) #packet len low byte
        outmsg.append(0) #packet len high byte
        outmsg.append(0) #SRC ADDR
        outmsg.append(0) #DEST ADDR
        outmsg.append(0x24) #MSG TYPE
        outmsg.append(8) #MSG ID low byte
        outmsg.append(0) #MSG ID high byte
        
    #value:
        s=self.selChannelFC.currentIndex()              #channel

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
            f = open(fcM  ,'wb') 

            f.write(outmsg)


            f.close()
    
        except:
            print('\n\n save to board error7' )

    
    @pyqtSlot()
    def on_FcConfigBu_clicked(self):
        self.fcEnable=fcEnable()
        self.fcEnable.show()
    
    
    @pyqtSlot()
    def on_channelEnaCheck_clicked(self):
        enaCheck=bytearray(1)
        if(self.channelEnaCheck.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(8+self.selChannelFC.currentIndex(),0)
        f.write(enaCheck)
        f.close() 
    
    @pyqtSlot(int)
    def on_selChannelFC_currentIndexChanged(self, index):

        self.on_getFromBoardBu_clicked()
#=================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = fcTable()
    ui.show()
    sys.exit(app.exec_())  
    

