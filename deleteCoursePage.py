import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import MainPage
import CoursePage
import AlertInfo
from PyQt5 import QtCore, QtGui,QtWidgets

import CoursePage
from deleteCoursePageUi import Ui_Dialog

class deleteCousePage(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(deleteCousePage, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.course_delete_btn_clicked)
        self.pushButton_2.clicked.connect(self.goback)


    def course_delete_btn_clicked(self):

        self.s = AlertInfo.AlertInfo(self)
        self.s.set_label_delete_msg()
        self.s.show()

    def goback(self):
        self.hide()
        self.s = CoursePage.CoursePage()
        self.s.show()


    def get_class_name(self):
        return self.__class__.__name__