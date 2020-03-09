from PyQt5 import QtWidgets
from Ui.ScorePanelUi import Ui_Dialog
import FilePool
import CoursePanel
import MbasedScore_S1

class ScorePanel(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self,cname):
        super(ScorePanel, self).__init__()
        self.setupUi(self)
        self.label.setText(cname)
        self.pushButton_3.clicked.connect(lambda: self.callFilePool(cname))
        self.pushButton_4.clicked.connect(lambda : self.goback(cname))
        self.pushButton.clicked.connect(lambda :self.MbasedScore(cname))


    def callFilePool(self,cname):
        self.hide()
        self.s = FilePool.FilePool(cname)
        # self.s.setFixedSize(900,700)

        self.s.show()


    def goback(self,cname):
        self.hide()
        self.s = CoursePanel.CoursePanel(cname)
        self.s.show()

    def MbasedScore(self,cname):
        self.hide()
        self.s = MbasedScore_S1.MbasedScore_S1(cname)
        self.s.show()