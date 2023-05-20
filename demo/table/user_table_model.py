
from PyQt5.QtCore import QVariant, QModelIndex, QAbstractTableModel, Qt


class UserTableModel(QAbstractTableModel):
    def __init__(self, data=None, parent=None):
        super().__init__(parent)
        self._headers = ['ID', 'Name', 'Age']
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
                if col == 0:
                    return self._data[row].id
                elif col == 1:
                    return self._data[row].name
                elif col == 2:
                    return self._data[row].age
        return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._headers[section]
        return QVariant()

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and role == Qt.EditRole:
            row = index.row()
            col = index.column()
            if row < len(self._data):
                if col == 1:
                    self._data[row].name = value
                elif col == 2:
                    self._data[row].age = value
                self.dataChanged.emit(index, index, (Qt.DisplayRole,))
                return True
        return False
