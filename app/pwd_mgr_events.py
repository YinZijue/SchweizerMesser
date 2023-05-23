from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMenu, QMessageBox, QWidget

from models.pwd_mgr_models import PwdMgr
from utils.custom_widget import fill_combo_box, generate_message_box
from utils.get_widget_value import get_widget_value_batch, get_current_row


def reset_conditions_pwd(my_window):
    """
    密码管理界面:重置密码查询条件
    :param my_window:
    :return:
    """
    my_window.lineEdit_title.clear()
    my_window.lineEdit_usr.clear()
    my_window.comboBox_pwd_category.clear()
    my_window.lineEdit_url.clear()
    my_window.lineEdit_remark.clear()
    query_pwd(my_window)


def query_pwd(my_window):
    """
    密码管理界面:按条件查询密码记录
    :param my_window:
    :return:
    """
    conditions = {
        'title': my_window.lineEdit_title.text(),
        'usr': my_window.lineEdit_usr.text(),
        'url': my_window.lineEdit_url.text(),
        'remark': my_window.lineEdit_remark.text(),
        'category': my_window.comboBox_pwd_category.currentText()
    }
    pwd_records = [[v for k, v in p.to_dict().items()] for p in PwdMgr(conditions).get_pwd(conditions=conditions)]
    # 密码ID无需在界面上显示
    for pwd in pwd_records:
        pwd.remove(pwd[0])
    model = my_window.tableView_pwd.model()
    # 查询结果小于固定行数时，用空数据填充表格
    while len(pwd_records) < model.rowCount():
        pwd_records.append(['', '', '', '', '', '', '', '', '', ''])
    model.beginResetModel()
    model._data = pwd_records
    model.endResetModel()


def context_menu(my_window):
    my_window.menu = QMenu()
    update_action = my_window.menu.addAction("修改")
    delete_action = my_window.menu.addAction("删除")
    my_window.menu.popup(QCursor.pos())
    selected_row_data = get_current_row(my_window.tableView_pwd)
    my_window.signal_to_pwd_editor.emit(selected_row_data)
    my_window.menu.show()
    # 右键选中一行时,获取该行数据及对应的列名

    if selected_row_data['title'] == '':
        message_box = QMessageBox()
        message_box.setWindowTitle("提示")
        message_box.setIcon(QMessageBox.Warning)
        message_box.setText("当前选中的行无数据！")
        message_box.addButton("确定", QMessageBox.AcceptRole)
        message_box.exec_()
    else:
        action = my_window.menu.exec()
        if action == update_action:
            fill_combo_box(PwdMgr.get_category(), my_window.pwd_add.comboBox_pwd_category_add)
            widgets = my_window.pwd_add.findChildren(QWidget)
            update_pwd(my_window)
            get_widget_value_batch(widgets, selected_row_data)
        if action == delete_action:
            delete_pwd_single(my_window, [selected_row_data])


def update_pwd(my_window):
    my_window.pwd_add.setWindowModality(Qt.ApplicationModal)
    my_window.pwd_add.show()
    my_window.pwd_add.label.setText("修改密码")
    my_window.pwd_add.label_notice.clear()
    my_window.pwd_add.p_btn_pwd_save_continue.hide()


def delete_pwd_single(my_window, select_pwd_id):
    message_box, q_yes, q_no = generate_message_box(
        my_window, QMessageBox.Warning, "注意", "您确定要删除选中的密码记录吗?"
    )
    if message_box.clickedButton() == q_yes:
        PwdMgr.delete_pwd_logical(select_pwd_id)
        query_pwd(my_window)
    elif message_box.clickedButton() == q_no:
        message_box.close()
