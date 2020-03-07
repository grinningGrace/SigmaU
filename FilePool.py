from PyQt5 import QtWidgets
from Ui.FilePoolUi import Ui_Dialog
import ScorePanel

class FilePool(QtWidgets.QDialog, Ui_Dialog ):
    def __init__(self, cname):
        super(FilePool, self).__init__()
        self.setupUi(self)
        self.label.setText(cname)

        self.pushButton.clicked.connect(lambda : self.goback(cname))


    def goback(self, cname):
        self.hide()
        self.s = ScorePanel.ScorePanel(cname)
        self.s.show()
