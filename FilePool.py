from sqlite3 import connect

from PyQt5 import QtWidgets, Qt
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QStringListModel, QAbstractTableModel, QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QVBoxLayout, \
    QCheckBox

from Ui.FilePoolUi import Ui_Dialog
import ScorePanel
import CheckBoxHeader
import MyModel
import MyButtonDelegate

def SIGNAL(param):
    pass


class FilePool(QtWidgets.QDialog, Ui_Dialog):
    myModel = MyModel.MyModel()
    def __init__(self, cname):
        super(FilePool, self).__init__()
        self.setupUi(self)
        self.label.setText(cname)


        self.pushButton.clicked.connect(lambda : self.goback(cname))
        #
        self.setWindowTitle('File Pool')

        self.tableView.setModel(self.myModel)
        header = CheckBoxHeader.CheckBoxHeader()
        self.tableView.setHorizontalHeader(header)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        header.clicked.connect(self.myModel.headerClick)

        self.tableView.setItemDelegateForColumn(3, MyButtonDelegate.MyButtonDelegate(self))


    def cellUpdateButtonClicked(self):
        print("Update Cell Button Clicked", self.sender().index)


    def cellDeleteButtonClicked(self):
        print("Delete Cell Button Clicked", self.sender().index)


    def goback(self, cname):
        self.hide()
        self.s = ScorePanel.ScorePanel(cname)
        self.s.show()





