# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\egidi\Documents\Taskmanager\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import logging

import qdarkstyle as qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut, QWidget, QLabel, QSizePolicy

from src.reference.reference import master_ui, init_master_ui
from src.ui.all import Ui_All
from src.ui.new import Ui_New
from src.ui_handler.main_handler import init_handler


class Ui_TaskManagerMainWindow(QWidget):
    def setupUi(self, TaskManagerMainWindow):
        init_master_ui(self)
        init_handler(self)
        TaskManagerMainWindow.setObjectName("TaskManagerMainWindow")
        TaskManagerMainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(TaskManagerMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMouseTracking(True)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setObjectName("stackedWidget")

        self.new_page = Ui_New()
        self.all_page = Ui_All()

        self.stackedWidget.addWidget(self.new_page)
        self.stackedWidget.addWidget(self.all_page)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        TaskManagerMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TaskManagerMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 982, 21))
        self.menubar.setObjectName("menubar")

        self.menubar.addMenu("Menu")
        self.menubar.addSeparator()
        self.menubar.hide()


        TaskManagerMainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(TaskManagerMainWindow)
        self.statusBar.setObjectName("statusBar")
        TaskManagerMainWindow.setStatusBar(self.statusBar)

        from src.ui.help import Ui_Help
        self.helpWidget = Ui_Help()
        self.statusBar.addWidget(self.helpWidget)

        self.statusLabel = QLabel()
        self.statusBar.addWidget(self.statusLabel)
        self.retranslateUi(TaskManagerMainWindow)

        self.stackedWidget.setCurrentWidget(self.all_page)

        QtCore.QMetaObject.connectSlotsByName(TaskManagerMainWindow)

    def retranslateUi(self, TaskManagerMainWindow):
        _translate = QtCore.QCoreApplication.translate
        TaskManagerMainWindow.setWindowTitle(_translate("TaskManagerMainWindow", "TaskManager"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    TaskManagerMainWindow = QtWidgets.QMainWindow()
    ui = Ui_TaskManagerMainWindow()
    ui.setupUi(TaskManagerMainWindow)
    TaskManagerMainWindow.show()
    sys.exit(app.exec_())
