import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView

from app.page_switch import page_switched, open_pwd_add_ui
from app.pwd_editor import PwdEditor
from app.pwd_mgr_events import reset_conditions_pwd, query_pwd, context_menu
from models.pwd_mgr_models import PwdMgr
from models.table_model import UserTableModel
from ui.ui_interface import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        # 实例化添加密码弹窗界面的功能类
        self.pwd_add = PwdEditor()
        self.treeWidget.clicked.connect(self.page_switched)
        self.tableView_pwd.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tableView_pwd.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_pwd.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_pwd.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:darkgray;color:white;border:0;padding:5px;}")
        self.model = UserTableModel()
        self.tableView_pwd.setModel(self.model)
        # ---------------------------Pwd_Manager--------------------------------------------------------------#
        self.toolButton_pwd_add.clicked.connect(self.open_pwd_add_ui)
        self.toolButton_pwd_query.clicked.connect(self.query_pwd)
        self.toolButton_pwd_reset_conditons.clicked.connect(self.reset_conditions_pwd)
        self.tableView_pwd.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView_pwd.customContextMenuRequested.connect(self.context_menu)
        # 监听鼠标点击事件，若该控件被点击，则用list填充combobox
        self.comboBox_pwd_category.installEventFilter(self)

    # 菜单页切换
    def page_switched(self):
        page_switched(self)

    def reset_conditions_pwd(self):
        reset_conditions_pwd(self)

    def query_pwd(self):
        query_pwd(self)

    def context_menu(self):
        context_menu(self)

    def open_pwd_add_ui(self):
        self.pwd_add.setWindowModality(Qt.ApplicationModal)
        self.pwd_add.show()

    def eventFilter(self, a0: 'QObject', a1: 'QEvent') -> bool:
        # 鼠标点击comboBox时从数据库获取分组
        if a0 == self.comboBox_pwd_category and a1.type() == QtCore.QEvent.MouseButtonPress:
            category_set = PwdMgr.get_category()
            if self.comboBox_pwd_category.count() == 0:
                self.comboBox_pwd_category.addItems(category_set)
            else:
                # 后续添加时去重
                for category in category_set:
                    if category not in [self.comboBox_pwd_category.itemText(idx) for idx in
                                        range(0, self.comboBox_pwd_category.count())]:
                        self.comboBox_pwd_category.addItem(category)
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
