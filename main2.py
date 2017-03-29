# -*- coding: utf-8 -*-
#  Project:     LEML Mini Tx
#  File:        main2.py
#
#  Created on:  17 Dec 2016
#  Reversion:   V1017
#////////////////////////////////////////////////

from PyQt5 import QtCore,QtGui
from PyQt5.QtCore import  *
from PyQt5.QtWidgets import  *
import sys
from PyQt5.QtGui import *

#import tkinter.messagebox as msgbx
import serial
from tcTable import tcTable
from fcTable import fcTable
from alarm import alarm
from boardInfo import boardInfo
#from main import main
#import main.py 

from Ui_main2 import Ui_miniTx

import struct
import os
#---------General Global Variables----------------------------------------------------------------------------------------------------------


COMPORT_STR="COM7"
ser = 0
SOT = 0x7E
inbuflen =122
inmsg= bytearray(122)
vRef=3.3

countSubResendTc=0
countSubResendFc=0
countSubResendAl=0
countSubResendBo=0
countSaveResend=0
countGetResend=0
tcM=os.getcwd()+'\\tcM'    
tcS=os.getcwd()+'\\tcS'   
tcSe=os.getcwd()+'\\tcSe'   

fcM=os.getcwd()+'\\fcM'    
fcS=os.getcwd()+'\\fcS'    
fcSe=os.getcwd()+'\\fcSe'   
alM=os.getcwd()+'\\alM'   
alS=os.getcwd()+'\\alS'   
alC=os.getcwd()+'\\alC'  
boM=os.getcwd()+'\\boM'   
boS=os.getcwd()+'\\boS'  
counReceive=0
sliRun=0
spiRun=0

scaleChange=0
getDac=0
alarmSta =[0 for i in range(12)]
adcData =[0 for i in range(12)]
dacSpin =[0 for i in range(24)]
rlsrBias_co=[0 for i in range(10)]

stepRefresh=0
refreshLa=0
autoRefCheckLa=0
autoRefCheckDc=0

dacReco =[0 for i in range(25)] #DAC record
for i in range(25):
    dacReco[i]=4098             #DAC record initial

dacLasEdit=0
spinRun=0
sliderRun=0

pdiMwRaw=0
vt=[]
#-------------class-------------------------------------------------------------
class miniTx(QDialog, Ui_miniTx):

    def __init__(self, parent=None):
        super(miniTx, self).__init__(parent)
        self.setupUi(self)
        if  os.path.exists(tcM)==True:     
            os.remove(tcM)
        if  os.path.exists(fcM)==True:    
            os.remove(fcM)
        if  os.path.exists(alM)==True:   
            os.remove(alM) 
        if  os.path.exists(boM)==True:    
            os.remove(boM)       

    #ADC_data:
        adcData[0]=self.ModuleTemp_da
        adcData[1]=self.TEC_I_MON_da
        adcData[2]=self.Laser_Temp_da
        adcData[3]=self.Input_RF_MON_da
        adcData[5]=self.LAS_RF_da

        adcData[4]=self.SBS_MON_da
        adcData[6]=self.FLSR_BIAS_da
        adcData[7]=self.RLSR_BIAS_da
        adcData[8]=self.LSR_PDI_da
        adcData[9]=self.v5_da
        adcData[10]=self.v24_da


    #ADC_alarm:
        alarmSta[0]=self.ModuleTemp_al
        alarmSta[1]=self.TEC_I_MON_al
        alarmSta[2]=self.Laser_Temp_al
        alarmSta[3]=self.Input_RF_MON_al
        alarmSta[4]=self.LAS_RF_al

        #alarmSta[4]=self.SBS_MON_al
        alarmSta[5]=self.FLSR_BIAS_al
        alarmSta[6]=self.RLSR_BIAS_al
        alarmSta[7]=self.LSR_PDI_al
        alarmSta[8]=self.v5_al
        alarmSta[9]=self.v24_al

    #rlsrBias_coefficient:
        rlsrBias_co[0]=2
        rlsrBias_co[1]=14/20


        

        self.preTrigSli.hide()          
        self.lasTrigSli.hide()         
        self.type1Bo.hide()
        self.type2Bo.hide()
#--------DAC_initial-------------------------------------
        dacSpin[0]=self.attnSpi
        dacSpin[1]=self.mp_tilt_adjSpi
        dacSpin[2]=self.peak_adj_mpSpi
        dacSpin[3]=self.vampSpi        
        dacSpin[4]=self.tp_attnSpi
        dacSpin[5]=self.vsbsSpi
        dacSpin[6]=self.vxtSpi
        dacSpin[7]=self.vxtSpi  

        dacSpin[8]=self.vcso2Spi
        dacSpin[9]=self.vxmodSpi
        dacSpin[10]=self.modbiasSpi
        dacSpin[11]=self.vctbSpi        
        dacSpin[12]=self.vctb3Spi
        dacSpin[13]=self.vcso4Spi
        dacSpin[14]=self.vclampSpi
        dacSpin[15]=self.vcso3Spi          

        dacSpin[16]=self.FlsrBiasSpi
        dacSpin[17]=self.RlsrBiasSpi
        dacSpin[18]=self.LsrTempSpi
        dacSpin[19]=self.tp_tiltSpi        
        dacSpin[20]=self.peak_adj_tpSpi
        dacSpin[21]=self.vadjSpi
        dacSpin[22]=self.ditherSpi
        dacSpin[23]=self.ditherTuneSpi

#--------v to t-------------------------------------
        global  vt
        if  os.path.exists('vt')==True:  
            f = open('vt', "r")
            vt = f.readlines()
            print('\n\n', vt[2])
            f.close()

#--------reserver-------------------------------------
        self.SBS_MON_al.hide()
        self.v24_al.hide()
        self.v5_al.hide()            
