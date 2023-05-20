from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(10)
        self.popMenu = QMenu()
        deleteAction = QAction("删除行", self)
        modifyAction = QAction("修改行", self)
        self.popMenu.addAction(deleteAction)
        self.popMenu.addAction(modifyAction)
        deleteAction.triggered.connect(self.delete_row)
        modifyAction.triggered.connect(self.modify_row)


        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.popMenu.exec_(QCursor.pos())

    def delete_row(self):
        for i in self.tableWidget.selectionModel().selectedRows()[::-1]:
            self.tableWidget.removeRow(i.row())

    def modify_row(self):
        for i in self.tableWidget.selectionModel().selectedRows():
            items = [self.tableWidget.item(i.row(), j).text() for j in range(self.tableWidget.columnCount())]
            # 修改items中的数据
            for j, item in enumerate(items):
                self.tableWidget.setItem(i.row(), j, QTableWidgetItem(item))


if __name__ == '__main__':
    app = QApplication([])
    demo = Demo()
    demo.show()
    app.exec_()
