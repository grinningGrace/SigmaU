import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import CoursePage
import Register
from PyQt5 import QtCore, QtGui, QtWidgets
from Main_page_Ui import Ui_MainWindow


class MainPage(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainPage, self).__init__(parent)
        # self.init_ui()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_btn1_click)
        self.pushButton_2.clicked.connect(self.on_btn2_click)



    def on_btn1_click(self):
        self.hide()
        self.s = CoursePage. CoursePage()
        self.s.show()

    def on_btn2_click(self):
        self.hide()
        self.s = Register.Register()
        self.s.show()