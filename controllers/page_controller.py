# self.tableView_pwd.setPageController(10)
# self.tableView_pwd.control_signal.connect(self.page_controller)
from PyQt5.QtWidgets import QMessageBox

###################################################################################
    # 表格分页功能,https://blog.csdn.net/zizle_lin/article/details/89474813
    def setPageController(self, page):
        self.label_total_pages.setText(page)
        self.pushButton_home_page.clicked.connect(self.__home_page)
        self.pushButton_previous_page.clicked.connect(self.__pre_page)
        self.pushButton_next_page.clicked.connect(self.__next_page)
        self.pushButton_final_page.clicked.connect(self.__final_page)
        self.pushButton_confirm_skip.clicked.connect(self.__confirm_skip)

    def __home_page(self):
        """点击首页信号"""
        self.control_signal.emit(["home", self.lineEdit_current_page.text()])

    def __pre_page(self):
        """点击上一页信号"""
        self.control_signal.emit(["pre", self.lineEdit_current_page.text()])

    def __next_page(self):
        """点击下一页信号"""
        self.control_signal.emit(["next", self.lineEdit_current_page.text()])

    def __final_page(self):
        """尾页点击信号"""
        self.control_signal.emit(["final", self.lineEdit_current_page.text()])

    def __confirm_skip(self):
        """跳转页码确定"""
        self.control_signal.emit(["confirm", self.lineEdit_skip_page.text()])

    def showTotalPage(self):
        """返回当前总页数"""
        return int(self.label_total_pages.text()[1:-1])

    def page_controller(self, signal):
        total_page = self.table_widget.showTotalPage()
        if "home" == signal[0]:
            self.table_widget.curPage.setText("1")
        elif "pre" == signal[0]:
            if 1 == int(signal[1]):
                QMessageBox.information(self, "提示", "已经是第一页了", QMessageBox.Yes)
                return
            self.table_widget.curPage.setText(str(int(signal[1]) - 1))
        elif "next" == signal[0]:
            if total_page == int(signal[1]):
                QMessageBox.information(self, "提示", "已经是最后一页了", QMessageBox.Yes)
                return
            self.table_widget.curPage.setText(str(int(signal[1]) + 1))
        elif "final" == signal[0]:
            self.table_widget.curPage.setText(str(total_page))
        elif "confirm" == signal[0]:
            if total_page < int(signal[1]) or int(signal[1]) < 0:
                QMessageBox.information(self, "提示", "跳转页码超出范围", QMessageBox.Yes)
                return
            self.table_widget.curPage.setText(signal[1])

        self.changeTableContent()  # 改变表格内容

    # def changeTableContent(self):
    #     """根据当前页改变表格的内容"""
    #     pass


###################################################################################