# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pwd_editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_pwd_add(object):
    def setupUi(self, Dialog_pwd_add):
        Dialog_pwd_add.setObjectName("Dialog_pwd_add")
        Dialog_pwd_add.resize(411, 588)
        self.label = QtWidgets.QLabel(Dialog_pwd_add)
        self.label.setGeometry(QtCore.QRect(0, 10, 91, 16))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Dialog_pwd_add)
        self.groupBox.setGeometry(QtCore.QRect(10, 510, 411, 81))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.p_btn_pwd_reset = QtWidgets.QPushButton(self.groupBox)
        self.p_btn_pwd_reset.setGeometry(QtCore.QRect(10, 30, 75, 31))
        self.p_btn_pwd_reset.setObjectName("p_btn_pwd_reset")
        self.p_btn_pwd_cancel = QtWidgets.QPushButton(self.groupBox)
        self.p_btn_pwd_cancel.setGeometry(QtCore.QRect(100, 30, 75, 31))
        self.p_btn_pwd_cancel.setObjectName("p_btn_pwd_cancel")
        self.p_btn_pwd_save_continue = QtWidgets.QPushButton(self.groupBox)
        self.p_btn_pwd_save_continue.setGeometry(QtCore.QRect(200, 30, 75, 31))
        self.p_btn_pwd_save_continue.setObjectName("p_btn_pwd_save_continue")
        self.p_btn_pwd_save_exit = QtWidgets.QPushButton(self.groupBox)
        self.p_btn_pwd_save_exit.setGeometry(QtCore.QRect(300, 30, 75, 31))
        self.p_btn_pwd_save_exit.setObjectName("p_btn_pwd_save_exit")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog_pwd_add)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 30, 411, 481))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_url_add = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_url_add.setGeometry(QtCore.QRect(70, 200, 291, 30))
        self.lineEdit_url_add.setMaxLength(64)
        self.lineEdit_url_add.setObjectName("lineEdit_url_add")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 31, 30))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(30, 140, 41, 30))
        self.label_7.setObjectName("label_7")
        self.label_notice = QtWidgets.QLabel(self.groupBox_2)
        self.label_notice.setGeometry(QtCore.QRect(70, 55, 291, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_notice.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setWeight(75)
        self.label_notice.setFont(font)
        self.label_notice.setObjectName("label_notice")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 80, 41, 30))
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(30, 340, 31, 30))
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(30, 240, 31, 30))
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(30, 200, 31, 30))
        self.label_8.setObjectName("label_8")
        self.lineEdit_pwd_add = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_pwd_add.setGeometry(QtCore.QRect(70, 140, 291, 30))
        self.lineEdit_pwd_add.setMaxLength(32)
        self.lineEdit_pwd_add.setObjectName("lineEdit_pwd_add")
        self.comboBox_pwd_category_add = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_pwd_category_add.setGeometry(QtCore.QRect(70, 340, 291, 31))
        self.comboBox_pwd_category_add.setMaxVisibleItems(8)
        self.comboBox_pwd_category_add.setObjectName("comboBox_pwd_category_add")
        self.plainTextEdit_remark_add = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_remark_add.setGeometry(QtCore.QRect(70, 250, 291, 71))
        self.plainTextEdit_remark_add.setObjectName("plainTextEdit_remark_add")
        self.lineEdit_title_add = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_title_add.setGeometry(QtCore.QRect(70, 20, 291, 30))
        self.lineEdit_title_add.setMaxLength(32)
        self.lineEdit_title_add.setObjectName("lineEdit_title_add")
        self.lineEdit_usr_add = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_usr_add.setGeometry(QtCore.QRect(70, 80, 291, 30))
        self.lineEdit_usr_add.setMaxLength(32)
        self.lineEdit_usr_add.setObjectName("lineEdit_usr_add")

        self.retranslateUi(Dialog_pwd_add)
        QtCore.QMetaObject.connectSlotsByName(Dialog_pwd_add)

    def retranslateUi(self, Dialog_pwd_add):
        _translate = QtCore.QCoreApplication.translate
        Dialog_pwd_add.setWindowTitle(_translate("Dialog_pwd_add", "Dialog"))
        self.label.setText(_translate("Dialog_pwd_add", "新增密码"))
        self.p_btn_pwd_reset.setText(_translate("Dialog_pwd_add", "重置"))
        self.p_btn_pwd_cancel.setText(_translate("Dialog_pwd_add", "取消"))
        self.p_btn_pwd_save_continue.setText(_translate("Dialog_pwd_add", "保存并继续"))
        self.p_btn_pwd_save_exit.setText(_translate("Dialog_pwd_add", "保存并退出"))
        self.label_5.setText(_translate("Dialog_pwd_add", "标题："))
        self.label_7.setText(_translate("Dialog_pwd_add", "密码："))
        self.label_6.setText(_translate("Dialog_pwd_add", "用户名："))
        self.label_10.setText(_translate("Dialog_pwd_add", "分组："))
        self.label_9.setText(_translate("Dialog_pwd_add", "备注："))
        self.label_8.setText(_translate("Dialog_pwd_add", "网址："))