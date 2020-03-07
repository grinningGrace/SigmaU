import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import CoursePage
import Register
from PyQt5 import QtCore, QtGui, QtWidgets
from ScorePanelUi import Ui_Dialog
import FilePool
import CoursePanel

class ScorePanel(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self,cname):
        super(ScorePanel, self).__init__()
        self.setupUi(self)
        self.label.setText(cname)
        self.pushButton_3.clicked.connect(lambda: self.callFilePool(cname))
        self.pushButton_4.clicked.connect(lambda : self.goback(cname))


    def callFilePool(self,cname):
        self.hide()
        self.s = FilePool.FilePool(cname)

        self.s.show()


    def goback(self,cname):
        self.hide()
        self.s = CoursePanel.CoursePanel(cname)
        self.s.show()
