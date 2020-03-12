from sqlite3 import connect

from PyQt5 import QtWidgets, Qt
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QStringListModel, QAbstractTableModel, QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QVBoxLayout, \
    QCheckBox, QFileDialog, QWidget, QPushButton

from Ui.FilePoolUi import Ui_Dialog
import ScorePanel









class FilePool(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self, cname):
        super(FilePool, self).__init__()
        self.setupUi(self)
        self.label.setText(cname)


        self.pushButton.clicked.connect(lambda : self.goback(cname))

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.setWindowTitle('File Pool')

        update_btn  = QtWidgets.QPushButton()
        hlayout = QHBoxLayout()
        hlayout.addWidget(update_btn)
        # self.tableWidget.setCellWidget(0,3,update_btn)
        self.setWindowTitle("File Pool")
        rsdata = [[1,2,3],[5,6,7,],[9,10,11]]
        for row_number, row_data in enumerate(rsdata):
            self.tableWidget.insertRow(row_number)
            for i in range(len(row_data)+1):
                if i<len(row_data):
                    self.tableWidget.setItem(row_number,i,QtWidgets.QTableWidgetItem(str(row_data[i])))

                    #Add button
                if i == len(row_data):
                    self.tableWidget.setCellWidget(row_number,i,self.buttonForRow(str(row_data[0])))


    def goback(self, cname):
        self.hide()
        self.s = ScorePanel.ScorePanel(cname)
        self.s.show()


    def buttonForRow(self,id):
        widget = QWidget()
        updateBtn = QPushButton('Update')

        updateBtn.clicked.connect(lambda:self.updateTable(id))

        releaseBtn = QPushButton('Release')

        releaseBtn.clicked.connect(lambda :self.releaseFile(id))

        hlayout = QHBoxLayout()
        hlayout.addWidget(updateBtn)
        hlayout.addWidget(releaseBtn)
        hlayout.setContentsMargins(5,2,5,2)
        widget.setLayout(hlayout)
        return widget

    def updateTable(self,id):

        filePath, filetype = QFileDialog.getOpenFileName(self,
                                                     "Choose File",
                                                     "./",
                                                     "Excel (*.xls);;Text Files (*.txt)")  #设置文件扩展名过滤,注意用双分号间隔

        print(filePath,filetype)
        # update the tale after connect with db


    def releaseFile(self,id):
        pass

        #release file after connect with db


