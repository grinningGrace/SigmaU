from PyQt5 import QtWidgets
import MainPage
from Ui.AlertInfoUi import Ui_Dialog

class AlertInfo(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self,Dialog):
        super(AlertInfo, self).__init__()
        self.setupUi(self)
        if Dialog.__class__.__name__=="Register":
            self.pushButton.setText("Confirm and Log in")
            self.pushButton.clicked.connect(self.go_to_longin)
        else:
            self.pushButton.clicked.connect(self.confirm_return)
        # if self.parent.get_class_name()== AddCoursePage or deleteCoursePage:
        #     print(self.parent.get_class_name())
        #     print("test")
        #     self.pushButton.clicked.connect(self.confirm_return)
        # elif type(QtWidgets.QDialog.parent(self)) == Register:
        #     self.pushButton.setText("Return to Log in Page")
        #     self.pushButton.clicked.connect(self.go_to_longin)


    def confirm_return(self):
        self.hide()

    def go_to_longin(self):
        self.hide()
        self.s = MainPage.MainPage()
        self.s.show()

    def set_label_delete_msg(self):
        self.label_2.setText("This Course is successfully deleted!")


    def set_label1_msg(self, str):
        self.label.setText(str)

    def set_label2_msg(self,str):
        self.label_2.setText(str)

    def get_class_name(self):
        return self.__class__.__name__



