from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QListView, QFileDialog
from qtpy import QtCore
import datetime

from PyQt5 import QtWidgets

# import pandas as pd
from xlutils.copy import copy
import xlrd
import xlwt
import openpyxl
# import pyexcel as p
import ScorePanel

from Ui.MbasedScore_S2_Ui import Ui_Dialog

import MbasedScore_S3

class MbasedScore_S2(QtWidgets.QDialog,Ui_Dialog):
    _stype = ""
    _percent = 0


    def __init__(self,cname,stype,percent):
        super(MbasedScore_S2, self).__init__()
        self.setupUi(self)
        self._stype = stype
        self._percent = percent
        self.pushButton_3.clicked.connect(lambda :self.returntoScorePanel(cname))
        course_code, course_title,course_session = cname.split("#")
        self.label_courseName.setText(course_title+" ( "+course_session+" ) ")
        self.label_scoreFileType.setText(stype)
        self.pushButton.clicked.connect(self.saveMatrix)
        self.pushButton_2.clicked.connect(self.importMatrix)
        self.setWindowTitle("Import Matrix based Score - Step 2")
        self.label_3.setText("")
        self.commandLinkButton.clicked.connect(lambda:self.nextstep(cname,stype,percent))
        self.lineEdit.setText(percent)






    def returntoScorePanel(self,cname):
        self.hide()
        self.s = ScorePanel.ScorePanel(cname)
        self.s.show()


    def saveMatrix(self):
        wbFormulas = openpyxl.load_workbook('./excel file template/Matrix Template.xlsx')
        #
        filePath, suffix = QFileDialog.getSaveFileName(self, "Save File", "", "Excel file (*.xlsx)")
        print(filePath)  # 打印保存文件的全部路径（包括文件名和后缀名）
        #
        #
        if not filePath =="":
            wbFormulas.save(filePath)




        # p.save_book_as(file_name='Matrix Template.xlsx',
        #                dest_file_name=fileName)

    def importMatrix(self):
        filePath,suffix = QFileDialog.getOpenFileName(self, "Import Matrix xlsx File", "", "Excel file (*.xlsx)")
        if not filePath =="":
            self.label_3.setText(filePath)
            wbFormulas = openpyxl.load_workbook(filePath)
            dic = {"Continuous Assessment Score File":'CA',
                   "Final Exam Score File":'Final'
                   }
            is_subtype = self._stype.split("#")[2]

            score_type = ""


            if is_subtype =='False':
                score_type = dic[self._stype.split("#")[0]]


            elif is_subtype=='True':
                score_type = dic[self._stype.split(";")[0]]+"-"+self._stype.split(";")[1]+"-"+self._stype.split(";")[3]

            fileName = score_type+'.xlsx'
            wbFormulas.save("./Raw Score Files/"+fileName)




    def nextstep(self,cname,stype,percent):
        if self.label_3.text()=="":

            msg_box = QtWidgets.QMessageBox()
            msg_box.information(self,'Alert Message','please choose the matrix file path!')
        else:

            self.hide()
            self.s = MbasedScore_S3.MbasedScore_S3(cname,stype,percent)
            self.s.show()




