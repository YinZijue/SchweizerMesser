from PyQt5.QtCore import QVariant, QModelIndex, QAbstractTableModel, Qt

from models.db_engine import get_column_info


class UserTableModel(QAbstractTableModel):
    def __init__(self, data=None, parent=None):
        super().__init__(parent)
        self._headers = get_column_info()[0:8]
        self._data = data or []

    def rowCount(self, parent=QModelIndex()):
        return 10

    def columnCount(self, parent=QModelIndex()):
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return QVariant()
        if role in (Qt.DisplayRole, Qt.EditRole):
            row = index.row()
            col = index.column()
            if row < len(self._data):
                if self._data:
                    return self._data[row][col]
                else:
                    return []
        return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._headers[section]
        return QVariant()

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and role == Qt.EditRole:
            row = index.row()
            col = index.column()
            if self._data:
                return self._data[row][col]
            else:
                return []
            self.dataChanged.emit(index, index, (Qt.DisplayRole,))
            return True
        return False
