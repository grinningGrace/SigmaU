import ScorePanel
import CoursePage
from PyQt5 import QtWidgets
from Ui.CoursePanelUi import Ui_Dialog

class CoursePanel(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self,cname):
        super(CoursePanel, self).__init__()

        self.setupUi(self)
        course_code, course_name, course_session = cname.split("#")

        self.label.setText(course_name+" ( "+course_session+" ) ")
        self.Scores.clicked.connect(lambda: self.callScorePanel(cname))
        self.Goback.clicked.connect(self.goback)
        self.setWindowTitle("Course Panel")




    def callScorePanel(self,cname):
        self.hide()
        self.s = ScorePanel.ScorePanel(cname)
        self.s.show()


    def goback(self):
        self.hide()
        self.s = CoursePage.CoursePage()
        self.s.show()




