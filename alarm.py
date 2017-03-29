# -*- coding: utf-8 -*-
from PyQt5 import  QtCore
from PyQt5.QtCore import  *
from PyQt5.QtWidgets import  *
import sys
from PyQt5.QtGui import *

from Ui_alarm import Ui_Dialog
import struct
#-------------------------------------------------------------------------------------------------------------------
# Global Variables
SOT = 0x7E

inmsg= bytearray(121)
vt=[]
vRef=3300>>4 
vRefTecI=330  
vRefLasT=33 
import os
alM=os.getcwd()+'\\alM'    
alS=os.getcwd()+'\\alS'    
alC=os.getcwd()+'\\alC'    

matrixDc=[[]]
matrixUn=[[]]
matrixCh=[]
dmw=0                     
textEdit=0
#-----------------------------------------------------

class alarm(QDialog, Ui_Dialog):

    def __init__(self, parent=None):

        super(alarm, self).__init__(parent)
        self.setupUi(self)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.readUart)
        self.timer.start(500)

        global matrixDc
        matrixDc =[[0 for i in range(5)] for j in range(10)]
        matrixDc[0][0]=self.ModuleTemp_LA
        matrixDc[0][1]=self.ModuleTemp_LA  
        matrixDc[0][2]=self.ModuleTemp_OK
        matrixDc[0][3]=self.ModuleTemp_OK   
        matrixDc[0][4]=self.ModuleTemp_HA


        matrixDc[1][0]=self.TEC_I_MON_LA
        matrixDc[1][1]=self.TEC_I_MON_LA   
        matrixDc[1][2]=self.TEC_I_MON_OK
        matrixDc[1][3]=self.TEC_I_MON_OK  
        matrixDc[1][4]=self.TEC_I_MON_HA


        matrixDc[2][0]=self.Laser_Temp_LA
        matrixDc[2][1]=self.Laser_Temp_LW
        matrixDc[2][2]=self.Laser_Temp_OK
        matrixDc[2][3]=self.Laser_Temp_HW
        matrixDc[2][4]=self.Laser_Temp_HA


        matrixDc[3][0]=self.Input_RF_MON_LA
        matrixDc[3][1]=self.Input_RF_MON_LA  
        matrixDc[3][2]=self.Input_RF_MON_OK
        matrixDc[3][3]=self.Input_RF_MON_OK   
        matrixDc[3][4]=self.Input_RF_MON_HA


        matrixDc[4][0]=self.LAS_RF_LA
        matrixDc[4][1]=self.LAS_RF_LA  
        matrixDc[4][2]=self.LAS_RF_OK
        matrixDc[4][3]=self.LAS_RF_OK   
        matrixDc[4][4]=self.LAS_RF_HA


        matrixDc[5][0]=self.FLSR_BIAS_LA
        matrixDc[5][1]=self.FLSR_BIAS_LW
        matrixDc[5][2]=self.FLSR_BIAS_OK
        matrixDc[5][3]=self.FLSR_BIAS_HW
        matrixDc[5][4]=self.FLSR_BIAS_HA


        matrixDc[6][0]=self.RLSR_BIAS_LA
        matrixDc[6][1]=self.RLSR_BIAS_LW
        matrixDc[6][2]=self.RLSR_BIAS_OK
        matrixDc[6][3]=self.RLSR_BIAS_HW
        matrixDc[6][4]=self.RLSR_BIAS_HA


        matrixDc[7][0]=self.LSR_PDI_LA
        matrixDc[7][1]=self.LSR_PDI_LW
        matrixDc[7][2]=self.LSR_PDI_OK
        matrixDc[7][3]=self.LSR_PDI_HW
        matrixDc[7][4]=self.LSR_PDI_HA


        matrixDc[8][0]=self.v5_LA
        matrixDc[8][1]=self.v5_LW
        matrixDc[8][2]=self.v5_OK
        matrixDc[8][3]=self.v5_HW
        matrixDc[8][4]=self.v5_HA

        
        matrixDc[9][0]=self.v24_LA
        matrixDc[9][1]=self.v24_LW
        matrixDc[9][2]=self.v24_OK
        matrixDc[9][3]=self.v24_HW
        matrixDc[9][4]=self.v24_HA



        global matrixUn
        matrixUn =[[0 for i in range(6)] for j in range(10)]
        matrixUn[0][0]=self.ModuleTemp_LA_2

        matrixUn[0][2]=self.ModuleTemp_OK_2

        matrixUn[0][4]=self.ModuleTemp_HA_2

        matrixUn[1][0]=self.TEC_I_MON_LA_2
   
        matrixUn[1][2]=self.TEC_I_MON_OK_2

        matrixUn[1][4]=self.TEC_I_MON_HA_2

        matrixUn[2][0]=self.Laser_Temp_LA_2
        matrixUn[2][1]=self.Laser_Temp_LW_2
        matrixUn[2][2]=self.Laser_Temp_OK_2
        matrixUn[2][3]=self.Laser_Temp_HW_2
        matrixUn[2][4]=self.Laser_Temp_HA_2

        matrixUn[3][0]=self.Input_RF_MON_LA_2

        matrixUn[3][2]=self.Input_RF_MON_OK_2

        matrixUn[3][4]=self.Input_RF_MON_HA_2
 
        matrixUn[4][0]=self.LAS_RF_LA_2

        matrixUn[4][2]=self.LAS_RF_OK_2

        matrixUn[4][4]=self.LAS_RF_HA_2       

        matrixUn[5][0]=self.FLSR_BIAS_LA_2
        matrixUn[5][1]=self.FLSR_BIAS_LW_2
        matrixUn[5][2]=self.FLSR_BIAS_OK_2
        matrixUn[5][3]=self.FLSR_BIAS_HW_2
        matrixUn[5][4]=self.FLSR_BIAS_HA_2

        matrixUn[6][0]=self.RLSR_BIAS_LA_2
        matrixUn[6][1]=self.RLSR_BIAS_LW_2
        matrixUn[6][2]=self.RLSR_BIAS_OK_2
        matrixUn[6][3]=self.RLSR_BIAS_HW_2
        matrixUn[6][4]=self.RLSR_BIAS_HA_2
        
        matrixUn[7][0]=self.LSR_PDI_LA_2
        matrixUn[7][1]=self.LSR_PDI_LW_2
        matrixUn[7][2]=self.LSR_PDI_OK_2
        matrixUn[7][3]=self.LSR_PDI_HW_2
        matrixUn[7][4]=self.LSR_PDI_HA_2

        global matrixCh
        matrixCh =[0 for i in range(10)] 
        matrixCh[0]=self.ModuleTemp_Ch
        matrixCh[1]=self.TEC_I_MON_Ch
        matrixCh[2]=self.Laser_Temp_Ch
        matrixCh[3]=self.Input_RF_MON_Ch
        matrixCh[4]=self.LAS_RF_Ch
        matrixCh[5]=self.FLSR_BIAS_Ch
        matrixCh[6]=self.RLSR_BIAS_Ch
        matrixCh[7]=self.LSR_PDI_Ch
        matrixCh[8]=self.v5_Ch
        matrixCh[9]=self.v24_Ch
      
    #reserver:
        for i in range(5):
            matrixDc[8][i].hide()
            matrixDc[9][i].hide()
        matrixCh[8].hide()
        matrixCh[9].hide()
        self.label_VIN.hide()
        self.label_v5.hide()
        
        self.on_getFromBoardBu_clicked()


        global  vt
        if  os.path.exists('vt')==True:  #
            f = open('vt', "r")
            vt = f.readlines()

            f.close()

        self.textEditBu.hide()
  
  #---------------UART-------------------------------------
    def readUart(self):
        global  inmsg
        if  os.path.exists(alS)==True:  #received from UART
            with open(alS, 'rb') as f:
                f.readinto(inmsg)
            f.close()

            alSSize=os.path.getsize(alS)


            value1=bytearray(inmsg)
            try:
                os.remove(alS)

            except:
                print('\n\nremove error 11')
                                                                                             

            if(sys.getsizeof(value1)<6):return

            if (value1[0]==0x7e):
                value1[0]=0
                if((value1[5]==0x31)or(value1[5]==0x33)or(value1[5]==0x35)):   
                     
                    if(value1[5]==0x31):#save all enable to board ACK
                        QMessageBox.question(self, 'Save  Status', "Save Alarm Successful.", QMessageBox.Ok)
                        return

                #get alarm table from board:
                    if(value1[5]==0x33):
                        global matrixDc
                        global matrixCh
                        for i in range(9):
                            for j in range(0,5):   
                                s2=struct.unpack('H', bytes([value1[8+i*11+j*2+1], value1[8+i*11+j*2]]))[0]      

                                s=s2*vRef/0x1000
                                s=round(s)
                                if(i>7):
                                    s/=10

                                matrixDc[i][j].setText(str(s))
                                    
                            if(value1[8+i*11+10]==1):            #enable
                                matrixCh[i].setChecked(True)
                            else:
                                matrixCh[i].setChecked(False)
                        QMessageBox.question(self, 'Get Alarm Status', "Get Alarm Successful.", QMessageBox.Ok)
                        self.DcToUn()
                        return
                    
                 #get alarm Calibrate from board:   
                    if(value1[5]==0x35):
                        
                        for i in range(10):
                            s2=struct.unpack('H', bytes([value1[8+i*2+1], value1[8+i*2]]))[0]

                            if(i==8):        #v5
                                s=s2*(3300)/0x1000/1000
                                matrixDc[i][2].setText("{:2.1f}".format(s/13.3*60.8))
                            elif(i==9):                #v24
                                s=s2*(3300)/0x1000/1000
  
                                s1=s*25
                                matrixDc[i][2].setText("{:2.1f}".format(s1))

                            else:
                                s=s2*(3300)/0x1000

                                s=round(s)
                                matrixDc[i][2].setText(str(s))

                        global dmw    #LSR-PDI calibrate value
                        dmw=int((value1[28]<<8)|value1[29])
                        if(dmw> 0x7FFF):
                            dmw-= 0x10000
                        dmw/=100

                        self.DcToUn()
                        self.UnToDc()
                        QMessageBox.question(self, 'Alarm Caliberate', "Alarm Caliberate Successful.", QMessageBox.Ok)
                        return  
        if  os.path.exists(alC)==True:  
            with open(alC, 'rb') as f:
                f.readinto(inmsg)
            f.close()
            value1=bytearray(inmsg)

 #============Save/Get/caliberate=======================================================                       
    @pyqtSlot()
    def on_saveToBoardBu_clicked(self):
        global textEdit
        self.on_textEditBu_clicked()
        outmsg = bytearray(99)

        outmsg = bytearray()
        outmsg.append(SOT)
        outmsg.append(0) #packet len high byte
        outmsg.append(94) #packet len low byte
        outmsg.append(0) #SRC ADDR
        outmsg.append(0) #DEST ADDR
        outmsg.append(0x30) #MSG TYPE
        outmsg.append(8) #MSG ID low byte
        outmsg.append(0) #MSG ID high byte

    #alarm_value:

        for i in range(8):
            for j in range(0,5):
                
                s=float(matrixDc[i][j].text())    #save as  mV
                if(i>7):    #+5v,+24v
                   s*=10                          #save as 100 mV
                   s=s*0x1000/vRef
                   s=s/60.8*13.3
                   s=round(s)

                else:   
                    s=round(s*0x1000/vRef)
                s1=int(s)
                if(s1>65535 or s1<0):    
                    QMessageBox.question(self, "Save Alarm Table", "Value over(Equivalency Box): raw="+str(i) +", column="+str(j)+", value="+matrixUn[i][j].text())
                    return
                s2=struct.pack('H',int(s))
                
                outmsg.append(s2[1])
                outmsg.append(s2[0])
                

    #alarm_enable:
            if(matrixCh[i].isChecked()==True):s=1
            else:s=0
            outmsg.append(s)


            
            
        bChkSum=0
        value1=bytearray(outmsg)
        for i in range(3,len(outmsg)):
            bChkSum+=value1[i]
        outmsg.append(bChkSum&0xff)  # CRC8
        outmsg.append(0x74) 
        outmsg.append(0x03)

        value1=bytearray(outmsg)
        try:
            f = open(alM  ,'wb')     #alarm  ->  main2
            f.write(outmsg)
            f.close()
            
  
        except:
            print('\n save to board error5' )

        textEdit=0
        
    @pyqtSlot()
    def on_getFromBoardBu_clicked(self):
        
        global textEdit
        if(textEdit==1):
            textEdit=0
            return
        outmsg = bytearray()
        outmsg.append(SOT)
        outmsg.append(9) #packet len low byte
        outmsg.append(0) #packet len high byte
        outmsg.append(0) #SRC ADDR
        outmsg.append(0) #DEST ADDR
        outmsg.append(0x32) #MSG TYPE
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
            f = open(alM  ,'wb') 
            f.write(outmsg)

            f.close()
    
        except:
            print('\n\n get from board error6' )


    @pyqtSlot()
    def on_CalibrateBu_clicked(self):
        outmsg = bytearray()
        outmsg.append(SOT)
        outmsg.append(9) #packet len low byte
        outmsg.append(0) #packet len high byte
        outmsg.append(0) #SRC ADDR
        outmsg.append(0) #DEST ADDR
        outmsg.append(0x34) #MSG TYPE
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
            f = open(alM  ,'wb') 
            f.write(outmsg)

            f.close()
    
        except:
            print('\n\n get from board error6' )
 #----------groupBoxDc to groupBox_Un--------------------------------------------------   
    def DcToUn(self):


    #Unit_value:
        try:
            for j in range(0,5,2):
                tmv=int(matrixDc[0][j].text())                          #module temp
                t=(tmv-500)/10

                matrixUn[0][j].setText( "{:3.1f}".format(t))

        except:
            print('except:module temp' )
                    
        try:
            for j in range(0,5,2):
                VCTLI =int(matrixDc[1][j].text())/1000                       #TEC-I-MON (mA)

                ITEC=(VCTLI*1000 - 1500)/.68

                matrixUn[1][j].setText("{:4.0f}".format(ITEC))

        except:
            print('except:TEC-I-MON' )

        try:
            for j in range(0,5):
                RTH =int(matrixDc[2][j].text())/1000                        #Laser temp
                
                if(RTH>1.593):
                    laserTem=2504*(pow(RTH,6))-9340.9*pow(RTH,5)+13651*pow(RTH,4)-9914.9*pow(RTH,3)+3781.4*pow(RTH,2)-788*pow(RTH,1)+123.07
                    laserTem/=100
                else:
                    global  vt
                    for i in range(100):
                        if(RTH<=float(vt[i])):break
                        dt=(RTH-float(vt[i-1]))/(float(vt[i])-float(vt[i-1]))
  
                        laserTem=101-i-dt
                    
                if(laserTem>100):laserTem=100
                matrixUn[2][j].setText("{:3.1f}".format(laserTem))

        except:
            print('except:Laser temp' )

                
          
        try:
            for j in range(0,5,2):
                tmv=int(matrixDc[3][j].text())/1000                     #Input-RF-MON (mv)
                inputRfV =45*(tmv*1000-360)/(1450-360)
                inputRfDbm=inputRfV-45

                matrixUn[3][j].setText("{:3.1f}".format(inputRfDbm))

        except:
            print('except:Input-RF-MON')

        try:
            for j in range(0,5,2):
                tmv=int(matrixDc[4][j].text())/1000                      #LAS-RF(mv)
                inputRfV =45*(tmv*1000-360)/(1450-360)
                inputRfDbm=inputRfV-45

                matrixUn[4][j].setText("{:3.1f}".format(inputRfDbm))

        except:
            print('except:LAS-RF' )
                

        try:
            for j in range(0,5):
                mv =int(matrixDc[5][j].text())				#FLSR-BIAS (mA)
                mv-=12.6  
                mA=mv*(75/200)/4.75
                flsrBias=self.flsrBiasCali(mv,mA)   #calibrat

                matrixUn[5][j].setText( "{:4.1f}".format(flsrBias)) 
                          
        except:
            print('except:FLSR-BIAS')    

        try:
            for j in range(0,5):
                mv =int(matrixDc[6][j].text())                          #RLSR-BIAS (mA)
                
                mA=mv/2
                rlsrBias=self.rlsrBiasCali(mv,mA)
                matrixUn[6][j].setText( "{:4.1f}".format(rlsrBias/10))        

        except:
            print('except:RLSR-BIAS' )

      
        try:
            for j in range(0,5):
                mv =int(matrixDc[7][j].text())                                    #LSR-PDI(mw)
                v=mv/1000
                k=0

                k=37

                mw=(v-.200)*k+2.31
                mwC=mw+dmw                          #mw check

                if(mwC<8):
                    mwC=mwC+(354-mv)/135           
                                                 
                
                if(mwC<0):mwC=0;
                if(mwC>65):mwC=65;

                matrixUn[7][j].setText( "{:4.1f}".format(mwC))

        except:
            print('except:LSR-PDI(mw)' )

        try:
            v5 =float(matrixDc[8][2].text())                          #+5(v)
            matrixDc[8][0].setText( "{:4.1f}".format(v5-1))        
            matrixDc[8][1].setText( "{:4.1f}".format(v5-0.5)) 
            matrixDc[8][3].setText( "{:4.1f}".format(v5+0.5))
            matrixDc[8][4].setText( "{:4.1f}".format(v5+1))
        except:
            print('except:+5' )

            
        try:
            v24 =float(matrixDc[9][2].text())                          #+24(v)
            matrixDc[9][0].setText( "{:4.1f}".format(v24-1))        
            matrixDc[9][1].setText( "{:4.1f}".format(v24-0.5)) 
            matrixDc[9][3].setText( "{:4.1f}".format(v24+0.5))
            matrixDc[9][4].setText( "{:4.1f}".format(v24+1))
        except:
            print('except:+24' )          
