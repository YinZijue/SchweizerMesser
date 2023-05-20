from PyQt5.QtCore import Qt, QAbstractTableModel, QVariant
from PyQt5.QtGui import QColor


class TableModel(QAbstractTableModel):
    def __init__(self, data=None, header=None, parent=None):
        super().__init__(parent)
        self._data = data or []
        self._header = header or []

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        if self._data:
            return len(self._data[0])
        return 0

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return QVariant()

        row = index.row()
        col = index.column()

        if role == Qt.DisplayRole:
            value = self._data[row][col]
            return str(value)

        if role == Qt.BackgroundRole:
            if row % 2 == 0:
                return QVariant(QColor(Qt.lightGray).lighter(105 + row))
            else:
                return QVariant(QColor(Qt.gray).lighter(105 + row))

        return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return QVariant()

        if orientation == Qt.Horizontal:
            return self._header[section]

        return section + 1

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable


if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication, QTableView

    app = QApplication(sys.argv)

    data = [
        # ["apple", "orange", "banana", "grape"],
        # [1, 2, 3, 4],
        # [4, 3, 2, 1],
        # [0.1, 0.2, 0.3, 0.4]
    ]
    header = ["Fruit", "Number1", "Number2", "Decimals"]

    table_model = TableModel(data, header)

    table_view = QTableView()
    table_view.setModel(table_model)

    table_view.setColumnWidth(0, 150)
    table_view.show()

    sys.exit(app.exec_())