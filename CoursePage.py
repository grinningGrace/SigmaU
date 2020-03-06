import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import MainPage
import deleteCoursePage
from PyQt5 import QtCore, QtGui, QtWidgets
from CourseaPageUi import Ui_Dialog
import AddCoursePage
import MainPage
class CoursePage(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        super(CoursePage, self).__init__()
        # self.init_ui(self)
        self.setupUi(self)
        self.addCourse.clicked.connect(self.addCourse_btn_click)
        self.deleteCourse.clicked.connect(self.deleteCourse_btn_click)
        self.logOut.clicked.connect(self.logOut_btn_click)


    def addCourse_btn_click(self):
        self.hide()
        self.s = AddCoursePage.AddCoursePage()
        self.s.show()


    def logOut_btn_click(self):
        self.hide()
        self.s = MainPage.MainPage()
        self.s.show()


    def deleteCourse_btn_click(self):
        self.hide()
        self.s = deleteCoursePage.deleteCousePage()
        self.s.show()