from PyQt5.QtCore import Qt, QModelIndex, QVariant
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QHeaderView
from PyQt5.QtCore import QAbstractTableModel, Qt


class MyTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self._data)

    def columnCount(self, parent=QModelIndex()) -> int:
        return len(self._data[0])

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return QVariant()

        row, col = index.row(), index.column()
        if role == Qt.DisplayRole:
            return str(self._data[row][col])
        return QVariant()

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return f'Col {section + 1}'
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return f'Row {section + 1}'
        return QVariant()


class MainWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()

        # 创建数据模型
        self.model = MyTableModel(data)

        # 创建QTableView并设置数据模型
        self.tableView = QTableView()
        self.tableView.setModel(self.model)

        # 设置每一行的高度为25
        vert_header = self.tableView.verticalHeader()
        vert_header.setDefaultSectionSize(25)

        # 设置第一列的宽度为100
        hori_header = self.tableView.horizontalHeader()
        hori_header.setSectionResizeMode(0, QHeaderView.Fixed)
        hori_header.resizeSection(0, 100)

        # 设置窗口大小并显示
        self.setGeometry(100, 100, 500, 300)
        self.setCentralWidget(self.tableView)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    data = [[i for i in range(2)] for j in range(3)]
    window = MainWindow(data)
    app.exec_()
