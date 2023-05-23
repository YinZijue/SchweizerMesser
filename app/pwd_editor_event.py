import logging

from PyQt5.QtWidgets import QMessageBox, QPushButton, QWidget

from config import get_moment
from models.db_engine import column_map
from models.pwd_mgr_models import PwdMgr
from utils.get_widget_value import get_widget_name_value_batch


def edit_pwd_record(my_window, original_pwd: dict):
    """
    密码编辑界面:新增密码记录
    :param original_pwd:
    :param my_window:
    :return:
    """
    # 通过按钮容器获取sender，以便不同的按钮使用用一个槽函数
    button = QPushButton().sender()
    exist_title = [title.to_dict()['title'] for title in PwdMgr.get_pwd({'title': ''})]
    try:
        if my_window.label.text() == '新增密码':
            if len(my_window.lineEdit_title_add.text()) == 0:
                my_window.label_notice.setText('标题不能为空！')
            elif my_window.lineEdit_title_add.text() in exist_title:
                my_window.label_notice.setText('标题已存在,请检查！')
            else:
                conditions = {
                    'title': my_window.lineEdit_title_add.text(),
                    'url': my_window.lineEdit_url_add.text(),
                    'usr': my_window.lineEdit_usr_add.text(),
                    'password': my_window.lineEdit_password_add.text(),
                    'category': my_window.comboBox_pwd_category_add.currentText(),
                    'remark': my_window.plainTextEdit_remark_add.toPlainText(),
                    'create_time': get_moment(),
                    'last_update_time': get_moment(),
                    'delete_flag': 0
                }
                PwdMgr.insert_pwd(conditions)
                my_window.reset_input_pwd()
                if button.objectName() == 'p_btn_pwd_save_exit':
                    my_window.close()
        elif my_window.label.text() == '修改密码':
            widgets = my_window.findChildren(QWidget)
            widget_dict = get_widget_name_value_batch(widgets)
            new_pwd_record = {k1: v for k1 in column_map.keys() for k2, v in widget_dict.items() if k1 in k2}
            if len(my_window.lineEdit_title_add.text()) == 0:
                my_window.label_notice.setText('标题不能为空！')
            elif original_pwd['title'] != new_pwd_record['title'] and new_pwd_record['title'] in exist_title:
                my_window.label_notice.setText('该标题已存在,请更换为其他标题！')
            else:
                PwdMgr.update_pwd(original_pwd, new_pwd_record)
                my_window.close()

    except Exception as e:
        logging.error(str(e))


def reset_input_pwd(my_window):
    """
    密码编辑界面：清空输入内容
    :param my_window:
    :return:
    """
    my_window.lineEdit_title_add.setText('')
    my_window.lineEdit_usr_add.setText('')
    my_window.lineEdit_password_add.setText('')
    my_window.lineEdit_url_add.setText('')
    my_window.plainTextEdit_remark_add.setPlainText('')
    my_window.comboBox_pwd_category_add.clear()


def add_pwd_cancel(my_window):
    """
    密码编辑界面:取消按钮功能
    :param my_window:
    :return:
    """
    len0 = len(my_window.lineEdit_title_add.text())
    len1 = len(my_window.lineEdit_usr_add.text())
    len2 = len(my_window.lineEdit_password_add.text())
    len3 = len(my_window.lineEdit_url_add.text())
    len4 = len(my_window.plainTextEdit_remark_add.toPlainText())
    len5 = len(my_window.comboBox_pwd_category_add.currentText())
    if (len0 + len1 + len2 + len3 + len4 + len5) == 0:
        my_window.close()
    else:
        message_box = QMessageBox(QMessageBox.Warning, "注意！", "当前输入的内容尚未保存,您确定要退出吗？")
        q_yes = message_box.addButton(my_window.tr("确定"), QMessageBox.YesRole)
        q_no = message_box.addButton(my_window.tr("取消"), QMessageBox.NoRole)
        message_box.exec_()
        if message_box.clickedButton() == q_yes:
            my_window.close()
        elif message_box.clickedButton() == q_no:
            return
