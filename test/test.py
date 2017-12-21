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
    def __init__(self):
        QWidget.__init__(self)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Label")
        self.horizontalLayout.addWidget(self.label)

        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setText("Checkbox")
        self.horizontalLayout.addWidget(self.checkBox)
        """
    def setupUi(self, Form):
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)

        self.label = QtWidgets.QLabel(Form)
        self.label.setText("Label")
        self.horizontalLayout.addWidget(self.label)

        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setText("Checkbox")
        self.horizontalLayout.addWidget(self.checkBox)
"""

class AbsolutePositioningExample(QWidget):
    ''' An example of PySide absolute positioning; the main window
        inherits from QWidget, a convenient widget for an empty window. '''

    def __init__(self):
        # Initialize the object as a QWidget
        QWidget.__init__(self)

        # We have to set the size of the main window
        # ourselves, since we control the entire layout
        self.setMinimumSize(400, 185)
        self.setWindowTitle('Dynamic Greeter')

        # Create the controls with this object as their parent and set
        # their position individually; each row is a label followed by
        # another control

        # Label for the salutation chooser
        self.salutation_lbl = QLabel('Salutation:', self)
        self.salutation_lbl.move(5, 5)  # offset the first control 5px
        # from top and left
        self.salutations = ['Ahoy',
                            'Good day',
                            'Hello',
                            'Heyo',
                            'Hi',
                            'Salutations',
                            'Wassup',
                            'Yo']
        # Create and fill the combo box to choose the salutation
        self.salutation = QComboBox(self)
        self.salutation.addItems(self.salutations)

        # Allow 100px for the label and 5px each for borders at the
        # far left, between the label and the combobox, and at the far
        # right
        self.salutation.setMinimumWidth(285)
        # Place it five pixels to the right of the end of the label
        self.salutation.move(110, 5)

        # The label for the recipient control
        self.recipient_lbl = QLabel('Recipient:', self)
        # 5 pixel indent, 25 pixels lower than last pair of widgets
        self.recipient_lbl.move(5, 30)

        # The recipient control is an entry textbox
        self.recipient = QLineEdit(self)
        # Add some ghost text to indicate what sort of thing to enter
        self.recipient.setPlaceholderText('world' or 'Matey')
        # Same width as the salutation
        self.recipient.setMinimumWidth(285)
        # Same indent as salutation but 25 pixels lower
        self.recipient.move(110, 30)

        # The label for the greeting widget
        self.greeting_lbl = QLabel('Greeting:', self)
        # Same indent as the others, but 45 pixels lower so it has
        # physical separation, indicating difference of function
        self.greeting_lbl.move(5, 75)

        # The greeting widget is also a label
        self.greeting = QLabel('', self)
        # Same indent as the other controls
        self.greeting.move(110, 75)

        # The build button is a push button
        self.build_button = QPushButton('&amp;Build Greeting', self)

        # Place it at the bottom right, narrower than
        # the other interactive widgets
        self.build_button.setMinimumWidth(145)
        self.build_button.move(250, 150)
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
