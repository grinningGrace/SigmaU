# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MbasedScore_S2_Ui.ui'
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
        self.label.setGeometry(QtCore.QRect(20, 120, 231, 41))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 180, 351, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 270, 351, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 350, 141, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 400, 60, 16))
        self.label_3.setObjectName("label_3")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(330, 600, 151, 41))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.label_courseName = QtWidgets.QLabel(Dialog)
        self.label_courseName.setGeometry(QtCore.QRect(20, 70, 111, 21))
        self.label_courseName.setObjectName("label_courseName")
        self.label_scoreFileType = QtWidgets.QLabel(Dialog)
        self.label_scoreFileType.setGeometry(QtCore.QRect(20, 90, 451, 31))
        self.label_scoreFileType.setObjectName("label_scoreFileType")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 10, 81, 51))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Step 2. Setup settings"))
        self.pushButton.setText(_translate("Dialog", "Export Example Matrix"))
        self.pushButton_2.setText(_translate("Dialog", "Import Matrix File"))
        self.label_2.setText(_translate("Dialog", "Matrix Path:"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.commandLinkButton_3.setText(_translate("Dialog", "Next Step"))
        self.label_courseName.setText(_translate("Dialog", "Course Name"))
        self.label_scoreFileType.setText(_translate("Dialog", "Score File Type"))
        self.pushButton_3.setText(_translate("Dialog", "Go back"))
