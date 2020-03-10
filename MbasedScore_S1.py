from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QListView
import deleteCoursePage
from PyQt5 import QtWidgets
import MbasedScore_S2
import ScorePanel

from Ui.MbasedScore_S1_Ui import Ui_Dialog

class MbasedScore_S1(QtWidgets.QDialog,Ui_Dialog):
    _stype =""
    _percent = 0
    def __init__(self, cname):
        super(MbasedScore_S1, self).__init__()
        self.setupUi(self)
        self.label_cname.setText(cname)

        percent = 0
        if self.comboBox_3.currentText() =="Yes":
            self.label_7.setVisible(False)
            self.label_8.setVisible(False)
            self.label_9.setVisible(False)

            self.plainTextEdit.setVisible(False)
        self._stype = self.comboBox.currentText()+","+self.comboBox_2.currentText()

        self.comboBox_3.activated.connect(self.combox3_choose)

        self.comboBox.activated.connect(self.comboBox_act)

        self.comboBox_2.activated.connect(self.comboBox_2_act)



        percent = self._percent



        self.commandLinkButton.clicked.connect(lambda :self.toMbasedScore_S2(cname,self._stype, percent))
        self.pushButton.clicked.connect(lambda :self.goback(cname))





    def toMbasedScore_S2(self,cname,stype, percent):
        self.hide()
        self.s = MbasedScore_S2.MbasedScore_S2(cname,stype, percent)
        stype = self.comboBox.currentText()+","+self.comboBox_2.currentText()
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


    def comboBox_act(self):
        self._stype=""
        if self.comboBox.currentText()=="Final Exam Score File":
            self.comboBox_2.setVisible(False)

        if self.comboBox.currentText()=="Continuous Assessment Score File":
            self.comboBox_2.setVisible(True)
        self._stype = self.comboBox.currentText()
        print("_stype:", self._stype)



    def comboBox_2_act(self):
        self._stype = self._stype +","+self.comboBox_2.currentText()
