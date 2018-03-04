import qdarkstyle
from PyQt5 import QtWidgets

from src.manager.system_tray_manager import start_system_tray
from src.reference.reference import set_global_app
from src.ui.main import Ui_TaskManagerMainWindow
from src.ui_handler.main_handler import add_taskbar_icon

if __name__ == "__main__":
    import sys

    app = (QtWidgets.QApplication(sys.argv))
    tray = start_system_tray(app)
    add_taskbar_icon(app)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    TaskManagerMainWindow = QtWidgets.QMainWindow()
    set_global_app(TaskManagerMainWindow)
    ui = Ui_TaskManagerMainWindow()
    ui.setupUi(TaskManagerMainWindow)
    TaskManagerMainWindow.show()
    app.exec_()
    #sys.exit(tray)
