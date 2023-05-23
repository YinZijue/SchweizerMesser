from PyQt5.QtCore import Qt

from models.db_engine import column_mapping, column_map, get_column_info


def get_widget_value_batch(widgets: list, data: dict):
    """
    根据控件类型,批量将数据填入控件中
    :param widgets:
    :param data:
    :return:
    """
    for widget in widgets:
        name = widget.objectName()
        wg_type = widget.metaObject().className()
        for k, v in data.items():
            if k in name:
                if wg_type in ['QLabel', 'QLineEdit']:
                    widget.setText(v)
                elif wg_type in ['QPlainTextEdit']:
                    widget.setPlainText(v)
                elif wg_type in ['QComboBox']:
                    widget.setCurrentText(v)


def get_widget_name_value_batch(widgets: list):
    """
    获取当前窗口中控件的名称和值组成的字典
    :param widgets:
    :return:
    """
    widget_dict = {}
    for widget in widgets:
        name = widget.objectName()
        wg_type = widget.metaObject().className()
        if wg_type in ['QLineEdit', 'QLabel']:
            widget_dict[name] = widget.text()
        elif wg_type in ['QPlainTextEdit']:
            widget_dict[name] = widget.toPlainText()
        elif wg_type in ['QComboBox']:
            widget_dict[name] = widget.currentText()
    return widget_dict


def get_current_row(table_view):
    model = table_view.model()
    selected_row_index = table_view.currentIndex().row()
    selected_row_data = {}
    for column in range(model.columnCount()):
        column_name = column_mapping(model.headerData(column, Qt.Horizontal), column_map)
        index = model.index(selected_row_index, column)
        item_value = str(model.data(index))
        if 'PyQt5.QtCore.QVariant' in item_value:
            item_value = ''
        selected_row_data[column_name] = item_value
    return selected_row_data


def get_new_data(columns: list, data: dict):
    """用列名组成的列表替换字典的键"""
    return {column: v for k, v in data.items() for column in columns if column in k}


if __name__ == '__main__':
    data1 = {'label': '修改密码', 'lineEdit_url_add': 'http://www.blizzard.com', 'label_5': '标题：', 'label_7': '密码：',
             'label_notice': '', 'label_6': '用户名：', 'label_10': '分组：', 'label_9': '备注：', 'label_8': '网址：',
             'lineEdit_password_add': 'smwhsnaj23413124dfaf', 'comboBox_pwd_category_add': '日常',
             'plainTextEdit_remark_add': '国服已停运', 'lineEdit_title_add': '炉石传说', 'lineEdit_usr_add': 'yinzijue'}
    cols = get_column_info('PwdMgr')['en_col_name']
    print(get_new_data(cols, data1))
