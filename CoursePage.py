import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import MainPage
from PyQt5 import QtCore, QtGui, QtWidgets
class CoursePage(QMainWindow):
    def __init__(self):
        super(CoursePage, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(300, 200)
        self.setWindowTitle('course Page')
        self.btn = QPushButton('jump', self)
        self.btn.setGeometry(50, 100, 100, 50)
        self.btn.clicked.connect(self.slot_btn_function)

    def slot_btn_function(self):
        self.hide()
        self.s = MainPage.MainPage()
        self.s.show()



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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Your courses"))
        self.addCourse.setText(_translate("Dialog", "Add a Course"))
        self.deleteCourse.setText(_translate("Dialog", "Delete a Course"))
