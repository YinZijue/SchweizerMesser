import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from ui.interface import Ui_MainWindow


class PagePwdMgr(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(PagePwdMgr, self).__init__(parent)
        self.setupUi(self)
        self.stack_list.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    page_1 = PagePwdMgr()
    page_1.show()
    sys.exit(app.exec_())
