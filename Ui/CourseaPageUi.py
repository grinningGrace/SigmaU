# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CourseaPageUi.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import qtawesome

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 640)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 50, 141, 41))
        self.label.setObjectName("label")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(30, 110, 271, 461))
        self.listView.setObjectName("listView")
        self.addCourse = QtWidgets.QPushButton(Dialog)
        self.addCourse.setGeometry(QtCore.QRect(332, 110, 121, 32))
        self.addCourse.setObjectName("addCourse")
        self.deleteCourse = QtWidgets.QPushButton(Dialog)
        self.deleteCourse.setGeometry(QtCore.QRect(332, 150, 121, 32))
        self.deleteCourse.setObjectName("deleteCourse")
        self.logOut = QtWidgets.QPushButton(Dialog)
        self.logOut.setGeometry(QtCore.QRect(332, 190, 121, 32))
        self.logOut.setObjectName("logOut")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 590, 271, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)





    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Your courses"))
        self.addCourse.setText(_translate("Dialog", "Add a Course"))
        self.deleteCourse.setText(_translate("Dialog", "Delete a Course"))
        self.logOut.setText(_translate("Dialog", "Log out"))
        self.label_2.setText(_translate("Dialog", "You have 7 courses in total"))
