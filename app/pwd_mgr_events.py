from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMenu, QWidget, QMessageBox

from models.db_engine import column_map, column_mapping
from models.pwd_mgr_models import PwdMgr
from utils.get_widget_value import get_widget_value_batch


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
    my_window.lineEdit_remarks.clear()
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
        'remarks': my_window.lineEdit_remarks.text(),
        'category': my_window.comboBox_pwd_category.currentText()
    }
    pwd_records = [[v for k, v in p.to_dict().items()] for p in PwdMgr(conditions).get_pwd(conditions=conditions)]
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
    my_window.menu.popup(QCursor.pos())
    my_window.menu.show()
    # 右键选中一行时,获取该行数据及对应的列名
    model = my_window.tableView_pwd.model()
    selected_row_index = my_window.tableView_pwd.currentIndex().row()
    selected_row_data = {}
    for column in range(model.columnCount()):
        column_name = column_mapping(model.headerData(column, Qt.Horizontal), column_map)
        index = model.index(selected_row_index, column)
        item_value = str(model.data(index))
        if 'PyQt5.QtCore.QVariant' in item_value:
            item_value = ''
        selected_row_data[column_name] = item_value
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
            update_pwd(my_window, selected_row_data)


def update_pwd(my_window, original_pwd: dict):
    my_window.pwd_add.setWindowModality(Qt.ApplicationModal)
    my_window.pwd_add.show()
    my_window.pwd_add.label.setText("修改密码")
    widgets = my_window.pwd_add.findChildren(QWidget)
    get_widget_value_batch(widgets, original_pwd)
