import sys

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView

from models.pwd_mgr_models import PwdMgr
from ui.interface import Ui_MainWindow
from models.db_engine import get_column_info


class MainWindow(QMainWindow, Ui_MainWindow):
    control_signal = pyqtSignal(list)

    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.data_model = QStandardItemModel(10, get_column_info()['main_col_count'])
        self.data_model.setHorizontalHeaderLabels(get_column_info()['main_col'])
        self.tableView_pwd.setModel(self.data_model)
        self.tableView_pwd.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_pwd.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.treeWidget.clicked.connect(self.page_switched)
        self.toolButton_pwd_query.clicked.connect(self.query_pwd)
        self.toolButton_pwd_reset_conditons.clicked.connect(self.reset_conditions_pwd)
        # 监听鼠标点击事件，若该控件被点击，则用list填充combobox
        self.comboBox_pwd_category.installEventFilter(self)

    # 菜单页切换
    def page_switched(self):
        item = self.treeWidget.currentItem()
        for index in range(self.stack_list.count()):
            if item.text(0) == self.stack_list.widget(index).accessibleName():
                self.stack_list.setCurrentIndex(index)

    # 重置密码查询条件
    def reset_conditions_pwd(self):
        self.lineEdit_title.clear()
        self.lineEdit_usr.clear()
        self.comboBox_pwd_category.clear()
        self.lineEdit_url.clear()
        self.lineEdit_remarks.clear()
        self.label_result_notice.clear()

    def query_pwd(self):
        # 查询前先清理上一次的查询结果
        for i in range(10):
            for j in range(get_column_info()['main_col_count']):
                clear_item = QStandardItem('')
                self.data_model.setItem(i, j, clear_item)
        conditions = {
            'title': self.lineEdit_title.text(),
            'usr': self.lineEdit_usr.text(),
            'url': self.lineEdit_url.text(),
            'remarks': self.lineEdit_remarks.text(),
            'category': self.comboBox_pwd_category.currentText()
        }
        pwd_records = [p.to_dict() for p in PwdMgr().get_pwd(conditions=conditions)]
        # 查询结果是一个列表中嵌套了字典，每一个字典代表一行记录，理论上应当按行显示结果，
        # 但实际使用的方法是按单元格填充，使用枚举函数给查询结果的每一个元素带上坐标，然后填充到对应单元格中
        if pwd_records:
            for rows, pwd_record in enumerate(pwd_records):
                for columns, pwd_info in enumerate(list(pwd_record.values())):
                    if columns < get_column_info()['main_col_count']:  # 该界面不需要显示删除标识和删除时间
                        item = QStandardItem(pwd_info)
                        self.data_model.setItem(rows, columns, item)
        else:
            self.label_result_notice.setText('当前查询条件下，查询无结果。')

    def eventFilter(self, a0: 'QObject', a1: 'QEvent') -> bool:
        # 鼠标按下comboBox时从数据库获取分组
        if a0 == self.comboBox_pwd_category and a1.type() == QtCore.QEvent.MouseButtonPress:
            category_list = [category.to_dict()['category'] for category in PwdMgr.get_pwd({'category': ''})]
            self.comboBox_pwd_category.addItems(category_list)
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
