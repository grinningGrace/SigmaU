import sys
from PyQt5.QtWidgets import (QApplication, QHeaderView, QStyle, QStyleOptionButton, QTableView)
from PyQt5.QtCore import (pyqtSignal, Qt, QAbstractTableModel, QModelIndex, QRect, QVariant)

class MyModel(QAbstractTableModel):
    _column_count = 4
    def __init__(self, parent=None):
        super(MyModel, self).__init__(parent)
        # Keep track of which object are checked
        self.checkList = ['Unchecked', 'Unchecked']

    def rowCount(self, QModelIndex):
        return len(self.checkList)

    def columnCount(self, QModelIndex):
        return self._column_count

    def set_columnCount(self,i):
        self._column_count = i

    def data(self, index, role):
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            if col != self._column_count-1:
                return 'Row %d, Column %d' % (row + 1, col + 1)
            elif col ==self._column_count-1:
                return "Update"
        elif role == Qt.CheckStateRole:
            if col == 0:
                return Qt.Checked if self.checkList[row] == 'Checked' else Qt.Unchecked
        elif role == Qt.ToolTipRole:
            if col == 0:
                return self.checkList[row]
        return QVariant()

    def setData(self, index, value, role):
        row = index.row()
        col = index.column()
        if role == Qt.CheckStateRole and col == 0:
            self.checkList[row] = 'Checked' if value == Qt.Checked else 'Unchecked'


        return True

    def flags(self, index):
        if index.column() == 0:
            return Qt.ItemIsEnabled | Qt.ItemIsUserCheckable
        return Qt.ItemIsEnabled

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                if section == 0:
                    return 'File Name'
                elif section == 1:
                    return 'Score Type'
                elif section == 2:
                    return 'Upload Time'
                elif section == 3:
                    return 'Update the file'

    def headerClick(self, isOn):
        self.beginResetModel()
        if isOn:
            self.checkList = ['Checked', 'Checked']
        else:
            self.checkList = ['Unchecked', 'Unchecked']
        self.endResetModel()
