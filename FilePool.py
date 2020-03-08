from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView

from Ui.FilePoolUi import Ui_Dialog
import ScorePanel

class FilePool(QtWidgets.QDialog, Ui_Dialog ):
    def __init__(self, cname):
        super(FilePool, self).__init__()
        self.setupUi(self)
        self.label.setText(cname)

        self.pushButton.clicked.connect(lambda : self.goback(cname))

        TableWidget = QTableWidget(1,5)
        TableWidget.setHorizontalHeaderLabels(['File Name','Score Type','Upload Time','Operation 1','Operation 2'])
        layout = QHBoxLayout()

        TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        QTableWidget.resizeColumnsToContents(TableWidget)
        QTableWidget.resizeRowsToContents(TableWidget)
        TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        l = ["Introduction to Entrepreneurship and Innovation (1001) 19-20 S2 mid-term.xls",'CA_Mid-term',"20-3-8 20:20","download","Update"]
        newItem = QTableWidgetItem(l[0])
        TableWidget.setItem(0,0,newItem)

        newItem = QTableWidgetItem(l[1])
        TableWidget.setItem(0,1,newItem)

        newItem = QTableWidgetItem(l[2])
        TableWidget.setItem(0,2,newItem)

        newItem = QTableWidgetItem(l[3])
        TableWidget.setItem(0,3,newItem)

        newItem = QTableWidgetItem(l[4])
        TableWidget.setItem(0,4,newItem)
        layout.addWidget(TableWidget)

        self.setLayout(layout)
        #
        # my_Signal1 = pyqtSignal()
        #
        # self.tableWidget.cellClicked(5).connect(self.Slot_mySignal1)

    def goback(self, cname):
        self.hide()
        self.s = ScorePanel.ScorePanel(cname)
        self.s.show()

    # def Slot_mySignal1(self):
    #     print("OK")