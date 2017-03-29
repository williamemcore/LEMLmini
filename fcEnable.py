# -*- coding: utf-8 -*-

from PyQt5 import  QtCore, QtGui
from PyQt5.QtCore import  *
from PyQt5.QtWidgets import  *
import sys
from PyQt5.QtGui import *

from Ui_fcEnable import Ui_Dialog
#-------------------------------------------------------------------------------------------------------------------
# Global Variables
SOT = 0x7E

inmsg= bytearray(61)
vRef=3.3
import os
fcM=os.getcwd()+'\\fcM'    
fcSe=os.getcwd()+'\\fcSe'  
fcE=os.getcwd()+'\\fcE'   
#-----------------------------------------------------

class fcEnable(QDialog, Ui_Dialog):

    def __init__(self, parent=None):

        super(fcEnable, self).__init__(parent)
        self.setupUi(self)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.readUart)
        self.timer.start(500)

        self.on_getFromBoardBu_clicked()
  #----------------------------------------------------
    def readUart(self):
        global  inmsg
        if  os.path.exists(fcSe)==True:  #received from UART
            with open(fcSe, 'rb') as f:
                f.readinto(inmsg)
            f.close()

            fcSSize=os.path.getsize(fcSe)


            value1=bytearray(inmsg)
            try:
                os.remove(fcSe)

            except:
                print('\n\nremove error 11')
 

            if(sys.getsizeof(value1)<6):return

            if (value1[0]==0x7e):

                if((value1[5]==0x29)or(value1[5]==0x2b)):    #fc enable to/from board

                       
                    if(value1[5]==0x29):#save fc enable to board ACK

                        QMessageBox.question(self, 'Save FC Enable Status', "Save FC Enable Successful.", QMessageBox.Ok)
                        return


                    if(value1[5]==0x2b):#get fc enable from board
                    #raw1:
                        if(value1[8]==0):
                            self.Attn.setChecked(False)
                        else:
                            self.Attn.setChecked(True)
                            
                        if(value1[9]==0):
                            self.MpTiltAdj.setChecked(False)
                        else:
                            self.MpTiltAdj.setChecked(True)

                        if(value1[10]==0):
                            self.PeakAdjMp.setChecked(False)
                        else:
                            self.PeakAdjMp.setChecked(True)

                        if(value1[11]==0):
                            self.Vamp.setChecked(False)
                        else:
                            self.Vamp.setChecked(True)

                        if(value1[12]==0):
                            self.TpAttn.setChecked(False)
                        else:
                            self.TpAttn.setChecked(True)
                            
                        if(value1[13]==0):
                            self.VSbs.setChecked(False)
                        else:
                            self.VSbs.setChecked(True)

                        if(value1[14]==0):
                            self.Vxt.setChecked(False)
                        else:
                            self.Vxt.setChecked(True)

                        if(value1[15]==0):
                            self.Res1.setChecked(False)
                        else:
                            self.Res1.setChecked(True)


                     #raw2:
                        if(value1[16]==0):
                            self.Vcso2.setChecked(False)
                        else:
                            self.Vcso2.setChecked(True)
                            
                        if(value1[17]==0):
                            self.Vxmod.setChecked(False)
                        else:
                            self.Vxmod.setChecked(True)

                        if(value1[18]==0):
                            self.ModBias.setChecked(False)
                        else:
                            self.ModBias.setChecked(True)

                        if(value1[19]==0):
                            self.Vctb.setChecked(False)
                        else:
                            self.Vctb.setChecked(True)

                        if(value1[20]==0):
                            self.Vctb3.setChecked(False)
                        else:
                            self.Vctb3.setChecked(True)
                            
                        if(value1[21]==0):
                            self.Vcso4.setChecked(False)
                        else:
                            self.Vcso4.setChecked(True)

                        if(value1[22]==0):
                            self.Vclamp.setChecked(False)
                        else:
                            self.Vclamp.setChecked(True)

                        if(value1[23]==0):
                            self.Vcso3.setChecked(False)
                        else:
                            self.Vcso3.setChecked(True)                           

                     #raw3:
                        if(value1[16]==0):
                            self.FlsrBias.setChecked(False)
                        else:
                            self.FlsrBias.setChecked(True)
                            
                        if(value1[17]==0):
                            self.RlsrBias.setChecked(False)
                        else:
                            self.RlsrBias.setChecked(True)

                        if(value1[18]==0):
                            self.LsrTemp.setChecked(False)
                        else:
                            self.LsrTemp.setChecked(True)

                        if(value1[19]==0):
                            self.TpTiltAdj.setChecked(False)
                        else:
                            self.TpTiltAdj.setChecked(True)

                        if(value1[20]==0):
                            self.PeakAdjTp.setChecked(False)
                        else:
                            self.PeakAdjTp.setChecked(True)
                            
                        if(value1[21]==0):
                            self.Vadj.setChecked(False)
                        else:
                            self.Vadj.setChecked(True)

                        if(value1[22]==0):
                            self.DitherCorr.setChecked(False)
                        else:
                            self.DitherCorr.setChecked(True)

                        if(value1[23]==0):
                            self.Res2.setChecked(False)
                        else:
                            self.Res2.setChecked(True)
                            
                    
                        f = open(fcE  ,'wb')    
                        f.write(inmsg)
                        f.close() 
                        
                        QMessageBox.question(self, 'Get FC Enable Status', "Get FC Enable Successful.", QMessageBox.Ok)
                        return
        else:   
            #update enable:
            if  os.path.exists(fcE)==True: 
                with open(fcE, 'rb') as f:
                    f.readinto(inmsg)
                f.close()
                value1=bytearray(inmsg)
                
            #raw1:
                if(value1[8]==0):
                    self.Attn.setChecked(False)
                else:
                    self.Attn.setChecked(True)
                    
                if(value1[9]==0):
                    self.MpTiltAdj.setChecked(False)
                else:
                    self.MpTiltAdj.setChecked(True)

                if(value1[10]==0):
                    self.PeakAdjMp.setChecked(False)
                else:
                    self.PeakAdjMp.setChecked(True)

                if(value1[11]==0):
                    self.Vamp.setChecked(False)
                else:
                    self.Vamp.setChecked(True)

                if(value1[12]==0):
                    self.TpAttn.setChecked(False)
                else:
                    self.TpAttn.setChecked(True)
                    
                if(value1[13]==0):
                    self.VSbs.setChecked(False)
                else:
                    self.VSbs.setChecked(True)

                if(value1[14]==0):
                    self.Vxt.setChecked(False)
                else:
                    self.Vxt.setChecked(True)

                if(value1[15]==0):
                    self.Res1.setChecked(False)
                else:
                    self.Res1.setChecked(True)


             #raw2:
                if(value1[16]==0):
                    self.Vcso2.setChecked(False)
                else:
                    self.Vcso2.setChecked(True)
                    
                if(value1[17]==0):
                    self.Vxmod.setChecked(False)
                else:
                    self.Vxmod.setChecked(True)

                if(value1[18]==0):
                    self.ModBias.setChecked(False)
                else:
                    self.ModBias.setChecked(True)

                if(value1[19]==0):
                    self.Vctb.setChecked(False)
                else:
                    self.Vctb.setChecked(True)

                if(value1[20]==0):
                    self.Vctb3.setChecked(False)
                else:
                    self.Vctb3.setChecked(True)
                    
                if(value1[21]==0):
                    self.Vcso4.setChecked(False)
                else:
                    self.Vcso4.setChecked(True)

                if(value1[22]==0):
                    self.Vclamp.setChecked(False)
                else:
                    self.Vclamp.setChecked(True)

                if(value1[23]==0):
                    self.Vcso3.setChecked(False)
                else:
                    self.Vcso3.setChecked(True)                           

             #raw3:
                if(value1[24]==0):
                    self.FlsrBias.setChecked(False)
                else:
                    self.FlsrBias.setChecked(True)
                    
                if(value1[25]==0):
                    self.RlsrBias.setChecked(False)
                else:
                    self.RlsrBias.setChecked(True)

                if(value1[26]==0):
                    self.LsrTemp.setChecked(False)
                else:
                    self.LsrTemp.setChecked(True)

                if(value1[27]==0):
                    self.TpTiltAdj.setChecked(False)
                else:
                    self.TpTiltAdj.setChecked(True)

                if(value1[28]==0):
                    self.PeakAdjTp.setChecked(False)
                else:
                    self.PeakAdjTp.setChecked(True)
                    
                if(value1[29]==0):
                    self.Vadj.setChecked(False)
                else:
                    self.Vadj.setChecked(True)

                if(value1[30]==0):
                    self.DitherCorr.setChecked(False)
                else:
                    self.DitherCorr.setChecked(True)

                if(value1[31]==0):
                    self.Res2.setChecked(False)
                else:
                    self.Res2.setChecked(True)
 #====================================Save/Get=======================================================                       

    @pyqtSlot()
    def on_saveToBoardBu_clicked(self):

        outmsg = bytearray()
        outmsg.append(SOT)
        outmsg.append(0) #packet len high byte
        outmsg.append(30) #packet len low byte
        outmsg.append(0) #SRC ADDR
        

        outmsg.append(0) #DEST ADDR
        

        outmsg.append(0x28) #MSG TYPE

        outmsg.append(8) #MSG ID low byte
        

        outmsg.append(0) #MSG ID high byte
        

