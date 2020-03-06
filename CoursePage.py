import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import MainPage
from PyQt5 import QtCore, QtGui, QtWidgets
from CourseaPageUi import Ui_Dialog
import AddCoursePage
class CoursePage(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        super(CoursePage, self).__init__()
        # self.init_ui(self)
        self.setupUi(self)
        self.addCourse.clicked.connect(self.addCourse_btn_click)


    def addCourse_btn_click(self):
        self.hide()
        self.s = AddCoursePage.AddCoursePage()
        self.s.show()



