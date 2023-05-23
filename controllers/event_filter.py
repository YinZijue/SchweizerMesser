from PyQt5 import QtCore
from PyQt5.QtCore import QObject

from models.pwd_mgr_models import PwdMgr
from utils.custom_widget import fill_combo_box


class MyEventFilter(QObject):
    def __init__(self, my_window):
        super(MyEventFilter, self).__init__()
        self.my_window = my_window

    def eventFilter(self, obj, event):
        try:
            if obj == self.my_window.comboBox_pwd_category and event.type() == QtCore.QEvent.MouseButtonPress:
                category_set = PwdMgr.get_category()
                fill_combo_box(category_set, self.my_window.comboBox_pwd_category)
            elif obj == self.my_window.pwd_add and event.type() == QtCore.QEvent.Close:
                self.my_window.query_pwd()
            elif obj == self.my_window.comboBox_pwd_category_add and event.type() == QtCore.QEvent.MouseButtonPress:
                category_set = PwdMgr.get_category()
                fill_combo_box(category_set, self.my_window.comboBox_pwd_category_add)
            # title输入框获得输入焦点后，清空异常提示
            elif obj == self.my_window.lineEdit_title_add and event.type() == QtCore.QEvent.FocusIn:
                self.my_window.label_notice.setText('')
        except AttributeError:
            pass
        return False
