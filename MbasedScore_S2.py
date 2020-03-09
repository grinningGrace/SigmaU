from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QListView
import deleteCoursePage
from PyQt5 import QtWidgets

from Ui.MbasedScore_S2_Ui import Ui_Dialog

class MbasedScore_S2(QtWidgets.QDialog,Ui_Dialog):
    _stype = 0
    _percent = 0


    def __init__(self,cname,stype,percent):
        super(MbasedScore_S2, self).__init__()
        self.setupUi(self)
        self._stype = stype
        self._percent = percent

