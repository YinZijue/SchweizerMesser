# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1174, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1171, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_title_area = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_title_area.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_title_area.setObjectName("verticalLayout_title_area")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(190, 50, 981, 781))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_activity_area = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_activity_area.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_activity_area.setObjectName("verticalLayout_activity_area")
        self.scrollArea_main = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
        self.scrollArea_main.setWidgetResizable(True)
        self.scrollArea_main.setObjectName("scrollArea_main")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 977, 777))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.stack_list = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents)
        self.stack_list.setGeometry(QtCore.QRect(0, 0, 971, 781))
        self.stack_list.setAccessibleName("")
        self.stack_list.setObjectName("stack_list")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.label_2 = QtWidgets.QLabel(self.page_home)
        self.label_2.setGeometry(QtCore.QRect(240, 120, 231, 101))
        self.label_2.setObjectName("label_2")
        self.stack_list.addWidget(self.page_home)
        self.page_dict = QtWidgets.QWidget()
        self.page_dict.setObjectName("page_dict")
        self.label_3 = QtWidgets.QLabel(self.page_dict)
        self.label_3.setGeometry(QtCore.QRect(283, 1, 131, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.stack_list.addWidget(self.page_dict)
        self.page_query = QtWidgets.QWidget()
        self.page_query.setObjectName("page_query")
        self.label = QtWidgets.QLabel(self.page_query)
        self.label.setGeometry(QtCore.QRect(300, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.page_query)
        self.plainTextEdit.setGeometry(QtCore.QRect(80, 50, 491, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.btn_translate = QtWidgets.QPushButton(self.page_query)
        self.btn_translate.setGeometry(QtCore.QRect(620, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.btn_translate.setFont(font)
        self.btn_translate.setStyleSheet("")
        self.btn_translate.setObjectName("btn_translate")
        self.stack_list.addWidget(self.page_query)
        self.page_pwd_mgr = QtWidgets.QWidget()
        self.page_pwd_mgr.setObjectName("page_pwd_mgr")
        self.label_4 = QtWidgets.QLabel(self.page_pwd_mgr)
        self.label_4.setGeometry(QtCore.QRect(360, 10, 81, 21))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.groupBox = QtWidgets.QGroupBox(self.page_pwd_mgr)
        self.groupBox.setGeometry(QtCore.QRect(0, 40, 971, 101))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(480, 10, 31, 30))
        self.label_9.setObjectName("label_9")
        self.lineEdit_remark = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_remark.setGeometry(QtCore.QRect(390, 60, 281, 30))
        self.lineEdit_remark.setObjectName("lineEdit_remark")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(240, 10, 41, 30))
        self.label_6.setObjectName("label_6")
        self.lineEdit_usr = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_usr.setGeometry(QtCore.QRect(290, 10, 161, 30))
        self.lineEdit_usr.setObjectName("lineEdit_usr")
        self.lineEdit_url = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_url.setGeometry(QtCore.QRect(40, 60, 291, 30))
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 31, 30))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(350, 60, 31, 30))
        self.label_8.setObjectName("label_8")
        self.lineEdit_title = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_title.setGeometry(QtCore.QRect(40, 10, 171, 30))
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 31, 30))
        self.label_5.setObjectName("label_5")
        self.comboBox_pwd_category = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_pwd_category.setGeometry(QtCore.QRect(520, 10, 181, 30))
        self.comboBox_pwd_category.setMaxVisibleItems(5)
        self.comboBox_pwd_category.setObjectName("comboBox_pwd_category")
        self.toolButton_pwd_query = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_pwd_query.setGeometry(QtCore.QRect(770, 10, 91, 31))
        self.toolButton_pwd_query.setObjectName("toolButton_pwd_query")
        self.toolButton_pwd_reset_conditons = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_pwd_reset_conditons.setGeometry(QtCore.QRect(870, 10, 91, 31))
        self.toolButton_pwd_reset_conditons.setObjectName("toolButton_pwd_reset_conditons")
        self.tableView_pwd = QtWidgets.QTableView(self.page_pwd_mgr)
        self.tableView_pwd.setGeometry(QtCore.QRect(-1, 220, 971, 511))
        self.tableView_pwd.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView_pwd.setAlternatingRowColors(True)
        self.tableView_pwd.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView_pwd.setSortingEnabled(True)
        self.tableView_pwd.setObjectName("tableView_pwd")
        self.tableView_pwd.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView_pwd.verticalHeader().setCascadingSectionResizes(True)
        self.tableView_pwd.verticalHeader().setSortIndicatorShown(False)
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_pwd_mgr)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 140, 971, 80))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.toolButton_pwd_add = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_pwd_add.setGeometry(QtCore.QRect(690, 20, 111, 41))
        self.toolButton_pwd_add.setObjectName("toolButton_pwd_add")
        self.toolButton_pwd_del = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_pwd_del.setGeometry(QtCore.QRect(840, 20, 111, 41))
        self.toolButton_pwd_del.setObjectName("toolButton_pwd_del")
        self.label_result_notice = QtWidgets.QLabel(self.groupBox_2)
        self.label_result_notice.setGeometry(QtCore.QRect(310, 50, 171, 16))
        self.label_result_notice.setText("")
        self.label_result_notice.setObjectName("label_result_notice")
        self.groupBox_3 = QtWidgets.QGroupBox(self.page_pwd_mgr)
        self.groupBox_3.setGeometry(QtCore.QRect(-1, 730, 971, 41))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_home_page = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_home_page.setGeometry(QtCore.QRect(90, 10, 75, 23))
        self.pushButton_home_page.setObjectName("pushButton_home_page")
        self.pushButton_previous_page = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_previous_page.setGeometry(QtCore.QRect(200, 10, 75, 23))
        self.pushButton_previous_page.setObjectName("pushButton_previous_page")
        self.lineEdit_current_page = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_current_page.setGeometry(QtCore.QRect(300, 10, 71, 20))
        self.lineEdit_current_page.setReadOnly(True)
        self.lineEdit_current_page.setObjectName("lineEdit_current_page")
        self.pushButton_next_page = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_next_page.setGeometry(QtCore.QRect(390, 10, 75, 23))
        self.pushButton_next_page.setObjectName("pushButton_next_page")
        self.pushButton_final_page = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_final_page.setGeometry(QtCore.QRect(490, 10, 75, 23))
        self.pushButton_final_page.setObjectName("pushButton_final_page")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(590, 11, 21, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(660, 11, 71, 20))
        self.label_11.setObjectName("label_11")
        self.label_total_pages = QtWidgets.QLabel(self.groupBox_3)
        self.label_total_pages.setGeometry(QtCore.QRect(610, 11, 41, 20))
        self.label_total_pages.setText("")
        self.label_total_pages.setObjectName("label_total_pages")
        self.lineEdit_skip_page = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_skip_page.setGeometry(QtCore.QRect(730, 10, 71, 20))
        self.lineEdit_skip_page.setObjectName("lineEdit_skip_page")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(810, 10, 21, 20))
        self.label_12.setObjectName("label_12")
        self.pushButton_confirm_skip = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_confirm_skip.setGeometry(QtCore.QRect(850, 10, 75, 23))
        self.pushButton_confirm_skip.setObjectName("pushButton_confirm_skip")
        self.stack_list.addWidget(self.page_pwd_mgr)
        self.page_sys_param = QtWidgets.QWidget()
        self.page_sys_param.setObjectName("page_sys_param")
        self.label_13 = QtWidgets.QLabel(self.page_sys_param)
        self.label_13.setGeometry(QtCore.QRect(270, 30, 321, 91))
        self.label_13.setObjectName("label_13")
        self.stack_list.addWidget(self.page_sys_param)
        self.scrollArea_main.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_activity_area.addWidget(self.scrollArea_main)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(-1, 50, 191, 781))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 189, 779))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents_2)
        self.treeWidget.setGeometry(QtCore.QRect(0, 1, 191, 781))
        self.treeWidget.setAccessibleName("")
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stack_list.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.page_home.setAccessibleName(_translate("MainWindow", "欢迎界面"))
        self.label_2.setText(_translate("MainWindow", "欢迎页面"))
        self.page_dict.setAccessibleName(_translate("MainWindow", "本地词典"))
        self.label_3.setText(_translate("MainWindow", "本地词典"))
        self.page_query.setAccessibleName(_translate("MainWindow", "单词查询"))
        self.label.setText(_translate("MainWindow", "单词查询"))
        self.btn_translate.setText(_translate("MainWindow", "翻译"))
        self.page_pwd_mgr.setAccessibleName(_translate("MainWindow", "本地密码"))
        self.label_4.setText(_translate("MainWindow", "密码管理"))
        self.label_9.setText(_translate("MainWindow", "分组："))
        self.label_6.setText(_translate("MainWindow", "用户名："))
        self.label_7.setText(_translate("MainWindow", "网址："))
        self.label_8.setText(_translate("MainWindow", "备注："))
        self.label_5.setText(_translate("MainWindow", "标题："))
        self.toolButton_pwd_query.setText(_translate("MainWindow", "查询"))
        self.toolButton_pwd_reset_conditons.setText(_translate("MainWindow", "重置"))
        self.toolButton_pwd_add.setText(_translate("MainWindow", "新增密码"))
        self.toolButton_pwd_del.setText(_translate("MainWindow", "删除密码"))
        self.pushButton_home_page.setText(_translate("MainWindow", "<<首页"))
        self.pushButton_previous_page.setText(_translate("MainWindow", "<上一页"))
        self.pushButton_next_page.setText(_translate("MainWindow", "下一页>"))
        self.pushButton_final_page.setText(_translate("MainWindow", "末页>>"))
        self.label_10.setText(_translate("MainWindow", "共"))
        self.label_11.setText(_translate("MainWindow", "页     跳至"))
        self.label_12.setText(_translate("MainWindow", "页"))
        self.pushButton_confirm_skip.setText(_translate("MainWindow", "确定"))
        self.page_sys_param.setAccessibleName(_translate("MainWindow", "数据字典"))
        self.label_13.setText(_translate("MainWindow", "数据字典"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "功能菜单"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "词典管理"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "本地词典"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "单词查询"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "密码管理"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "本地密码"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "数据字典"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
# import img_rc
