

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(943, 316)
        Dialog.setSizeGripEnabled(True)
        self.Attn = QtWidgets.QCheckBox(Dialog)
        self.Attn.setGeometry(QtCore.QRect(20, 60, 101, 31))
        self.Attn.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.Attn.setChecked(True)
        self.Attn.setObjectName("Attn")
        self.saveToBoardBu = QtWidgets.QPushButton(Dialog)
        self.saveToBoardBu.setGeometry(QtCore.QRect(560, 270, 111, 31))
        self.saveToBoardBu.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.saveToBoardBu.setObjectName("saveToBoardBu")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(400, 0, 121, 31))
        self.label.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 131, 63);\n"
"")
        self.label.setObjectName("label")
        self.MpTiltAdj = QtWidgets.QCheckBox(Dialog)
        self.MpTiltAdj.setGeometry(QtCore.QRect(140, 60, 91, 31))
        self.MpTiltAdj.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.MpTiltAdj.setChecked(True)
        self.MpTiltAdj.setObjectName("MpTiltAdj")
        self.Vamp = QtWidgets.QCheckBox(Dialog)
        self.Vamp.setGeometry(QtCore.QRect(380, 60, 91, 31))
        self.Vamp.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.Vamp.setChecked(True)
        self.Vamp.setObjectName("Vamp")
        self.PeakAdjMp = QtWidgets.QCheckBox(Dialog)
        self.PeakAdjMp.setGeometry(QtCore.QRect(260, 60, 101, 31))
        self.PeakAdjMp.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.PeakAdjMp.setChecked(True)
        self.PeakAdjMp.setObjectName("PeakAdjMp")
        self.Res1 = QtWidgets.QCheckBox(Dialog)
        self.Res1.setGeometry(QtCore.QRect(860, 60, 91, 31))
        self.Res1.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.Res1.setChecked(True)
        self.Res1.setObjectName("Res1")
        self.VSbs = QtWidgets.QCheckBox(Dialog)
        self.VSbs.setGeometry(QtCore.QRect(620, 60, 91, 31))
        self.VSbs.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.VSbs.setChecked(True)
        self.VSbs.setObjectName("VSbs")
        self.TpAttn = QtWidgets.QCheckBox(Dialog)
        self.TpAttn.setGeometry(QtCore.QRect(500, 60, 101, 31))
        self.TpAttn.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.TpAttn.setChecked(True)
        self.TpAttn.setObjectName("TpAttn")
        self.Vxt = QtWidgets.QCheckBox(Dialog)
        self.Vxt.setGeometry(QtCore.QRect(740, 60, 101, 31))
        self.Vxt.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.Vxt.setChecked(True)
        self.Vxt.setObjectName("Vxt")
        self.Vclamp = QtWidgets.QCheckBox(Dialog)
        self.Vclamp.setGeometry(QtCore.QRect(740, 120, 101, 31))
        self.Vclamp.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.Vclamp.setChecked(True)
        self.Vclamp.setObjectName("Vclamp")
        self.Vcso4 = QtWidgets.QCheckBox(Dialog)
        self.Vcso4.setGeometry(QtCore.QRect(620, 120, 91, 31))
        self.Vcso4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.Vcso4.setChecked(True)
        self.Vcso4.setObjectName("Vcso4")
        self.Vctb = QtWidgets.QCheckBox(Dialog)
        self.Vctb.setGeometry(QtCore.QRect(380, 120, 91, 31))
        self.Vctb.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.Vctb.setChecked(True)
        self.Vctb.setObjectName("Vctb")
        self.Vxmod = QtWidgets.QCheckBox(Dialog)
        self.Vxmod.setGeometry(QtCore.QRect(140, 120, 91, 31))
        self.Vxmod.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.Vxmod.setChecked(True)
        self.Vxmod.setObjectName("Vxmod")
        self.Vcso2 = QtWidgets.QCheckBox(Dialog)
        self.Vcso2.setGeometry(QtCore.QRect(20, 120, 101, 31))
        self.Vcso2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.Vcso2.setChecked(True)
        self.Vcso2.setObjectName("Vcso2")
        self.Vctb3 = QtWidgets.QCheckBox(Dialog)
        self.Vctb3.setGeometry(QtCore.QRect(500, 120, 101, 31))
        self.Vctb3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.Vctb3.setChecked(True)
        self.Vctb3.setObjectName("Vctb3")
        self.Vcso3 = QtWidgets.QCheckBox(Dialog)
        self.Vcso3.setGeometry(QtCore.QRect(860, 120, 91, 31))
        self.Vcso3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.Vcso3.setChecked(True)
        self.Vcso3.setObjectName("Vcso3")
        self.ModBias = QtWidgets.QCheckBox(Dialog)
        self.ModBias.setGeometry(QtCore.QRect(260, 120, 101, 31))
        self.ModBias.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.ModBias.setChecked(True)
        self.ModBias.setObjectName("ModBias")
        self.DitherCorr = QtWidgets.QCheckBox(Dialog)
        self.DitherCorr.setGeometry(QtCore.QRect(740, 180, 101, 31))
        self.DitherCorr.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.DitherCorr.setChecked(True)
        self.DitherCorr.setObjectName("DitherCorr")
        self.Vadj = QtWidgets.QCheckBox(Dialog)
        self.Vadj.setGeometry(QtCore.QRect(620, 180, 91, 31))
        self.Vadj.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.Vadj.setChecked(True)
        self.Vadj.setObjectName("Vadj")
        self.TpTiltAdj = QtWidgets.QCheckBox(Dialog)
        self.TpTiltAdj.setGeometry(QtCore.QRect(380, 180, 91, 31))
        self.TpTiltAdj.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.TpTiltAdj.setChecked(True)
        self.TpTiltAdj.setObjectName("TpTiltAdj")
        self.RlsrBias = QtWidgets.QCheckBox(Dialog)
        self.RlsrBias.setGeometry(QtCore.QRect(140, 180, 91, 31))
        self.RlsrBias.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.RlsrBias.setChecked(True)
        self.RlsrBias.setObjectName("RlsrBias")
        self.FlsrBias = QtWidgets.QCheckBox(Dialog)
        self.FlsrBias.setGeometry(QtCore.QRect(20, 180, 101, 31))
        self.FlsrBias.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.FlsrBias.setChecked(True)
        self.FlsrBias.setObjectName("FlsrBias")
        self.PeakAdjTp = QtWidgets.QCheckBox(Dialog)
        self.PeakAdjTp.setGeometry(QtCore.QRect(500, 180, 101, 31))
        self.PeakAdjTp.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.PeakAdjTp.setChecked(True)
        self.PeakAdjTp.setObjectName("PeakAdjTp")
        self.Res2 = QtWidgets.QCheckBox(Dialog)
        self.Res2.setGeometry(QtCore.QRect(860, 180, 91, 31))
        self.Res2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.Res2.setChecked(True)
        self.Res2.setObjectName("Res2")
        self.LsrTemp = QtWidgets.QCheckBox(Dialog)
        self.LsrTemp.setGeometry(QtCore.QRect(260, 180, 101, 31))
        self.LsrTemp.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.LsrTemp.setChecked(True)
        self.LsrTemp.setObjectName("LsrTemp")
        self.closeBu = QtWidgets.QPushButton(Dialog)
        self.closeBu.setGeometry(QtCore.QRect(790, 270, 111, 31))
        self.closeBu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.closeBu.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.closeBu.setObjectName("closeBu")
        self.enableAllBu = QtWidgets.QPushButton(Dialog)
        self.enableAllBu.setGeometry(QtCore.QRect(30, 270, 111, 31))
        self.enableAllBu.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.enableAllBu.setObjectName("enableAllBu")
        self.disableAllBu = QtWidgets.QPushButton(Dialog)
        self.disableAllBu.setGeometry(QtCore.QRect(160, 270, 111, 31))
        self.disableAllBu.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.disableAllBu.setObjectName("disableAllBu")
        self.getFromBoardBu = QtWidgets.QPushButton(Dialog)
        self.getFromBoardBu.setGeometry(QtCore.QRect(430, 270, 111, 31))
        self.getFromBoardBu.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.getFromBoardBu.setObjectName("getFromBoardBu")

        self.retranslateUi(Dialog)
        self.closeBu.clicked.connect(Dialog.close)
        self.closeBu.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TC Enable"))
        self.Attn.setText(_translate("Dialog", "Attn"))
        self.saveToBoardBu.setText(_translate("Dialog", "Save to Board"))
        self.label.setText(_translate("Dialog", "TC Enable"))
        self.MpTiltAdj.setText(_translate("Dialog", "MpTiltAdj"))
        self.Vamp.setText(_translate("Dialog", "Vamp"))
        self.PeakAdjMp.setText(_translate("Dialog", "PeakAdjMp"))
        self.Res1.setText(_translate("Dialog", "Res"))
        self.VSbs.setText(_translate("Dialog", "VSbs"))
        self.TpAttn.setText(_translate("Dialog", "TpAttn"))
        self.Vxt.setText(_translate("Dialog", "Vxt"))
        self.Vclamp.setText(_translate("Dialog", "Vclamp"))
        self.Vcso4.setText(_translate("Dialog", "Vcso4"))
        self.Vctb.setText(_translate("Dialog", "Vctb"))
        self.Vxmod.setText(_translate("Dialog", "Vxmod"))
        self.Vcso2.setText(_translate("Dialog", "Vcso2"))
        self.Vctb3.setText(_translate("Dialog", "Vctb3"))
        self.Vcso3.setText(_translate("Dialog", "Vcso3"))
        self.ModBias.setText(_translate("Dialog", "ModBias"))
        self.DitherCorr.setText(_translate("Dialog", "DitherCorr"))
        self.Vadj.setText(_translate("Dialog", "Vadj"))
        self.TpTiltAdj.setText(_translate("Dialog", "TpTiltAdj"))
        self.RlsrBias.setText(_translate("Dialog", "RlsrBias"))
        self.FlsrBias.setText(_translate("Dialog", "FlsrBias"))
        self.PeakAdjTp.setText(_translate("Dialog", "PeakAdjTp"))
        self.Res2.setText(_translate("Dialog", "Res"))
        self.LsrTemp.setText(_translate("Dialog", "LsrTemp"))
        self.closeBu.setText(_translate("Dialog", "EXIT"))
        self.enableAllBu.setText(_translate("Dialog", "Enable All"))
        self.disableAllBu.setText(_translate("Dialog", "Disable All"))
        self.getFromBoardBu.setText(_translate("Dialog", "Get fromBoard"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

