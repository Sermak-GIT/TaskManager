from PyQt5 import QtCore, QtWidgets

from src.manager.sqlmanager import *

entry_list = ()


def init_handler(ui_instance):
    global ui
    ui = ui_instance


def init_from_db():
    init()
    entries = get_all_entries()
    for e in entries:
        add_widget(e)


def add_widget(entry):
    global entry_list
    from src.ui.entry_widget import Ui_EntryWidget
    lineTop = QtWidgets.QFrame()
    lineTop.setGeometry(QtCore.QRect(110, 140, 118, 3))
    lineTop.setFrameShape(QtWidgets.QFrame.HLine)
    lineTop.setFrameShadow(QtWidgets.QFrame.Plain)
    lineBot = QtWidgets.QFrame()
    lineBot.setGeometry(QtCore.QRect(110, 140, 118, 3))
    lineBot.setFrameShape(QtWidgets.QFrame.HLine)
    lineBot.setFrameShadow(QtWidgets.QFrame.Plain)
    new_entry = Ui_EntryWidget()
    next_action = entry[1]
    new_entry.init_content(next_action)
    ui.scrollLayout.addRow(lineTop)
    ui.scrollLayout.addRow(new_entry)
    ui.scrollLayout.addRow(lineBot)

    entry_list = entry_list + ((entry, new_entry, lineTop, lineBot),)


def color_alternate():
    pass
    # TODO
    # i = 0
    # while ui.scrollLayout.takeAt(i) is not None:
    #     if i % 2 == 0:
    #         pass
    #         ui.scrollLayout.takeAt(i).setStyleSheet("background-color:#999999;")
    #     else:
    #         pass
    #        # ui.scrollLayout.takeAt(i).setStyleSheet("background-color:#ffffff;")
    #     i += 1
    #     print(i)


def search(text):
    color_alternate()
    for entry_pair in entry_list:
        entry = entry_pair[0]
        next_action = entry[1]
        if text.replace(" ", "") in next_action.replace(" ", ""):
            entry_pair[1].setMaximumHeight(100)
            entry_pair[1].show()
            entry_pair[1].setVisible(True)
            entry_pair[2].setMaximumHeight(3)
            entry_pair[2].setVisible(True)
            entry_pair[2].show()
            entry_pair[3].setMaximumHeight(3)
            entry_pair[3].setVisible(True)
            entry_pair[3].show()
        else:
            entry_pair[1].hide()
            entry_pair[1].resize(0, 0)
            entry_pair[1].setVisible(False)
            entry_pair[2].hide()
            entry_pair[2].setVisible(False)
            entry_pair[2].resize(0, 0)
            entry_pair[3].hide()
            entry_pair[3].setVisible(False)
            entry_pair[3].resize(0, 0)
