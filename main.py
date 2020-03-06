import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
import MainPage
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainPage.MainPage()

    w.show()
    sys.exit(app.exec_())