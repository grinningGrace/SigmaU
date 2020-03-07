import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import CoursePage
import Register
from PyQt5 import QtCore, QtGui, QtWidgets
from ScorePanelUi import Ui_Dialog

class ScorePanel(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self,cname):
        super(ScorePanel, self).__init__()
        self.setupUi(self)
        self.label.setText(cname)
