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
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 231, 41))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 240, 351, 41))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 310, 351, 41))
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 390, 141, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 440, 441, 20))
        self.label_3.setObjectName("label_3")
        self.label_courseName = QtWidgets.QLabel(Dialog)
        self.label_courseName.setGeometry(QtCore.QRect(20, 110, 431, 21))
        self.label_courseName.setObjectName("label_courseName")
        self.label_scoreFileType = QtWidgets.QLabel(Dialog)
        self.label_scoreFileType.setGeometry(QtCore.QRect(20, 150, 451, 31))
        self.label_scoreFileType.setObjectName("label_scoreFileType")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 10, 161, 41))
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 180, 301, 41))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 190, 61, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(180, 570, 193, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setIconSize(QtCore.QSize(100, 100))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Step 2. Import Matrix File"))
        self.pushButton.setText(_translate("Dialog", "Export Example Matrix"))
        self.pushButton_2.setText(_translate("Dialog", "Import Matrix File"))
        self.label_2.setText(_translate("Dialog", "Matrix Path:"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.label_courseName.setText(_translate("Dialog", "Course Name"))
        self.label_scoreFileType.setText(_translate("Dialog", "Score File Type"))
        self.pushButton_3.setText(_translate("Dialog", "Return to Score Panel"))
        self.label_5.setText(_translate("Dialog", "% of the Total Score"))
        self.commandLinkButton.setText(_translate("Dialog", "Next Step"))
