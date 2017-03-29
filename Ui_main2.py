

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_miniTx(object):
    def setupUi(self, miniTx):
        miniTx.setObjectName("miniTx")
        miniTx.resize(931, 1895)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Green-Fish.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        miniTx.setWindowIcon(icon)
        miniTx.setSizeGripEnabled(False)
        self.dcMonitorBu = QtWidgets.QPushButton(miniTx)
        self.dcMonitorBu.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.dcMonitorBu.setObjectName("dcMonitorBu")
        self.PredistorterBu = QtWidgets.QPushButton(miniTx)
        self.PredistorterBu.setGeometry(QtCore.QRect(70, 0, 75, 23))
        self.PredistorterBu.setObjectName("PredistorterBu")
        self.LsrControlsBu = QtWidgets.QPushButton(miniTx)
        self.LsrControlsBu.setGeometry(QtCore.QRect(140, 0, 75, 23))
        self.LsrControlsBu.setObjectName("LsrControlsBu")
        self.TCBu = QtWidgets.QPushButton(miniTx)
        self.TCBu.setGeometry(QtCore.QRect(280, 0, 75, 23))
        self.TCBu.setObjectName("TCBu")
        self.FcBu = QtWidgets.QPushButton(miniTx)
        self.FcBu.setGeometry(QtCore.QRect(350, 0, 75, 23))
        self.FcBu.setObjectName("FcBu")
        self.alarmBu = QtWidgets.QPushButton(miniTx)
        self.alarmBu.setGeometry(QtCore.QRect(420, 0, 75, 23))
        self.alarmBu.setObjectName("alarmBu")
        self.dcMonitorWi = QtWidgets.QGroupBox(miniTx)
        self.dcMonitorWi.setGeometry(QtCore.QRect(10, 30, 771, 361))
        self.dcMonitorWi.setInputMethodHints(QtCore.Qt.ImhNone)
        self.dcMonitorWi.setObjectName("dcMonitorWi")
        self.label_5 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 91, 21))
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 111, 21))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_8.setGeometry(QtCore.QRect(20, 180, 111, 21))
        self.label_8.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 101, 21))
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_7.setGeometry(QtCore.QRect(20, 150, 71, 21))
        self.label_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_9.setGeometry(QtCore.QRect(20, 270, 91, 21))
        self.label_9.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setObjectName("label_9")
        self.label_6 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_6.setGeometry(QtCore.QRect(20, 210, 101, 21))
        self.label_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 91, 21))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_10.setGeometry(QtCore.QRect(20, 240, 101, 21))
        self.label_10.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_13.setGeometry(QtCore.QRect(390, 120, 31, 21))
        self.label_13.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_13.setObjectName("label_13")
        self.label_22 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_22.setGeometry(QtCore.QRect(20, 300, 91, 21))
        self.label_22.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_22.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_22.setObjectName("label_22")
        self.label_61 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_61.setGeometry(QtCore.QRect(470, 10, 81, 21))
        self.label_61.setStyleSheet("color: rgb(0, 136, 65);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_62.setGeometry(QtCore.QRect(130, 10, 71, 21))
        self.label_62.setStyleSheet("color: rgb(0, 136, 65);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_63.setGeometry(QtCore.QRect(290, 10, 71, 21))
        self.label_63.setStyleSheet("color: rgb(0, 136, 65);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_63.setObjectName("label_63")
        self.label_15 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_15.setGeometry(QtCore.QRect(390, 30, 31, 21))
        self.label_15.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_15.setObjectName("label_15")
        self.label_24 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_24.setGeometry(QtCore.QRect(390, 90, 31, 21))
        self.label_24.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_24.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_25.setGeometry(QtCore.QRect(390, 210, 31, 21))
        self.label_25.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_25.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_26.setGeometry(QtCore.QRect(390, 240, 31, 21))
        self.label_26.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_26.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_27.setGeometry(QtCore.QRect(390, 60, 31, 21))
        self.label_27.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_27.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_27.setObjectName("label_27")
        self.label_23 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_23.setGeometry(QtCore.QRect(390, 150, 31, 21))
        self.label_23.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_23.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_23.setObjectName("label_23")
        self.label_79 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_79.setGeometry(QtCore.QRect(20, 330, 91, 21))
        self.label_79.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_79.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_79.setObjectName("label_79")
        self.continueBo = QtWidgets.QCheckBox(self.dcMonitorWi)
        self.continueBo.setGeometry(QtCore.QRect(680, 280, 81, 17))
        self.continueBo.setObjectName("continueBo")
        self.refreshBu = QtWidgets.QPushButton(self.dcMonitorWi)
        self.refreshBu.setGeometry(QtCore.QRect(680, 330, 75, 23))
        self.refreshBu.setObjectName("refreshBu")
        self.ModuleTemp_da = QtWidgets.QLabel(self.dcMonitorWi)
        self.ModuleTemp_da.setGeometry(QtCore.QRect(110, 30, 101, 21))
        self.ModuleTemp_da.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ModuleTemp_da.setFrameShape(QtWidgets.QFrame.Box)
        self.ModuleTemp_da.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ModuleTemp_da.setText("")
        self.ModuleTemp_da.setAlignment(QtCore.Qt.AlignCenter)
        self.ModuleTemp_da.setObjectName("ModuleTemp_da")
        self.TEC_I_MON_da = QtWidgets.QLabel(self.dcMonitorWi)
        self.TEC_I_MON_da.setGeometry(QtCore.QRect(110, 60, 101, 21))
        self.TEC_I_MON_da.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.TEC_I_MON_da.setFrameShape(QtWidgets.QFrame.Box)
        self.TEC_I_MON_da.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TEC_I_MON_da.setText("")
        self.TEC_I_MON_da.setAlignment(QtCore.Qt.AlignCenter)
        self.TEC_I_MON_da.setObjectName("TEC_I_MON_da")
        self.Input_RF_MON_da = QtWidgets.QLabel(self.dcMonitorWi)
        self.Input_RF_MON_da.setGeometry(QtCore.QRect(110, 120, 101, 21))
        self.Input_RF_MON_da.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.Input_RF_MON_da.setFrameShape(QtWidgets.QFrame.Box)
        self.Input_RF_MON_da.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Input_RF_MON_da.setText("")
        self.Input_RF_MON_da.setAlignment(QtCore.Qt.AlignCenter)
        self.Input_RF_MON_da.setObjectName("Input_RF_MON_da")
        self.Laser_Temp_da = QtWidgets.QLabel(self.dcMonitorWi)
        self.Laser_Temp_da.setGeometry(QtCore.QRect(110, 90, 101, 21))
        self.Laser_Temp_da.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.Laser_Temp_da.setFrameShape(QtWidgets.QFrame.Box)
        self.Laser_Temp_da.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Laser_Temp_da.setText("")
        self.Laser_Temp_da.setAlignment(QtCore.Qt.AlignCenter)
        self.Laser_Temp_da.setObjectName("Laser_Temp_da")
        self.SBS_MON_da = QtWidgets.QLabel(self.dcMonitorWi)
        self.SBS_MON_da.setGeometry(QtCore.QRect(110, 180, 101, 21))
        self.SBS_MON_da.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.SBS_MON_da.setFrameShape(QtWidgets.QFrame.Box)
        self.SBS_MON_da.setFrameShadow(QtWidgets.QFrame.Plain)
        self.SBS_MON_da.setText("")
        self.SBS_MON_da.setAlignment(QtCore.Qt.AlignCenter)
        self.SBS_MON_da.setObjectName("SBS_MON_da")
        self.LAS_RF_da = QtWidgets.QLabel(self.dcMonitorWi)
        self.LAS_RF_da.setGeometry(QtCore.QRect(110, 150, 101, 21))
        self.LAS_RF_da.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.LAS_RF_da.setFrameShape(QtWidgets.QFrame.Box)
        self.LAS_RF_da.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LAS_RF_da.setText("")
        self.LAS_RF_da.setAlignment(QtCore.Qt.AlignCenter)
        self.LAS_RF_da.setObjectName("LAS_RF_da")
        self.RLSR_BIAS_da = QtWidgets.QLabel(self.dcMonitorWi)
        self.RLSR_BIAS_da.setGeometry(QtCore.QRect(110, 240, 101, 21))
        self.RLSR_BIAS_da.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.RLSR_BIAS_da.setFrameShape(QtWidgets.QFrame.Box)
        self.RLSR_BIAS_da.setFrameShadow(QtWidgets.QFrame.Plain)
        self.RLSR_BIAS_da.setText("")
        self.RLSR_BIAS_da.setAlignment(QtCore.Qt.AlignCenter)
        self.RLSR_BIAS_da.setObjectName("RLSR_BIAS_da")
        self.FLSR_BIAS_da = QtWidgets.QLabel(self.dcMonitorWi)
        self.FLSR_BIAS_da.setGeometry(QtCore.QRect(110, 210, 101, 21))
        self.FLSR_BIAS_da.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.FLSR_BIAS_da.setFrameShape(QtWidgets.QFrame.Box)
        self.FLSR_BIAS_da.setFrameShadow(QtWidgets.QFrame.Plain)
        self.FLSR_BIAS_da.setText("")
        self.FLSR_BIAS_da.setAlignment(QtCore.Qt.AlignCenter)
        self.FLSR_BIAS_da.setObjectName("FLSR_BIAS_da")
        self.LSR_PDI_da = QtWidgets.QLabel(self.dcMonitorWi)
        self.LSR_PDI_da.setGeometry(QtCore.QRect(110, 270, 101, 21))
        self.LSR_PDI_da.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.LSR_PDI_da.setFrameShape(QtWidgets.QFrame.Box)
        self.LSR_PDI_da.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LSR_PDI_da.setText("")
        self.LSR_PDI_da.setAlignment(QtCore.Qt.AlignCenter)
        self.LSR_PDI_da.setObjectName("LSR_PDI_da")
        self.v24_da = QtWidgets.QLabel(self.dcMonitorWi)
        self.v24_da.setGeometry(QtCore.QRect(110, 330, 101, 21))
        self.v24_da.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.v24_da.setFrameShape(QtWidgets.QFrame.Box)
        self.v24_da.setFrameShadow(QtWidgets.QFrame.Plain)
        self.v24_da.setText("")
        self.v24_da.setAlignment(QtCore.Qt.AlignCenter)
        self.v24_da.setObjectName("v24_da")
        self.v5_da = QtWidgets.QLabel(self.dcMonitorWi)
        self.v5_da.setGeometry(QtCore.QRect(110, 300, 101, 21))
        self.v5_da.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.v5_da.setFrameShape(QtWidgets.QFrame.Box)
        self.v5_da.setFrameShadow(QtWidgets.QFrame.Plain)
        self.v5_da.setText("")
        self.v5_da.setAlignment(QtCore.Qt.AlignCenter)
        self.v5_da.setObjectName("v5_da")
        self.TEC_I_MON_da_2 = QtWidgets.QLabel(self.dcMonitorWi)
        self.TEC_I_MON_da_2.setGeometry(QtCore.QRect(280, 60, 101, 21))
        self.TEC_I_MON_da_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.TEC_I_MON_da_2.setFrameShape(QtWidgets.QFrame.Box)
        self.TEC_I_MON_da_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TEC_I_MON_da_2.setText("")
        self.TEC_I_MON_da_2.setAlignment(QtCore.Qt.AlignCenter)
        self.TEC_I_MON_da_2.setObjectName("TEC_I_MON_da_2")
        self.ModuleTemp_da_2 = QtWidgets.QLabel(self.dcMonitorWi)
        self.ModuleTemp_da_2.setGeometry(QtCore.QRect(280, 30, 101, 21))
        self.ModuleTemp_da_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ModuleTemp_da_2.setFrameShape(QtWidgets.QFrame.Box)
        self.ModuleTemp_da_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ModuleTemp_da_2.setText("")
        self.ModuleTemp_da_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ModuleTemp_da_2.setObjectName("ModuleTemp_da_2")
        self.Laser_Temp_da_2 = QtWidgets.QLabel(self.dcMonitorWi)
        self.Laser_Temp_da_2.setGeometry(QtCore.QRect(280, 90, 101, 21))
        self.Laser_Temp_da_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.Laser_Temp_da_2.setFrameShape(QtWidgets.QFrame.Box)
        self.Laser_Temp_da_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Laser_Temp_da_2.setText("")
        self.Laser_Temp_da_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Laser_Temp_da_2.setObjectName("Laser_Temp_da_2")
        self.FLSR_BIAS_da_2 = QtWidgets.QLabel(self.dcMonitorWi)
        self.FLSR_BIAS_da_2.setGeometry(QtCore.QRect(280, 210, 101, 21))
        self.FLSR_BIAS_da_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.FLSR_BIAS_da_2.setFrameShape(QtWidgets.QFrame.Box)
        self.FLSR_BIAS_da_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.FLSR_BIAS_da_2.setText("")
        self.FLSR_BIAS_da_2.setAlignment(QtCore.Qt.AlignCenter)
        self.FLSR_BIAS_da_2.setObjectName("FLSR_BIAS_da_2")
        self.RLSR_BIAS_da_2 = QtWidgets.QLabel(self.dcMonitorWi)
        self.RLSR_BIAS_da_2.setGeometry(QtCore.QRect(280, 240, 101, 21))
        self.RLSR_BIAS_da_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.RLSR_BIAS_da_2.setFrameShape(QtWidgets.QFrame.Box)
        self.RLSR_BIAS_da_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.RLSR_BIAS_da_2.setText("")
        self.RLSR_BIAS_da_2.setAlignment(QtCore.Qt.AlignCenter)
        self.RLSR_BIAS_da_2.setObjectName("RLSR_BIAS_da_2")
        self.ModuleTemp_al = QtWidgets.QLabel(self.dcMonitorWi)
        self.ModuleTemp_al.setGeometry(QtCore.QRect(490, 30, 40, 21))
        self.ModuleTemp_al.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.ModuleTemp_al.setFrameShape(QtWidgets.QFrame.Box)
        self.ModuleTemp_al.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ModuleTemp_al.setText("")
        self.ModuleTemp_al.setAlignment(QtCore.Qt.AlignCenter)
        self.ModuleTemp_al.setObjectName("ModuleTemp_al")
        self.TEC_I_MON_al = QtWidgets.QLabel(self.dcMonitorWi)
        self.TEC_I_MON_al.setGeometry(QtCore.QRect(490, 60, 40, 21))
        self.TEC_I_MON_al.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.TEC_I_MON_al.setFrameShape(QtWidgets.QFrame.Box)
        self.TEC_I_MON_al.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TEC_I_MON_al.setText("")
        self.TEC_I_MON_al.setAlignment(QtCore.Qt.AlignCenter)
        self.TEC_I_MON_al.setObjectName("TEC_I_MON_al")
        self.v24_al = QtWidgets.QLabel(self.dcMonitorWi)
        self.v24_al.setGeometry(QtCore.QRect(490, 330, 40, 21))
        self.v24_al.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.v24_al.setFrameShape(QtWidgets.QFrame.Box)
        self.v24_al.setFrameShadow(QtWidgets.QFrame.Plain)
        self.v24_al.setText("")
        self.v24_al.setAlignment(QtCore.Qt.AlignCenter)
        self.v24_al.setObjectName("v24_al")
        self.Input_RF_MON_al = QtWidgets.QLabel(self.dcMonitorWi)
        self.Input_RF_MON_al.setGeometry(QtCore.QRect(490, 120, 40, 21))
        self.Input_RF_MON_al.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.Input_RF_MON_al.setFrameShape(QtWidgets.QFrame.Box)
        self.Input_RF_MON_al.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Input_RF_MON_al.setText("")
        self.Input_RF_MON_al.setAlignment(QtCore.Qt.AlignCenter)
        self.Input_RF_MON_al.setObjectName("Input_RF_MON_al")
        self.FLSR_BIAS_al = QtWidgets.QLabel(self.dcMonitorWi)
        self.FLSR_BIAS_al.setGeometry(QtCore.QRect(490, 210, 40, 21))
        self.FLSR_BIAS_al.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.FLSR_BIAS_al.setFrameShape(QtWidgets.QFrame.Box)
        self.FLSR_BIAS_al.setFrameShadow(QtWidgets.QFrame.Plain)
        self.FLSR_BIAS_al.setText("")
        self.FLSR_BIAS_al.setAlignment(QtCore.Qt.AlignCenter)
        self.FLSR_BIAS_al.setObjectName("FLSR_BIAS_al")
        self.SBS_MON_al = QtWidgets.QLabel(self.dcMonitorWi)
        self.SBS_MON_al.setGeometry(QtCore.QRect(490, 180, 40, 21))
        self.SBS_MON_al.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.SBS_MON_al.setFrameShape(QtWidgets.QFrame.Box)
        self.SBS_MON_al.setFrameShadow(QtWidgets.QFrame.Plain)
        self.SBS_MON_al.setText("")
        self.SBS_MON_al.setAlignment(QtCore.Qt.AlignCenter)
        self.SBS_MON_al.setObjectName("SBS_MON_al")
        self.LAS_RF_al = QtWidgets.QLabel(self.dcMonitorWi)
        self.LAS_RF_al.setGeometry(QtCore.QRect(490, 150, 40, 21))
        self.LAS_RF_al.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.LAS_RF_al.setFrameShape(QtWidgets.QFrame.Box)
        self.LAS_RF_al.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LAS_RF_al.setText("")
        self.LAS_RF_al.setAlignment(QtCore.Qt.AlignCenter)
        self.LAS_RF_al.setObjectName("LAS_RF_al")
        self.RLSR_BIAS_al = QtWidgets.QLabel(self.dcMonitorWi)
        self.RLSR_BIAS_al.setGeometry(QtCore.QRect(490, 240, 40, 21))
        self.RLSR_BIAS_al.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.RLSR_BIAS_al.setFrameShape(QtWidgets.QFrame.Box)
        self.RLSR_BIAS_al.setFrameShadow(QtWidgets.QFrame.Plain)
        self.RLSR_BIAS_al.setText("")
        self.RLSR_BIAS_al.setAlignment(QtCore.Qt.AlignCenter)
        self.RLSR_BIAS_al.setObjectName("RLSR_BIAS_al")
        self.LSR_PDI_al = QtWidgets.QLabel(self.dcMonitorWi)
        self.LSR_PDI_al.setGeometry(QtCore.QRect(490, 270, 40, 21))
        self.LSR_PDI_al.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.LSR_PDI_al.setFrameShape(QtWidgets.QFrame.Box)
        self.LSR_PDI_al.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LSR_PDI_al.setText("")
        self.LSR_PDI_al.setAlignment(QtCore.Qt.AlignCenter)
        self.LSR_PDI_al.setObjectName("LSR_PDI_al")
        self.Laser_Temp_al = QtWidgets.QLabel(self.dcMonitorWi)
        self.Laser_Temp_al.setGeometry(QtCore.QRect(490, 90, 40, 21))
        self.Laser_Temp_al.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.Laser_Temp_al.setFrameShape(QtWidgets.QFrame.Box)
        self.Laser_Temp_al.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Laser_Temp_al.setText("")
        self.Laser_Temp_al.setAlignment(QtCore.Qt.AlignCenter)
        self.Laser_Temp_al.setObjectName("Laser_Temp_al")
        self.v5_al = QtWidgets.QLabel(self.dcMonitorWi)
        self.v5_al.setGeometry(QtCore.QRect(490, 300, 40, 21))
        self.v5_al.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.v5_al.setFrameShape(QtWidgets.QFrame.Box)
        self.v5_al.setFrameShadow(QtWidgets.QFrame.Plain)
        self.v5_al.setText("")
        self.v5_al.setAlignment(QtCore.Qt.AlignCenter)
        self.v5_al.setObjectName("v5_al")
        self.LSR_PDI_da_2 = QtWidgets.QLabel(self.dcMonitorWi)
        self.LSR_PDI_da_2.setGeometry(QtCore.QRect(280, 270, 101, 21))
        self.LSR_PDI_da_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.LSR_PDI_da_2.setFrameShape(QtWidgets.QFrame.Box)
        self.LSR_PDI_da_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LSR_PDI_da_2.setText("")
        self.LSR_PDI_da_2.setAlignment(QtCore.Qt.AlignCenter)
        self.LSR_PDI_da_2.setObjectName("LSR_PDI_da_2")
        self.label_81 = QtWidgets.QLabel(self.dcMonitorWi)
        self.label_81.setGeometry(QtCore.QRect(390, 270, 31, 21))
        self.label_81.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_81.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_81.setObjectName("label_81")
        self.Input_RF_MON_dbm = QtWidgets.QLineEdit(self.dcMonitorWi)
        self.Input_RF_MON_dbm.setEnabled(True)
        self.Input_RF_MON_dbm.setGeometry(QtCore.QRect(280, 120, 101, 21))
        self.Input_RF_MON_dbm.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";border-width: 1px;")
        self.Input_RF_MON_dbm.setAlignment(QtCore.Qt.AlignCenter)
        self.Input_RF_MON_dbm.setObjectName("Input_RF_MON_dbm")
        self.LAS_RF_dbm = QtWidgets.QLineEdit(self.dcMonitorWi)
        self.LAS_RF_dbm.setEnabled(True)
        self.LAS_RF_dbm.setGeometry(QtCore.QRect(280, 150, 101, 21))
        self.LAS_RF_dbm.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";border-width: 2px;")
        self.LAS_RF_dbm.setAlignment(QtCore.Qt.AlignCenter)
        self.LAS_RF_dbm.setObjectName("LAS_RF_dbm")
        self.lsrControlsWi = QtWidgets.QGroupBox(miniTx)
        self.lsrControlsWi.setEnabled(True)
        self.lsrControlsWi.setGeometry(QtCore.QRect(10, 420, 771, 441))
        self.lsrControlsWi.setObjectName("lsrControlsWi")
        self.label_31 = QtWidgets.QLabel(self.lsrControlsWi)
        self.label_31.setGeometry(QtCore.QRect(200, 40, 81, 21))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.lsrControlsWi)
        self.label_32.setGeometry(QtCore.QRect(350, 40, 71, 21))
        self.label_32.setObjectName("label_32")
        self.label_16 = QtWidgets.QLabel(self.lsrControlsWi)
        self.label_16.setGeometry(QtCore.QRect(60, 270, 81, 21))
        self.label_16.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(self.lsrControlsWi)
        self.label_18.setGeometry(QtCore.QRect(510, 140, 71, 21))
        self.label_18.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_18.setObjectName("label_18")
        self.label_17 = QtWidgets.QLabel(self.lsrControlsWi)
        self.label_17.setGeometry(QtCore.QRect(510, 70, 61, 21))
        self.label_17.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_17.setObjectName("label_17")
        self.label_12 = QtWidgets.QLabel(self.lsrControlsWi)
        self.label_12.setGeometry(QtCore.QRect(350, 270, 81, 21))
        self.label_12.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_12.setObjectName("label_12")
        self.label_19 = QtWidgets.QLabel(self.lsrControlsWi)
        self.label_19.setGeometry(QtCore.QRect(200, 270, 81, 21))
        self.label_19.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_19.setObjectName("label_19")
        self.label_14 = QtWidgets.QLabel(self.lsrControlsWi)
        self.label_14.setGeometry(QtCore.QRect(350, 330, 101, 21))
        self.label_14.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_14.setObjectName("label_14")
        self.FlsrBiasSpi = QtWidgets.QSpinBox(self.lsrControlsWi)
        self.FlsrBiasSpi.setGeometry(QtCore.QRect(50, 190, 91, 31))
        self.FlsrBiasSpi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.FlsrBiasSpi.setAlignment(QtCore.Qt.AlignCenter)
        self.FlsrBiasSpi.setMaximum(3000)
        self.FlsrBiasSpi.setProperty("value", 750)
        self.FlsrBiasSpi.setObjectName("FlsrBiasSpi")
        self.label_20 = QtWidgets.QLabel(self.lsrControlsWi)
        self.label_20.setGeometry(QtCore.QRect(60, 40, 81, 21))
        self.label_20.setObjectName("label_20")
        self.freqEdit = QtWidgets.QLineEdit(self.lsrControlsWi)
        self.freqEdit.setGeometry(QtCore.QRect(670, 110, 91, 31))
        self.freqEdit.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.freqEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.freqEdit.setObjectName("freqEdit")
        self.FlsrBiasSli = QtWidgets.QSlider(self.lsrControlsWi)
        self.FlsrBiasSli.setGeometry(QtCore.QRect(70, 60, 40, 126))
        self.FlsrBiasSli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.FlsrBiasSli.setMaximum(3000)
        self.FlsrBiasSli.setSingleStep(10)
        self.FlsrBiasSli.setPageStep(100)
        self.FlsrBiasSli.setProperty("value", 750)
        self.FlsrBiasSli.setOrientation(QtCore.Qt.Vertical)
        self.FlsrBiasSli.setObjectName("FlsrBiasSli")
        self.freqBSet = QtWidgets.QPushButton(self.lsrControlsWi)
        self.freqBSet.setGeometry(QtCore.QRect(670, 42, 81, 31))
        self.freqBSet.setObjectName("freqBSet")
        self.LsrTempSli = QtWidgets.QSlider(self.lsrControlsWi)
        self.LsrTempSli.setGeometry(QtCore.QRect(360, 60, 40, 126))
        self.LsrTempSli.setStyleSheet(" QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.LsrTempSli.setMaximum(4092)
        self.LsrTempSli.setSingleStep(10)
        self.LsrTempSli.setPageStep(100)
        self.LsrTempSli.setProperty("value", 750)
        self.LsrTempSli.setOrientation(QtCore.Qt.Vertical)
        self.LsrTempSli.setObjectName("LsrTempSli")
        self.LsrTempSpi = QtWidgets.QSpinBox(self.lsrControlsWi)
        self.LsrTempSpi.setGeometry(QtCore.QRect(340, 190, 91, 31))
        self.LsrTempSpi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.LsrTempSpi.setAlignment(QtCore.Qt.AlignCenter)
        self.LsrTempSpi.setMaximum(4092)
        self.LsrTempSpi.setProperty("value", 750)
        self.LsrTempSpi.setObjectName("LsrTempSpi")
        self.RlsrBiasSli = QtWidgets.QSlider(self.lsrControlsWi)
        self.RlsrBiasSli.setGeometry(QtCore.QRect(210, 60, 40, 126))
        self.RlsrBiasSli.setStyleSheet("  QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.RlsrBiasSli.setMaximum(1500)
        self.RlsrBiasSli.setSingleStep(10)
        self.RlsrBiasSli.setPageStep(100)
        self.RlsrBiasSli.setProperty("value", 750)
        self.RlsrBiasSli.setOrientation(QtCore.Qt.Vertical)
        self.RlsrBiasSli.setObjectName("RlsrBiasSli")
        self.RlsrBiasSpi = QtWidgets.QSpinBox(self.lsrControlsWi)
        self.RlsrBiasSpi.setGeometry(QtCore.QRect(190, 190, 91, 31))
        self.RlsrBiasSpi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.RlsrBiasSpi.setAlignment(QtCore.Qt.AlignCenter)
        self.RlsrBiasSpi.setMaximum(1500)
        self.RlsrBiasSpi.setProperty("value", 750)
        self.RlsrBiasSpi.setObjectName("RlsrBiasSpi")
        self.label_11 = QtWidgets.QLabel(self.lsrControlsWi)
        self.label_11.setGeometry(QtCore.QRect(350, 400, 91, 21))
        self.label_11.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_11.setObjectName("label_11")
        self.label_33 = QtWidgets.QLabel(self.lsrControlsWi)
        self.label_33.setGeometry(QtCore.QRect(140, 400, 71, 21))
        self.label_33.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label_33.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_33.setObjectName("label_33")
        self.e10_2 = QtWidgets.QLineEdit(self.lsrControlsWi)
        self.e10_2.setGeometry(QtCore.QRect(180, 470, 101, 31))
        self.e10_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 0);")
        self.e10_2.setAlignment(QtCore.Qt.AlignCenter)
        self.e10_2.setObjectName("e10_2")
        self.label_21 = QtWidgets.QLabel(self.lsrControlsWi)
        self.label_21.setGeometry(QtCore.QRect(60, 330, 81, 21))
        self.label_21.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label_21.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_21.setObjectName("label_21")
        self.label_37 = QtWidgets.QLabel(self.lsrControlsWi)
        self.label_37.setGeometry(QtCore.QRect(200, 330, 81, 21))
        self.label_37.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label_37.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.lsrControlsWi)
        self.label_38.setGeometry(QtCore.QRect(700, 140, 41, 21))
        self.label_38.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label_38.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_38.setObjectName("label_38")
        self.label_76 = QtWidgets.QLabel(self.lsrControlsWi)
        self.label_76.setGeometry(QtCore.QRect(240, 70, 31, 16))
        self.label_76.setObjectName("label_76")
        self.label_77 = QtWidgets.QLabel(self.lsrControlsWi)
        self.label_77.setGeometry(QtCore.QRect(100, 70, 31, 16))
        self.label_77.setObjectName("label_77")
        self.label_78 = QtWidgets.QLabel(self.lsrControlsWi)
        self.label_78.setGeometry(QtCore.QRect(390, 70, 31, 16))
        self.label_78.setObjectName("label_78")
        self.laserContinueBo = QtWidgets.QCheckBox(self.lsrControlsWi)
        self.laserContinueBo.setGeometry(QtCore.QRect(670, 370, 81, 17))
        self.laserContinueBo.setObjectName("laserContinueBo")
        self.laserRefreshBu = QtWidgets.QPushButton(self.lsrControlsWi)
        self.laserRefreshBu.setGeometry(QtCore.QRect(670, 410, 75, 23))
        self.laserRefreshBu.setObjectName("laserRefreshBu")
        self.e7 = QtWidgets.QLabel(self.lsrControlsWi)
        self.e7.setGeometry(QtCore.QRect(50, 240, 91, 31))
        self.e7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);font: 14pt \"MS Shell Dlg 2\";")
        self.e7.setFrameShape(QtWidgets.QFrame.Box)
        self.e7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.e7.setText("")
        self.e7.setAlignment(QtCore.Qt.AlignCenter)
        self.e7.setObjectName("e7")
        self.e2 = QtWidgets.QLabel(self.lsrControlsWi)
        self.e2.setGeometry(QtCore.QRect(340, 240, 91, 31))
        self.e2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);font: 14pt \"MS Shell Dlg 2\";")
        self.e2.setFrameShape(QtWidgets.QFrame.Box)
        self.e2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.e2.setText("")
        self.e2.setAlignment(QtCore.Qt.AlignCenter)
        self.e2.setObjectName("e2")
        self.e8 = QtWidgets.QLabel(self.lsrControlsWi)
        self.e8.setGeometry(QtCore.QRect(190, 240, 91, 31))
        self.e8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);font: 14pt \"MS Shell Dlg 2\";")
        self.e8.setFrameShape(QtWidgets.QFrame.Box)
        self.e8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.e8.setText("")
        self.e8.setAlignment(QtCore.Qt.AlignCenter)
        self.e8.setObjectName("e8")
        self.e5 = QtWidgets.QLabel(self.lsrControlsWi)
        self.e5.setGeometry(QtCore.QRect(500, 40, 91, 31))
        self.e5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);font: 14pt \"MS Shell Dlg 2\";")
        self.e5.setFrameShape(QtWidgets.QFrame.Box)
        self.e5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.e5.setText("")
        self.e5.setAlignment(QtCore.Qt.AlignCenter)
        self.e5.setObjectName("e5")
        self.e3 = QtWidgets.QLabel(self.lsrControlsWi)
        self.e3.setGeometry(QtCore.QRect(340, 300, 91, 31))
        self.e3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);font: 14pt \"MS Shell Dlg 2\";")
        self.e3.setFrameShape(QtWidgets.QFrame.Box)
        self.e3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.e3.setText("")
        self.e3.setAlignment(QtCore.Qt.AlignCenter)
        self.e3.setObjectName("e3")
        self.e1 = QtWidgets.QLabel(self.lsrControlsWi)
        self.e1.setGeometry(QtCore.QRect(340, 370, 91, 31))
        self.e1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);font: 14pt \"MS Shell Dlg 2\";")
        self.e1.setFrameShape(QtWidgets.QFrame.Box)
        self.e1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.e1.setText("")
        self.e1.setAlignment(QtCore.Qt.AlignCenter)
        self.e1.setObjectName("e1")
        self.flasrScale = QtWidgets.QLabel(self.lsrControlsWi)
        self.flasrScale.setGeometry(QtCore.QRect(50, 300, 91, 31))
        self.flasrScale.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);font: 14pt \"MS Shell Dlg 2\";")
        self.flasrScale.setFrameShape(QtWidgets.QFrame.Box)
        self.flasrScale.setFrameShadow(QtWidgets.QFrame.Plain)
        self.flasrScale.setText("")
        self.flasrScale.setAlignment(QtCore.Qt.AlignCenter)
        self.flasrScale.setObjectName("flasrScale")
        self.rlasrScale = QtWidgets.QLabel(self.lsrControlsWi)
        self.rlasrScale.setGeometry(QtCore.QRect(190, 300, 91, 31))
        self.rlasrScale.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);font: 14pt \"MS Shell Dlg 2\";")
        self.rlasrScale.setFrameShape(QtWidgets.QFrame.Box)
        self.rlasrScale.setFrameShadow(QtWidgets.QFrame.Plain)
        self.rlasrScale.setText("")
        self.rlasrScale.setAlignment(QtCore.Qt.AlignCenter)
        self.rlasrScale.setObjectName("rlasrScale")
        self.e10 = QtWidgets.QLabel(self.lsrControlsWi)
        self.e10.setGeometry(QtCore.QRect(130, 370, 91, 31))
        self.e10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 127);\n"
