# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MbasedScore_S3_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 640)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 70, 201, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 110, 431, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 210, 431, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 321, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 151, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 270, 141, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 320, 60, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 360, 431, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(280, 590, 193, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Step 3."))
        self.pushButton.setText(_translate("Dialog", "Generate and Export Raw Score Input Template"))
        self.pushButton_2.setText(_translate("Dialog", "Import Raw Score File"))
        self.label_2.setText(_translate("Dialog", "Course name"))
        self.label_3.setText(_translate("Dialog", "Score Type"))
        self.label_4.setText(_translate("Dialog", "Raw Score FIle Path"))
        self.label_5.setText(_translate("Dialog", "TextLabel"))
        self.pushButton_3.setText(_translate("Dialog", "View File Pool"))
        self.commandLinkButton.setText(_translate("Dialog", "Finish and go to Course Panel"))
