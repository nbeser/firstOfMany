# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_silmek.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Silmek(object):
    def setupUi(self, Silmek):
        Silmek.setObjectName("Silmek")
        Silmek.resize(549, 370)

        Silmek.setFixedSize(549,370)

        self.lblSilmek = QtWidgets.QLabel(Silmek)
        self.lblSilmek.setGeometry(QtCore.QRect(40, 40, 101, 41))
        self.lblSilmek.setObjectName("lblSilmek")
        self.cmbSilmek1 = QtWidgets.QComboBox(Silmek)
        self.cmbSilmek1.setGeometry(QtCore.QRect(160, 40, 341, 41))
        self.cmbSilmek1.setObjectName("cmbSilmek1")
        self.btnSecimSil = QtWidgets.QPushButton(Silmek)
        self.btnSecimSil.setGeometry(QtCore.QRect(220, 90, 111, 31))
        self.btnSecimSil.setObjectName("btnSecimSil")
        self.btnSil = QtWidgets.QPushButton(Silmek)
        self.btnSil.setGeometry(QtCore.QRect(180, 210, 221, 41))
        self.btnSil.setObjectName("btnSil")
        self.cmbSilmek2 = QtWidgets.QComboBox(Silmek)
        self.cmbSilmek2.setGeometry(QtCore.QRect(40, 150, 461, 31))
        self.cmbSilmek2.setObjectName("cmbSilmek2")
        self.lblTalimat = QtWidgets.QLabel(Silmek)
        self.lblTalimat.setGeometry(QtCore.QRect(40, 300, 481, 41))
        self.lblTalimat.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTalimat.setObjectName("lblTalimat")

        self.retranslateUi(Silmek)
        QtCore.QMetaObject.connectSlotsByName(Silmek)

    def retranslateUi(self, Silmek):
        _translate = QtCore.QCoreApplication.translate
        Silmek.setWindowTitle(_translate("Silmek", "Form"))
        self.lblSilmek.setText(_translate("Silmek", "TextLabel"))
        self.btnSecimSil.setText(_translate("Silmek", "Seç"))
        self.btnSil.setText(_translate("Silmek", "Sil"))
        self.lblTalimat.setText(_translate("Silmek", "<html><head/><body><p align=\"center\">TextLabel</p></body></html>"))
