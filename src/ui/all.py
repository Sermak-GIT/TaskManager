# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\egidi\Documents\Taskmanager\ui\all.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QFormLayout, QWidget, QScrollArea, QShortcut
from src.reference.reference import *

from src.ui_handler.all_handler import init_handler, search
from src.ui_handler.shortcuts import init_shortcuts


class Ui_All(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        init_handler(self)
        self.resize(1022, 647)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.search_bar = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_bar.sizePolicy().hasHeightForWidth())
        self.search_bar.setSizePolicy(sizePolicy)
        self.search_bar.setMaximumSize(QtCore.QSize(16777215, 100))

        self.search_bar.textChanged.connect(self.on_text_change)

        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(48)
        self.search_bar.setFont(font)
        self.search_bar.setClearButtonEnabled(True)
        self.search_bar.setObjectName("search_bar")
        self.gridLayout.addWidget(self.search_bar, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self)
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

        # scroll area widget
        self.scrollLayout = QFormLayout()
        self.scrollLayout.setSpacing(0)
        self.scrollLayout.setVerticalSpacing(0)

        # scroll area widget contents
        self.scrollWidget = QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)

        # scroll area
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)

        self.verticalLayout.addWidget(self.scrollArea)

        init_shortcuts(self)

        self.retranslateUi(self)
        from src.ui_handler.all_handler import init_from_db
        init_from_db()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.search_bar.setPlaceholderText(_translate("Form", "Search"))
        self.label.setText(_translate("Form", "Sort by:"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.groupBox.setTitle(_translate("Form", "Filters"))

    def on_text_change(self):
        search(self.search_bar.text())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_All()
    ui.show()
    sys.exit(app.exec_())
