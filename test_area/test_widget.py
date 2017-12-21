import sys
from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QWidget


class TestWidgetFile(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Label")
        self.horizontalLayout.addWidget(self.label)

        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setText("Checkbox")
        self.horizontalLayout.addWidget(self.checkBox)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setText("Kill me")
        self.pushButton.clicked.connect(self.deleteLater)  # delete button from layout
        self.horizontalLayout.addWidget(self.pushButton)

"""
app = QtWidgets.QApplication(sys.argv)
ui = TestWidgetFile()
ui.show()
sys.exit(app.exec_())"""