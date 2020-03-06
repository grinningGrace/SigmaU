import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import MainPage
from PyQt5 import QtCore, QtGui, QtWidgets

from AlertInfoUi import Ui_Dialog

class AlertInfo(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        super(AlertInfo, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.confirm_return)

    def confirm_return(self):
        self.hide()