"border-color: rgb(0, 0, 0);font: 14pt \"MS Shell Dlg 2\";")
        self.e10.setFrameShape(QtWidgets.QFrame.Box)
        self.e10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.e10.setText("")
        self.e10.setAlignment(QtCore.Qt.AlignCenter)
        self.e10.setObjectName("e10")
        self.lasTrigSli = QtWidgets.QToolButton(self.lsrControlsWi)
        self.lasTrigSli.setGeometry(QtCore.QRect(150, 10, 25, 19))
        self.lasTrigSli.setText("")
        self.lasTrigSli.setObjectName("lasTrigSli")
        self.laserCalibrateBu = QtWidgets.QPushButton(self.lsrControlsWi)
        self.laserCalibrateBu.setGeometry(QtCore.QRect(510, 410, 75, 23))
        self.laserCalibrateBu.setObjectName("laserCalibrateBu")
        self.label_80 = QtWidgets.QLabel(self.lsrControlsWi)
        self.label_80.setGeometry(QtCore.QRect(490, 380, 131, 21))
        self.label_80.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label_80.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_80.setObjectName("label_80")
        self.LSR_PDICalEdit = QtWidgets.QLineEdit(self.lsrControlsWi)
        self.LSR_PDICalEdit.setGeometry(QtCore.QRect(500, 350, 91, 31))
        self.LSR_PDICalEdit.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.LSR_PDICalEdit.setText("")
        self.LSR_PDICalEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.LSR_PDICalEdit.setObjectName("LSR_PDICalEdit")
        self.LSR_PDIEdit = QtWidgets.QLabel(self.lsrControlsWi)
        self.LSR_PDIEdit.setGeometry(QtCore.QRect(500, 110, 91, 31))
        self.LSR_PDIEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);font: 14pt \"MS Shell Dlg 2\";")
        self.LSR_PDIEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.LSR_PDIEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LSR_PDIEdit.setText("")
        self.LSR_PDIEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.LSR_PDIEdit.setObjectName("LSR_PDIEdit")
        self.LSR_Alarm = QtWidgets.QLabel(self.lsrControlsWi)
        self.LSR_Alarm.setGeometry(QtCore.QRect(670, 200, 31, 21))
        self.LSR_Alarm.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.LSR_Alarm.setFrameShape(QtWidgets.QFrame.Box)
        self.LSR_Alarm.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LSR_Alarm.setText("")
        self.LSR_Alarm.setAlignment(QtCore.Qt.AlignCenter)
        self.LSR_Alarm.setObjectName("LSR_Alarm")
        self.label_82 = QtWidgets.QLabel(self.lsrControlsWi)
        self.label_82.setGeometry(QtCore.QRect(710, 200, 41, 21))
        self.label_82.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label_82.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_82.setObjectName("label_82")
        self.type1Bo = QtWidgets.QRadioButton(self.lsrControlsWi)
        self.type1Bo.setGeometry(QtCore.QRect(670, 260, 101, 21))
        self.type1Bo.setObjectName("type1Bo")
        self.type2Bo = QtWidgets.QRadioButton(self.lsrControlsWi)
        self.type2Bo.setGeometry(QtCore.QRect(670, 290, 101, 21))
        self.type2Bo.setObjectName("type2Bo")
        self.groupBox = QtWidgets.QGroupBox(miniTx)
        self.groupBox.setGeometry(QtCore.QRect(800, 140, 111, 91))
        self.groupBox.setObjectName("groupBox")
        self.getBu = QtWidgets.QPushButton(self.groupBox)
        self.getBu.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.getBu.setObjectName("getBu")
        self.saveBu = QtWidgets.QPushButton(self.groupBox)
        self.saveBu.setGeometry(QtCore.QRect(20, 30, 75, 23))
        self.saveBu.setObjectName("saveBu")
        self.groupBox_2 = QtWidgets.QGroupBox(miniTx)
        self.groupBox_2.setGeometry(QtCore.QRect(800, 30, 111, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.connectBu = QtWidgets.QPushButton(self.groupBox_2)
        self.connectBu.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.connectBu.setObjectName("connectBu")
        self.comCom = QtWidgets.QComboBox(self.groupBox_2)
        self.comCom.setGeometry(QtCore.QRect(20, 30, 75, 22))
        self.comCom.setObjectName("comCom")
        self.comCom.addItem("")
        self.comCom.addItem("")
        self.comCom.addItem("")
        self.comCom.addItem("")
        self.comCom.addItem("")
        self.comCom.addItem("")
        self.comCom.addItem("")
        self.comCom.addItem("")
        self.comCom.addItem("")
        self.comCom.addItem("")
        self.closeBu = QtWidgets.QPushButton(miniTx)
        self.closeBu.setGeometry(QtCore.QRect(820, 360, 75, 23))
        self.closeBu.setObjectName("closeBu")
        self.PredistorterWi = QtWidgets.QGroupBox(miniTx)
        self.PredistorterWi.setEnabled(True)
        self.PredistorterWi.setGeometry(QtCore.QRect(10, 870, 771, 601))
        self.PredistorterWi.setStyleSheet(" QScrollBar:vertical {\n"
"              border: 0px solid black;\n"
"              background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,\n"
"stop: 0 #323232, stop: 1 #323232);\n"
"              margin: 20px 0 20px 0;\n"
"              max-width: 10px;\n"
"          }\n"
"QScrollBar::handle:vertical {\n"
"              background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,\n"
"stop: 0 #323232, stop: 0.8 #CECECE, stop: 1 #323232);\n"
"              min-height: 20px;\n"
"          }\n"
"QScrollBar::add-line:vertical {\n"
"              border: 0px solid black;\n"
"              background-color: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0,\n"
"stop: 0 #323232, stop: 0.8 #CECECE, stop: 1 #323232);\n"
"              height: 19px;\n"
"              subcontrol-position: bottom;\n"
"              subcontrol-origin: margin;\n"
"          }\n"
"QScrollBar::sub-line:vertical {\n"
"              border: 0px solid black;\n"
"              background-color: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0,\n"
"stop: 0 #323232, stop: 0.8 #CECECE, stop: 1 #323232);\n"
"              height: 19px;\n"
"              subcontrol-position: top;\n"
"              subcontrol-origin: margin;\n"
"          }\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"              border: 0px solid black;\n"
"              width: 5px;\n"
"              height: 5px;\n"
"              background-color: white;\n"
"          }\n"
"\n"
"QScrollBar::add-page:vertical {\n"
"               background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"                    stop: 0 #66e, stop: 1 #bbf);\n"
"                background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"                    stop: 0 #bbf, stop: 1 #55f);\n"
"                height: 100px;\n"
"          }\n"
"QScrollBar::sub-page:vertical {\n"
"              background-color: white;\n"
"          }")
        self.PredistorterWi.setObjectName("PredistorterWi")
        self.attnSpi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.attnSpi.setGeometry(QtCore.QRect(10, 170, 71, 31))
        self.attnSpi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.attnSpi.setAlignment(QtCore.Qt.AlignCenter)
        self.attnSpi.setMaximum(4092)
        self.attnSpi.setProperty("value", 750)
        self.attnSpi.setObjectName("attnSpi")
        self.label_28 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_28.setGeometry(QtCore.QRect(20, 20, 61, 21))
        self.label_28.setObjectName("label_28")
        self.peak_adj_mpSli = QtWidgets.QSlider(self.PredistorterWi)
        self.peak_adj_mpSli.setGeometry(QtCore.QRect(200, 40, 40, 126))
        self.peak_adj_mpSli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.peak_adj_mpSli.setMaximum(4092)
        self.peak_adj_mpSli.setSingleStep(10)
        self.peak_adj_mpSli.setPageStep(100)
        self.peak_adj_mpSli.setProperty("value", 750)
        self.peak_adj_mpSli.setOrientation(QtCore.Qt.Vertical)
        self.peak_adj_mpSli.setObjectName("peak_adj_mpSli")
        self.peak_adj_mpSpi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.peak_adj_mpSpi.setGeometry(QtCore.QRect(190, 170, 71, 31))
        self.peak_adj_mpSpi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.peak_adj_mpSpi.setAlignment(QtCore.Qt.AlignCenter)
        self.peak_adj_mpSpi.setMaximum(4092)
        self.peak_adj_mpSpi.setProperty("value", 750)
        self.peak_adj_mpSpi.setObjectName("peak_adj_mpSpi")
        self.mp_tilt_adjSli = QtWidgets.QSlider(self.PredistorterWi)
        self.mp_tilt_adjSli.setGeometry(QtCore.QRect(110, 40, 40, 126))
        self.mp_tilt_adjSli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.mp_tilt_adjSli.setMaximum(4092)
        self.mp_tilt_adjSli.setSingleStep(10)
        self.mp_tilt_adjSli.setPageStep(100)
        self.mp_tilt_adjSli.setProperty("value", 750)
        self.mp_tilt_adjSli.setOrientation(QtCore.Qt.Vertical)
        self.mp_tilt_adjSli.setObjectName("mp_tilt_adjSli")
        self.mp_tilt_adjSpi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.mp_tilt_adjSpi.setGeometry(QtCore.QRect(100, 170, 71, 31))
        self.mp_tilt_adjSpi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.mp_tilt_adjSpi.setAlignment(QtCore.Qt.AlignCenter)
        self.mp_tilt_adjSpi.setMaximum(4092)
        self.mp_tilt_adjSpi.setProperty("value", 750)
        self.mp_tilt_adjSpi.setObjectName("mp_tilt_adjSpi")
        self.tp_attnSli = QtWidgets.QSlider(self.PredistorterWi)
        self.tp_attnSli.setGeometry(QtCore.QRect(290, 40, 40, 126))
        self.tp_attnSli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.tp_attnSli.setMaximum(4092)
        self.tp_attnSli.setSingleStep(10)
        self.tp_attnSli.setPageStep(100)
        self.tp_attnSli.setProperty("value", 750)
        self.tp_attnSli.setOrientation(QtCore.Qt.Vertical)
        self.tp_attnSli.setObjectName("tp_attnSli")
        self.tp_tiltSli = QtWidgets.QSlider(self.PredistorterWi)
        self.tp_tiltSli.setGeometry(QtCore.QRect(380, 40, 40, 126))
        self.tp_tiltSli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.tp_tiltSli.setMaximum(4092)
        self.tp_tiltSli.setSingleStep(10)
        self.tp_tiltSli.setPageStep(100)
        self.tp_tiltSli.setProperty("value", 750)
        self.tp_tiltSli.setOrientation(QtCore.Qt.Vertical)
        self.tp_tiltSli.setObjectName("tp_tiltSli")
        self.tp_attnSpi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.tp_attnSpi.setGeometry(QtCore.QRect(280, 170, 71, 31))
        self.tp_attnSpi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.tp_attnSpi.setAlignment(QtCore.Qt.AlignCenter)
        self.tp_attnSpi.setMaximum(4092)
        self.tp_attnSpi.setProperty("value", 750)
        self.tp_attnSpi.setObjectName("tp_attnSpi")
        self.peak_adj_tpSpi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.peak_adj_tpSpi.setGeometry(QtCore.QRect(460, 170, 71, 31))
        self.peak_adj_tpSpi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.peak_adj_tpSpi.setAlignment(QtCore.Qt.AlignCenter)
        self.peak_adj_tpSpi.setMaximum(4092)
        self.peak_adj_tpSpi.setProperty("value", 750)
        self.peak_adj_tpSpi.setObjectName("peak_adj_tpSpi")
        self.peak_adj_tpSli = QtWidgets.QSlider(self.PredistorterWi)
        self.peak_adj_tpSli.setGeometry(QtCore.QRect(470, 40, 40, 126))
        self.peak_adj_tpSli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.peak_adj_tpSli.setMaximum(4092)
        self.peak_adj_tpSli.setSingleStep(10)
        self.peak_adj_tpSli.setPageStep(100)
        self.peak_adj_tpSli.setProperty("value", 750)
        self.peak_adj_tpSli.setOrientation(QtCore.Qt.Vertical)
        self.peak_adj_tpSli.setObjectName("peak_adj_tpSli")
        self.tp_tiltSpi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.tp_tiltSpi.setGeometry(QtCore.QRect(370, 170, 71, 31))
        self.tp_tiltSpi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.tp_tiltSpi.setAlignment(QtCore.Qt.AlignCenter)
        self.tp_tiltSpi.setMaximum(4092)
        self.tp_tiltSpi.setProperty("value", 750)
        self.tp_tiltSpi.setObjectName("tp_tiltSpi")
        self.label_29 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_29.setGeometry(QtCore.QRect(100, 20, 61, 21))
        self.label_29.setObjectName("label_29")
        self.label_34 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_34.setGeometry(QtCore.QRect(280, 20, 71, 21))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_35.setGeometry(QtCore.QRect(190, 20, 71, 21))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_36.setGeometry(QtCore.QRect(460, 20, 71, 21))
        self.label_36.setObjectName("label_36")
        self.label_39 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_39.setGeometry(QtCore.QRect(370, 20, 71, 21))
        self.label_39.setObjectName("label_39")
        self.label_53 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_53.setGeometry(QtCore.QRect(720, 10, 51, 21))
        self.label_53.setObjectName("label_53")
        self.vampSpi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.vampSpi.setGeometry(QtCore.QRect(280, 360, 71, 31))
        self.vampSpi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.vampSpi.setAlignment(QtCore.Qt.AlignCenter)
        self.vampSpi.setMaximum(4092)
        self.vampSpi.setProperty("value", 750)
        self.vampSpi.setObjectName("vampSpi")
        self.vcso3Sli = QtWidgets.QSlider(self.PredistorterWi)
        self.vcso3Sli.setGeometry(QtCore.QRect(110, 230, 40, 126))
        self.vcso3Sli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.vcso3Sli.setMaximum(4092)
        self.vcso3Sli.setSingleStep(10)
        self.vcso3Sli.setPageStep(100)
        self.vcso3Sli.setProperty("value", 750)
        self.vcso3Sli.setOrientation(QtCore.Qt.Vertical)
        self.vcso3Sli.setObjectName("vcso3Sli")
        self.vcso2Sli = QtWidgets.QSlider(self.PredistorterWi)
        self.vcso2Sli.setGeometry(QtCore.QRect(20, 230, 40, 126))
        self.vcso2Sli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.vcso2Sli.setMaximum(4092)
        self.vcso2Sli.setSingleStep(10)
        self.vcso2Sli.setPageStep(100)
        self.vcso2Sli.setProperty("value", 750)
        self.vcso2Sli.setOrientation(QtCore.Qt.Vertical)
        self.vcso2Sli.setObjectName("vcso2Sli")
        self.vctb3Spi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.vctb3Spi.setGeometry(QtCore.QRect(460, 360, 71, 31))
        self.vctb3Spi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.vctb3Spi.setAlignment(QtCore.Qt.AlignCenter)
        self.vctb3Spi.setMaximum(4092)
        self.vctb3Spi.setProperty("value", 750)
        self.vctb3Spi.setObjectName("vctb3Spi")
        self.vcso3Spi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.vcso3Spi.setGeometry(QtCore.QRect(100, 360, 71, 31))
        self.vcso3Spi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.vcso3Spi.setAlignment(QtCore.Qt.AlignCenter)
        self.vcso3Spi.setMaximum(4092)
        self.vcso3Spi.setProperty("value", 750)
        self.vcso3Spi.setObjectName("vcso3Spi")
        self.label_30 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_30.setGeometry(QtCore.QRect(110, 210, 61, 21))
        self.label_30.setObjectName("label_30")
        self.vctb3Sli = QtWidgets.QSlider(self.PredistorterWi)
        self.vctb3Sli.setGeometry(QtCore.QRect(470, 230, 40, 126))
        self.vctb3Sli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.vctb3Sli.setMaximum(4092)
        self.vctb3Sli.setSingleStep(10)
        self.vctb3Sli.setPageStep(100)
        self.vctb3Sli.setProperty("value", 750)
        self.vctb3Sli.setOrientation(QtCore.Qt.Vertical)
        self.vctb3Sli.setObjectName("vctb3Sli")
        self.vampSli = QtWidgets.QSlider(self.PredistorterWi)
        self.vampSli.setGeometry(QtCore.QRect(290, 230, 40, 126))
        self.vampSli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.vampSli.setMaximum(4092)
        self.vampSli.setSingleStep(10)
        self.vampSli.setPageStep(100)
        self.vampSli.setProperty("value", 750)
        self.vampSli.setOrientation(QtCore.Qt.Vertical)
        self.vampSli.setObjectName("vampSli")
        self.label_40 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_40.setGeometry(QtCore.QRect(30, 210, 61, 21))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_41.setGeometry(QtCore.QRect(480, 210, 61, 21))
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_42.setGeometry(QtCore.QRect(390, 210, 61, 21))
        self.label_42.setObjectName("label_42")
        self.vcso4Spi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.vcso4Spi.setGeometry(QtCore.QRect(190, 360, 71, 31))
        self.vcso4Spi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.vcso4Spi.setAlignment(QtCore.Qt.AlignCenter)
        self.vcso4Spi.setMaximum(4092)
        self.vcso4Spi.setProperty("value", 750)
        self.vcso4Spi.setObjectName("vcso4Spi")
        self.label_43 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_43.setGeometry(QtCore.QRect(200, 210, 61, 21))
        self.label_43.setObjectName("label_43")
        self.vcso2Spi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.vcso2Spi.setGeometry(QtCore.QRect(20, 360, 71, 31))
        self.vcso2Spi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.vcso2Spi.setAlignment(QtCore.Qt.AlignCenter)
        self.vcso2Spi.setMaximum(4092)
        self.vcso2Spi.setProperty("value", 750)
        self.vcso2Spi.setObjectName("vcso2Spi")
        self.vctbSpi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.vctbSpi.setGeometry(QtCore.QRect(370, 360, 71, 31))
        self.vctbSpi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.vctbSpi.setAlignment(QtCore.Qt.AlignCenter)
        self.vctbSpi.setMaximum(4092)
        self.vctbSpi.setProperty("value", 750)
        self.vctbSpi.setObjectName("vctbSpi")
        self.vctbSli = QtWidgets.QSlider(self.PredistorterWi)
        self.vctbSli.setGeometry(QtCore.QRect(380, 230, 40, 126))
        self.vctbSli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.vctbSli.setMaximum(4092)
        self.vctbSli.setSingleStep(10)
        self.vctbSli.setPageStep(100)
        self.vctbSli.setProperty("value", 750)
        self.vctbSli.setOrientation(QtCore.Qt.Vertical)
        self.vctbSli.setObjectName("vctbSli")
        self.vcso4Sli = QtWidgets.QSlider(self.PredistorterWi)
        self.vcso4Sli.setGeometry(QtCore.QRect(200, 230, 40, 126))
        self.vcso4Sli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.vcso4Sli.setMaximum(4092)
        self.vcso4Sli.setSingleStep(10)
        self.vcso4Sli.setPageStep(100)
        self.vcso4Sli.setProperty("value", 750)
        self.vcso4Sli.setOrientation(QtCore.Qt.Vertical)
        self.vcso4Sli.setObjectName("vcso4Sli")
        self.label_44 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_44.setGeometry(QtCore.QRect(300, 210, 61, 21))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_45.setGeometry(QtCore.QRect(650, 210, 61, 21))
        self.label_45.setObjectName("label_45")
        self.vclampSpi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.vclampSpi.setGeometry(QtCore.QRect(640, 360, 71, 31))
        self.vclampSpi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.vclampSpi.setAlignment(QtCore.Qt.AlignCenter)
        self.vclampSpi.setMaximum(4092)
        self.vclampSpi.setProperty("value", 750)
        self.vclampSpi.setObjectName("vclampSpi")
        self.vxmodSpi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.vxmodSpi.setGeometry(QtCore.QRect(550, 360, 71, 31))
        self.vxmodSpi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.vxmodSpi.setAlignment(QtCore.Qt.AlignCenter)
        self.vxmodSpi.setMaximum(4092)
        self.vxmodSpi.setProperty("value", 750)
        self.vxmodSpi.setObjectName("vxmodSpi")
        self.vxmodSli = QtWidgets.QSlider(self.PredistorterWi)
        self.vxmodSli.setGeometry(QtCore.QRect(560, 230, 40, 126))
        self.vxmodSli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.vxmodSli.setMaximum(4092)
        self.vxmodSli.setSingleStep(10)
        self.vxmodSli.setPageStep(100)
        self.vxmodSli.setProperty("value", 750)
        self.vxmodSli.setOrientation(QtCore.Qt.Vertical)
        self.vxmodSli.setObjectName("vxmodSli")
        self.vclampSli = QtWidgets.QSlider(self.PredistorterWi)
        self.vclampSli.setGeometry(QtCore.QRect(650, 230, 40, 126))
        self.vclampSli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.vclampSli.setMaximum(4092)
        self.vclampSli.setSingleStep(10)
        self.vclampSli.setPageStep(100)
        self.vclampSli.setProperty("value", 750)
        self.vclampSli.setOrientation(QtCore.Qt.Vertical)
        self.vclampSli.setObjectName("vclampSli")
        self.label_46 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_46.setGeometry(QtCore.QRect(560, 210, 61, 21))
        self.label_46.setObjectName("label_46")
        self.vxtSpi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.vxtSpi.setGeometry(QtCore.QRect(280, 550, 71, 31))
        self.vxtSpi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.vxtSpi.setAlignment(QtCore.Qt.AlignCenter)
        self.vxtSpi.setMaximum(4092)
        self.vxtSpi.setProperty("value", 750)
        self.vxtSpi.setObjectName("vxtSpi")
        self.ditherSli = QtWidgets.QSlider(self.PredistorterWi)
        self.ditherSli.setGeometry(QtCore.QRect(110, 420, 40, 126))
        self.ditherSli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.ditherSli.setMaximum(4092)
        self.ditherSli.setSingleStep(100)
        self.ditherSli.setPageStep(100)
        self.ditherSli.setProperty("value", 750)
        self.ditherSli.setOrientation(QtCore.Qt.Vertical)
        self.ditherSli.setObjectName("ditherSli")
        self.modbiasSli = QtWidgets.QSlider(self.PredistorterWi)
        self.modbiasSli.setGeometry(QtCore.QRect(20, 420, 40, 126))
        self.modbiasSli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.modbiasSli.setMaximum(4092)
        self.modbiasSli.setSingleStep(100)
        self.modbiasSli.setPageStep(100)
        self.modbiasSli.setProperty("value", 750)
        self.modbiasSli.setOrientation(QtCore.Qt.Vertical)
        self.modbiasSli.setObjectName("modbiasSli")
        self.ditherTuneSpi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.ditherTuneSpi.setGeometry(QtCore.QRect(460, 550, 71, 31))
        self.ditherTuneSpi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.ditherTuneSpi.setAlignment(QtCore.Qt.AlignCenter)
        self.ditherTuneSpi.setMaximum(4092)
        self.ditherTuneSpi.setProperty("value", 750)
        self.ditherTuneSpi.setObjectName("ditherTuneSpi")
        self.ditherSpi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.ditherSpi.setGeometry(QtCore.QRect(100, 550, 71, 31))
        self.ditherSpi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.ditherSpi.setAlignment(QtCore.Qt.AlignCenter)
        self.ditherSpi.setMaximum(4092)
        self.ditherSpi.setProperty("value", 750)
        self.ditherSpi.setObjectName("ditherSpi")
        self.label_47 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_47.setGeometry(QtCore.QRect(100, 400, 81, 21))
        self.label_47.setObjectName("label_47")
        self.ditherTuneSli = QtWidgets.QSlider(self.PredistorterWi)
        self.ditherTuneSli.setGeometry(QtCore.QRect(470, 420, 40, 126))
        self.ditherTuneSli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.ditherTuneSli.setMaximum(4092)
        self.ditherTuneSli.setSingleStep(10)
        self.ditherTuneSli.setPageStep(100)
        self.ditherTuneSli.setProperty("value", 750)
        self.ditherTuneSli.setOrientation(QtCore.Qt.Vertical)
        self.ditherTuneSli.setObjectName("ditherTuneSli")
        self.vxtSli = QtWidgets.QSlider(self.PredistorterWi)
        self.vxtSli.setGeometry(QtCore.QRect(290, 420, 40, 126))
        self.vxtSli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.vxtSli.setMaximum(4092)
        self.vxtSli.setSingleStep(100)
        self.vxtSli.setPageStep(100)
        self.vxtSli.setProperty("value", 750)
        self.vxtSli.setOrientation(QtCore.Qt.Vertical)
        self.vxtSli.setObjectName("vxtSli")
        self.label_48 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_48.setGeometry(QtCore.QRect(30, 400, 61, 21))
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_49.setGeometry(QtCore.QRect(460, 400, 71, 21))
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_50.setGeometry(QtCore.QRect(390, 400, 61, 21))
        self.label_50.setObjectName("label_50")
        self.vsbsSpi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.vsbsSpi.setGeometry(QtCore.QRect(190, 550, 71, 31))
        self.vsbsSpi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.vsbsSpi.setAlignment(QtCore.Qt.AlignCenter)
        self.vsbsSpi.setMaximum(4092)
        self.vsbsSpi.setProperty("value", 750)
        self.vsbsSpi.setObjectName("vsbsSpi")
        self.label_51 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_51.setGeometry(QtCore.QRect(210, 400, 61, 21))
        self.label_51.setObjectName("label_51")
        self.modbiasSpi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.modbiasSpi.setGeometry(QtCore.QRect(10, 550, 71, 31))
        self.modbiasSpi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.modbiasSpi.setAlignment(QtCore.Qt.AlignCenter)
        self.modbiasSpi.setMaximum(4092)
        self.modbiasSpi.setProperty("value", 750)
        self.modbiasSpi.setObjectName("modbiasSpi")
        self.vadjSpi = QtWidgets.QSpinBox(self.PredistorterWi)
        self.vadjSpi.setGeometry(QtCore.QRect(370, 550, 71, 31))
        self.vadjSpi.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.vadjSpi.setAlignment(QtCore.Qt.AlignCenter)
        self.vadjSpi.setMaximum(4092)
        self.vadjSpi.setProperty("value", 750)
        self.vadjSpi.setObjectName("vadjSpi")
        self.vadjSli = QtWidgets.QSlider(self.PredistorterWi)
        self.vadjSli.setGeometry(QtCore.QRect(380, 420, 40, 126))
        self.vadjSli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.vadjSli.setMaximum(4092)
        self.vadjSli.setSingleStep(100)
        self.vadjSli.setPageStep(100)
        self.vadjSli.setProperty("value", 750)
        self.vadjSli.setOrientation(QtCore.Qt.Vertical)
        self.vadjSli.setObjectName("vadjSli")
        self.vsbsSli = QtWidgets.QSlider(self.PredistorterWi)
        self.vsbsSli.setGeometry(QtCore.QRect(200, 420, 40, 126))
        self.vsbsSli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.vsbsSli.setMaximum(4092)
        self.vsbsSli.setSingleStep(100)
        self.vsbsSli.setPageStep(100)
        self.vsbsSli.setProperty("value", 750)
        self.vsbsSli.setOrientation(QtCore.Qt.Vertical)
        self.vsbsSli.setObjectName("vsbsSli")
        self.label_52 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_52.setGeometry(QtCore.QRect(300, 400, 61, 21))
        self.label_52.setObjectName("label_52")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.PredistorterWi)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(630, 430, 0, 126))
        self.verticalScrollBar_2.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.verticalScrollBar_2.setMaximum(4096)
        self.verticalScrollBar_2.setSingleStep(100)
        self.verticalScrollBar_2.setPageStep(100)
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setInvertedAppearance(True)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.attnSli = QtWidgets.QSlider(self.PredistorterWi)
        self.attnSli.setGeometry(QtCore.QRect(20, 40, 40, 126))
        self.attnSli.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.attnSli.setMaximum(4092)
        self.attnSli.setSingleStep(10)
        self.attnSli.setPageStep(100)
        self.attnSli.setProperty("value", 750)
        self.attnSli.setOrientation(QtCore.Qt.Vertical)
        self.attnSli.setObjectName("attnSli")
        self.label = QtWidgets.QLabel(self.PredistorterWi)
        self.label.setGeometry(QtCore.QRect(50, 50, 21, 16))
        self.label.setObjectName("label")
        self.label_54 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_54.setGeometry(QtCore.QRect(140, 50, 21, 16))
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_55.setGeometry(QtCore.QRect(230, 50, 21, 16))
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_56.setGeometry(QtCore.QRect(320, 50, 21, 16))
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_57.setGeometry(QtCore.QRect(410, 50, 31, 16))
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_58.setGeometry(QtCore.QRect(500, 50, 31, 16))
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_59.setGeometry(QtCore.QRect(50, 240, 31, 16))
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_60.setGeometry(QtCore.QRect(140, 240, 31, 16))
        self.label_60.setObjectName("label_60")
        self.label_64 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_64.setGeometry(QtCore.QRect(320, 240, 31, 16))
        self.label_64.setObjectName("label_64")
        self.label_65 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_65.setGeometry(QtCore.QRect(230, 240, 31, 16))
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_66.setGeometry(QtCore.QRect(410, 240, 31, 16))
        self.label_66.setObjectName("label_66")
        self.label_67 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_67.setGeometry(QtCore.QRect(500, 240, 31, 16))
        self.label_67.setObjectName("label_67")
        self.label_68 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_68.setGeometry(QtCore.QRect(680, 240, 31, 16))
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_69.setGeometry(QtCore.QRect(590, 240, 31, 16))
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_70.setGeometry(QtCore.QRect(50, 430, 31, 16))
        self.label_70.setObjectName("label_70")
        self.label_71 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_71.setGeometry(QtCore.QRect(140, 430, 31, 16))
        self.label_71.setObjectName("label_71")
        self.label_72 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_72.setGeometry(QtCore.QRect(320, 430, 31, 16))
        self.label_72.setObjectName("label_72")
        self.label_73 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_73.setGeometry(QtCore.QRect(230, 430, 31, 16))
        self.label_73.setObjectName("label_73")
        self.label_74 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_74.setGeometry(QtCore.QRect(500, 430, 31, 16))
        self.label_74.setObjectName("label_74")
        self.label_75 = QtWidgets.QLabel(self.PredistorterWi)
        self.label_75.setGeometry(QtCore.QRect(410, 430, 31, 16))
        self.label_75.setObjectName("label_75")
        self.preTrigSli = QtWidgets.QToolButton(self.PredistorterWi)
        self.preTrigSli.setGeometry(QtCore.QRect(260, 270, 25, 19))
        self.preTrigSli.setText("")
        self.preTrigSli.setObjectName("preTrigSli")
        self.boardInfBu = QtWidgets.QPushButton(miniTx)
        self.boardInfBu.setGeometry(QtCore.QRect(490, 0, 75, 23))
        self.boardInfBu.setObjectName("boardInfBu")
        self.fileGroupBo = QtWidgets.QGroupBox(miniTx)
        self.fileGroupBo.setGeometry(QtCore.QRect(800, 250, 111, 91))
        self.fileGroupBo.setObjectName("fileGroupBo")
        self.getFileBu = QtWidgets.QPushButton(self.fileGroupBo)
        self.getFileBu.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.getFileBu.setObjectName("getFileBu")
        self.saveFileBu = QtWidgets.QPushButton(self.fileGroupBo)
        self.saveFileBu.setGeometry(QtCore.QRect(20, 30, 75, 23))
        self.saveFileBu.setObjectName("saveFileBu")
        self.rfGainfBu = QtWidgets.QPushButton(miniTx)
        self.rfGainfBu.setGeometry(QtCore.QRect(210, 0, 75, 23))
        self.rfGainfBu.setObjectName("rfGainfBu")
        self.rfGainWi = QtWidgets.QGroupBox(miniTx)
        self.rfGainWi.setEnabled(True)
        self.rfGainWi.setGeometry(QtCore.QRect(10, 1480, 771, 360))
        self.rfGainWi.setObjectName("rfGainWi")
        self.label_85 = QtWidgets.QLabel(self.rfGainWi)
        self.label_85.setGeometry(QtCore.QRect(40, 165, 81, 21))
        self.label_85.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label_85.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_85.setObjectName("label_85")
        self.label_91 = QtWidgets.QLabel(self.rfGainWi)
        self.label_91.setGeometry(QtCore.QRect(500, 60, 81, 21))
        self.label_91.setObjectName("label_91")
        self.e10_6 = QtWidgets.QLineEdit(self.rfGainWi)
        self.e10_6.setGeometry(QtCore.QRect(180, 470, 101, 31))
        self.e10_6.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 0);")
        self.e10_6.setAlignment(QtCore.Qt.AlignCenter)
        self.e10_6.setObjectName("e10_6")
        self.attnSli_2 = QtWidgets.QSlider(self.rfGainWi)
        self.attnSli_2.setGeometry(QtCore.QRect(500, 85, 40, 141))
        self.attnSli_2.setStyleSheet("QSlider::groove:vertical {\n"
"     border: 1px solid #999999;\n"
"     width: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 0 2px;\n"
" }\n"
"\n"
" QSlider::handle:vertical {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     height: 18px;\n"
"     margin: 0 -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }")
        self.attnSli_2.setMaximum(4092)
        self.attnSli_2.setSingleStep(10)
        self.attnSli_2.setPageStep(100)
        self.attnSli_2.setProperty("value", 750)
        self.attnSli_2.setOrientation(QtCore.Qt.Vertical)
        self.attnSli_2.setObjectName("attnSli_2")
        self.attnSpi_2 = QtWidgets.QSpinBox(self.rfGainWi)
        self.attnSpi_2.setGeometry(QtCore.QRect(480, 230, 91, 31))
        self.attnSpi_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.attnSpi_2.setAlignment(QtCore.Qt.AlignCenter)
        self.attnSpi_2.setMaximum(4092)
        self.attnSpi_2.setProperty("value", 750)
        self.attnSpi_2.setObjectName("attnSpi_2")
        self.agcBo = QtWidgets.QCheckBox(self.rfGainWi)
        self.agcBo.setGeometry(QtCore.QRect(670, 30, 81, 21))
        self.agcBo.setObjectName("agcBo")
        self.refreshBu_2 = QtWidgets.QPushButton(self.rfGainWi)
        self.refreshBu_2.setGeometry(QtCore.QRect(660, 320, 75, 23))
        self.refreshBu_2.setObjectName("refreshBu_2")
        self.continueBo_2 = QtWidgets.QCheckBox(self.rfGainWi)
        self.continueBo_2.setGeometry(QtCore.QRect(670, 270, 81, 17))
        self.continueBo_2.setObjectName("continueBo_2")
        self.Input_RF_MON_dbm_2 = QtWidgets.QLabel(self.rfGainWi)
        self.Input_RF_MON_dbm_2.setGeometry(QtCore.QRect(170, 100, 101, 21))
        self.Input_RF_MON_dbm_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.Input_RF_MON_dbm_2.setFrameShape(QtWidgets.QFrame.Box)
        self.Input_RF_MON_dbm_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Input_RF_MON_dbm_2.setText("")
        self.Input_RF_MON_dbm_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Input_RF_MON_dbm_2.setObjectName("Input_RF_MON_dbm_2")
        self.label_83 = QtWidgets.QLabel(self.rfGainWi)
        self.label_83.setGeometry(QtCore.QRect(40, 100, 121, 21))
        self.label_83.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_83.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_83.setObjectName("label_83")
        self.LAS_RF_dbm_2 = QtWidgets.QLabel(self.rfGainWi)
        self.LAS_RF_dbm_2.setGeometry(QtCore.QRect(170, 240, 101, 21))
        self.LAS_RF_dbm_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.LAS_RF_dbm_2.setFrameShape(QtWidgets.QFrame.Box)
        self.LAS_RF_dbm_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LAS_RF_dbm_2.setText("")
        self.LAS_RF_dbm_2.setAlignment(QtCore.Qt.AlignCenter)
        self.LAS_RF_dbm_2.setObjectName("LAS_RF_dbm_2")
        self.label_84 = QtWidgets.QLabel(self.rfGainWi)
        self.label_84.setGeometry(QtCore.QRect(40, 240, 101, 21))
        self.label_84.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_84.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_84.setObjectName("label_84")
        self.getFromBoardGainBu = QtWidgets.QPushButton(self.rfGainWi)
        self.getFromBoardGainBu.setEnabled(True)
        self.getFromBoardGainBu.setGeometry(QtCore.QRect(100, 320, 90, 27))
        self.getFromBoardGainBu.setObjectName("getFromBoardGainBu")
        self.saveToBoardGainBu = QtWidgets.QPushButton(self.rfGainWi)
        self.saveToBoardGainBu.setGeometry(QtCore.QRect(240, 320, 90, 27))
        self.saveToBoardGainBu.setToolTipDuration(-8)
        self.saveToBoardGainBu.setObjectName("saveToBoardGainBu")
        self.gainUpBu = QtWidgets.QPushButton(self.rfGainWi)
        self.gainUpBu.setGeometry(QtCore.QRect(290, 150, 51, 23))
        self.gainUpBu.setObjectName("gainUpBu")
        self.gainDownBu = QtWidgets.QPushButton(self.rfGainWi)
        self.gainDownBu.setGeometry(QtCore.QRect(290, 180, 51, 23))
        self.gainDownBu.setObjectName("gainDownBu")
        self.rfAttnDb = QtWidgets.QLineEdit(self.rfGainWi)
        self.rfAttnDb.setGeometry(QtCore.QRect(170, 160, 101, 31))
        self.rfAttnDb.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.rfAttnDb.setAlignment(QtCore.Qt.AlignCenter)
        self.rfAttnDb.setObjectName("rfAttnDb")

        self.retranslateUi(miniTx)
        self.comCom.setCurrentIndex(1)
        self.mp_tilt_adjSpi.valueChanged['int'].connect(self.mp_tilt_adjSli.setValue)
        self.mp_tilt_adjSli.valueChanged['int'].connect(self.mp_tilt_adjSpi.setValue)
        self.peak_adj_mpSpi.valueChanged['int'].connect(self.peak_adj_mpSpi.setValue)
        self.peak_adj_mpSpi.valueChanged['int'].connect(self.peak_adj_mpSli.setValue)
        self.tp_attnSli.valueChanged['int'].connect(self.tp_attnSpi.setValue)
        self.tp_attnSpi.valueChanged['int'].connect(self.tp_attnSli.setValue)
        self.tp_tiltSli.valueChanged['int'].connect(self.tp_tiltSpi.setValue)
        self.tp_tiltSpi.valueChanged['int'].connect(self.tp_tiltSli.setValue)
        self.peak_adj_tpSli.valueChanged['int'].connect(self.peak_adj_tpSpi.setValue)
        self.peak_adj_tpSpi.valueChanged['int'].connect(self.peak_adj_tpSli.setValue)
        self.vcso2Spi.valueChanged['int'].connect(self.vcso2Sli.setValue)
        self.vcso2Sli.valueChanged['int'].connect(self.vcso2Spi.setValue)
        self.vcso3Sli.valueChanged['int'].connect(self.vcso3Spi.setValue)
        self.vcso3Spi.valueChanged['int'].connect(self.vcso3Sli.setValue)
        self.vcso4Sli.valueChanged['int'].connect(self.vcso4Spi.setValue)
        self.vcso4Spi.valueChanged['int'].connect(self.vcso4Sli.setValue)
        self.vampSli.valueChanged['int'].connect(self.vampSpi.setValue)
        self.vampSpi.valueChanged['int'].connect(self.vampSli.setValue)
        self.vctbSli.valueChanged['int'].connect(self.vctbSpi.setValue)
        self.vctbSpi.valueChanged['int'].connect(self.vctbSli.setValue)
        self.vctb3Sli.valueChanged['int'].connect(self.vctb3Spi.setValue)
        self.vctb3Spi.valueChanged['int'].connect(self.vctb3Sli.setValue)
        self.vxmodSli.valueChanged['int'].connect(self.vxmodSpi.setValue)
        self.vxmodSpi.valueChanged['int'].connect(self.vxmodSli.setValue)
        self.vclampSli.valueChanged['int'].connect(self.vclampSpi.setValue)
        self.vclampSpi.valueChanged['int'].connect(self.vclampSli.setValue)
        self.modbiasSli.valueChanged['int'].connect(self.modbiasSpi.setValue)
        self.modbiasSpi.valueChanged['int'].connect(self.modbiasSli.setValue)
        self.ditherSli.valueChanged['int'].connect(self.ditherSpi.setValue)
        self.ditherSpi.valueChanged['int'].connect(self.ditherSli.setValue)
        self.vsbsSli.valueChanged['int'].connect(self.vsbsSpi.setValue)
        self.vsbsSpi.valueChanged['int'].connect(self.vsbsSli.setValue)
        self.vxtSli.valueChanged['int'].connect(self.vxtSpi.setValue)
        self.vxtSpi.valueChanged['int'].connect(self.vxtSli.setValue)
        self.vadjSli.valueChanged['int'].connect(self.vadjSpi.setValue)
        self.vadjSpi.valueChanged['int'].connect(self.vadjSli.setValue)
        self.ditherTuneSli.valueChanged['int'].connect(self.ditherTuneSpi.setValue)
        self.ditherTuneSpi.valueChanged['int'].connect(self.ditherTuneSli.setValue)
        self.FlsrBiasSli.valueChanged['int'].connect(self.FlsrBiasSpi.setValue)
        self.FlsrBiasSpi.valueChanged['int'].connect(self.FlsrBiasSli.setValue)
        self.RlsrBiasSli.valueChanged['int'].connect(self.RlsrBiasSpi.setValue)
        self.RlsrBiasSpi.valueChanged['int'].connect(self.RlsrBiasSli.setValue)
        self.LsrTempSli.valueChanged['int'].connect(self.LsrTempSpi.setValue)
        self.LsrTempSpi.valueChanged['int'].connect(self.LsrTempSli.setValue)
        self.peak_adj_mpSli.valueChanged['int'].connect(self.peak_adj_mpSpi.setValue)
        self.attnSli.valueChanged['int'].connect(self.attnSpi.setValue)
        self.attnSpi.valueChanged['int'].connect(self.attnSli.setValue)
        self.FlsrBiasSli.actionTriggered['int'].connect(self.lasTrigSli.click)
        self.RlsrBiasSli.actionTriggered['int'].connect(self.lasTrigSli.click)
        self.LsrTempSli.actionTriggered['int'].connect(self.lasTrigSli.click)
        self.peak_adj_mpSli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.tp_attnSli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.tp_tiltSli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.peak_adj_tpSli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.mp_tilt_adjSli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.attnSli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.vcso4Sli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.vampSli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.vcso3Sli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.vctb3Sli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.vxmodSli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.vcso2Sli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.vxmodSli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.vclampSli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.vsbsSli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.vxtSli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.ditherSli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.vadjSli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.modbiasSli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.vadjSli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.ditherTuneSli.actionTriggered['int'].connect(self.preTrigSli.click)
        self.attnSli_2.valueChanged['int'].connect(self.attnSli.setValue)
        self.attnSli.valueChanged['int'].connect(self.attnSli_2.setValue)
        self.attnSpi.valueChanged['int'].connect(self.attnSpi_2.setValue)
        self.attnSpi_2.valueChanged['int'].connect(self.attnSpi.setValue)
        self.Input_RF_MON_dbm.textChanged['QString'].connect(self.Input_RF_MON_dbm_2.setText)
        self.LAS_RF_dbm.textChanged['QString'].connect(self.LAS_RF_dbm_2.setText)
        self.refreshBu_2.clicked.connect(self.refreshBu.click)
        self.continueBo_2.clicked.connect(self.continueBo.click)
        QtCore.QMetaObject.connectSlotsByName(miniTx)
        miniTx.setTabOrder(self.PredistorterBu, self.LsrControlsBu)
        miniTx.setTabOrder(self.LsrControlsBu, self.TCBu)
        miniTx.setTabOrder(self.TCBu, self.FcBu)
        miniTx.setTabOrder(self.FcBu, self.alarmBu)
        miniTx.setTabOrder(self.alarmBu, self.peak_adj_mpSpi)
        miniTx.setTabOrder(self.peak_adj_mpSpi, self.closeBu)
        miniTx.setTabOrder(self.closeBu, self.boardInfBu)
        miniTx.setTabOrder(self.boardInfBu, self.FlsrBiasSpi)
        miniTx.setTabOrder(self.FlsrBiasSpi, self.freqEdit)
        miniTx.setTabOrder(self.freqEdit, self.FlsrBiasSli)
        miniTx.setTabOrder(self.FlsrBiasSli, self.freqBSet)
        miniTx.setTabOrder(self.freqBSet, self.LsrTempSli)
        miniTx.setTabOrder(self.LsrTempSli, self.LsrTempSpi)
        miniTx.setTabOrder(self.LsrTempSpi, self.RlsrBiasSli)
        miniTx.setTabOrder(self.RlsrBiasSli, self.RlsrBiasSpi)
        miniTx.setTabOrder(self.RlsrBiasSpi, self.e10_2)
        miniTx.setTabOrder(self.e10_2, self.getBu)
        miniTx.setTabOrder(self.getBu, self.saveBu)
        miniTx.setTabOrder(self.saveBu, self.connectBu)
        miniTx.setTabOrder(self.connectBu, self.comCom)
        miniTx.setTabOrder(self.comCom, self.attnSpi)
        miniTx.setTabOrder(self.attnSpi, self.peak_adj_mpSli)
        miniTx.setTabOrder(self.peak_adj_mpSli, self.dcMonitorBu)
        miniTx.setTabOrder(self.dcMonitorBu, self.mp_tilt_adjSli)
        miniTx.setTabOrder(self.mp_tilt_adjSli, self.mp_tilt_adjSpi)
        miniTx.setTabOrder(self.mp_tilt_adjSpi, self.tp_attnSli)
        miniTx.setTabOrder(self.tp_attnSli, self.tp_tiltSli)
        miniTx.setTabOrder(self.tp_tiltSli, self.tp_attnSpi)
        miniTx.setTabOrder(self.tp_attnSpi, self.peak_adj_tpSpi)
        miniTx.setTabOrder(self.peak_adj_tpSpi, self.peak_adj_tpSli)
        miniTx.setTabOrder(self.peak_adj_tpSli, self.tp_tiltSpi)
        miniTx.setTabOrder(self.tp_tiltSpi, self.vampSpi)
        miniTx.setTabOrder(self.vampSpi, self.vcso3Sli)
        miniTx.setTabOrder(self.vcso3Sli, self.vcso2Sli)
        miniTx.setTabOrder(self.vcso2Sli, self.vctb3Spi)
        miniTx.setTabOrder(self.vctb3Spi, self.vcso3Spi)
        miniTx.setTabOrder(self.vcso3Spi, self.vctb3Sli)
        miniTx.setTabOrder(self.vctb3Sli, self.vampSli)
        miniTx.setTabOrder(self.vampSli, self.vcso4Spi)
        miniTx.setTabOrder(self.vcso4Spi, self.vcso2Spi)
        miniTx.setTabOrder(self.vcso2Spi, self.vctbSpi)
        miniTx.setTabOrder(self.vctbSpi, self.vctbSli)
        miniTx.setTabOrder(self.vctbSli, self.vcso4Sli)
        miniTx.setTabOrder(self.vcso4Sli, self.vclampSpi)
        miniTx.setTabOrder(self.vclampSpi, self.vxmodSpi)
        miniTx.setTabOrder(self.vxmodSpi, self.vxmodSli)
        miniTx.setTabOrder(self.vxmodSli, self.vclampSli)
        miniTx.setTabOrder(self.vclampSli, self.vxtSpi)
        miniTx.setTabOrder(self.vxtSpi, self.ditherSli)
        miniTx.setTabOrder(self.ditherSli, self.modbiasSli)
        miniTx.setTabOrder(self.modbiasSli, self.ditherTuneSpi)
        miniTx.setTabOrder(self.ditherTuneSpi, self.ditherSpi)
        miniTx.setTabOrder(self.ditherSpi, self.ditherTuneSli)
        miniTx.setTabOrder(self.ditherTuneSli, self.vxtSli)
        miniTx.setTabOrder(self.vxtSli, self.vsbsSpi)
        miniTx.setTabOrder(self.vsbsSpi, self.modbiasSpi)
        miniTx.setTabOrder(self.modbiasSpi, self.vadjSpi)
        miniTx.setTabOrder(self.vadjSpi, self.vadjSli)
        miniTx.setTabOrder(self.vadjSli, self.vsbsSli)

    def retranslateUi(self, miniTx):
        _translate = QtCore.QCoreApplication.translate
        miniTx.setWindowTitle(_translate("miniTx", "MiniTx GUI --- SIDxxxx --- V1010"))
        self.dcMonitorBu.setText(_translate("miniTx", "DC Monitor"))
        self.PredistorterBu.setText(_translate("miniTx", "Predistorter"))
        self.LsrControlsBu.setText(_translate("miniTx", "Lsr Controls"))
        self.TCBu.setText(_translate("miniTx", "TC"))
        self.FcBu.setText(_translate("miniTx", "FC"))
        self.alarmBu.setText(_translate("miniTx", "Alarm"))
        self.dcMonitorWi.setTitle(_translate("miniTx", "DC Monitor"))
        self.label_5.setText(_translate("miniTx", "Laser Temp"))
        self.label_2.setText(_translate("miniTx", "Module Temp"))
        self.label_8.setText(_translate("miniTx", "SBS-MON"))
        self.label_4.setText(_translate("miniTx", "Input-RF-MON"))
        self.label_7.setText(_translate("miniTx", "LAS-RF"))
        self.label_9.setText(_translate("miniTx", "LSR-PDI"))
        self.label_6.setText(_translate("miniTx", "FLSR-BIAS"))
        self.label_3.setText(_translate("miniTx", "TEC-I-MON"))
        self.label_10.setText(_translate("miniTx", "RLSR-BIAS"))
        self.label_13.setText(_translate("miniTx", "dBm"))
        self.label_22.setText(_translate("miniTx", "+5V MON"))
        self.label_61.setText(_translate("miniTx", "Alarm Status"))
        self.label_62.setText(_translate("miniTx", "Voltage (v)"))
        self.label_63.setText(_translate("miniTx", "Equivalence"))
        self.label_15.setText(_translate("miniTx", "C"))
        self.label_24.setText(_translate("miniTx", "C"))
        self.label_25.setText(_translate("miniTx", "mA"))
        self.label_26.setText(_translate("miniTx", "mA"))
        self.label_27.setText(_translate("miniTx", "mA"))
        self.label_23.setText(_translate("miniTx", "dBm"))
        self.label_79.setText(_translate("miniTx", "VIN  MON"))
        self.continueBo.setText(_translate("miniTx", "Auto Refesh"))
        self.refreshBu.setText(_translate("miniTx", "Refresh"))
        self.label_81.setText(_translate("miniTx", "mW"))
        self.lsrControlsWi.setTitle(_translate("miniTx", "Lsr Controls"))
        self.label_31.setText(_translate("miniTx", "RLSR-BIAS(mv)"))
        self.label_32.setText(_translate("miniTx", "LSR-TEMP(mv)"))
        self.label_16.setText(_translate("miniTx", "FLSR-BIAS (mA)"))
        self.label_18.setText(_translate("miniTx", "LSR-PDI (mW)"))
        self.label_17.setText(_translate("miniTx", "SBS-MON (v)"))
        self.label_12.setText(_translate("miniTx", "TEC-I-MON (mA)"))
        self.label_19.setText(_translate("miniTx", "RLSR-BIAS (mA)"))
        self.label_14.setText(_translate("miniTx", "Laser Temp (C)"))
        self.label_20.setText(_translate("miniTx", "FLSR-BIAS(mv)"))
        self.freqEdit.setText(_translate("miniTx", "2557"))
        self.freqBSet.setText(_translate("miniTx", "Set Frequency "))
        self.label_11.setText(_translate("miniTx", "Module Temp (C)"))
        self.label_33.setText(_translate("miniTx", "RATIO (F/R)"))
        self.label_21.setText(_translate("miniTx", "SCALE FACTOR"))
        self.label_37.setText(_translate("miniTx", "SCALE FACTOR"))
        self.label_38.setText(_translate("miniTx", "F (MHz)"))
        self.label_76.setText(_translate("miniTx", "Ch17"))
        self.label_77.setText(_translate("miniTx", "Ch16"))
        self.label_78.setText(_translate("miniTx", "Ch18"))
        self.laserContinueBo.setText(_translate("miniTx", "Auto Refesh"))
        self.laserRefreshBu.setText(_translate("miniTx", "Refresh"))
        self.laserCalibrateBu.setText(_translate("miniTx", "Calibrate"))
        self.label_80.setText(_translate("miniTx", "Power meter value (mW)"))
        self.label_82.setText(_translate("miniTx", "Alarm"))
        self.type1Bo.setText(_translate("miniTx", "Type_1(20mA)"))
        self.type2Bo.setText(_translate("miniTx", "Type_2(60mA)"))
        self.groupBox.setTitle(_translate("miniTx", "DAC ( Board)"))
        self.getBu.setText(_translate("miniTx", "Get"))
        self.saveBu.setText(_translate("miniTx", "Save"))
        self.groupBox_2.setTitle(_translate("miniTx", "COM"))
        self.connectBu.setText(_translate("miniTx", "Connect"))
        self.comCom.setItemText(0, _translate("miniTx", "COM1"))
        self.comCom.setItemText(1, _translate("miniTx", "COM2"))
        self.comCom.setItemText(2, _translate("miniTx", "COM3"))
        self.comCom.setItemText(3, _translate("miniTx", "COM4"))
        self.comCom.setItemText(4, _translate("miniTx", "COM5"))
        self.comCom.setItemText(5, _translate("miniTx", "COM6"))
        self.comCom.setItemText(6, _translate("miniTx", "COM7"))
        self.comCom.setItemText(7, _translate("miniTx", "COM8"))
        self.comCom.setItemText(8, _translate("miniTx", "COM9"))
        self.comCom.setItemText(9, _translate("miniTx", "COM10"))
        self.closeBu.setText(_translate("miniTx", "Close"))
        self.PredistorterWi.setTitle(_translate("miniTx", "Predistorter"))
        self.label_28.setText(_translate("miniTx", "ATTN-SET"))
        self.label_29.setText(_translate("miniTx", "MpTiltAdj"))
        self.label_34.setText(_translate("miniTx", "TP-ATTN-SET"))
        self.label_35.setText(_translate("miniTx", "PEAK-ADJ-MP"))
        self.label_36.setText(_translate("miniTx", "PEAK-ADJ-TP"))
        self.label_39.setText(_translate("miniTx", "TP-TILT-ADJ"))
        self.label_53.setText(_translate("miniTx", "Unit: mv"))
        self.label_30.setText(_translate("miniTx", "VCSO3"))
        self.label_40.setText(_translate("miniTx", "VCSO2"))
        self.label_41.setText(_translate("miniTx", "VCTB3"))
        self.label_42.setText(_translate("miniTx", "VCTB"))
        self.label_43.setText(_translate("miniTx", "VCSO4"))
        self.label_44.setText(_translate("miniTx", "VAMP"))
        self.label_45.setText(_translate("miniTx", "VCLAMP"))
        self.label_46.setText(_translate("miniTx", "VXMOD"))
        self.label_47.setText(_translate("miniTx", "DITHER-CORR"))
        self.label_48.setText(_translate("miniTx", "MODBIAS"))
        self.label_49.setText(_translate("miniTx", "DITHER-TUNE"))
        self.label_50.setText(_translate("miniTx", "VADJ"))
        self.label_51.setText(_translate("miniTx", "VSBS"))
        self.label_52.setText(_translate("miniTx", "VXT"))
        self.label.setText(_translate("miniTx", "Ch0"))
        self.label_54.setText(_translate("miniTx", "Ch1"))
        self.label_55.setText(_translate("miniTx", "Ch2"))
        self.label_56.setText(_translate("miniTx", "Ch4"))
        self.label_57.setText(_translate("miniTx", "Ch19"))
        self.label_58.setText(_translate("miniTx", "Ch20"))
        self.label_59.setText(_translate("miniTx", "Ch8"))
        self.label_60.setText(_translate("miniTx", "Ch15"))
        self.label_64.setText(_translate("miniTx", "Ch3"))
        self.label_65.setText(_translate("miniTx", "Ch13"))
        self.label_66.setText(_translate("miniTx", "Ch11"))
        self.label_67.setText(_translate("miniTx", "Ch12"))
        self.label_68.setText(_translate("miniTx", "Ch14"))
        self.label_69.setText(_translate("miniTx", "Ch9"))
        self.label_70.setText(_translate("miniTx", "Ch10"))
        self.label_71.setText(_translate("miniTx", "Ch22"))
        self.label_72.setText(_translate("miniTx", "Ch6"))
        self.label_73.setText(_translate("miniTx", "Ch5"))
        self.label_74.setText(_translate("miniTx", "Ch23"))
        self.label_75.setText(_translate("miniTx", "Ch21"))
        self.boardInfBu.setText(_translate("miniTx", "Board Info"))
        self.fileGroupBo.setTitle(_translate("miniTx", "File"))
        self.getFileBu.setText(_translate("miniTx", "Get"))
        self.saveFileBu.setText(_translate("miniTx", "Save"))
        self.rfGainfBu.setText(_translate("miniTx", "RF Gain"))
        self.rfGainWi.setTitle(_translate("miniTx", "RF Gain Control"))
        self.label_85.setText(_translate("miniTx", "RF Gain (dB)"))
        self.label_91.setText(_translate("miniTx", "ATTN-SET"))
        self.agcBo.setText(_translate("miniTx", "AGC On"))
        self.refreshBu_2.setText(_translate("miniTx", "Refresh"))
        self.continueBo_2.setText(_translate("miniTx", "Auto Refesh"))
        self.label_83.setText(_translate("miniTx", "Input-RF-MON (dBm)"))
        self.label_84.setText(_translate("miniTx", "LAS-RF (dBm)"))
        self.getFromBoardGainBu.setText(_translate("miniTx", "Get from Board"))
        self.saveToBoardGainBu.setText(_translate("miniTx", "Save to Board"))
        self.gainUpBu.setText(_translate("miniTx", "Up"))
        self.gainDownBu.setText(_translate("miniTx", "Down"))
        self.rfAttnDb.setText(_translate("miniTx", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    miniTx = QtWidgets.QDialog()
    ui = Ui_miniTx()
    ui.setupUi(miniTx)
    miniTx.show()
    sys.exit(app.exec_())

