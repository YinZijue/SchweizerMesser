import sys

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView

from app.page_switch import page_switched
from app.pwd_editor import PwdEditor
from app.pwd_mgr_events import reset_conditions_pwd, query_pwd, context_menu
from controllers.event_filter import MyEventFilter
from controllers.event_listener import MyListener
from models.pwd_mgr_models import PwdMgr
from models.table_model import UserTableModel
from ui.ui_interface import Ui_MainWindow
from utils.custom_widget import fill_combo_box


class MainWindow(QMainWindow, Ui_MainWindow):
    signal_to_pwd_editor = pyqtSignal(dict)

    def __init__(self, parent=None):
        self.my_listener = MyListener()
        self.my_filter = MyEventFilter(self)
        self.pwd_add = PwdEditor()
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        # 实例化添加密码弹窗界面的功能类
        self.signal_to_pwd_editor.connect(self.pwd_add.receive_data_from_pwd_mgr)
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
        fill_combo_box(PwdMgr.get_category(), self.comboBox_pwd_category)
        self.comboBox_pwd_category.clear()
        # 监听鼠标点击事件，若该控件被点击，则用list填充combobox
        self.pwd_add.closeEvent = self.my_listener
        self.pwd_add.installEventFilter(self.my_filter)
        self.comboBox_pwd_category.mousePressEvent = self.my_listener
        self.comboBox_pwd_category.installEventFilter(self.my_filter)

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
        self.pwd_add.label_notice.clear()
        self.pwd_add.label.setText('新增密码')
        self.pwd_add.p_btn_pwd_save_continue.show()
        self.pwd_add.show()
        self.pwd_add.reset_input_pwd()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
