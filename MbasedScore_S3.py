from PyQt5.QtWidgets import QListView, QFileDialog
from PyQt5 import QtWidgets
import ScorePanel
import FilePool

from Ui.MbasedScore_S3_Ui import Ui_Dialog

class MbasedScore_S3(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self,cname,stype,percent):
        super(MbasedScore_S3, self).__init__()
        self.setupUi(self)
        self.label_2.setText(cname)
        self.label_3.setText(stype)
        self.lineEdit.setText(percent)
        self.commandLinkButton.clicked.connect(lambda :self.rtn_to_score_panel(cname))



    def rtn_to_score_panel(self,cname):
        self.hide()
        self.s = ScorePanel.ScorePanel(cname)
        self.s.show()



