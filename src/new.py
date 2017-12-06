# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\egidi\Documents\Taskmanager\ui\new.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_New(object):
    def setupUi(self, New):
        New.setObjectName("New")
        New.resize(1100, 817)
        self.gridLayout_2 = QtWidgets.QGridLayout(New)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(New)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_2.addWidget(self.calendarWidget, 1, 0, 2, 1)
        self.textEdit = QtWidgets.QTextEdit(New)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 1, 2, 5, 1)
        self.graphicsView = QtWidgets.QGraphicsView(New)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.nextAction = QtWidgets.QLineEdit(New)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.nextAction.setFont(font)
        self.nextAction.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.nextAction.setInputMask("")
        self.nextAction.setText("")
        self.nextAction.setObjectName("nextAction")
        self.gridLayout_2.addWidget(self.nextAction, 0, 2, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(New)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_2.addWidget(self.timeEdit, 5, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(New)
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

        self.retranslateUi(New)
        QtCore.QMetaObject.connectSlotsByName(New)

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    New = QtWidgets.QWidget()
    ui = Ui_New()
    ui.setupUi(New)
    New.show()
    sys.exit(app.exec_())

