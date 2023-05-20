import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from demo.table.events import query_users
# 创建 SQLite 数据库引擎和会话工厂
from demo.table.untitled import Ui_MainWindow
from demo.table.user_table_model import UserTableModel

engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


# 创建主窗口并设置标题
class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)
        self.setupUi(self)

        self.model = UserTableModel()
        self.tableView.setModel(self.model)

        # 设置表格视图的列宽
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.query_button.clicked.connect(self.query_users)

    def query_users(self):
        query_users(self)


# 启动应用程序
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AppWindow()
    win.show()
    app.exec_()
