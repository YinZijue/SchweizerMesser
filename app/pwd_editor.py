import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

from app.pwd_editor_event import reset_input_pwd, add_pwd_record, add_pwd_cancel
from models.pwd_mgr_models import PwdMgr
from ui.ui_pwd_editor import Ui_Dialog_pwd_add


class PwdEditor(QWidget, Ui_Dialog_pwd_add):
    def __init__(self, parent=None):
        super(PwdEditor, self).__init__(parent)
        self.setupUi(self)
        # 固定窗口大小，隐藏标题栏
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.p_btn_pwd_reset.clicked.connect(self.reset_input_pwd)
        self.p_btn_pwd_save_continue.clicked.connect(self.add_pwd_record)
        self.p_btn_pwd_save_exit.clicked.connect(self.add_pwd_record)
        self.p_btn_pwd_cancel.clicked.connect(self.add_pwd_cancel)
        # 为控件添加事件监听
        self.comboBox_pwd_category_add.installEventFilter(self)
        self.lineEdit_title_add.installEventFilter(self)

    def reset_input_pwd(self):
        reset_input_pwd(self)

    def add_pwd_record(self):
        add_pwd_record(self)

    def add_pwd_cancel(self):
        add_pwd_cancel(self)

    def eventFilter(self, a0: 'QObject', a1: 'QEvent') -> bool:
        # 鼠标按下comboBox时从数据库获取分组
        if a0 == self.comboBox_pwd_category_add and a1.type() == QtCore.QEvent.MouseButtonPress:
            category_set = PwdMgr.get_category()
            # 首次直接添加查询到的内容
            if self.comboBox_pwd_category_add.count() == 0:
                self.comboBox_pwd_category_add.addItems(category_set)
            else:
                # 后续添加时去重
                for category in category_set:
                    if category not in [self.comboBox_pwd_category_add.itemText(idx) for idx in
                                        range(0, self.comboBox_pwd_category_add.count())]:
                        self.comboBox_pwd_category_add.addItem(category)

        # title输入框获得输入焦点后，清空异常提示
        elif a0 == self.lineEdit_title_add and a1.type() == QtCore.QEvent.FocusIn:
            self.label_notice.setText('')
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pwd_add_interface = PwdEditor()
    pwd_add_interface.show()
    sys.exit(app.exec_())
