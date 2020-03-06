import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import MainPage
import AlertInfo
import CoursePage
from PyQt5 import QtCore, QtGui, QtWidgets

from AddCoursePageUi import Ui_Dialog

class AddCoursePage(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        super(AddCoursePage, self).__init__()
        # self.init_ui(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.course_add_btn_clicked)
        self.pushButton_2.clicked.connect(self.goback)

    def course_add_btn_clicked(self):
        self.s = AlertInfo.AlertInfo()
        self.s.setFixedSize(450,317)
        self.s.show()

    def goback(self):
        self.hide()
        self.s = CoursePage.CoursePage()
        self.s.show()