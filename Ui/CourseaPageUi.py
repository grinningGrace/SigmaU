# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CourseaPageUi.ui'
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
        self.label.setGeometry(QtCore.QRect(20, 60, 231, 41))
        self.label.setObjectName("label")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(20, 110, 441, 411))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.listView.setFont(font)
        self.listView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listView.setMouseTracking(True)
        self.listView.setObjectName("listView")
        self.addCourse = QtWidgets.QPushButton(Dialog)
        self.addCourse.setGeometry(QtCore.QRect(50, 580, 121, 32))
        self.addCourse.setObjectName("addCourse")
        self.deleteCourse = QtWidgets.QPushButton(Dialog)
        self.deleteCourse.setGeometry(QtCore.QRect(180, 580, 121, 32))
        self.deleteCourse.setObjectName("deleteCourse")
        self.logOut = QtWidgets.QPushButton(Dialog)
        self.logOut.setGeometry(QtCore.QRect(300, 580, 121, 32))
        self.logOut.setObjectName("logOut")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 530, 271, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 181, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(200, 30, 131, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(333, 30, 121, 26))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Your courses of this semester:"))
        self.addCourse.setText(_translate("Dialog", "Add a Course"))
        self.deleteCourse.setText(_translate("Dialog", "Delete a Course"))
        self.logOut.setText(_translate("Dialog", "Log out"))
        self.label_2.setText(_translate("Dialog", "You have 7 courses in total"))
        self.label_3.setText(_translate("Dialog", "Select Year and Semester"))
        self.comboBox.setItemText(0, _translate("Dialog", "2019-2020"))
        self.comboBox.setItemText(1, _translate("Dialog", "2020-2021"))
        self.comboBox.setItemText(2, _translate("Dialog", "2021-2022"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Semester 1"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Semester 2"))