#============UART============================================================        
    def readUart(self):
        global ser
        global countSubResendTc
        global countSubResendFc
        global countSubResendAl
        global countSubResendBo
        global countSaveResend
        global countGetResend


    #commands from sub-windows:
        if(self.connectBu.text()!='Disconnect'):return
        if  os.path.exists(tcM)==True:      
            if(countSubResendTc%4==0):        

                outmsg = bytearray(os.path.getsize(tcM))   
                with open(tcM, 'rb') as f:
                     f.readinto(outmsg)
                f.close()


                try:
                    ser.write(outmsg)

                except:
                    print('\n\nser.write error7' )
                
                countSubResendTc+=1 
                return
            else:
                if(countSubResendTc>50):
                    countSubResendTc=0
                    os.remove(tcM)


            countSubResendTc+=1
    
        if  os.path.exists(fcM)==True:      
            if(countSubResendFc%4==0):         
                outmsg = bytearray(os.path.getsize(fcM)) 
                with open(fcM, 'rb') as f:
                     f.readinto(outmsg)
                f.close()
            

                try:
                    ser.write(outmsg)
                except:
                    print('\n\nFC.write error7' )
                countSubResendFc+=1 
                return
            else:
                if(countSubResendFc>50):
                    countSubResendFc=0
                    os.remove(fcM)
            countSubResendFc+=1
            
        if  os.path.exists(alM)==True:      
            if(countSubResendAl%4==0):        

                outmsg = bytearray(os.path.getsize(alM))  
                with open(alM, 'rb') as f:
                     f.readinto(outmsg)
                f.close()
  
                try:
                    ser.write(outmsg)

                except:
                    print('\n\nser.write error7' )
                countSubResendAl+=1
                return
            else:
                if(countSubResendAl>50):
                    countSubResendAl=0
                    os.remove(alM)
                    
            countSubResendAl+=1
            
        if  os.path.exists(boM)==True:      
            
            if(countSubResendBo%4==0):          
                outmsg = bytearray(os.path.getsize(boM))   
                with open(boM, 'rb') as f:
                     f.readinto(outmsg)
                f.close()

                try:
                    ser.write(outmsg)
   
                except:
                    print('\n\nser.write error7' )
                countSubResendBo+=1
                return
            else:

                if(countSubResendBo>50):
                    countSubResendBo=0
                    os.remove(boM)

            countSubResendBo+=1      
     #resend:           
        if(self.saveBu.text()=='Save...'):
            if(countSaveResend%10==0):           
                self.on_saveBu_clicked()

                countSaveResend+=1
                return
            if(countSaveResend>50):
                countSaveResend=0

                self.saveBu.setText("Save")

            countSaveResend+=1

        if(self.getBu.text()=='Get...'):
            
            if(countGetResend%4==0):         
                self.on_getBu_clicked()

                countGetResend+=1
                return
            if(countGetResend>50):
                countGetResend=0

                self.getBu.setText("Get")
            countGetResend+=1      

    #UART RX:               
        global  inmsg
        global counReceive

        inmsg = ser.read(ser.inWaiting())

        value1=bytearray(inmsg)

        if(len(value1)<10):

            return
       
        
        
        if (value1[0]==0x7e):
            if((value1[5]==0x7)or(value1[5]==0x9)or(value1[5]==0x11)or(value1[5]==0x13)or(value1[5]==0x15)or
              (value1[5]==0x17)or (value1[5]==0x19)or(value1[5]==0x1b) or
              (value1[5]==0x21)or(value1[5]==0x23)or(value1[5]==0x25)or (value1[5]==0x29)or(value1[5]==0x2b)or    
              (value1[5]==0x31)or(value1[5]==0x33)or(value1[5]==0x35)or(value1[5]==0x51)or(value1[5]==0x53)or(value1[5]==0x61)or
              (value1[5]==0x71)or(value1[5]==0x73)or(value1[5]==0x75)): 

                if((value1[5]==0x7)):
                    QMessageBox.about(self, "Save DAC Status", "Save DACSuccessful.")
                    self.saveBu.setText("Save") 
                    return
 
                if(value1[5]==0x09):#get DAC
                    if(self.checkSum(value1)!=value1[58]):
                        return
                    global getDac
                    getDac =1
                    
                #IC1:
                    s = (4096*(value1[8]*256+value1[9]))/1024/10   
                    s=round(s,3)
                    self.attnSli.setValue(s)

                    s = (4096*(value1[10]*256+value1[11]))/1024/10   
                    s=round(s,3)
                    self.mp_tilt_adjSli.setValue(s)

                    s = (4096*(value1[12]*256+value1[13]))/1024/10   
                    s=round(s,3)
                    self.peak_adj_mpSli.setValue(s)

                    s = (4096*(value1[14]*256+value1[15]))/1024/10   
                    s=round(s,3)
                    self.vampSli.setValue(s)

                    s = (4096*(value1[16]*256+value1[17]))/1024/10   
                    s=round(s,3)
                    self.tp_attnSli.setValue(s)

                    s = (4096*(value1[18]*256+value1[19]))/1024/10   
                    s=round(s,3)
                    self.vsbsSli.setValue(s)

                    s = (4096*(value1[20]*256+value1[21]))/1024/10   
                    s=round(s,3)
                    self.vxtSli.setValue(s)


                 #IC2:   
                    s = (4096*(value1[24]*256+value1[25]))/1024/10   
                    s=round(s,3)
                    self.vcso2Sli.setValue(s)

                    s = (4096*(value1[26]*256+value1[27]))/1024/10   
                    s=round(s,3)
                    self.vxmodSli.setValue(s)

                    s = (4096*(value1[28]*256+value1[29]))/1024/10   
                    s=round(s,3)
                    self.modbiasSli.setValue(s)

                    s = (4096*(value1[30]*256+value1[31]))/1024/10   
                    s=round(s,3)
                    self.vctbSli.setValue(s)

                    s = (4096*(value1[32]*256+value1[33]))/1024/10   
                    s=round(s,3)
                    self.vctb3Sli.setValue(s)

                    s = (4096*(value1[34]*256+value1[35]))/1024/10   
                    s=round(s,3)
                    self.vcso4Sli.setValue(s)

                    s = (4096*(value1[36]*256+value1[37]))/1024/10   
                    s=round(s,3)
                    self.vclampSli.setValue(s)

                    s = (4096*(value1[38]*256+value1[39]))/1024/10   
                    s=round(s,3)
                    self.vcso3Sli.setValue(s)

                #IC3:
                    s = (4096*(value1[40]*256+value1[41]))/1024/10   
                    s=round(s,3)
                    self.FlsrBiasSli.setValue(s)

                    s = (4096*(value1[42]*256+value1[43]))/1024/10   
                    s=round(s,3)
                    self.RlsrBiasSli.setValue(s)

                    s = (4096*(value1[44]*256+value1[45]))/1024/10   
                    s=round(s,3)
                    self.LsrTempSli.setValue(s)

                    s = (4096*(value1[46]*256+value1[47]))/1024/10   
                    s=round(s,3)
                    self.tp_tiltSli.setValue(s)

                    s = (4096*(value1[48]*256+value1[49]))/1024/10   
                    s=round(s,3)
                    self.peak_adj_tpSli.setValue(s)

                    s = (4096*(value1[50]*256+value1[51]))/1024/10   
                    s=round(s,3)
                    self.vadjSli.setValue(s)

                    s = (4096*(value1[52]*256+value1[53]))/1024/10   
                    s=round(s,3)
                    self.ditherSli.setValue(s)

                    s = (4096*(value1[54]*256+value1[55]))/1024/10   #ditherTune
                    s=round(s,3)
                    self.ditherTuneSli.setValue(s)

                #frequency:
                    s=value1[56]*256+value1[57] 
                    s=round(s,4)
                    self.freqEdit.setText(str(s))
	
  
                    self.getBu.setText("Get")
                    self.rfRatio()

                    value1[5]=0
                    getDac=0
                    return

                if((value1[5]==0x11)):
                    counReceive+=1
                    countSubResendTc=0
                    if  os.path.exists(tcM)==True:
                        os.remove(tcM)
                    
                    inmsg1= bytearray(6)
                    for i in range(6):
                        inmsg1[i]=inmsg[i]

                    f = open(tcS,'wb') 
                    f.write(inmsg1)

                    f.close()

                    if  os.path.exists(tcM)==True:
                        os.remove(tcM)
                        countSubResendTc=0

                    return
                        
                if((value1[5]==0x13)):
                    counReceive+=1
                    countSubResendTc=0
                    f = open(tcS  ,'wb') 
                    f.write(inmsg)

                    f.close()
                    if  os.path.exists(tcM)==True:
                        os.remove(tcM)
                        countSubResendTc=0
                    return

                if((value1[5]==0x15)):
                    countSubResendTc=0
                    if(sys.getsizeof(inmsg)>18):
                        inmsg1= bytearray(19)
                        for i in range(18):
                            inmsg1[i]=inmsg[i]

                    counReceive+=1
                    f = open(tcS,'wb') 
                    f.write(inmsg1)

                    f.close()

                    if  os.path.exists(tcM)==True:
                        os.remove(tcM)
                        countSubResendTc=0
                    value1[5]=0    #clear
                    return

                if((value1[5]==0x19)):
                    counReceive+=1
                    countSubResendTc=0
                    inmsg1= bytearray(6)
                    for i in range(6):
                        inmsg1[i]=inmsg[i]
 
                    f = open(tcSe,'wb') 
                    f.write(inmsg1)

                    f.close()
                    if  os.path.exists(tcM)==True:
                        os.remove(tcM)

                        countSubResendTc=0
                    return

                if((value1[5]==0x1b)):
                    counReceive+=1
                    countSubResendTc=0
                    f = open(tcSe  ,'wb') 
                    f.write(inmsg)

                    f.close()
                    if  os.path.exists(tcM)==True:
                        os.remove(tcM)
                        countSubResendTc=0

                    return
   
                if  os.path.exists(fcM)==True:
                    os.remove(fcM)
                    countSubResendFc=0                  


                if((value1[5]==0x21)):
                    counReceive+=1
                    countSubResendFc=0

                    inmsg1= bytearray(6)
                    for i in range(6):
                        inmsg1[i]=inmsg[i]

                    f = open(fcS,'wb') 
                    f.write(inmsg1)

                    f.close()
                    if  os.path.exists(fcM)==True:
                        os.remove(fcM)

                    return
                        
                if((value1[5]==0x23)):
                    counReceive+=1
                    countSubResendFc=0
                    f = open(fcS  ,'wb') 
                    f.write(inmsg)
 
                    f.close()
                    if  os.path.exists(fcM)==True:
                        os.remove(fcM)

                    return
  
                if((value1[5]==0x25)):
                    countSubResendFc=0
                    if(sys.getsizeof(inmsg)>18):
                        inmsg1= bytearray(19)
                        for i in range(18):
                            inmsg1[i]=inmsg[i]

                    counReceive+=1
                    f = open(fcS  ,'wb') 
                    f.write(inmsg1)
                    f.close()

                    value1[5]=0    
                    if  os.path.exists(fcM)==True:
                        os.remove(fcM)
                    return

                if((value1[5]==0x29)):
                    counReceive+=1
                    countSubResendFc=0
                    inmsg1= bytearray(6)
                    for i in range(6):
                        inmsg1[i]=inmsg[i]
                    f = open(fcSe,'wb') 
                    f.write(inmsg1)

                    f.close()
                    if  os.path.exists(fcM)==True:
                        os.remove(fcM)

                    return
 
                if((value1[5]==0x2b)):
                    counReceive+=1
                    countSubResendFc=0
                    f = open(fcSe  ,'wb') 
                    f.write(inmsg)
                    f.close()
                    if  os.path.exists(fcM)==True:
                        os.remove(fcM)
                    return
                if((value1[5]==0x31)):
                    counReceive+=1
                    countSubResendAl=0
                    if  os.path.exists(alM)==True:
                        os.remove(alM)

                    
                    inmsg1= bytearray(6)
                    for i in range(6):
                        inmsg1[i]=inmsg[i]

                    f = open(alS,'wb') 
                    f.write(inmsg1)

                    f.close()
                    return
     
                if((value1[5]==0x33)):
                    counReceive+=1
                    countSubResendAl=0
                    if  os.path.exists(alM)==True:
                        os.remove(alM)
                    
                    f = open(alS  ,'wb') 
                    f.write(inmsg)

                    f.close()
                    return
                if((value1[5]==0x35)):#get alarm caliberate from board
                    counReceive+=1
                    countSubResendAl=0

                    
                    f = open(alS  ,'wb') 
                    f.write(inmsg)

                    f.close()

                    if  os.path.exists(alM)==True:
                        os.remove(alM)

                    return
                if((value1[5]==0x51)):#save board info to board ACK
                    counReceive+=1
                    countSubResendBo=0

                    inmsg1= bytearray(6)
                    for i in range(6):
                        inmsg1[i]=inmsg[i]

                    f = open(boS,'wb') 
                    f.write(inmsg1)

                    f.close()
                    if  os.path.exists(boM)==True:
                        os.remove(boM)
                       
                    return

                if((value1[5]==0x53)):#get board info from board
                    print('read len3=',len(value1))
                    counReceive+=1
                    countSubResendBo=0

                    
                    f = open(boS  ,'wb') 
                    f.write(inmsg)

                    f.close()
                    if  os.path.exists(boM)==True:
                        os.remove(boM)

                    return 
                if((value1[5]==0x61)):#Calibrate laser power ACK
                    QMessageBox.about(self, "Calibrate laser power", "Calibrate laser power Successfully.")
                    return

                if((value1[5]==0x71)):#Gain  Save  ACK
                    QMessageBox.about(self, "Gain  Save", "Gain  Save  Successfully.")
                    return

                if((value1[5]==0x73)):#Get Gain
                    s = value1[8]                       #AGC/manual
                    if(s==1):
                        self.agcBo.setChecked(True)
                    else:
                        self.agcBo.setChecked(False)
                    
                    s=struct.unpack('h', bytes([value1[10], value1[9]]))[0] 
                    s/=100    

                 
                    self.rfAttnDb.setText(str(s))

                    self.getFromBoardGainBu.setText('Get from Board')
                    return
                
                if((value1[5]==0x75)):#Gain control single step
                    self.gainUpBu.setText('Up')
                    self.gainDownBu.setText('Down')
                    
            else:   #ADC

                counReceive=0

            #DC monitor interface:
                if((len(value1)<61)or(value1[5]!=0x41)or(value1[59]!=0x74)or(value1[60]!=0x03)):

                    return

                global stepRefresh
                if((stepRefresh==1)or(self.continueBo.isChecked()==True)):
                    stepRefresh=0
                    for i in range(0,11):                                       #V: 
                        mv=(vRef*(value1[8+i*2]*256+value1[9+i*2]))/0x1000
                        if(i==9):                                               #v5
                            adcData[i].setText("{:1.3f}".format(mv/13.3*60.8))
                        elif(i==10):                                            #v24

                            adcData[i].setText("{:1.3f}".format(mv*25.23))
                        else:
                            adcData[i].setText("{:1.3f}".format(mv))
                #module temp:
                    tmv=(vRef*(value1[8]*256+value1[9]))/0x1000                 
                    t=(tmv*1000-500)/10  
                    self.ModuleTemp_da_2.setText( "{:3.1f}".format(t))

                 #TEC-I-MON (mA):    
                    VCTLI =float(adcData[1].text())
                    ITEC=((VCTLI*1000 - 1500)/0.68)
                    self.TEC_I_MON_da_2.setText("{:4.0f}".format(ITEC))
                    
                 #Laser temp:
                    RTH =float(vRef*(value1[12]*256+value1[13]))/0x1000

                    if(RTH>1593):
                        laserTem=2504*(pow(RTH,6))-9340.9*pow(RTH,5)+13651*pow(RTH,4)-9914.9*pow(RTH,3)+3781.4*pow(RTH,2)-788*pow(RTH,1)+123.07
                        laserTem/=100
                    else:
                        global  vt
                        for i in range(100):
                            if(RTH<=float(vt[i])):break
                            dt=(RTH-float(vt[i-1]))/(float(vt[i])-float(vt[i-1]))
                            laserTem=101-i-dt


                    self.Laser_Temp_da_2.setText("{:3.1f}".format(laserTem))

                    
                  #Input-RF-MON:
                    tmv=vRef*(value1[14]*256+value1[15])/0x1000                 #dBm:
                    inputRfV =45*(tmv*1000-360)/(1450-360)
                    inputRfDbm=inputRfV-45
                    self.Input_RF_MON_dbm.setText("{:3.1f}".format(inputRfDbm))

                  #LAS-RF:
                    tmv=vRef*(value1[18]*256+value1[19])/0x1000                 #dBm:
                    LasRfV =45*(tmv*1000-360)/(1450-360)          
                    LasRfDbm=LasRfV-45
                    self.LAS_RF_dbm.setText("{:3.1f}".format(LasRfDbm))

                  #FLSR-BIAS:   
                    v =(vRef*(value1[20]*256+value1[21]))/0x1000     
                    mv=v*1000
                    mv-=12.6    
                    mA=mv*(75/200)/4.75
                    self.flasrScale.setText("{:1.3f}".format((75/200)/4.75))
                    flsrBias=self.flsrBiasCali(mv,mA)                           #calibrat 
                    self.FLSR_BIAS_da_2.setText( "{:4.1f}".format(flsrBias))    #mA
                    
                 #RLSR-BIAS:  
                    v =(vRef*(value1[22]*256+value1[23]))/0x1000     
                    mv=v*1000
                    mA=mv/2
                    self.rlasrScale.setText("{:1.3f}".format((100/200)/10))
                    rlsrBias=self.rlsrBiasCali(mv,mA)                           #calibrat
                    self.RLSR_BIAS_da_2.setText( "{:4.1f}".format(rlsrBias/10))  #mA


                #LSR-PDI(mw):
                    v=(vRef*(value1[8+16]*256+value1[9+16]))/0x1000
                    k=37
                    
                    mw=(v-.200)*k+2.31
                    global pdiMwRaw
                    pdiMwRaw=mw                                 #for board calibrate as record

                    dmw=int((value1[52]<<8)|value1[53])         #board caliberate
                    if(dmw> 0x7FFF):
                        dmw-= 0x10000
                    dmw/=100
                    mwC=mw+dmw                          #mw check
                    if(mwC<8):     
                        mwC=mwC+(8-mwC)/4           #GUI caliberate
                    if(mwC<0):mwC=0;
                    if(mwC>65):mwC=65;
                    self.LSR_PDI_da_2.setText("{:3.1f}".format(mwC))

            #Laser control interface:
                if((stepRefresh==2)or(self.laserContinueBo.isChecked()==True)):
                    stepRefresh=0    

                    
                #FLSR-BIAS:
                    v =(vRef*(value1[20]*256+value1[21]))/0x1000     
                    mv=v*1000
                    mv-=12.6   
                    mA=mv*(75/200)/4.75
                    self.flasrScale.setText("{:1.3f}".format((75/200)/4.75))    #scale factor
                    flsrBias=self.flsrBiasCali(mv,mA)                           #calibrat 
                    self.e7.setText( "{:4.1f}".format(flsrBias))                #mA
                    
                 #RLSR-BIAS:  
                    v =(vRef*(value1[22]*256+value1[23]))/0x1000     
                    mv=v*1000
                    mA=mv/2
                    self.rlasrScale.setText("{:1.3f}".format((100/200)/10))

                    rlsrBias=self.rlsrBiasCali(mv,mA)                           #calibrat
                    self.e8.setText( "{:4.1f}".format(rlsrBias/10))             #mA

                     
                #module temp:
                    tmv=(vRef*(value1[8]*256+value1[9]))/0x1000             
                    t=(tmv*1000-500)/10  
                    self.e1.setText( "{:3.1f}".format(t))
                    
                #TEC-I-MON (mA):
                    VCTLI =vRef*(value1[10]*256+value1[11])/0x1000

                    ITEC=((VCTLI*1000 - 1500)/0.68)
                    self.e2.setText("{:4.0f}".format(ITEC))
                    
                #Laser temp:
                    self.e3.setText(self.Laser_Temp_da_2.text())

                #SBS-MON(v):
                    mv=(vRef*(value1[8+8]*256+value1[9+8]))/0x1000
                    self.e5.setText("{:1.3f}".format(mv))

                #LSR-PDI(mw):
                    self.LSR_PDIEdit.setText(self.LSR_PDI_da_2.text())
                    
                    
              #alarm_check:
                self.LSR_Alarm.setStyleSheet("background-color: white;")
                self.LSR_Alarm.setText('OK')
                alarming=0
                if(len(value1)<41):
                    return
                for i in range(10):
                    if(value1[30+i]==1):
                        alarmSta[i].setStyleSheet("background-color: red;")                #LA
                        alarmSta[i].setText('LA')
                        self.LSR_Alarm.setStyleSheet("background-color: red;")            
                        self.LSR_Alarm.setText('LA')
                        alarming=1

                    else:
                        if(value1[30+i]==2):
                            if((i==0)or(i==1)or(i==3)or(i==4)):
                                alarmSta[i].setStyleSheet("background-color: white;")       #OK (Module Temp,TEC-I-MON,LAS-RF)
                                alarmSta[i].setText('OK')
                            else:
                                alarmSta[i].setStyleSheet("background-color: yellow;")      #LW
                                alarmSta[i].setText('LW')
                                if(alarming!=1):
                                    self.LSR_Alarm.setStyleSheet("background-color: yellow;")    
                                    self.LSR_Alarm.setText('LW')
                        else:
                            if(value1[30+i]==4):                                            #HW
                                if((i==0)or(i==1)or(i==3)or(i==4)):
                                    alarmSta[i].setStyleSheet("background-color: white;")   #OK (Module Temp,TEC-I-MON,LAS-RF)
                                    alarmSta[i].setText('OK')
                                else:
                                    alarmSta[i].setStyleSheet("background-color: yellow;")
                                    alarmSta[i].setText('HW')
                                    if(alarming!=1):
                                        self.LSR_Alarm.setStyleSheet("background-color: yellow;")
                                        self.LSR_Alarm.setText('HW')
                            else:
                                if(value1[30+i]==8):
                                    alarmSta[i].setStyleSheet("background-color: red;")     #HA
                                    alarmSta[i].setText('HA')
                                    self.LSR_Alarm.setStyleSheet("background-color: red;")             
                                    self.LSR_Alarm.setText('HA')
                                    alarming=1
                                else:
                                    alarmSta[i].setStyleSheet("background-color: white;")    #OK
                                    alarmSta[i].setText('OK')
                
                f = open(alC  ,'wb') 
                f.write(inmsg)
                f.close()

        else:
                ser.close()
                ser.open()
