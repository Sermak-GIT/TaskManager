from PyQt5.QtWidgets import QPushButton


class TestButton(QPushButton):
    def __init__(self, parent=None):
        super(TestButton, self).__init__(parent)
        self.setText("When I grow up, I wanna be a real QWidget")
        self.clicked.connect(self.deleteLater)