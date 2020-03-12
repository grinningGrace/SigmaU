import AlertInfo
import CoursePage
from PyQt5 import QtWidgets
import AddCourseAssessCriteira
from Ui.AddCoursePageUi import Ui_Dialog

class AddCoursePage(QtWidgets.QDialog,Ui_Dialog):
    _ccode=""
    _csession=""
    _cyear=""
    _csem=""
    _cname=""

    def __init__(self):
        super(AddCoursePage, self).__init__()
        # self.init_ui(self)
        self.setupUi(self)


        self.comboBox.activated.connect(self.yearcombo)
        self.comboBox_2.activated.connect(self.semcombo)

        self._cname = self.lineEdit_7.text()+"#"+self.lineEdit_3.text()+"#"+self.comboBox.currentText()+"#"+ self.comboBox_2.currentText()

        self.pushButton.clicked.connect(self.course_add_btn_clicked)
        self.pushButton_2.clicked.connect(self.goback)
        self.setWindowTitle("Add a Course")

    def course_add_btn_clicked(self):
        # self.s = AlertInfo.AlertInfo(self)
        # self.s.setFixedSize(450,317)
        self._cname = self.lineEdit_7.text()+"#"+self.lineEdit_3.text()+"#"+self.comboBox.currentText()+"#"+ self.comboBox_2.currentText()
        print(self._cname)
        self.hide()
        self.s = AddCourseAssessCriteira.AddCourseAssessCriteria(self._cname)
        self.s.show()

    def goback(self):
        self.hide()
        self.s = CoursePage.CoursePage()
        self.s.show()


    def get_class_name(self):
        return self.__class__.__name__

    def yearcombo(self):
        self._cyear = self.comboBox.currentText()
        self._cname = self.lineEdit_7.text()+"#"+self.lineEdit_3.text()+"#"+self.comboBox.currentText()+"#"+ self.comboBox_2.currentText()

    def semcombo(self):
        self._csem = self.comboBox_2.currentText()
        self._cname = self.lineEdit_7.text()+"#"+self.lineEdit_3.text()+"#"+self.comboBox.currentText()+"#"+ self.comboBox_2.currentText()