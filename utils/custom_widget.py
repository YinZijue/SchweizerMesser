from PyQt5.QtWidgets import QMessageBox


def fill_combo_box(data_set: set, widget):
    """
    用集合填充下拉框,填充时去空，去重.
    :param data_set:
    :param widget:
    :return:
    """
    if widget.count() == 0:
        widget.addItems(data_set)
    else:
        for data in data_set:
            if data not in [widget.itemText(idx) for idx in range(0, widget.count())]:
                widget.addItem(data)


def generate_message_box(my_window, ms_type, ms_title, ms_content):
    message_box = QMessageBox(ms_type, ms_title, ms_content)
    q_yes = message_box.addButton(my_window.tr("确定"), QMessageBox.YesRole)
    q_no = message_box.addButton(my_window.tr("取消"), QMessageBox.NoRole)
    message_box.exec_()
    return message_box, q_yes, q_no
