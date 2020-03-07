# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddCoursePageUi.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 640)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 271, 61))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(190, 80, 231, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 60, 347, 78))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 120, 347, 78))
        self.label_4.setObjectName("label_4")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(190, 140, 231, 31))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(190, 200, 231, 31))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 180, 347, 78))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(60, 240, 347, 78))
        self.label_6.setObjectName("label_6")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(190, 260, 231, 31))
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(60, 300, 347, 78))
        self.label_7.setObjectName("label_7")
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(190, 320, 231, 31))
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_7.setGeometry(QtCore.QRect(190, 380, 231, 31))
        self.plainTextEdit_7.setObjectName("plainTextEdit_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(60, 360, 347, 78))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(60, 420, 347, 78))
        self.label_9.setObjectName("label_9")
        self.plainTextEdit_8 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_8.setGeometry(QtCore.QRect(190, 440, 231, 31))
        self.plainTextEdit_8.setObjectName("plainTextEdit_8")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 520, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 520, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Please input the following information"))
        self.label.setText(_translate("Dialog", "Course Title:"))
        self.label_4.setText(_translate("Dialog", "Course Code:"))
        self.label_5.setText(_translate("Dialog", "Session No."))
        self.label_6.setText(_translate("Dialog", "Semester"))
        self.label_7.setText(_translate("Dialog", "Course  Instructor:"))
        self.label_8.setText(_translate("Dialog", "Course  Convenor:"))
        self.label_9.setText(_translate("Dialog", "Assistant Instructor"))
        self.pushButton.setText(_translate("Dialog", "Add"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