#------------------chechsum----------------------------
    def checkSum(self,value1):
        bChkSum=0
        for i in range(3,value1[2]+2):
            bChkSum+=value1[i]
        return bChkSum&0xff
                
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
  
  #////////////////////////////////////////button click////////////////////////////////////////////////////////  
    @pyqtSlot()
    def on_dcMonitorBu_clicked(self):
        global scaleChange
        if(scaleChange!=0):
            scaleChange=0
            self.on_LsrControlsBu_clicked()
            return
        self.dcMonitorWi.show()
        self.PredistorterWi.hide()
        self.lsrControlsWi.hide()
        self.rfGainWi.hide()
        ui.resize(920, 400)
        
    @pyqtSlot()
    def on_PredistorterBu_clicked(self):
        global dacLasEdit
        if(dacLasEdit==1):
            dacLasEdit=0
            return
        self.dcMonitorWi.hide()
        self.lsrControlsWi.hide()
        self.rfGainWi.hide()
        self.PredistorterWi.setGeometry(10,30,780,590);
        self.PredistorterWi.show()
        ui.resize(920, 630)

    
    @pyqtSlot()
    def on_LsrControlsBu_clicked(self):
        self.dcMonitorWi.hide()
        self.PredistorterWi.hide()
        self.rfGainWi.hide()
        self.lsrControlsWi.setGeometry(10,30,780,460);
        self.lsrControlsWi.show()
        ui.resize(920, 500)

    
    @pyqtSlot()
    def on_rfGainfBu_clicked(self):
        self.dcMonitorWi.hide()
        self.PredistorterWi.hide()
        self.lsrControlsWi.hide()
        self.rfGainWi.setGeometry(10,30,780,360);
        self.rfGainWi.show()
        ui.resize(920, 400)
    
    @pyqtSlot()
    def on_TCBu_clicked(self):
        self.tcTable=tcTable()
        self.tcTable.show()



  #-----------------------------------save-get----------------------------------  
    @pyqtSlot()
    def on_saveBu_clicked(self):
        outmsg = bytearray()
        outmsg.append(SOT)
        outmsg.append(0) #packet len highlow byte
        outmsg.append(56) #packet len high byte

        outmsg.append(0) #SRC ADDR
        outmsg.append(0) #DEST ADDR

        outmsg.append(6) #MSG TYPE
        outmsg.append(8) #MSG ID low byte

        outmsg.append(0) #MSG ID high byte
     #value:

     #IC1:   
        dacData= round(self.attnSpi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        dacData= round(self.mp_tilt_adjSpi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        dacData= round(self.peak_adj_mpSpi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        dacData= round(self.vampSpi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        dacData= round(self.tp_attnSpi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        dacData= round(self.vsbsSpi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        dacData= round(self.vxtSpi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        d1=0                 #Res1
        outmsg.append(d1)    
        d2=0
        outmsg.append(d2)    
        

#IC2:

        dacData= round(self.vcso2Spi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        dacData= round(self.vxmodSpi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        dacData= round(self.modbiasSpi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        dacData= round(self.vctbSpi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        dacData= round(self.vctb3Spi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        dacData= round(self.vcso4Spi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        dacData= round(self.vclampSpi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        dacData= round(self.vcso3Spi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

#IC3:
        dacData= round(self.FlsrBiasSli.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        dacData= round(self.RlsrBiasSli.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        dacData= round(self.LsrTempSli.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        dacData= round(self.tp_tiltSpi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        dacData= round(self.peak_adj_tpSpi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        



        dacData= round(self.vadjSpi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        dacData= round(self.ditherSpi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        

        dacData= round(self.ditherTuneSpi.value()*1024/409.6)
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=round(dacData%256)
        outmsg.append(d2)    #low byte
        


     #frequency:   
        dacData=int(self.freqEdit.text())
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=int(dacData%256)
        outmsg.append(d2)    #low byte
         
        bChkSum=0
        value1=bytearray(outmsg)
        for i in range(3,len(outmsg)):
            bChkSum+=value1[i]
        outmsg.append(bChkSum&0xff)  # CRC8
        print('\nsend to save:len=', len(outmsg),bChkSum&0xff,value1[len(outmsg)-2]  )
        outmsg.append(0x74) 
        outmsg.append(0x03)

        
        try:
            ser.write(outmsg)
            print('\n\nDAC Save.write OK',countSubResendTc )
        except:
            print("DAC Write failed!")
            return False

        value1=bytearray(outmsg)
        
        print('sys.getsizeof(outmsg)',sys.getsizeof(outmsg))
        self.saveBu.setText("Save...") 

   #save_to_file default:
        directory = r'C:\mini'              #directory
        _dir=os.path.join(directory)
        if not os.path.exists(_dir):
                os.makedirs(_dir)
        
        outData = str()                     #data
        for i in range(24):
            outData+=str(dacSpin[i].value())
            outData+=str(' ')

        s=int(self.freqEdit.text())
        if((s<2000)or(s>2700)):
            QMessageBox.about(self, "Save to file", "Frequency not correct.")
            return

        outData+=self.freqEdit.text()
        outData+=str(' ')
        
             
        f = open('C:\mini\miiniTx.txt'  ,'w')            #file
        f.write(outData)
        f.close()

  
    @pyqtSlot()
    def on_getBu_clicked(self):
        outmsg = bytearray()
        outmsg.append(SOT)
        outmsg.append(9) #packet len low byte
        outmsg.append(0) #packet len high byte

        outmsg.append(0) #SRC ADDR
        outmsg.append(0) #DEST ADDR
        

        outmsg.append(8) #MSG TYPE
        outmsg.append(8) #MSG ID low byte
        outmsg.append(0) #MSG ID high byte
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
            ser.write(outmsg)

        except:
            return False

        self.getBu.setText("Get...") 
        
        
        
    def  tcTableHan(self):
        self.e10.setText("{:1.3f}".format(tcTrans))
        self.timer.stop()

  #------------------------------------------connect-------------------------------------------------  
    @pyqtSlot()
    def on_connectBu_clicked(self):
        global ser

        if(self.connectBu.text()=='Connect'):

            ser = serial.Serial()
            ser.port = COMPORT_STR
            ser.baudrate = 38400
            ser.writeTimeout=5

            try:   
                ser.open()
            except:      
                QMessageBox.about(self, "Com", "Cannot open   "+ COMPORT_STR)
                return
            
            if(ser.isOpen()):
                self.connectBu.setText("Disconnect")

                self.timer = QtCore.QTimer()
                self.timer.timeout.connect(self.readUart)
                self.timer.start(300)

                    

        else:
            self.connectBu.setText('Connect')
            try:
                self.timer.stop()
                ser.close() 

            except:      
                QMessageBox.about(self, "Com", "Cannot close   "+ COMPORT_STR)
                
    #initial_req_ADC:

        self.on_continueBo_clicked()

            
    @pyqtSlot()
    def on_closeBu_clicked(self):

        global ser

        try:    
            ser.close()
        except:
            print('\nser.close fail')
                
        try:
            self.timer.stop()
        except:      
            print('\ntimer.stop fail')   
        self.destroy()

    @pyqtSlot()
    def on_FcBu_clicked(self):
        
        self.fcTable=fcTable()
        self.fcTable.show()
    
    @pyqtSlot()
    def on_alarmBu_clicked(self):
        self.alarm=alarm()
        self.alarm.show()
        print('\nalarmB stop') 

    @pyqtSlot()
    def on_boardInfBu_clicked(self):
        self.boardInfo=boardInfo()
        self.boardInfo.show()  

    @pyqtSlot(int)
    def on_comCom_currentIndexChanged(self, index):
        if(self.connectBu.text()=='Disconnect'):

            self.on_connectBu_clicked()
        global COMPORT_STR
        COMPORT_STR= 'COM'+str(ui.comCom.currentIndex()+1)

#================================lsr control ============================

    @pyqtSlot(int)
    def on_FlsrBiasSpi_valueChanged(self, p0):
        if(DAC_Set(16,p0)==True):

            self.rfRatio()

    @pyqtSlot(int)
    def on_RlsrBiasSpi_valueChanged(self, p0):
        if(DAC_Set(17,p0)==True):

            self.rfRatio()
        
    @pyqtSlot(int)
    def on_LsrTempSpi_valueChanged(self, p0):
        if(DAC_Set(18,p0)==True):
            print('DAC interface successfully')


    @pyqtSlot()
    def on_laserCalibrateBu_clicked(self):
        if(self.connectBu.text()=='Connect'):
            QMessageBox.about(self, "Laser Power calibrate", "Please connect Serial Port.")
            return
        if(self.laserContinueBo.isChecked()==False):
            QMessageBox.about(self, "Laser Power calibrate", "Please set Auto Refresh.")
            return
        try:
            mw=float(self.LSR_PDICalEdit.text())
            if((mw<0)or(mw>65)):
                QMessageBox.about(self, "Laser Power calibrate", "Laser Power calibrate not correct.")
                return
        except:
                QMessageBox.about(self, "Laser Power calibrate", "Laser Power calibrate not correct.")
                return

        
        ret=QMessageBox.question(self, "Laser Power calibrate", 'Do you want to write meter value to board?', QMessageBox.Yes, QMessageBox.No)

        lasPowCal=mw-pdiMwRaw

        uw10=round(lasPowCal*100)
        
        
   
        if (ret == QMessageBox.Yes):
            print('\n\nYes')
        else:
            print('\n\nNo')
            return

        result=struct.pack(">h",uw10)

        
        outmsg = bytearray()
        outmsg.append(SOT)
        outmsg.append(9) #packet len low byte
        outmsg.append(0) #packet len high byte

        outmsg.append(0) #SRC ADDR
        outmsg.append(0) #DEST ADDR

        outmsg.append(0x60) #MSG TYPE
        outmsg.append(3) #MSG ID low byte
        outmsg.append(0) #MSG ID high byte

        outmsg.append(result[0])    #high-byte
        outmsg.append(result[1])    #low-byte
        outmsg.append(0)

        bChkSum=0
        value1=bytearray(outmsg)
        for i in range(3,len(outmsg)):
            bChkSum+=value1[i]
        outmsg.append(bChkSum&0xff)  # CRC8

        outmsg.append(0x74) 
        outmsg.append(0x03)
        try:
            ser.write(outmsg)

        except:
            print("refresh failed!")


    @pyqtSlot()
    def on_LSR_PDICalEdit_returnPressed(self):
        global dacLasEdit
        dacLasEdit=1
        self.on_laserCalibrateBu_clicked()
#----------------------------------------ratio/scale----------------------        
      
    def rfRatio(self):
        f=float(self.FlsrBiasSli.value())
        r=float(self.RlsrBiasSli.value())
        if(r!=0):
            s=f/r
            self.e10.setText( "{:4.3f}".format(s))
        else:
            self.e10.setText('')

            

#======================================Predistorter===========================================           
  #raw1:  
    @pyqtSlot(int)
    def on_attnSpi_valueChanged(self, p0):
        if(DAC_Set(0,p0)==True):
            print('DAC interface successfully')
        
    @pyqtSlot(int)
    def on_mp_tilt_adjSpi_valueChanged(self, p0):
        if(DAC_Set(1,p0)==True):
            print('DAC interface successfully')
        
 
    @pyqtSlot(int)
    def on_peak_adj_mpSpi_valueChanged(self, p0):
        if(DAC_Set(2,p0)==True):
            print('DAC interface successfully')
    

    @pyqtSlot(int)
    def on_vampSpi_valueChanged(self, p0):
        if(DAC_Set(3,p0)==True):
            print('DAC interface successfully')
        
    @pyqtSlot(int)
    def on_tp_attnSpi_valueChanged(self, p0):
        if(DAC_Set(4,p0)==True):
            print('DAC interface successfully')

    @pyqtSlot(int)
    def on_vsbsSpi_valueChanged(self, p0):
        if(DAC_Set(5,p0)==True):
            print('DAC interface successfully')

    @pyqtSlot(int)
    def on_vxtSpi_valueChanged(self, p0):
        if(DAC_Set(6,p0)==True):
            print('DAC interface successfully')
#raw2:
    @pyqtSlot(int)
    def on_vcso2Spi_valueChanged(self, p0):
        if(DAC_Set(8,p0)==True):
            print('DAC interface successfully')

    @pyqtSlot(int)
    def on_vxmodSpi_valueChanged(self, p0):
        if(DAC_Set(9,p0)==True):
            print('DAC interface successfully')

    @pyqtSlot(int)
    def on_modbiasSpi_valueChanged(self, p0):
        if(DAC_Set(10,p0)==True):
            print('DAC interface successfully')

    @pyqtSlot(int)
    def on_vctbSpi_valueChanged(self, p0):
        if(DAC_Set(11,p0)==True):
            print('DAC interface successfully')

    @pyqtSlot(int)
    def on_vctb3Spi_valueChanged(self, p0):
        if(DAC_Set(12,p0)==True):
            print('DAC interface successfully')

    @pyqtSlot(int)
    def on_vcso4Spi_valueChanged(self, p0):
        if(DAC_Set(13,p0)==True):
            print('DAC interface successfully')
        
    @pyqtSlot(int)
    def on_vclampSpi_valueChanged(self, p0):
        if(DAC_Set(14,p0)==True):
            print('DAC interface successfully')

    @pyqtSlot(int)
    def on_vcso3Spi_valueChanged(self, p0):
        if(DAC_Set(15,p0)==True):
            print('DAC interface successfully')

    @pyqtSlot(int)
    def on_tp_tiltSpi_valueChanged(self, p0):
        if(DAC_Set(19,p0)==True):
            print('DAC interface successfully')
    
    @pyqtSlot(int)
    def on_peak_adj_tpSpi_valueChanged(self, p0):
        if(DAC_Set(20,p0)==True):
            print('DAC interface successfully')

    @pyqtSlot(int)
    def on_vadjSpi_valueChanged(self, p0):
        if(DAC_Set(21,p0)==True):
            print('DAC interface successfully')



    @pyqtSlot(int)
    def on_ditherSpi_valueChanged(self, p0):
        if(DAC_Set(22,p0)==True):
            print('DAC interface successfully')

    @pyqtSlot(int)
    def on_ditherTuneSpi_valueChanged(self, p0):
        if(DAC_Set(23,p0)==True):
            print('DAC interface successfully')

    @pyqtSlot()
    def on_freqBSet_clicked(self):
        getmsg=bytearray(59)
        f=int(self.freqEdit.text())
           
        if(freq_Set(f,getmsg)==True):
            value=bytearray(getmsg)
            if(value[5]==Ack):
                print('DAC interface successfully',value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9],value[10],value[11],value[12])
            else:
                print('DAC interface failed')


         


 #------------file-------------------------------------   
    @pyqtSlot()
    def on_getFileBu_clicked(self):
      #directory:
        directory = r'C:\mini'
        _dir=os.path.join(directory)
        if not os.path.exists(_dir):
                os.makedirs(_dir)

      #file:
 
        if  os.path.exists(directory)==True:
            file  = QFileDialog.getOpenFileName(self, 'Open file',directory, filter='All file (*.*)')

            fileName=file[0]

        else:
            QMessageBox.about(self, "Get from file", "Get from file failed.")
            return

        f = open(fileName  ,'r')
        inData=f.read()
        f.close()
        
      #check data:
        words = inData.split()

        for i in range(24):
            s=int(words[i])

            if((s<0)or(s>4096)):
                QMessageBox.about(self, "Get from file", "Get from file failed.")
                return
            
        s=int(words[24])
        if((s<2000)or(s>2700)):
            QMessageBox.about(self, "Get from file", "Frequency not correct.")
            return
        self.freqEdit.setText(str(s))
            
      #set_DAC:
        for i in range(24):
            dacSpin[i].setValue(int(words[i]))

            
            
        QMessageBox.about(self, "Get from file", "Get from file DACSuccessful.")

      #set_board_DAC:
        outmsg = bytearray()
        outmsg.append(SOT)
        outmsg.append(56) #packet len low byte
        outmsg.append(0) #packet len high byte
        outmsg.append(0) #SRC ADDR
        outmsg.append(0) #DEST ADDR
        outmsg.append(4) #MSG TYPE
        outmsg.append(8) #MSG ID low byte
        outmsg.append(0) #MSG ID high byte
 
        for i in range(24):                                     #value
            dacData= round(dacSpin[i].value()*1024/409.6)
            d1=int(dacData/256)
            outmsg.append(d1)    #high byte
            d2=round(dacData%256)
            outmsg.append(d2)    #low byte


   
        dacData=int(self.freqEdit.text())                        #frequency:
        d1=int(dacData/256)
        outmsg.append(d1)    #high byte
        d2=int(dacData%256)
        outmsg.append(d2)    #low byte
         
        bChkSum=0
        value1=bytearray(outmsg)
        for i in range(3,len(outmsg)):
            bChkSum+=value1[i]
        outmsg.append(bChkSum&0xff)  # CRC8
        outmsg.append(0x74) 
        outmsg.append(0x03)
 
        try:
            ser.write(outmsg)

        except:
            print("DAC Write failed!")

        
            
    @pyqtSlot()
    def on_saveFileBu_clicked(self):
      #directory:
        directory = r'C:\mini'
        _dir=os.path.join(directory)
        if not os.path.exists(_dir):
                os.makedirs(_dir)


      #file name:
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,
                "Mini TX",directory,
                "*.xls *.xlsx *.txt", '.xlsx' )
        if fileName:
            print(fileName,QtCore.QDateTime.currentDateTime())

      #read data:
        outData = str()
        for i in range(24):
            outData+=str(dacSpin[i].value())
            outData+=str(' ')

        s=int(self.freqEdit.text())
        if((s<2000)or(s>2700)):
            QMessageBox.about(self, "Save to file", "Frequency not correct.")
            return

        outData+=self.freqEdit.text()
        outData+=str(' ')
        
       #save:      
        f = open(fileName  ,'w')
        f.write(outData)
        f.close()
        QMessageBox.about(self, "Save to file", "Save to file DACSuccessful.")

        

#############################################################################################
    
    @pyqtSlot()
    def on_refreshBu_clicked(self):
        self.refresh()
        global stepRefresh
        stepRefresh=1
        
    @pyqtSlot()
    def on_laserRefreshBu_clicked(self):
        self.refresh()
        global stepRefresh
        stepRefresh=2
        
    @pyqtSlot()
    def on_continueBo_clicked(self):
        self.autoRefresh()
        global autoRefCheckDc
        if(self.continueBo.isChecked()==True):
            autoRefCheckDc=1
            self.continueBo_2.setChecked(True)
        else:
           autoRefCheckDc=0
           self.continueBo_2.setChecked(False)
        
    @pyqtSlot()
    def on_laserContinueBo_clicked(self):
        self.autoRefresh()
        global autoRefCheckLa
        if(self.laserContinueBo.isChecked()==True):
            autoRefCheckLa=1
        else:
            autoRefCheckLa=0

        
#----------auto refresh function---------------------
    
    def autoRefresh(self):
        outmsg = bytearray()
        outmsg.append(SOT)
        outmsg.append(9) #packet len low byte
        outmsg.append(0) #packet len high byte

        outmsg.append(0) #SRC ADDR
        outmsg.append(0) #DEST ADDR

        outmsg.append(0x44) #MSG TYPE
        outmsg.append(3) #MSG ID low byte
        outmsg.append(0) #MSG ID high byte

        if((self.continueBo.isChecked()==True)or(self.laserContinueBo.isChecked()==True) ):
            enaCheck=1
        else:
            enaCheck=0
        outmsg.append(enaCheck)
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
            ser.write(outmsg)
            print('\n\ncontinue.write OK', enaCheck)
        except:
            print("continue failed!")
#----------step refresh function---------------------
    def refresh(self):
        outmsg = bytearray()
        outmsg.append(SOT)
        outmsg.append(9) #packet len low byte
        outmsg.append(0) #packet len high byte

        outmsg.append(0) #SRC ADDR
        outmsg.append(0) #DEST ADDR

        outmsg.append(0x42) #MSG TYPE
        outmsg.append(3) #MSG ID low byte
        outmsg.append(0) #MSG ID high byte

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
            ser.write(outmsg)

        except:
            print("refresh failed!")
 #-----------DAC spinbox edit (Predistorter) ----------------------------------------   
    @pyqtSlot()
    def on_attnSpi_editingFinished(self):
        global spinRun
        spinRun=1
        if(DAC_Set(0,self.attnSpi.value())==True):
            print('DAC interface successfully')

    @pyqtSlot()
    def on_mp_tilt_adjSpi_editingFinished(self):
        global spinRun
        spinRun=1        
        if(DAC_Set(1,self.attnSpi.value())==True):
            print('DAC interface successfully')
            
    @pyqtSlot()
    def on_peak_adj_mpSpi_editingFinished(self):
        global spinRun
        spinRun=1
        if(DAC_Set(2,self.peak_adj_mpSpi.value())==True):
            print('DAC interface successfully')
    @pyqtSlot()
    def on_vampSpi_editingFinished(self):
        global spinRun
        spinRun=1
        if(DAC_Set(3,self.vampSpi.value())==True):
            print('DAC interface successfully')

    @pyqtSlot()
    def on_tp_attnSpi_editingFinished(self):
        global spinRun
        spinRun=1
        if(DAC_Set(4,self.tp_attnSpi.value())==True):
            print('DAC interface successfully')
    @pyqtSlot()
    def on_vsbsSpi_editingFinished(self):
        global spinRun
        spinRun=1
        if(DAC_Set(5,self.vsbsSpi.value())==True):
            print('DAC interface successfully')
    @pyqtSlot()
    def on_vxtSpi_editingFinished(self):
        global spinRun
        spinRun=1
        if(DAC_Set(6,self.vxtSpi.value())==True):
            print('DAC interface successfully')


            
    @pyqtSlot()
    def on_vcso2Spi_editingFinished(self):
        global spinRun
        spinRun=1
        if(DAC_Set(8,self.vcso2Spi.value())==True):
            print('DAC interface successfully')
    @pyqtSlot()
    def on_vxmodSpi_editingFinished(self):
        global spinRun
        spinRun=1
        if(DAC_Set(9,self.vxmodSpi.value())==True):
            print('DAC interface successfully')
    @pyqtSlot()
    def on_modbiasSpi_editingFinished(self):
        global spinRun
        spinRun=1
        if(DAC_Set(10,self.modbiasSpi.value())==True):
            print('DAC interface successfully')  
    @pyqtSlot()
    def on_vctbSpi_editingFinished(self):
        global spinRun
        spinRun=1
        if(DAC_Set(11,self.vctbSpi.value())==True):
            print('DAC interface successfully')


            
    @pyqtSlot()
    def on_vctb3Spi_editingFinished(self):
        global spinRun
        spinRun=1
        if(DAC_Set(12,self.vctb3Spi.value())==True):
            print('DAC interface successfully')
        
    @pyqtSlot()
    def on_vcso4Spi_editingFinished(self):
        global spinRun
        spinRun=1
        if(DAC_Set(13,self.vcso4Spi.value())==True):
            print('DAC interface successfully')
    @pyqtSlot()
    def on_vclampSpi_editingFinished(self):
        global spinRun
        spinRun=1
        if(DAC_Set(14,self.vclampSpi.value())==True):
            print('DAC interface successfully')
    @pyqtSlot()
    def on_vcso3Spi_editingFinished(self):
        global spinRun
        spinRun=1
        if(DAC_Set(15,self.vcso3Spi.value())==True):
            print('DAC interface successfully')

            
            
    @pyqtSlot()
    def on_FlsrBiasSpi_editingFinished(self):
        global spinRun
        spinRun=1
        global dacLasEdit
        dacLasEdit=1
        if(DAC_Set(16,self.FlsrBiasSpi.value())==True):
            print('DAC interface successfully')

    
 
    @pyqtSlot()
    def on_RlsrBiasSpi_editingFinished(self):
        global dacLasEdit
        dacLasEdit=1
        global spinRun
        spinRun=1
        if(DAC_Set(17,self.RlsrBiasSpi.value())==True):
            print('DAC interface successfully')
            
    @pyqtSlot()
    def on_LsrTempSpi_editingFinished(self):
        global dacLasEdit
        dacLasEdit=1
        global spinRun
        spinRun=1
        if(DAC_Set(18,self.LsrTempSpi.value())==True):
            print('DAC interface successfully')
            
    @pyqtSlot()
    def on_tp_tiltSpi_editingFinished(self):
        global spinRun
        spinRun=1
        if(DAC_Set(19,self.tp_tiltSpi.value())==True):
            print('DAC interface successfully')

    @pyqtSlot()
    def on_peak_adj_tpSpi_editingFinished(self):
        global spinRun
        spinRun=1
        if(DAC_Set(20,self.peak_adj_tpSpi.value())==True):
            print('DAC interface successfully')
    
    @pyqtSlot()
    def on_vadjSpi_editingFinished(self):
        global spinRun
        spinRun=1
        if(DAC_Set(21,self.vadjSpi.value())==True):
            print('DAC interface successfully')

    @pyqtSlot()
    def on_ditherSpi_editingFinished(self):
        global spinRun
        spinRun=1
        if(DAC_Set(22,self.ditherSpi.value())==True):
            print('DAC interface successfully')

    @pyqtSlot()
    def on_ditherTuneSpi_editingFinished(self):
        global spinRun
        spinRun=1
        if(DAC_Set(23,self.ditherTuneSpi.value())==True):
            print('DAC interface successfully')
#-----------Gain Control-----------------------------------
    @pyqtSlot()
    def on_attnSpi_2_editingFinished(self):
        global spinRun
        spinRun=1
        global dacLasEdit
        dacLasEdit=1

        
    @pyqtSlot()
    def on_getFromBoardGainBu_clicked(self):
        s=0
        self.sendGain(s,0x72)
        self.getFromBoardGainBu.setText('Get from Board...')
        
    @pyqtSlot()
    def on_saveToBoardGainBu_clicked(self):
        try:
            s=float(self.rfAttnDb.text())
        except:
            QMessageBox.about(self, "Gain Control", "dB value over.")
            return
        if((s>-50)and(s<50)):
           self.sendGain(s,0x70)
        else:
           QMessageBox.about(self, "Gain Control", "dB value over.")
           return

    @pyqtSlot()
    def on_gainUpBu_clicked(self):
        try:
            s=float(self.rfAttnDb.text())
        except:
            QMessageBox.about(self, "Gain Control", "dB value over.")
            return
        if((s>-50)and(s<49.5)):
           s+=0.5
           s*=100
           s=round(s)
           s/=100
           self.sendGain(s,0x74)
        else:
           QMessageBox.about(self, "Gain Control", "dB value over.")
           return
        self.rfAttnDb.setText(str(s))
        self.gainUpBu.setText('Up...')
        
    @pyqtSlot()
    def on_gainDownBu_clicked(self):
        try:
            s=float(self.rfAttnDb.text())
        except:
            QMessageBox.about(self, "Gain Control", "dB value over.")
            return
        if((s>-45.5)and(s<50)):
           s-=0.5
           s*=100
           s=round(s)
           s/=100

           self.sendGain(s,0x74)
        else:
           QMessageBox.about(self, "Gain Control", "dB value over.")
           return
        self.rfAttnDb.setText(str(s))
        self.gainDownBu.setText('Down...')
            
    @pyqtSlot()
    def on_rfAttnDb_returnPressed(self):
        global spinRun
        spinRun=1
        global dacLasEdit
        dacLasEdit=1

        try:
            s=float(self.rfAttnDb.text())
            s*=100
            s=round(s)
            s/=100
        except:
            QMessageBox.about(self, "Gain Control", "dB value over.")
            return
            
        if((s<-50)or(s>50)):
           QMessageBox.about(self, "Gain Control", "dB value over.")
           return
        else:
            self.sendGain(s,0x74)

    def sendGain(self,s,msType):  #save,get,control
        outmsg = bytearray()
        outmsg.append(SOT)
        outmsg.append(0) 
        outmsg.append(9) 

        outmsg.append(0) 
        outmsg.append(0) 
        

        outmsg.append(msType) #MSG TYPE
        outmsg.append(8) #MSG ID low byte
        outmsg.append(0) #MSG ID high byte

        if(self.agcBo.isChecked()==True):
            outmsg.append(1)    #AGC

        else:
            outmsg.append(0)

            
        result=struct.pack('h',int(s*100))     
        outmsg.append(result[1])    #dB high-byte
        outmsg.append(result[0])    #dB low-byte


        bChkSum=0
        value1=bytearray(outmsg)
        for i in range(3,len(outmsg)):
            bChkSum+=value1[i]
        outmsg.append(bChkSum&0xff)  # CRC8
        
        outmsg.append(0x74) 
        outmsg.append(0x03)
        try:
            ser.write(outmsg)

        except:
            print("DAC Write failed!")
 
           
 #---------frequency----------------------------------  
    @pyqtSlot()
    def on_freqEdit_editingFinished(self):
        global dacLasEdit
        dacLasEdit=1
        self.on_freqBSet_clicked()

 #---------DAC_set_slider----------------------------------           
    @pyqtSlot()
    def on_lasTrigSli_clicked(self):
        global  sliderRun
        sliderRun=1;
        print('\n\n7:channel=', sliderRun)
        
    @pyqtSlot()
    def on_preTrigSli_clicked(self):
        global  sliderRun
        sliderRun=1;

        x = QtGui.QCursor()
        y = x.pos()



#---------DAC_set_spin----------------------------------   


def DAC_Set( channel: bytes, value: int)->bool:
    
  #check_record:
    global dacReco
    global spinRun
    global sliderRun

    xCursor=abs(QtGui.QCursor().pos().x()-ui.x())
    yCursor=abs(QtGui.QCursor().pos().y()-ui.y())
    xd=abs(xCursor-dacSpin[channel].x())
    yd=abs(yCursor-dacSpin[channel].y())

    if(((abs(dacReco[channel]-value)>1)or
       (abs(dacReco[channel]-value)==0) or
       ((xd+yd)>185))  and
       (sliderRun==0)and
       ((spinRun==0)or((xd+yd)>170))):      #return withoiut enter

        dacReco[channel]=value
        sliderRun=0
        spinRun=0 
        return False


    sliderRun=0
    spinRun=0   
    dacReco[channel]=value

  #set_value:  
    fTemp= round(value*1024/409.6)

    nTemp= int(fTemp)
    result=struct.pack('h',nTemp)

    outmsg = bytearray()
    outmsg.append(SOT)
    outmsg.append(9) #packet len low byte
    outmsg.append(0) #packet len high byte

    outmsg.append(0) #SRC ADDR
    outmsg.append(0) #DEST ADDR

    outmsg.append(2) #MSG TYPE
    outmsg.append(3) #MSG ID low byte
    outmsg.append(0) #MSG ID high byte

    outmsg.append(channel)
    outmsg.append(result[0])#high-byte
    outmsg.append(result[1])#low-byte

    bChkSum=0
    value1=bytearray(outmsg)
    for i in range(3,len(outmsg)):
        bChkSum+=value1[i]
    outmsg.append(bChkSum&0xff)  # CRC8

    outmsg.append(0x74) 
    outmsg.append(0x03)
    try:
        ser.write(outmsg)

    except:

        return False


    return True



#-----------set_frequency----------------------
def freq_Set(value_freq: int, response: bytearray(1))->bool:
    global freqSetRun
    freqSetRun =1

    value_freq+=0
    result=struct.pack(">I",value_freq) # 4 bytes

    outmsg = bytearray()
    outmsg.append(SOT)

    outmsg.append(14) #packet len low byte
    outmsg.append(0) #packet len high byte
    outmsg.append(0) #SRC ADDR
    outmsg.append(0) #DEST ADDR
    outmsg.append(0x0a) #MSG TYPE
    outmsg.append(3) #MSG ID low byte
    outmsg.append(0) #MSG ID high byte

    outmsg.append(result[2])
    outmsg.append(result[3])

    bChkSum=0
    value1=bytearray(outmsg)
    for i in range(3,len(outmsg)):
        bChkSum+=value1[i]
    outmsg.append(bChkSum&0xff)  # CRC8
    
    outmsg.append(0x74) 
    outmsg.append(0x03)

    try:
        ser.write(outmsg)

    except:
        print("DAC Write failed!")

    import time 

    time.sleep(0.1)  # Delay for 1  seconds
            
 
    try:
        ser.write(outmsg)

    except:

        freqSetRun=0
        return False
    

    freqSetRun=0

    

#//////////////////////////////////////////////////////////////////////////    
if __name__ == "__main__":          
    app = QApplication(sys.argv)
    ui =miniTx()
    ui.resize(920, 400)

    ui.setWindowTitle('MiniTx GUI --- SIDxxxx --- V1017')



    ui.show()
    ui.rfRatio()
    ui.comCom.setCurrentIndex(4)
    sys.exit(app.exec_()) 
