# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CoursePanelUi.ui'
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
        self.label.setGeometry(QtCore.QRect(20, 10, 381, 81))
        self.label.setObjectName("label")
        self.Scores = QtWidgets.QPushButton(Dialog)
        self.Scores.setGeometry(QtCore.QRect(70, 190, 321, 41))
        self.Scores.setObjectName("Scores")
        self.CRA = QtWidgets.QPushButton(Dialog)
        self.CRA.setGeometry(QtCore.QRect(70, 240, 321, 41))
        self.CRA.setObjectName("CRA")
        self.Grade = QtWidgets.QPushButton(Dialog)
        self.Grade.setGeometry(QtCore.QRect(70, 290, 321, 41))
        self.Grade.setObjectName("Grade")
        self.Analysis = QtWidgets.QPushButton(Dialog)
        self.Analysis.setGeometry(QtCore.QRect(70, 340, 321, 41))
        self.Analysis.setObjectName("Analysis")
        self.Goback = QtWidgets.QPushButton(Dialog)
        self.Goback.setGeometry(QtCore.QRect(320, 460, 113, 32))
        self.Goback.setObjectName("Goback")
        self.NmList = QtWidgets.QPushButton(Dialog)
        self.NmList.setGeometry(QtCore.QRect(70, 140, 321, 41))
        self.NmList.setObjectName("NmList")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Strategic Management (1001)"))
        self.Scores.setText(_translate("Dialog", "Scores"))
        self.CRA.setText(_translate("Dialog", "Generate CRA Report"))
        self.Grade.setText(_translate("Dialog", "Generate Grade Report"))
        self.Analysis.setText(_translate("Dialog", "Data Analysis"))
        self.Goback.setText(_translate("Dialog", "Go back"))
        self.NmList.setText(_translate("Dialog", "Import Updated Name List"))
