# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_analizEkleme.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnalizEkleme(object):
    def setupUi(self, AnalizEkleme):
        AnalizEkleme.setObjectName("AnalizEkleme")
        AnalizEkleme.resize(796, 668)

        AnalizEkleme.setFixedSize(796,668)

        self.lbl_talimat = QtWidgets.QLabel(AnalizEkleme)
        self.lbl_talimat.setGeometry(QtCore.QRect(100, 570, 601, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_talimat.setFont(font)
        self.lbl_talimat.setScaledContents(False)
        self.lbl_talimat.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_talimat.setObjectName("lbl_talimat")
        self.ln_degerGiris = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris.setGeometry(QtCore.QRect(30, 150, 61, 31))
        self.ln_degerGiris.setText("")
        self.ln_degerGiris.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris.setObjectName("ln_degerGiris")
        self.groupBox = QtWidgets.QGroupBox(AnalizEkleme)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 741, 121))
        self.groupBox.setObjectName("groupBox")
        self.cmbBoxMakina = QtWidgets.QComboBox(self.groupBox)
        self.cmbBoxMakina.setGeometry(QtCore.QRect(140, 60, 441, 22))
        self.cmbBoxMakina.setObjectName("cmbBoxMakina")
        self.lbl_makina = QtWidgets.QLabel(self.groupBox)
        self.lbl_makina.setGeometry(QtCore.QRect(30, 60, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_makina.setFont(font)
        self.lbl_makina.setObjectName("lbl_makina")
        self.lbl_musteri = QtWidgets.QLabel(self.groupBox)
        self.lbl_musteri.setGeometry(QtCore.QRect(30, 30, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_musteri.setFont(font)
        self.lbl_musteri.setLineWidth(1)
        self.lbl_musteri.setTextFormat(QtCore.Qt.MarkdownText)
        self.lbl_musteri.setObjectName("lbl_musteri")
        self.cmbBoxMusteri = QtWidgets.QComboBox(self.groupBox)
        self.cmbBoxMusteri.setGeometry(QtCore.QRect(140, 30, 441, 22))
        self.cmbBoxMusteri.setObjectName("cmbBoxMusteri")
        self.btnSecimMusteri = QtWidgets.QPushButton(self.groupBox)
        self.btnSecimMusteri.setGeometry(QtCore.QRect(610, 30, 75, 23))
        self.btnSecimMusteri.setObjectName("btnSecimMusteri")
        self.btnSecimMakina = QtWidgets.QPushButton(self.groupBox)
        self.btnSecimMakina.setGeometry(QtCore.QRect(610, 60, 75, 23))
        self.btnSecimMakina.setObjectName("btnSecimMakina")
        self.btnEkle = QtWidgets.QPushButton(AnalizEkleme)
        self.btnEkle.setGeometry(QtCore.QRect(110, 510, 171, 31))
        self.btnEkle.setAutoFillBackground(True)
        self.btnEkle.setObjectName("btnEkle")
        self.btnKaydet = QtWidgets.QPushButton(AnalizEkleme)
        self.btnKaydet.setGeometry(QtCore.QRect(310, 510, 171, 31))
        self.btnKaydet.setObjectName("btnKaydet")
        self.ln_degerGiris_2 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_2.setGeometry(QtCore.QRect(110, 150, 61, 31))
        self.ln_degerGiris_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_2.setObjectName("ln_degerGiris_2")
        self.ln_degerGiris_3 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_3.setGeometry(QtCore.QRect(190, 150, 121, 31))
        self.ln_degerGiris_3.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_3.setObjectName("ln_degerGiris_3")
        self.ln_degerGiris_4 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_4.setGeometry(QtCore.QRect(330, 150, 131, 31))
        self.ln_degerGiris_4.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_4.setObjectName("ln_degerGiris_4")
        self.ln_degerGiris_5 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_5.setGeometry(QtCore.QRect(480, 150, 131, 31))
        self.ln_degerGiris_5.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_5.setObjectName("ln_degerGiris_5")
        self.ln_degerGiris_6 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_6.setGeometry(QtCore.QRect(630, 150, 131, 31))
        self.ln_degerGiris_6.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_6.setObjectName("ln_degerGiris_6")
        self.ln_degerGiris_7 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_7.setGeometry(QtCore.QRect(30, 200, 131, 31))
        self.ln_degerGiris_7.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_7.setObjectName("ln_degerGiris_7")
        self.ln_degerGiris_8 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_8.setGeometry(QtCore.QRect(180, 200, 131, 31))
        self.ln_degerGiris_8.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_8.setObjectName("ln_degerGiris_8")
        self.ln_degerGiris_9 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_9.setGeometry(QtCore.QRect(330, 200, 131, 31))
        self.ln_degerGiris_9.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_9.setObjectName("ln_degerGiris_9")
        self.ln_degerGiris_10 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_10.setGeometry(QtCore.QRect(480, 200, 131, 31))
        self.ln_degerGiris_10.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_10.setObjectName("ln_degerGiris_10")
        self.ln_degerGiris_11 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_11.setGeometry(QtCore.QRect(630, 200, 131, 31))
        self.ln_degerGiris_11.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_11.setObjectName("ln_degerGiris_11")
        self.ln_degerGiris_12 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_12.setGeometry(QtCore.QRect(30, 250, 131, 31))
        self.ln_degerGiris_12.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_12.setObjectName("ln_degerGiris_12")
        self.ln_degerGiris_13 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_13.setGeometry(QtCore.QRect(180, 250, 131, 31))
        self.ln_degerGiris_13.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_13.setObjectName("ln_degerGiris_13")
        self.ln_degerGiris_14 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_14.setGeometry(QtCore.QRect(330, 250, 131, 31))
        self.ln_degerGiris_14.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_14.setObjectName("ln_degerGiris_14")
        self.ln_degerGiris_15 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_15.setGeometry(QtCore.QRect(480, 250, 131, 31))
        self.ln_degerGiris_15.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_15.setObjectName("ln_degerGiris_15")
        self.ln_degerGiris_16 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_16.setGeometry(QtCore.QRect(630, 250, 131, 31))
        self.ln_degerGiris_16.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_16.setObjectName("ln_degerGiris_16")
        self.ln_degerGiris_17 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_17.setGeometry(QtCore.QRect(30, 300, 131, 31))
        self.ln_degerGiris_17.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_17.setObjectName("ln_degerGiris_17")
        self.ln_degerGiris_18 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_18.setGeometry(QtCore.QRect(180, 300, 131, 31))
        self.ln_degerGiris_18.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_18.setObjectName("ln_degerGiris_18")
        self.ln_degerGiris_19 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_19.setGeometry(QtCore.QRect(330, 300, 131, 31))
        self.ln_degerGiris_19.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_19.setObjectName("ln_degerGiris_19")
        self.ln_degerGiris_20 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_20.setGeometry(QtCore.QRect(480, 300, 131, 31))
        self.ln_degerGiris_20.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_20.setObjectName("ln_degerGiris_20")
        self.ln_degerGiris_21 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_21.setGeometry(QtCore.QRect(630, 300, 131, 31))
        self.ln_degerGiris_21.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_21.setObjectName("ln_degerGiris_21")
        self.ln_degerGiris_22 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_22.setGeometry(QtCore.QRect(30, 350, 131, 31))
        self.ln_degerGiris_22.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_22.setObjectName("ln_degerGiris_22")
        self.ln_degerGiris_23 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_23.setGeometry(QtCore.QRect(180, 350, 131, 31))
        self.ln_degerGiris_23.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_23.setObjectName("ln_degerGiris_23")
        self.ln_degerGiris_24 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_24.setGeometry(QtCore.QRect(330, 350, 131, 31))
        self.ln_degerGiris_24.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_24.setObjectName("ln_degerGiris_24")
        self.ln_degerGiris_25 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_25.setGeometry(QtCore.QRect(480, 350, 131, 31))
        self.ln_degerGiris_25.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_25.setObjectName("ln_degerGiris_25")
        self.ln_degerGiris_26 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_26.setGeometry(QtCore.QRect(630, 350, 131, 31))
        self.ln_degerGiris_26.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_26.setObjectName("ln_degerGiris_26")
        self.ln_degerGiris_27 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_27.setGeometry(QtCore.QRect(30, 400, 131, 31))
        self.ln_degerGiris_27.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_27.setObjectName("ln_degerGiris_27")
        self.ln_degerGiris_28 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_28.setGeometry(QtCore.QRect(180, 400, 131, 31))
        self.ln_degerGiris_28.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_28.setObjectName("ln_degerGiris_28")
        self.ln_degerGiris_29 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_29.setGeometry(QtCore.QRect(330, 400, 131, 31))
        self.ln_degerGiris_29.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_29.setObjectName("ln_degerGiris_29")
        self.ln_degerGiris_30 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_30.setGeometry(QtCore.QRect(480, 400, 131, 31))
        self.ln_degerGiris_30.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_30.setObjectName("ln_degerGiris_30")
        self.ln_degerGiris_31 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_31.setGeometry(QtCore.QRect(630, 400, 131, 31))
        self.ln_degerGiris_31.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_31.setObjectName("ln_degerGiris_31")
        self.btnIptal = QtWidgets.QPushButton(AnalizEkleme)
        self.btnIptal.setGeometry(QtCore.QRect(510, 510, 171, 31))
        self.btnIptal.setObjectName("btnIptal")
        self.ln_degerGiris_32 = QtWidgets.QLineEdit(AnalizEkleme)
        self.ln_degerGiris_32.setGeometry(QtCore.QRect(330, 450, 131, 31))
        self.ln_degerGiris_32.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_degerGiris_32.setObjectName("ln_degerGiris_32")

        self.retranslateUi(AnalizEkleme)
        QtCore.QMetaObject.connectSlotsByName(AnalizEkleme)

    def retranslateUi(self, AnalizEkleme):
        _translate = QtCore.QCoreApplication.translate
        AnalizEkleme.setWindowTitle(_translate("AnalizEkleme", "Form"))
        self.lbl_talimat.setText(_translate("AnalizEkleme", "Talimatlar"))
        self.groupBox.setTitle(_translate("AnalizEkleme", "Müşteriler ve Makinalar"))
        self.lbl_makina.setText(_translate("AnalizEkleme", "Makina:"))
        self.lbl_musteri.setText(_translate("AnalizEkleme", "Müşteri:"))
        self.btnSecimMusteri.setText(_translate("AnalizEkleme", "Müşteri"))
        self.btnSecimMakina.setText(_translate("AnalizEkleme", "Makina"))
        self.btnEkle.setText(_translate("AnalizEkleme", "Ekle"))
        self.btnKaydet.setText(_translate("AnalizEkleme", "Analizleri kaydet"))
        self.btnIptal.setText(_translate("AnalizEkleme", "İptal"))
