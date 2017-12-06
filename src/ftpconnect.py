# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\egidi\Documents\Taskmanager\ui\ftpconnect.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_FTPConnect(object):
    def setupUi(self, FTPConnect):
        FTPConnect.setObjectName("FTPConnect")
        FTPConnect.resize(872, 578)
        self.gridLayout_2 = QtWidgets.QGridLayout(FTPConnect)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(FTPConnect)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(FTPConnect)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 2, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(FTPConnect)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(FTPConnect)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(FTPConnect)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 6, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(FTPConnect)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 4, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.pushButton.clicked.connect(self.connect)
        self.retranslateUi(FTPConnect)
        QtCore.QMetaObject.connectSlotsByName(FTPConnect)

    def retranslateUi(self, FTPConnect):
        _translate = QtCore.QCoreApplication.translate
        FTPConnect.setWindowTitle(_translate("FTPConnect", "FTP"))
        self.lineEdit.setPlaceholderText(_translate("FTPConnect", "Host"))
        self.lineEdit_4.setPlaceholderText(_translate("FTPConnect", "Port"))
        self.lineEdit_2.setPlaceholderText(_translate("FTPConnect", "Username"))
        self.pushButton.setText(_translate("FTPConnect", "Connect"))
        self.checkBox.setText(_translate("FTPConnect", "Remember"))
        self.lineEdit_3.setPlaceholderText(_translate("FTPConnect", "Password"))

    def connect(self):
        from src import ftpmanager
        ftp = ftpmanager.connect(self.lineEdit.text(), self.lineEdit_4.text(), self.lineEdit_2.text(),
                                 self.lineEdit_4.text())
        if ftp is None:
            self.pushButton.setStyleSheet('QPushButton {background-color: red; color: white;}')
        else:
            pass
            #self.pushButton.setStyleSheet('QPushButton {background-color: green; color: white;}')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    FTPConnect = QtWidgets.QWidget()
    ui = Ui_FTPConnect()
    ui.setupUi(FTPConnect)
    FTPConnect.show()
    sys.exit(app.exec_())