#---------caliberate-----------------------------------
    def flsrBiasCali(self,mv,mA):
        return mA
        if(mv>2800):
            flsrBias =mA-3.7
        elif(mv>2400):
            flsrBias =mA-3.7+(2800-mv)*0.5/400                       
        elif(mv>2000):
            flsrBias =mA-2.8+(2400-mv)*0.4/400                     
        elif(mv>1600):
            flsrBias =mA-2+(2000-mv)*0.8/400  
        elif(mv>1200):
            flsrBias =mA-2+(1600-mv)*0.3/400    
        elif(mv>800):
            flsrBias =mA-1.7+(1200-mv)*0.34/400
        elif(mv>400):
            flsrBias =mA-1.36+(800-mv)*0.66/400
        elif(mv>200):
            flsrBias =mA-0.6
        elif(mv>100):
            flsrBias =mA-0.6-(200-mv)*3.58/100
        elif(mv>70):
            flsrBias =mA-3.58-(100-mv)*2.18/10
        else:
            flsrBias=0
        if(flsrBias<0):  flsrBias=0        
        return flsrBias
        
    
    def rlsrBiasCali(self,mv,mA):
        return mA 
        if(mv>860):
            rlsrBias =mA+4-(1460-mv)*3/400  
        elif(mv>460):
            rlsrBias =mA+5-(860-mv)*3/400    
        elif(mv>260):
            rlsrBias =mA+6-(460-mv)*1/200
        elif(mv>160):
            rlsrBias =mA+6-(260-mv)*2/100
        elif(mv>140):
            rlsrBias =mA+4-(160-mv)*1/20
        elif(mv>120):
            rlsrBias =mA+3-(140-mv)*5/20
        elif(mv>100):
            rlsrBias =mA-2-(120-mv)*11/20
        elif(mv>80):
            rlsrBias =mA-8-(100-mv)*21/20
        elif(mv>70):
            rlsrBias =mA-28-(80-mv)*23/10
        else:
            rlsrBias=0
            
        if(rlsrBias<0):rlsrBias=0 
        return rlsrBias
                       
