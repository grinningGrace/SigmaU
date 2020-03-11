from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QListView
import deleteCoursePage
from PyQt5 import QtWidgets
import MbasedScore_S2
import ScorePanel
import re

from Ui.MbasedScore_S1_Ui import Ui_Dialog

class MbasedScore_S1(QtWidgets.QDialog,Ui_Dialog):
    _stype1 = ""
    _stype2 = ""
    _isSubtype = False
    _subtypeName = ""
    _stype=""
    _percent = 0
    _isMbased = True
    def __init__(self, cname):
        super(MbasedScore_S1, self).__init__()
        self.setupUi(self)



        if self.comboBox_3.currentText() =="Yes":
            self.label_7.setVisible(False)
            self.label_8.setVisible(False)
            self.label_9.setVisible(False)
            self.label_2.setVisible(False)
            self.label_10.setVisible(False)

            self.lineEdit.setVisible(False)
            self.lineEdit_3.setVisible(False)

        self._stype1 = self.comboBox.currentText()
        self._stype2 = ""
        self._subtypeName = ""


        self.comboBox_2.addItem("Mid-term test")
        self.comboBox_2.addItem("Group Project")
        course_code, course_title,course_session = cname.split("#")


        self.lineEdit_2.setText(course_title)
        self.lineEdit_ccode.setText(course_code)
        self.lineEdit_sno.setText(course_session)
        self.comboBox_3.activated.connect(self.combox3_choose)

        self.comboBox.activated.connect(self.comboBox_act)

        self.comboBox_2.activated.connect(self.comboBox_2_act)
        self.setWindowTitle("Import Matrix based Score - Step 1")
        self.lineEdit.textChanged.connect(self.setPercentChange)
        self.lineEdit_3.textChanged.connect(self.setSubTypeName)



        self.commandLinkButton.clicked.connect(lambda :self.toMbasedScore_S2(cname,self._stype, str(self._percent)))
        self.pushButton.clicked.connect(lambda :self.goback(cname))





    def toMbasedScore_S2(self,cname,stype, percent):

        if self.comboBox_2.isVisible()==True and self.comboBox_2.currentText()=="default value":
            msg_box = QtWidgets.QMessageBox()
            msg_box.information(self,"Alert Message","Please choose the sub-type of Continuous Assessment")

        elif self.comboBox_3.currentText()=="No" and self.comboBox_3.isVisible()==True:
            if self.lineEdit_3.text()=="":
                msg_box = QtWidgets.QMessageBox()
                msg_box.information(self,"Alert Message","Please name your score sub-type")


            elif self.lineEdit.text()=="":
                msg_box = QtWidgets.QMessageBox()
                msg_box.information(self,"Alert Message","Please set the percentage!")


            else:
                self.hide()
                self.s = MbasedScore_S2.MbasedScore_S2(cname,stype, percent)
                self.s.show()



        else:
                self.hide()
                self.s = MbasedScore_S2.MbasedScore_S2(cname,stype, percent)
                self.s.show()





    def combox3_choose(self):

        if self.comboBox_3.currentText()== "Yes":
            self.label_7.setVisible(False)
            self.label_8.setVisible(False)
            self.label_9.setVisible(False)
            self.lineEdit.setVisible(False)
            self.label_2.setVisible(False)
            self.label_10.setVisible(False)
            self.lineEdit_3.setVisible(False)
            self._isSubtype = False


        elif self.comboBox_3.currentText()=="No":
            # self.label_7.setVisible(True)
            self.label_8.setVisible(True)
            self.label_9.setVisible(True)
            self.lineEdit.setVisible(True)
            self.label_2.setVisible(True)
            self.label_10.setVisible(True)
            self.lineEdit_3.setVisible(True)
            self._isSubtype = True
            # print("No")



    def goback(self,cname):
        self.hide()
        self.s = ScorePanel.ScorePanel(cname)
        self.s.show()

    def comboBox_act(self):
        self._stype1=""
        self._stype2=""
        self._isSubtype = False
        if self.comboBox.currentText()=="Final Exam Score File":
            self.comboBox_2.setVisible(False)
            self.comboBox_3.setVisible(False)
            self.label_6.setVisible(False)
            self.label_2.setVisible(False)
            self.label_10.setVisible(False)
            self.lineEdit_3.setVisible(False)
            self.lineEdit.setVisible(False)
            self.label_8.setVisible(False)
            self.label_9.setVisible(False)


            self._stype1 = self.comboBox.currentText()
            self._stype = self._stype1+","+self._stype2+","+str(self._isSubtype)+","+self._subtypeName


        if self.comboBox.currentText()=="Continuous Assessment Score File":
            self.comboBox_2.setVisible(True)
            self.comboBox_3.setVisible(True)
            self.label_6.setVisible(True)
        self._stype1 = self.comboBox.currentText()
        # print("_stype:", self._stype)



    def comboBox_2_act(self):
        self._stype2 = ""
        self._stype2 = self.comboBox_2.currentText()


    def setPercentChange(self):
        self._percent = 0
        self._percent = self.lineEdit.text()

    def setSubTypeName(self):
        self._isSubtype = True
        self._subtypeName = ""
        self._subtypeName = self.lineEdit_3.text()
        self._stype = self._stype1+";"+self._stype2+";"+str(self._isSubtype)+";"+self._subtypeName
