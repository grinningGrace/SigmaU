from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QListView
import deleteCoursePage
from PyQt5 import QtWidgets


from Ui.CourseaPageUi import Ui_Dialog
import AddCoursePage
import MainPage
import CoursePanel
class CoursePage(QtWidgets.QDialog,Ui_Dialog):
    _cnamelist = []
    def __init__(self):
        super(CoursePage, self).__init__()
        # self.init_ui(self)

        self.setupUi(self)


        course_title = ['Developing Applications for Mobile and Social Media',
             'Introduction to Business Data Analytics',
             'Introduction to Entrepreneurship and Innovation',
             'Introduction to Entrepreneurship and Innovation ',
             'e-Customer Behaviours and Web Analytics' ,
             'Business Systems Design and Analysis',
             'Introduction to Entrepreneurship and Innovation']



        course_code=['EBIS 3093', 'EBIS 3103', 'GDBM 1013', 'GDBM 1013', 'EBIS 3083','EBIS 3013','GDBM 1013']
        course_session = ['1001','1001','1001','1002','1001','1001','1008']
        cname = []
        for i in range(0,len(course_title)):

            cname.append(course_code[i]+"#"+course_title[i]+"#"+course_session[i])
            # print(cname[i])
        self.setWindowTitle("Course Page")
        course_name = []
        for i in range(0,len(course_title)):
            course_name.append(course_title[i]+" ( " +course_session[i]+" ) ")

        # print(course_code)
        # print(course_name)
        self._cnamelist = cname




        slm = QStringListModel()

        self.listView.qList = course_name


        slm.setStringList(course_name)
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



    def CourseItemClicked(self,qModelIndex):
        # QMessageBox.information(self,'ListWidget','你选择了：'+self.listView.qList[qModelIndex.row()])
        course_name = self.listView.qList[qModelIndex.row()]
        # self._listViewIndex = qModelIndex.row()

        cname = self._cnamelist[qModelIndex.row()]
        self.hide()
        self.s = CoursePanel.CoursePanel(cname)
        self.s.show()
