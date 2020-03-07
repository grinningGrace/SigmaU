from PyQt5 import QtWidgets
import AlertInfo
from Ui.RegisterUi import Ui_Dialog

class Register(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(Register, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_btn_click)


    def on_btn_click(self):
        self.s = AlertInfo.AlertInfo(self)
        self.s.set_label1_msg("Hi, Grace!")
        self.s.set_label2_msg("Welcome to SigmaU!")
        self.s.show()


    def get_class_name(self):
        return self.__class__.__name__


