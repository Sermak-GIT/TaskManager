# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\egidi\Documents\Taskmanager\ui\all.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QAbstractItemModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QListWidgetItem, QWidget, QLabel, QPushButton, QHBoxLayout, QLayout

from src.ui.entry_widget import Ui_EntryWidget


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1022, 647)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.search_bar = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_bar.sizePolicy().hasHeightForWidth())
        self.search_bar.setSizePolicy(sizePolicy)
        self.search_bar.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(48)
        self.search_bar.setFont(font)
        self.search_bar.setClearButtonEnabled(True)
        self.search_bar.setObjectName("search_bar")
        self.gridLayout.addWidget(self.search_bar, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.listView = QtWidgets.QListView(Form)
        self.listView.setMinimumSize(QtCore.QSize(0, 0))
        self.listView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listView.setTabKeyNavigation(True)
        self.listView.setObjectName("listView")

        self.model = QStandardItemModel(self.listView)
        self.listView.setModel(self.model)

        self.verticalLayout.addWidget(self.listView)
        self.retranslateUi(Form)

        self.init_listview()

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.search_bar.setPlaceholderText(_translate("Form", "Search"))
        self.label.setText(_translate("Form", "Sort by:"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.groupBox.setTitle(_translate("Form", "Filters"))

    def init_listview(self):

        new_ui = Ui_EntryWidget()
        New = QtWidgets.QWidget()
        new_ui.setupUi(New)
        New.show()


        itemN = QListWidgetItem()
        self.listView.addItem(itemN)
        self.listView.setItemWidget(New, Ui_EntryWidget)


        """new_ui = Ui_EntryWidget()
        New = QtWidgets.QWidget()
        new_ui.setupUi(New)
        New.show()
        self.listView."""


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

