from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QListView, QFileDialog, QHeaderView
from qtpy import QtCore
import datetime

from PyQt5 import QtWidgets

from Ui.NMbasedScore_S2 import Ui_Dialog

class NMbasedScore_S2(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self,cname,stype,percent):
        super(NMbasedScore_S2, self).__init__()
        self.setupUi(self)
        self.label_3.setText(cname)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget.setColumnWidth(0, 240)



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



