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
