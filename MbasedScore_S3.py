from PyQt5.QtWidgets import QListView, QFileDialog
from PyQt5 import QtWidgets

from Ui.MbasedScore_S3_Ui import Ui_Dialog

class MbasedScore_S3(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self,cname,stype,percent):
        super(MbasedScore_S3, self).__init__()
        self.setupUi(self)
        self.label_2.setText(cname)
        self.label_3.setText(stype)
        self.lineEdit.setText(percent)


