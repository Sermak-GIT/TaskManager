# Form implementation generated from reading ui file 'C:\Users\egidi\Documents\Taskmanager\ui\entry_widget.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class Ui_EntryWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setMaximumHeight(100)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self)
        self.setAutoFillBackground(True)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setMaximumWidth(90)
        self.graphicsView.setMaximumHeight(90)
        self.graphicsView.setMinimumHeight(90)
        self.graphicsView.setMinimumWidth(90)
        self.horizontalLayout_2.addWidget(self.graphicsView)
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setSizeIncrement(QtCore.QSize(10, 10))
        self.checkBox.setBaseSize(QtCore.QSize(100, 100))
        self.checkBox.setAcceptDrops(False)
        self.checkBox.setStyleSheet("")
        self.checkBox.setText("")
        self.checkBox.setChecked(False)
        self.checkBox.setAutoRepeat(False)
        self.checkBox.setAutoExclusive(False)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)

        self.retranslateUi(self)

        self.small_mode()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))

    def init_content(self, next_action):
        self.label.setText(next_action)

    def small_mode(self):
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        self.label.setFont(font)
        self.setMaximumHeight(50)
        self.graphicsView.setMaximumWidth(35)
        self.graphicsView.setMaximumHeight(35)
        self.graphicsView.setMinimumHeight(35)
        self.graphicsView.setMinimumWidth(35)

    def big_mode(self):
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(36)
        self.label.setFont(font)
        self.setMaximumHeight(100)
        self.graphicsView.setMaximumWidth(80)
        self.graphicsView.setMaximumHeight(80)
        self.graphicsView.setMinimumHeight(80)
        self.graphicsView.setMinimumWidth(80)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_EntryWidget()
    ui.show()
    sys.exit(app.exec_())
