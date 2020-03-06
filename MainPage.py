import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import CoursePage
from PyQt5 import QtCore, QtGui, QtWidgets
from Main_page_Ui import Ui_MainWindow


class MainPage(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainPage, self).__init__(parent)
        # self.init_ui()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_btn1_click)


    def init_ui(self):
        self.resize(300, 200)
        self.setWindowTitle('Main Page')
        self.btn = QPushButton('jump', self)
        self.btn.setGeometry(50, 100, 100, 50)
        self.btn.clicked.connect(self.slot_btn_function)


    def slot_btn_function(self):
        self.hide()
        self.s = CoursePage.CoursePage()
        self.s.show()

    def on_btn1_click(self):
        self.hide()
        self.s = CoursePage. CoursePage()
        self.s.show()
