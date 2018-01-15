# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\egidi\Documents\Taskmanager\ui\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

from src.reference.reference import top_level_shortcuts
from src.ui_handler.help_handler import init_handler, add_entries, show_top_shortcuts


class Ui_Help(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        init_handler(self)
        self.setObjectName("Help")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Help()
    ui.show()
    sys.exit(app.exec_())