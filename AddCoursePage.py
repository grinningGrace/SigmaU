import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import MainPage
from PyQt5 import QtCore, QtGui, QtWidgets

from AddCoursePageUi import Ui_Dialog

class AddCoursePage(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        super(AddCoursePage, self).__init__()
        # self.init_ui(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.course_add_btn_clicked)

    def course_add_btn_clicked(self):
        pass
