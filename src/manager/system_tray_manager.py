import os
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QMenu, QAction, QSystemTrayIcon, QApplication


class RightClickMenu(QMenu):
    def __init__(self, parent=None):
        QMenu.__init__(self, "Edit", parent)

        icon = QtGui.QIcon.fromTheme("edit-cut")
        self.addAction(QAction(icon, "Cut (&X)", self))

        icon = QIcon.fromTheme("edit-copy")
        self.addAction(QAction(icon, "&Copy", self))

        icon = QIcon.fromTheme("edit-paste")
        self.addAction(QAction(icon, "&Paste", self))


class LeftClickMenu(QMenu):
    def __init__(self, parent=None):
        QMenu.__init__(self, "File", parent)

        icon = QIcon.fromTheme("document-new")
        self.addAction(QAction(icon, "&New", self))

        icon = QIcon.fromTheme("document-open")
        self.addAction(QAction(icon, "&Open", self))

        icon = QIcon.fromTheme("document-save")
        self.addAction(QAction(icon, "&Save", self))


class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        QSystemTrayIcon.__init__(self, parent)
        icon_path = os.path.join(os.path.abspath(""), "src", "ui", "images", "main_icon.png")
        icon = QIcon()
        from PyQt5.QtCore import QSize
        icon.addFile(icon_path, QSize(1600, 1600))
        self.setIcon(icon)

        self.right_menu = RightClickMenu()
        self.setContextMenu(self.right_menu)

        self.left_menu = LeftClickMenu()

        self.activated.connect(self.click_trap)

    def click_trap(self, value):
        if value == self.Trigger:  # left click!
            #self.left_menu.exec_(QCursor.pos())
            from src.reference.reference import master_ui
            from src.reference.reference import toggle_global_app
            #master_ui.setVisible(False)
            toggle_global_app()

    def welcome(self):
        pass
        #self.showMessage("Hello", "I should be aware of both buttons")

    def show(self):
        QSystemTrayIcon.show(self)
        #QtCore.QTimer.singleShot(100, self.welcome)


if __name__ == "__main__":
    app = QApplication([])

    tray = SystemTrayIcon()
    tray.show()

    # set the exec loop going
    app.exec_()


def start_system_tray(parent=None):
    tray = SystemTrayIcon(parent)
    tray.setToolTip("GNU/Tskmgr")
    tray.show()
    return tray