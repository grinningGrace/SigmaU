from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QListView, QFileDialog
from qtpy import QtCore

import deleteCoursePage
from PyQt5 import QtWidgets

# import pandas as pd
from xlutils.copy import copy
import xlrd
import xlwt
import openpyxl
import pyexcel as p



import MbasedScore_S1

from Ui.MbasedScore_S2_Ui import Ui_Dialog

class MbasedScore_S2(QtWidgets.QDialog,Ui_Dialog):
    _stype = 0
    _percent = 0


    def __init__(self,cname,stype,percent):
        super(MbasedScore_S2, self).__init__()
        self.setupUi(self)
        self._stype = stype
        self._percent = percent
        self.pushButton_3.clicked.connect(lambda :self.goback(cname))
        self.label_courseName.setText(cname)
        self.label_scoreFileType.setText(stype)
        self.pushButton.clicked.connect(self.saveMatrix)
        self.pushButton_2.clicked.connect(self.importMatrix)



    def goback(self,cname):
        self.hide()
        self.s = MbasedScore_S1.MbasedScore_S1(cname)
        self.s.show()


    def saveMatrix(self):
        wbFormulas = openpyxl.load_workbook('./excel file template/Matrix Template.xlsx')
        #
        fileName, suffix = QFileDialog.getSaveFileName(self, "Save File", "", "Excel file (*.xlsx)")
        print(fileName)  # 打印保存文件的全部路径（包括文件名和后缀名）
        #
        #
        if not fileName =="":
            wbFormulas.save(fileName)




        # p.save_book_as(file_name='Matrix Template.xlsx',
        #                dest_file_name=fileName[0])

    def importMatrix(self):
        fileName,suffix = QFileDialog.getOpenFileName(self, "Import Matrix xlsx File", "", "Excel file (*.xlsx)")

        self.label_3.setText(fileName)








