
import sys
from PyQt5.QtWidgets import (QApplication, QHeaderView, QStyle, QStyleOptionButton, QTableView, QItemDelegate,
                             QPushButton, QHBoxLayout, QWidget)
from PyQt5.QtCore import (pyqtSignal, Qt, QAbstractTableModel, QModelIndex, QRect, QVariant)

class MyButtonDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super(MyButtonDelegate, self).__init__(parent)

    def paint(self, painter, option, index):
        if not self.parent().tableView.indexWidget(index):
            button_update = QPushButton(
                self.tr('Update'),
                self.parent(),
                clicked=self.parent().cellUpdateButtonClicked
            )
            button_delete = QPushButton(
                self.tr('Delete'),
                self.parent(),
                clicked=self.parent().cellDeleteButtonClicked
            )
            button_update.index = [index.row(), index.column()]
            button_delete.index = [index.row(), index.column()]
            h_box_layout = QHBoxLayout()
            h_box_layout.addWidget(button_update)
            h_box_layout.addWidget(button_delete)
            h_box_layout.setContentsMargins(0, 0, 0, 0)
            h_box_layout.setAlignment(Qt.AlignCenter)
            widget = QWidget()
            widget.setLayout(h_box_layout)
            self.parent().tableView.setIndexWidget(
                index,
                widget
            )