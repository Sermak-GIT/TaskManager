# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\egidi\Documents\Taskmanager\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut, QWidget

from src.ui.new import Ui_New

new_ui = Ui_New()


class Ui_TaskManagerMainWindow(QWidget):
    def setupUi(self, TaskManagerMainWindow):
        TaskManagerMainWindow.setObjectName("TaskManagerMainWindow")
        TaskManagerMainWindow.resize(982, 473)
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

        New = QtWidgets.QWidget()
        new_ui.setupUi(New)
        New.show()
        self.page = New

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        TaskManagerMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TaskManagerMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 982, 21))
        self.menubar.setObjectName("menubar")
        TaskManagerMainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(TaskManagerMainWindow)
        self.statusBar.setObjectName("statusBar")
        TaskManagerMainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(TaskManagerMainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TaskManagerMainWindow)

    def retranslateUi(self, TaskManagerMainWindow):
        _translate = QtCore.QCoreApplication.translate
        TaskManagerMainWindow.setWindowTitle(_translate("TaskManagerMainWindow", "TaskManager"))

    def keyPressEvent(self, QKeyEvent):
        # TODO
        if QKeyEvent.key() == Qt.Key_W:
            self.close()

    def change_ui(self):
        i = (self.stackedWidget.currentIndex() + 1) % (self.stackedWidget.count())
        self.stackedWidget.setCurrentIndex(i)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    TaskManagerMainWindow = QtWidgets.QMainWindow()
    ui = Ui_TaskManagerMainWindow()
    ui.setupUi(TaskManagerMainWindow)
    TaskManagerMainWindow.show()
    sys.exit(app.exec_())
