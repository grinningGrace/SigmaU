from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QListView, QFileDialog, QHeaderView
from qtpy import QtCore
import datetime
import NMbasedScore_S3

from PyQt5 import QtWidgets
from Ui.AddCourseAssessCriteria import Ui_Dialog
import CoursePage

class AddCourseAssessCriteria(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self,cname):
        super(AddCourseAssessCriteria, self).__init__()
        self.setupUi(self)
        self.label_2.setText(cname)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget.setColumnWidth(0, 240)
        self.pushButton.clicked.connect(self.toCoursePage)



        for row in range(6):
            self.tableWidget.insertRow(row)
            for column in range(2):
                if row==0 and column==0:
                    self.tableWidget.setItem(row,column,QtWidgets.QTableWidgetItem("e.g. Knowledge"))
                elif row==0 and column ==1:
                    self.tableWidget.setItem(row,column,QtWidgets.QTableWidgetItem("0.3"))
                elif row==1 and column==0:
                    self.tableWidget.setItem(row,column,QtWidgets.QTableWidgetItem("click the cell to change text"))

                else:
                    self.tableWidget.setItem(row,column,QtWidgets.QTableWidgetItem("Null"))


    def toCoursePage(self):
        self.hide()
        self.s = CoursePage.CoursePage()
        self.s.show()