#----------groupBox_Un to groupBoxDc-------------------------------------------------- 
    def UnToDc(self):     

        for j in range(0,5):
            if((j==0)or(j==4)):
                try:   
                    t=float(matrixUn[0][j].text())                              #module temp
                    if(t<-20  or t>85 ):    
                        QMessageBox.question(self, "Alarm Table(Equivalency Box)", "module temp value over(range -20 to 85): raw="+str(0) +", column="+str(j)+", value="+matrixUn[0][j].text())
                        return
                    tmv=t*10+500
                    
                    matrixDc[0][j].setText( "{:4.0f}".format(tmv))
                except:
                    print('except:',j)

            if((j==0)or(j==4)):
                try:
                    ICTLI =float(matrixUn[1][j].text())                       #TEC-I-MON (mA)
                    if(ICTLI<-2000  or ICTLI>2000 ):    
                        QMessageBox.question(self, "Alarm Table(Equivalency Box)", "TEC-I-MON value over(range -200 to 2000): raw="+str(1) +", column="+str(j)+", value="+matrixUn[1][j].text())
                        return
                    VTEC=ICTLI*.68 + 1500
                    if(VTEC<0):
                        VTEC=0
    
                    matrixDc[1][j].setText("{:4.0f}".format(VTEC))
                except:
                    print('except:',j)

            if(j!=2):
                #try:
                RTH =float(matrixUn[2][j].text())                         #Laser temp
                 
                if(RTH<1  or RTH>85 ):    
                    QMessageBox.question(self, "Alarm Table(Equivalency Box)", "Laser temp value over(range 1 to 85): raw="+str(2) +", column="+str(j)+", value="+matrixUn[2][j].text())
                    return
                else:
                    global  vt
                    laserTemV=float(vt[100-round(RTH)])*1000
   
                matrixDc[2][j].setText("{:4.0f}".format(laserTemV))

                
            if((j==0)or(j==4)):
                try:
                    VCTLI =float(matrixUn[3][j].text())                       #Input-RF-MON (dBm)
                    if(VCTLI<-59  or VCTLI >40 ):    
                        QMessageBox.question(self, "Alarm Table(Equivalency Box)", "Input-RF-MON value over(range -59 to 40): raw="+str(3) +", column="+str(j)+", value="+matrixUn[3][j].text())
                        return

                    ITEC=((VCTLI+45)/45*(1450-360)+360)
                    
                    if(ITEC<0):
                        ITEC=0
                        
                    matrixDc[3][j].setText("{:4.0f}".format(ITEC))
 
                except:
                    print('except:',j)

                try:
                    VCTLI =float(matrixUn[4][j].text())                       #LAS-RF(dBm)dBm)
                    if(VCTLI<-59  or VCTLI >40 ):    
                        QMessageBox.question(self, "Alarm Table(Equivalency Box)", "LAS-RF value over(range -59 to 40): raw="+str(4) +", column="+str(j)+", value="+matrixUn[4][j].text())
                        return
                    ITEC=((VCTLI+45)/45*(1450-360)+360)
                    if(ITEC<0):
                        ITEC=0
                        
                    matrixDc[4][j].setText("{:4.0f}".format(ITEC))
                except:
                    print('except:',j)

            if(j!=2):
                try:
                    mA =float(matrixUn[5][j].text())                       #FLSR-BIAS (mA)
                    if(mA<0  or mA>250 ):    
                        QMessageBox.question(self, "Alarm Table(Equivalency Box)", "FLSR-BIAS value over(range 0 to 250): raw="+str(5) +", column="+str(j)+", value="+matrixUn[5][j].text())
                        return
                
                    mv=mA*4.75/(75/200)
  
                    if(mv<0):
                         mv=0

                    mv+=12.6    #caliberate 1mA   
                    matrixDc[5][j].setText("{:4.0f}".format(mv))
                except:
                    print('except:',j)

                try:
                    mA =float(matrixUn[6][j].text())                       #RLSR-BIAS (mA)
                    if(mA<0  or mA>250 ):    
                        QMessageBox.question(self, "Alarm Table(Equivalency Box)", "RLSR-BIAS value over(range 0 to 250 ): raw="+str(6) +", column="+str(j)+", value="+matrixUn[6][j].text())
                        return
                    mv=mA*20
  
                    if(mv<0):
                        mv=0

                    matrixDc[6][j].setText("{:4.0f}".format(mv))
                except:
                    print('except:',j)

                #try:
                mwC =float(matrixUn[7][j].text())                       #LSR-PDI (mw)
                if(mwC<0  or mwC>65):    
                    QMessageBox.question(self, "Alarm Table(Equivalency Box)", "LSR-PDI value over(range 0 to 65): raw="+str(7) +", column="+str(j)+", value="+matrixUn[7][j].text())
                    return

                if(mwC<8):     
                    mwC=mwC-(8-mwC)/4           #GUI caliberate   
                mw=mwC-dmw
                    
                k=37
                v=(mw-2.31)/k+.2
                mv=v*1000
                    
                if(mv<0):
                    mv=0
                    
                if(j<4):
                    if(matrixUn[7][j].text()==matrixUn[7][j+1].text()):
                        matrixDc[7][j].setText(matrixDc[7][j+1].text())
                    else:
                        matrixDc[7][j].setText("{:4.0f}".format(mv))
                else:
                    matrixDc[7][j].setText("{:4.0f}".format(mv))



 #---------threhold set------------------------------------               

    @pyqtSlot()
    def on_defaultBu_clicked(self):

    #Unit_value:
        matrixUn[0][0].setText( "{:3.1f}".format(-10))              #module temp
        matrixUn[0][4].setText( "{:3.1f}".format(85))

        ITEC =float(matrixUn[1][2].text())                            #TEC-I-MON (mA)
        matrixUn[1][0].setText("{:4.0f}".format(ITEC - 1500))
        matrixUn[1][4].setText("{:4.0f}".format(ITEC+1500))


        laserTem=float(matrixUn[2][2].text())                       #Laser temp
        matrixUn[2][0].setText("{:3.1f}".format(laserTem-5))
        matrixUn[2][1].setText("{:3.1f}".format(laserTem-3))
        matrixUn[2][3].setText("{:3.1f}".format(laserTem+3))
        matrixUn[2][4].setText("{:3.1f}".format(laserTem+5))  


        inputRfDbm=float(matrixUn[3][2].text())                     #Input-RF-MON (dBm)
        matrixUn[3][0].setText("{:1.2f}".format(inputRfDbm-5))
        matrixUn[3][2].setText("{:1.2f}".format(inputRfDbm))
        matrixUn[3][4].setText("{:1.2f}".format(inputRfDbm+5))

        inputRfDbm=float(matrixUn[4][2].text())                         #LAS-RF(dBm)
        matrixUn[4][0].setText("{:1.2f}".format(inputRfDbm-2))
        matrixUn[4][4].setText("{:1.2f}".format(inputRfDbm+2))

        flsrBias=float(matrixUn[5][2].text())                          #FLSR-BIAS (mA)
        matrixUn[5][0].setText( "{:4.1f}".format(flsrBias-25)) 
        matrixUn[5][1].setText( "{:4.1f}".format(flsrBias-10)) 
        matrixUn[5][3].setText( "{:4.1f}".format(flsrBias+10)) 
        matrixUn[5][4].setText( "{:4.1f}".format(flsrBias+25))                              

        rlsrBias=float(matrixUn[6][2].text())                          #RLSR-BIAS (mA)
        matrixUn[6][0].setText( "{:4.1f}".format(rlsrBias-25))        
        matrixUn[6][1].setText( "{:4.1f}".format(rlsrBias-10)) 
        matrixUn[6][3].setText( "{:4.1f}".format(rlsrBias+10))
        matrixUn[6][4].setText( "{:4.1f}".format(rlsrBias+25))

        mwC=float(matrixUn[7][2].text())                                #LSR-PDI(mw)                      
        matrixUn[7][0].setText( "{:4.2f}".format(mwC-3))
        matrixUn[7][1].setText( "{:4.2f}".format(mwC-2))
        matrixUn[7][3].setText( "{:4.2f}".format(mwC+2))
        matrixUn[7][4].setText( "{:4.2f}".format(mwC+3))

        self.UnToDc()

    @pyqtSlot()
    def on_textEditBu_clicked(self):
        global textEdit
        textEdit=1
        self.UnToDc()
#==================================================================================   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = alarm()
    ui.show()
    sys.exit(app.exec_()) 
    

