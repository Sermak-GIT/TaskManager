import qdarkstyle
from PyQt5 import QtWidgets

from src.ui.main import Ui_TaskManagerMainWindow
from src.ui_handler.main_handler import add_taskbar_icon

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    add_taskbar_icon(app)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    TaskManagerMainWindow = QtWidgets.QMainWindow()
    ui = Ui_TaskManagerMainWindow()
    ui.setupUi(TaskManagerMainWindow)
    TaskManagerMainWindow.show()
    sys.exit(app.exec_())
