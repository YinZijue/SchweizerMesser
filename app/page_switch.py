from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from ui.ui_pwd_editor import Ui_Dialog_pwd_add


def page_switched(main_window):
    """
    主菜单切换
    :param main_window:
    :return:
    """
    treeWidget = main_window.treeWidget
    item = treeWidget.currentItem()
    for index in range(main_window.stack_list.count()):
        if item.text(0) == main_window.stack_list.widget(index).accessibleName():
            main_window.stack_list.setCurrentIndex(index)


def open_pwd_add_ui(my_window):
    # new_dialog = QDialog(my_window)
    # pwd_add_ui = Ui_Dialog_pwd_add()
    # pwd_add_ui.setupUi(new_dialog)
    # new_dialog.setFixedSize(new_dialog.width(), new_dialog.height())
    # new_dialog.setWindowFlags(Qt.CustomizeWindowHint)
    # new_dialog.exec_()
    pass
