from demo.test2 import TableModel
from models.pwd_mgr_models import PwdMgr


def main():
    import sys
    from PyQt5.QtWidgets import QApplication, QTableView
    conditions = {
        'title': '',
        'usr': '',
        'url': '',
        'remarks': '',
        'category': ''
    }
    data = [[v for k, v in p.to_dict().items()] for p in PwdMgr(conditions).get_pwd(conditions=conditions)]



    app = QApplication(sys.argv)
    table_model = TableModel(data)
    table_view = QTableView()
    table_view.setModel(table_model)
    table_view.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
