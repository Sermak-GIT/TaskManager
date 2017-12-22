import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        # top button to add more buttons
        self.addButton = QPushButton('Add button')
        self.addButton.clicked.connect(self.add_button)

        # top button to add more widgets
        self.addWidget = QPushButton('Add widget')
        self.addWidget.clicked.connect(self.add_widget)

        # top button to add more widgets from the other file
        self.addWidgetFile = QPushButton('Add widget from other file')
        self.addWidgetFile.clicked.connect(self.add_widget_from_another_file)

        # scroll area widget
        self.scrollLayout = QFormLayout()

        # scroll area widget contents
        self.scrollWidget = QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)

        # scroll area
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)

        # main layout
        self.mainLayout = QVBoxLayout()

        # add all upper controls to the main vLayout
        self.mainLayout.addWidget(self.addButton)
        self.mainLayout.addWidget(self.addWidget)
        self.mainLayout.addWidget(self.addWidgetFile)
        self.mainLayout.addWidget(self.scrollArea)

        # central widget
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.mainLayout)

        # set central widget
        self.setCentralWidget(self.centralWidget)

    # adds a button to the scroll area
    def add_button(self):
        self.scrollLayout.addRow(TestButton())

    # adds a widget to the scroll area
    def add_widget(self):
        self.scrollLayout.addRow(TestWidget())

    # adds a widget from another file to the scroll area
    def add_widget_from_another_file(self):
        from test_area.test_widget import TestWidgetFile
        from src.ui.entry_widget import Ui_EntryWidget
        self.scrollLayout.addRow(Ui_EntryWidget())


# This is just a test to see what can be added to a layout
class TestButton(QPushButton):
    def __init__(self, parent=None):
        super(TestButton, self).__init__(parent)
        self.setText("When I grow up, I wanna be a real QWidget")
        self.clicked.connect(self.deleteLater)  # delete button from layout


# Copy pasted from other file. As the Widget can get pretty big, I ideally want it in its own file.
class TestWidget(QWidget):
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

print("here")
app = QApplication(sys.argv)
myWidget = Main()
myWidget.show()
app.exec_()
