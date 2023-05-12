from PyQt5.QtWidgets import QApplication, QTableView
import sys
from demo.r3sw import MyTableModel

if __name__ == "__main__":
    app = QApplication(sys.argv)

    data = ['apple', 'banana', 'orange', 'grape']

    table_model = MyTableModel(data)
    table_view = QTableView()
    table_view.setModel(table_model)
    table_view.show()

    sys.exit(app.exec_())
