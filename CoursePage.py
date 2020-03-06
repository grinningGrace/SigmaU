import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import MainPage
from PyQt5 import QtCore, QtGui, QtWidgets
from CourseaPageUi import Ui_Dialog
class CoursePage(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        super(CoursePage, self).__init__()
        # self.init_ui(self)
        self.setupUi(self)

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



