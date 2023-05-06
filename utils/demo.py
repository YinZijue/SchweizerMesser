from PyQt5.QtWidgets import QInputDialog, QLineEdit


def getText(self, okPressed=None):
    text,boolAction = QInputDialog.getText(self,'获取信息','请输入数据库名',QLineEdit.Normal)
    if okPressed and text != '':
        print(text)


if __name__ == '__main__':
    getText()