#value:
    #raw1:
        if(self.Attn.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.MpTiltAdj.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.PeakAdjMp.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.Vamp.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.TpAttn.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.VSbs.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.Vxt.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.Res1.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

    #raw2:
        if(self.Vcso2.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.Vxmod.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.ModBias.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.Vctb.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.Vctb3.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.Vcso4.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.Vclamp.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.Vcso3.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

    #raw3:

        if(self.FlsrBias.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.RlsrBias.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.LsrTemp.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.TpTiltAdj.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.PeakAdjTp.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.Vadj.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.DitherCorr.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        

        if(self.Res2.isChecked()==True):s=1
        else:s=0
        outmsg.append(s)
        
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
            
            f = open(fcE  ,'wb')     #TC enable <-> FC table
            f.write(outmsg)
            print('file po=',f.tell())
            f.close()    
        except:
            print('\n\n save to board error5' )
    @pyqtSlot()
    def on_getFromBoardBu_clicked(self):

        outmsg = bytearray()
        outmsg.append(SOT)

        outmsg.append(9) #packet len low byte

        outmsg.append(0) #packet len high byte
        

        outmsg.append(0) #SRC ADDR
        

        outmsg.append(0) #DEST ADDR
        

        outmsg.append(0x2a) #MSG TYPE
        

        outmsg.append(8) #MSG ID low byte
        

        outmsg.append(0) #MSG ID high byte
        
    #value:
       
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
            f = open(fcM  ,'wb') 
            f.write(outmsg)


            f.close()
    
        except:
            print('\n\n save to board error6' )

 #----------------------------all enable/disable----------------------------------  
    @pyqtSlot()
    def on_disableAllBu_clicked(self):
        self.Attn.setChecked(False)
        self.MpTiltAdj.setChecked(False)
        self.PeakAdjMp.setChecked(False)
        self.Vamp.setChecked(False)
        self.TpAttn.setChecked(False)
        self.VSbs.setChecked(False)
        self.Vxt.setChecked(False)
        self.Res1.setChecked(False)

        self.Vcso2.setChecked(False)
        self.Vxmod.setChecked(False)
        self.ModBias.setChecked(False)
        self.Vctb.setChecked(False)
        self.Vctb3.setChecked(False)
        self.Vcso4.setChecked(False)
        self.Vclamp.setChecked(False)
        self.Vcso3.setChecked(False)

        self.FlsrBias.setChecked(False)
        self.RlsrBias.setChecked(False)
        self.LsrTemp.setChecked(False)
        self.TpTiltAdj.setChecked(False)
        self.PeakAdjTp.setChecked(False)
        self.Vadj.setChecked(False)
        self.DitherCorr.setChecked(False)
        self.Res2.setChecked(False)

        enable = bytearray(35)
        for i in range(35):
           enable[i]=0
        f = open(fcE  ,'wb')     #TC enable <-> TC table
        f.write(enable)
        f.close()
    
    @pyqtSlot()
    def on_enableAllBu_clicked(self):
        self.Attn.setChecked(True)
        self.MpTiltAdj.setChecked(True)
        self.PeakAdjMp.setChecked(True)
        self.Vamp.setChecked(True)
        self.TpAttn.setChecked(True)
        self.VSbs.setChecked(True)
        self.Vxt.setChecked(True)
        self.Res1.setChecked(True)

        self.Vcso2.setChecked(True)
        self.Vxmod.setChecked(True)
        self.ModBias.setChecked(True)
        self.Vctb.setChecked(True)
        self.Vctb3.setChecked(True)
        self.Vcso4.setChecked(True)
        self.Vclamp.setChecked(True)
        self.Vcso3.setChecked(True)

        self.FlsrBias.setChecked(True)
        self.RlsrBias.setChecked(True)
        self.LsrTemp.setChecked(True)
        self.TpTiltAdj.setChecked(True)
        self.PeakAdjTp.setChecked(True)
        self.Vadj.setChecked(True)
        self.DitherCorr.setChecked(True)
        self.Res2.setChecked(True)
        
        enable = bytearray(35)
        for i in range(35):
           enable[i]=1
        f = open(fcE  ,'wb')     #FC enable <-> FC table
        f.write(enable)
        f.close()
 #--------------------------------single enable/disable--------------------------------------   

#raw1:   
    @pyqtSlot()
    def on_Attn_clicked(self):
        enaCheck=bytearray(1)
        if(self.Attn.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(8,0)
        f.write(enaCheck)
        f.close() 


    @pyqtSlot()
    def on_MpTiltAdj_clicked(self):
        enaCheck=bytearray(1)
        if(self.MpTiltAdj.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(9,0)
        f.write(enaCheck)
        f.close()

    @pyqtSlot()
    def on_PeakAdjMp_clicked(self):
        enaCheck=bytearray(1)
        if(self.PeakAdjMp.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(10,0)
        f.write(enaCheck)
        f.close()     
    
    @pyqtSlot()
    def on_Vamp_clicked(self):
        enaCheck=bytearray(1)
        if(self.Vamp.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(11,0)
        f.write(enaCheck)
        f.close() 
    
    @pyqtSlot()
    def on_TpAttn_clicked(self):
        enaCheck=bytearray(1)
        if(self.TpAttn.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(12,0)
        f.write(enaCheck)
        f.close()

    @pyqtSlot()
    def on_VSbs_clicked(self):
        enaCheck=bytearray(1)
        if(self.VSbs.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(13,0)
        f.write(enaCheck)
        f.close()

    @pyqtSlot()
    def on_Vxt_clicked(self):
        enaCheck=bytearray(1)
        if(self.Vxt.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(14,0)
        f.write(enaCheck)
        f.close()
    
    @pyqtSlot()
    def on_Res1_clicked(self):
        enaCheck=bytearray(1)
        if(self.Res1.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(15,0)
        f.write(enaCheck)
        f.close() 
    
  #raw2:
    @pyqtSlot()
    def on_Vcso2_clicked(self):
        enaCheck=bytearray(1)
        if(self.Vcso2.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(16,0)
        f.write(enaCheck)
        f.close() 

    @pyqtSlot()
    def on_Vxmod_clicked(self):
        enaCheck=bytearray(1)
        if(self.Vxmod.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(17,0)
        f.write(enaCheck)
        f.close() 

    @pyqtSlot()
    def on_ModBias_clicked(self):
        enaCheck=bytearray(1)
        if(self.ModBias.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(18,0)
        f.write(enaCheck)
        f.close() 

    @pyqtSlot()
    def on_Vctb_clicked(self):
        enaCheck=bytearray(1)
        if(self.Vctb.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(19,0)
        f.write(enaCheck)
        f.close() 

    @pyqtSlot()
    def on_Vctb3_clicked(self):
        enaCheck=bytearray(1)
        if(self.Vctb3.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(20,0)
        f.write(enaCheck)
        f.close()
        
    @pyqtSlot()
    def on_Vcso4_clicked(self):
        enaCheck=bytearray(1)
        if(self.Vcso4.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(21,0)
        f.write(enaCheck)
        f.close() 

    @pyqtSlot()
    def on_Vclamp_clicked(self):
        enaCheck=bytearray(1)
        if(self.Vclamp.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(22,0)
        f.write(enaCheck)
        f.close()

    @pyqtSlot()
    def on_Vcso3_clicked(self):
        enaCheck=bytearray(1)
        if(self.Vcso3.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(23,0)
        f.write(enaCheck)
        f.close() 

#raw3:
    @pyqtSlot()
    def on_FlsrBias_clicked(self):
        enaCheck=bytearray(1)
        if(self.FlsrBias.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(24,0)
        f.write(enaCheck)
        f.close() 
        
    @pyqtSlot()
    def on_RlsrBias_clicked(self):
        enaCheck=bytearray(1)
        if(self.RlsrBias.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(25,0)
        f.write(enaCheck)
        f.close()

    @pyqtSlot()
    def on_LsrTemp_clicked(self):
        enaCheck=bytearray(1)
        if(self.LsrTemp.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(26,0)
        f.write(enaCheck)
        f.close()

    @pyqtSlot()
    def on_TpTiltAdj_clicked(self):
        enaCheck=bytearray(1)
        if(self.TpTiltAdj.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(27,0)
        f.write(enaCheck)
        f.close()

    @pyqtSlot()
    def on_PeakAdjTp_clicked(self):
        enaCheck=bytearray(1)
        if(self.PeakAdjTp.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(28,0)
        f.write(enaCheck)
        f.close() 

    @pyqtSlot()
    def on_Vadj_clicked(self):
        enaCheck=bytearray(1)
        if(self.Vadj.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(29,0)
        f.write(enaCheck)
        f.close() 
        
    @pyqtSlot()
    def on_DitherCorr_clicked(self):
        enaCheck=bytearray(1)
        if(self.DitherCorr.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(30,0)
        f.write(enaCheck)
        f.close() 
     
    @pyqtSlot()
    def on_Res2_clicked(self):
        enaCheck=bytearray(1)
        if(self.Res2.isChecked()==True):enaCheck[0]=1
        else:enaCheck[0]=0
        if  os.path.exists(fcE)==False:     #FC enable <-> FC table
            f = open(fcE  ,'wb')     
        else:
            f = open(fcE  ,'rb+')   
        f.seek(31,0)
        f.write(enaCheck)
        f.close() 
    
 
#=================================================================
