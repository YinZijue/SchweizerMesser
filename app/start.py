import sys

from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView

from models.pwd_mgr import PwdMgr
from ui.interface import Ui_MainWindow
from models.db_engine import get_column_info


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.data_model = QStandardItemModel(10, get_column_info()['main_col_count'])
        self.data_model.setHorizontalHeaderLabels(get_column_info()['main_col'])
        self.tableView_pwd.setModel(self.data_model)
        self.tableView_pwd.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_pwd.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.treeWidget.clicked.connect(self.page_switched)
        self.toolButton_pwd_query.clicked.connect(self.query_pwd)

    def page_switched(self):
        item = self.treeWidget.currentItem()
        for index in range(self.stack_list.count()):
            if item.text(0) == self.stack_list.widget(index).accessibleName():
                self.stack_list.setCurrentIndex(index)

    def query_pwd(self):
        conditions = {
            'title': self.lineEdit_title.text(),
            'usr': self.lineEdit_usr.text(),
            'url': self.lineEdit_url.text(),
            'remarks': self.lineEdit_remarks.text(),
            'category': self.comboBox_category.currentText()
        }
        pwd_record = [p.to_dict() for p in PwdMgr().get_pwd(conditions=conditions)]
        if pwd_record:
            for p in pwd_record:
                print(PwdMgr().get_pwd(conditions=conditions))
        else:
            print("nothing found")

    # 表格分页功能,https://blog.csdn.net/zizle_lin/article/details/89474813
    def setPageController(self, page):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
