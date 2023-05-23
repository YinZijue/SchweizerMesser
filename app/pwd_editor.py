import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication

from app.pwd_editor_event import reset_input_pwd, edit_pwd_record, add_pwd_cancel
from controllers.event_filter import MyEventFilter
from controllers.event_listener import MyListener
from models.pwd_mgr_models import PwdMgr
from ui.ui_pwd_editor import Ui_Dialog_pwd_add
from utils.custom_widget import fill_combo_box


class PwdEditor(QWidget, Ui_Dialog_pwd_add):
    signal_to_pwd_mgr = pyqtSignal(str)

    def __init__(self, parent=None):
        self.my_listener = MyListener()
        self.my_filter = MyEventFilter(self)
        super(PwdEditor, self).__init__(parent)
        self.setupUi(self)
        self.data = None
        # 固定窗口大小，隐藏标题栏
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.p_btn_pwd_reset.clicked.connect(self.reset_input_pwd)
        self.p_btn_pwd_save_continue.clicked.connect(self.edit_pwd)
        self.p_btn_pwd_save_exit.clicked.connect(self.edit_pwd)
        self.p_btn_pwd_cancel.clicked.connect(self.add_pwd_cancel)
        # 为控件添加事件监听
        self.comboBox_pwd_category_add.installEventFilter(self)
        self.lineEdit_title_add.installEventFilter(self)
        # self.comboBox_pwd_category_add.mousePressEvent = self.my_listener
        # self.comboBox_pwd_category_add.installEventFilter(self.my_filter)
        #
        # self.lineEdit_title_add.focusInEvent = self.my_listener
        # self.lineEdit_title_add.installEventFilter(self.my_filter)

    def receive_data_from_pwd_mgr(self, data):
        self.data = data

    def reset_input_pwd(self):
        reset_input_pwd(self)

    def edit_pwd(self):
        edit_pwd_record(self, self.data)

    def add_pwd_cancel(self):
        add_pwd_cancel(self)

    def eventFilter(self, a0: 'QObject', a1: 'QEvent') -> bool:
        # 鼠标按下comboBox时从数据库获取分组
        if a0 == self.comboBox_pwd_category_add and a1.type() == QtCore.QEvent.MouseButtonPress:
            category_set = PwdMgr.get_category()
            fill_combo_box(category_set, self.comboBox_pwd_category_add)

        # title输入框获得输入焦点后，清空异常提示
        elif a0 == self.lineEdit_title_add and a1.type() == QtCore.QEvent.FocusIn:
            self.label_notice.setText('')
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pwd_add_interface = PwdEditor()
    pwd_add_interface.show()
    sys.exit(app.exec_())
