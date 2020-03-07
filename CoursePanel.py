import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import CoursePage
import Register
import CoursePanelUi
from PyQt5 import QtCore, QtGui, QtWidgets
from CoursePanelUi import Ui_Dialog

class CoursePanel(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self,cname):
        super(CoursePanel, self).__init__()

        self.setupUi(self)
        self.label.setText(cname)






