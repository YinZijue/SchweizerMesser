from PyQt5.QtCore import Qt, QModelIndex, QVariant, QAbstractTableModel


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data  # 表格数据

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._data[0])

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            row = index.row()
            col = index.column()
            return QVariant(str(self._data[row][col]))
        return QVariant()

    def setData(self, index, value, role=Qt.EditRole):
        """
        用于设置
        :param index:
        :param value:
        :param role:
        :return:
        """
        if role == Qt.EditRole:
            row = index.row()
            col = index.column()
            self._data[row][col] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsEditable | super().flags(index)
