from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QListView
import deleteCoursePage
from PyQt5 import QtWidgets
from Ui.CourseaPageUi import Ui_Dialog
import AddCoursePage
import MainPage
import CoursePanel
class CoursePage(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        super(CoursePage, self).__init__()
        # self.init_ui(self)

        self.setupUi(self)


        l = ['IEI (1001)', 'IEI (1002)', 'IEI (1008)','CBWA(1001)', 'MSM (1001)' ,'BSDA (1001)','BDA(1001)']
        slm = QStringListModel()
        self.listView.qList = l

        slm.setStringList(l)
        self.listView.setModel(slm)
        listView = QListView()
        listView.setModel(slm)

        self.listView.clicked.connect(self.CourseItemClicked)
        self.addCourse.clicked.connect(self.addCourse_btn_click)
        self.deleteCourse.clicked.connect(self.deleteCourse_btn_click)
        self.logOut.clicked.connect(self.logOut_btn_click)


    def addCourse_btn_click(self):
        self.hide()
        self.s = AddCoursePage.AddCoursePage()
        self.s.show()


    def logOut_btn_click(self):
        self.hide()
        self.s = MainPage.MainPage()
        self.s.show()


    def deleteCourse_btn_click(self):
        self.hide()
        self.s = deleteCoursePage.deleteCousePage()
        self.s.show()



    def CourseItemClicked(self, qModelIndex):
        # QMessageBox.information(self,'ListWidget','你选择了：'+self.listView.qList[qModelIndex.row()])
        cname = self.listView.qList[qModelIndex.row()]
        self.hide()
        self.s = CoursePanel.CoursePanel(cname)
        self.s.show()
