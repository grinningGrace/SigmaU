import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import CoursePage
import Register
from PyQt5 import QtCore, QtGui, QtWidgets
from FilePoolUi import Ui_Dialog

class FilePool(QtWidgets.QDialog, Ui_Dialog ):
    def __init__(self):
        super(FilePool, self).__init__()
        self.setupUi(self)