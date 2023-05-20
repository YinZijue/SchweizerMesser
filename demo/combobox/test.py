import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from demo.combobox.untitled import Ui_MainWindow


class Test(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Test, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_clicked)
        self.comboBox.addItems(['1', '2', '3', '5', '6'])

    def on_clicked(self):
        self.comboBox.setCurrentText('5')
        print([self.comboBox.itemText(i) for i in range(0,self.comboBox.count())])
        self.label.setText(self.comboBox.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Test()
    ui.show()
    sys.exit(app.exec_())
