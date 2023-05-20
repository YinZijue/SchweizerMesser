import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QVBoxLayout, QHBoxLayout, QPushButton

from demo.combobox.untitled import Ui_MainWindow


class Test(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Test, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_message)

    def show_message(self):
        message_box = QMessageBox()
        message_box.setWindowTitle("提示")
        message_box.setIcon(QMessageBox.Warning)
        message_box.setText("是否确定退出？")
        # 创建一个接受按钮，并设置角色为 AcceptRole
        accept_button = message_box.addButton("确定", QMessageBox.AcceptRole)
        # 设置样式
        style_sheet = """
            QMessageBox {
                font-size: 12px;
            }
            QPushButton[role="acceptRole"] {
                background-color: #FF0000;
                color: white;
                padding-top: 5px;
                padding-bottom: 5px;
                padding-left: 20px;
                padding-right: 20px;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
        """
        message_box.setStyleSheet(style_sheet)
        # 调整对话框和按钮布局
        for widget in message_box.findChildren(QVBoxLayout):
            widget.setAlignment(Qt.AlignCenter)
        for widget in message_box.findChildren(QHBoxLayout):
            widget.setAlignment(Qt.AlignCenter)
        # 设置对接受按钮的样式
        accept_button_object = message_box.findChild(QPushButton, "qt_msgbox_buttonbox").button(QMessageBox.AcceptRole)
        accept_button_object.setStyleSheet("QPushButton[role='acceptRole']{" + style_sheet + "}")
        message_box.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tt = Test()
    tt.show()
    sys.exit(app.exec_())
