# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\egidi\Documents\Taskmanager\ui\new.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from src.reference.reference import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QWidget, QShortcut

from src.ui_handler.new_handler import save, init_handler


class Ui_New(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        init_handler(self)
        self.resize(1100, 817)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_2.addWidget(self.calendarWidget, 1, 0, 2, 1)
        self.textEdit = QtWidgets.QTextEdit(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 1, 2, 5, 1)
        self.nextAction = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.nextAction.setFont(font)
        self.nextAction.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.nextAction.setInputMask("")
        self.nextAction.setText("")
        self.nextAction.setObjectName("nextAction")
        self.gridLayout_2.addWidget(self.nextAction, 0, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 0, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 2, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 2, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 2, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 3, 0, 2, 1)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("save_button")
        self.gridLayout_2.addWidget(self.pushButton, 6, 2, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(self)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_2.addWidget(self.timeEdit, 5, 0, 1, 1)

        self.save_shortcut = QShortcut(QKeySequence(save_shortcut_keys), self)
        self.save_shortcut.activated.connect(self.save_entry)

        self.switch_right_shortcut = QShortcut(QKeySequence(switch_right_shortcut_keys), self)
        from src.ui_handler.main_handler import change_ui_right, change_ui_left
        self.switch_right_shortcut.activated.connect(change_ui_right)
        self.switch_right_shortcut2 = QShortcut(QKeySequence(switch_right_shortcut_keys2), self)
        self.switch_right_shortcut2.activated.connect(change_ui_right)
        self.switch_left_shortcut = QShortcut(QKeySequence(switch_left_shortcut_keys), self)
        self.switch_left_shortcut.activated.connect(change_ui_left)
        self.switch_left_shortcut2 = QShortcut(QKeySequence(switch_left_shortcut_keys2), self)
        self.switch_left_shortcut2.activated.connect(change_ui_left)

        self.retranslateUi(self)

        self.init_buttons()

    def save_entry(self):
        next_action = self.nextAction.text()
        notes = self.textEdit.toPlainText()
        save(next_action, notes)

    def retranslateUi(self, New):
        _translate = QtCore.QCoreApplication.translate
        New.setWindowTitle(_translate("New", "New"))
        self.textEdit.setPlaceholderText(_translate("New", "Notes"))
        self.nextAction.setPlaceholderText(_translate("New", "Next Action"))
        self.groupBox.setTitle(_translate("New", "GroupBox"))
        self.checkBox_3.setText(_translate("New", "CheckBox"))
        self.checkBox_5.setText(_translate("New", "CheckBox"))
        self.checkBox_2.setText(_translate("New", "CheckBox"))
        self.checkBox.setText(_translate("New", "CheckBox"))
        self.checkBox_4.setText(_translate("New", "CheckBox"))
        self.checkBox_6.setText(_translate("New", "CheckBox"))
        self.pushButton.setText(_translate("New", "Save"))

    def init_buttons(self):
        self.pushButton.clicked.connect(self.save_entry)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_New()
    ui.show()
    sys.exit(app.exec_())

