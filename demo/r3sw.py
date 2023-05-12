from PyQt5.QtCore import QAbstractTableModel, Qt


class MyTableModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self._data = data
        # self._rows = rows

    def rowCount(self, parent=None):
        # return len(self._data)
        return 10
    def columnCount(self, parent=None):
        return len(self._data[0])  # 只有一列

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        row = index.row()
        if role == Qt.DisplayRole and row < len(self._data):
            return self._data[row]
        else:
            return ''
