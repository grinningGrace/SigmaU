from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QListView
import deleteCoursePage
from PyQt5 import QtWidgets
import MbasedScore_S2
import ScorePanel

from Ui.MbasedScore_S1_Ui import Ui_Dialog

class MbasedScore_S1(QtWidgets.QDialog,Ui_Dialog):
    _stype = ""
    _percent = 0
    def __init__(self, cname):
        super(MbasedScore_S1, self).__init__()
        self.setupUi(self)
        self.label_cname.setText(cname)
        stype = self.comboBox.currentText()+","+self.comboBox.currentText()
        percent = 0
        if self.comboBox_3.currentText() =="Yes":
            self.label_7.setVisible(False)
            self.label_8.setVisible(False)
            self.label_9.setVisible(False)

            self.plainTextEdit.setVisible(False)

        self.comboBox_3.activated.connect(self.combox3_choose)



        _stype = stype
        _percent = percent

        self.commandLinkButton.clicked.connect(lambda :self.toMbasedScore_S2(cname,stype, percent))
        self.pushButton.clicked.connect(lambda :self.goback(cname))





    def toMbasedScore_S2(self,cname,stype, percent):
        self.hide()
        self.s = MbasedScore_S2.MbasedScore_S2(cname,stype, percent)
        self.s.show()


    def combox3_choose(self):
        if self.comboBox_3.currentText()== "Yes":
            self.label_7.setVisible(False)
            self.label_8.setVisible(False)
            self.label_9.setVisible(False)
            self.plainTextEdit.setVisible(False)

            self.plainTextEdit.setVisible(False)
        elif self.comboBox_3.currentText()=="No":
            # self.label_7.setVisible(True)
            self.label_8.setVisible(True)
            self.label_9.setVisible(True)
            self.plainTextEdit.setVisible(True)
            self._percent = self.plainTextEdit.__str__



    def goback(self,cname):
        self.hide()
        self.s = ScorePanel.ScorePanel(cname)
        self.s.show()