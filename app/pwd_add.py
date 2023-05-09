import logging
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QDialog

from config import moment
from models.db_engine import insert_db
from models.pwd_mgr_models import PwdMgr
from ui.pwd_add import Ui_Dialog_pwd_add


class PwdAdd(QWidget, Ui_Dialog_pwd_add):
    def __init__(self, parent=None):
        super(PwdAdd, self).__init__(parent)
        self.setupUi(self)
        # 去掉右上的最小化、最大化、关闭按钮
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.p_btn_pwd_pwd_reset.clicked.connect(self.reset_input_pwd)
        self.p_btn_pwd_save_continue.clicked.connect(self.add_pwd_record)
        self.p_btn_pwd_save_exit.clicked.connect(self.add_pwd_record)
        self.p_btn_pwd_pwd_cancel.clicked.connect(QDialog.accepted)
        # 为控件添加事件监听
        self.comboBox_pwd_category_add.installEventFilter(self)
        self.lineEdit_title_add.installEventFilter(self)

    def reset_input_pwd(self):
        self.lineEdit_title_add.setText('')
        self.lineEdit_usr_add.setText('')
        self.lineEdit_pwd_add.setText('')
        self.lineEdit_url_add.setText('')
        self.plainTextEdit_remark_add.setPlainText('')
        self.comboBox_pwd_category_add.clear()

    def add_pwd_record(self):
        # 通过按钮容器获取sender，以便不同的按钮使用用一个槽函数
        button = QPushButton().sender()
        exist_title = [title.to_dict()['title'] for title in PwdMgr.get_pwd({'title': ''})]
        try:
            if len(self.lineEdit_title_add.text()) == 0:
                self.label_pwd_add_notice.setText('标题不能为空！')
            elif self.lineEdit_title_add.text() in exist_title:
                self.label_pwd_add_notice.setText('标题已存在,请检查！')
            else:
                conditions = {'title': self.lineEdit_title_add.text(), 'url': self.lineEdit_url_add.text(),
                              'usr': self.lineEdit_usr_add.text(), 'pwd': self.lineEdit_pwd_add.text(),
                              'category': self.comboBox_pwd_category_add.currentText(),
                              'remarks': self.plainTextEdit_remark_add.toPlainText(), 'create_time': moment,
                              'last_update_time': moment, 'delete_flag': 0}
                new_pwd = PwdMgr(conditions)
                insert_db(new_pwd)
                if button.objectName() == 'p_btn_pwd_save_exit':
                    QDialog.close(PwdAdd)
        except Exception as e:
            logging.error(str(e))
        finally:
            self.reset_input_pwd()

    def eventFilter(self, a0: 'QObject', a1: 'QEvent') -> bool:
        # 鼠标按下comboBox时从数据库获取分组
        if a0 == self.comboBox_pwd_category_add and a1.type() == QtCore.QEvent.MouseButtonPress:
            category_list = [category.to_dict()['category'] for category in PwdMgr.get_pwd({'category': ''})]
            self.comboBox_pwd_category_add.addItems(category_list)
        # title输入框获得输入焦点后，清空异常提示
        elif a0 == self.lineEdit_title_add and a1.type() == QtCore.QEvent.FocusIn:
            self.label_pwd_add_notice.setText('')
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pwd_add_interface = PwdAdd()
    pwd_add_interface.show()
    sys.exit(app.exec_())
