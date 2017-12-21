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
        self.mainLayout.addWidget(self.scrollArea)

        # central widget
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.mainLayout)

        # set central widget
        self.setCentralWidget(self.centralWidget)

    # adds a button to the scroll area
    def add_button(self):
        # from test.test_button import TestButton  # this somehow closes the program when clicking the main button
        self.scrollLayout.addRow(TestButton())

    # adds a widget to the scroll area
    def add_widget(self):
        # from test.test_button import TestButton  # this somehow closes the program when clicking the main button
        self.scrollLayout.addRow(TestWidget())


# Copy pasted from other file. This is just a test to see what can be added to a layout
class TestButton(QPushButton):
    def __init__(self, parent=None):
        super(TestButton, self).__init__(parent)
        self.setText("When I grow up, I wanna be a real QWidget")
        self.clicked.connect(self.deleteLater)  # delete button from layout


# Copy pasted from other file. As the Widget can get pretty big, I ideally want it in its own file.
class TestWidget(QWidget):
    def setupUi(self, Form):
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)

        self.label = QtWidgets.QLabel(Form)
        self.label.setText("Label")
        self.horizontalLayout.addWidget(self.label)

        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setText("Checkbox")
        self.horizontalLayout.addWidget(self.checkBox)

"""
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = TestWidget()
ui.setupUi(Form)
#Form.show()
#sys.exit(app.exec_())
"""

app = QApplication(sys.argv)
myWidget = Main()
myWidget.show()
app.exec_()
