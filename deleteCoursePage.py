import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import MainPage
from PyQt5 import QtCore, QtGui,QtWidgets

import CoursePage
from deleteCoursePageUi import Ui_Dialog

class deleteCousePage(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(deleteCousePage, self).__init__()
        self.setupUi(self)

