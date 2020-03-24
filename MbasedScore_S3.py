from PyQt5.QtWidgets import QListView, QFileDialog
from PyQt5 import QtWidgets
import openpyxl

import ScorePanel
import FilePool

from Ui.MbasedScore_S3_Ui import Ui_Dialog

class MbasedScore_S3(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self,cname,stype,percent):
        super(MbasedScore_S3, self).__init__()
        self.setupUi(self)
        course_code, course_title,course_session = cname.split("#")
        self.label_2.setText(course_title+" ( "+course_session+" ) ")
        self.setWindowTitle("Import Matrix based Score - Step 3")
        self.label_3.setText(stype)
        self.lineEdit.setText(percent)
        self.commandLinkButton.clicked.connect(lambda :self.rtn_to_score_panel(cname))
        self.pushButton_2.clicked.connect(lambda:self.imprtRawScore(cname))



    def rtn_to_score_panel(self,cname):
        self.hide()
        self.s = ScorePanel.ScorePanel(cname)
        self.s.show()


    def imprtRawScore(self,cname):
        filePath,suffix = QFileDialog.getOpenFileName(self, "Import Raw Score xlsx File", "", "Excel file (*.xlsx)")
        if not filePath =="":
            self.label_5.setText(filePath)
            wbFormulas = openpyxl.load_workbook(filePath)
            wbFormulas.save("./Raw Score Files/"+cname+'Raw Score'+'xlsx')

