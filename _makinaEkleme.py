# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_makinaekleme.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget_makinaEkle(object):
    def setupUi(self, widget_makinaEkle):
        widget_makinaEkle.setObjectName("widget_makinaEkle")
        widget_makinaEkle.resize(642, 367)

        widget_makinaEkle.setFixedSize(642, 367)

        self.ln_makinaAd = QtWidgets.QLineEdit(widget_makinaEkle)
        self.ln_makinaAd.setGeometry(QtCore.QRect(130, 110, 131, 31))
        self.ln_makinaAd.setObjectName("ln_makinaAd")
        self.lbl_makinaUretimtarihi = QtWidgets.QLabel(widget_makinaEkle)
        self.lbl_makinaUretimtarihi.setGeometry(QtCore.QRect(130, 170, 111, 31))
        self.lbl_makinaUretimtarihi.setObjectName("lbl_makinaUretimtarihi")
        self.ln_gun = QtWidgets.QLineEdit(widget_makinaEkle)
        self.ln_gun.setGeometry(QtCore.QRect(260, 170, 41, 31))
        self.ln_gun.setText("")
        self.ln_gun.setObjectName("ln_gun")
        self.ln_makinaSeriNum = QtWidgets.QLineEdit(widget_makinaEkle)
        self.ln_makinaSeriNum.setGeometry(QtCore.QRect(370, 110, 131, 31))
        self.ln_makinaSeriNum.setObjectName("ln_makinaSeriNum")
        self.lbl_makinaEklemeTalimatlar = QtWidgets.QLabel(widget_makinaEkle)
        self.lbl_makinaEklemeTalimatlar.setGeometry(QtCore.QRect(30, 280, 581, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_makinaEklemeTalimatlar.setFont(font)
        self.lbl_makinaEklemeTalimatlar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_makinaEklemeTalimatlar.setText("")
        self.lbl_makinaEklemeTalimatlar.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_makinaEklemeTalimatlar.setObjectName("lbl_makinaEklemeTalimatlar")
        self.btnSave = QtWidgets.QPushButton(widget_makinaEkle)
        self.btnSave.setGeometry(QtCore.QRect(250, 230, 131, 31))
        self.btnSave.setObjectName("btnSave")
        self.ln_yil = QtWidgets.QLineEdit(widget_makinaEkle)
        self.ln_yil.setGeometry(QtCore.QRect(380, 170, 41, 31))
        self.ln_yil.setText("")
        self.ln_yil.setObjectName("ln_yil")
        self.ln_ay = QtWidgets.QLineEdit(widget_makinaEkle)
        self.ln_ay.setGeometry(QtCore.QRect(320, 170, 41, 31))
        self.ln_ay.setText("")
        self.ln_ay.setObjectName("ln_ay")
        self.comboBox_musteriler = QtWidgets.QComboBox(widget_makinaEkle)
        self.comboBox_musteriler.setGeometry(QtCore.QRect(130, 20, 171, 31))
        self.comboBox_musteriler.setObjectName("comboBox_musteriler")
        self.btnMusteriSec = QtWidgets.QPushButton(widget_makinaEkle)
        self.btnMusteriSec.setGeometry(QtCore.QRect(340, 20, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnMusteriSec.setFont(font)
        self.btnMusteriSec.setAutoFillBackground(False)
        self.btnMusteriSec.setObjectName("btnMusteriSec")

        self.retranslateUi(widget_makinaEkle)
        QtCore.QMetaObject.connectSlotsByName(widget_makinaEkle)

    def retranslateUi(self, widget_makinaEkle):
        _translate = QtCore.QCoreApplication.translate
        widget_makinaEkle.setWindowTitle(_translate("widget_makinaEkle", "Form"))
        self.lbl_makinaUretimtarihi.setText(_translate("widget_makinaEkle", "Makina Üretim Tarihi:"))
        self.btnSave.setText(_translate("widget_makinaEkle", "Kaydet"))
        self.btnMusteriSec.setText(_translate("widget_makinaEkle", "Seçim"))
