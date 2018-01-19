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


def handle_settings(text):
    new_text = ""
    old_cursor_position = ui.search_bar.cursorPosition()
    for word in text.split(" "):
        if word.startswith("-"):
            if word[1:].upper() == "I":
                ui.check_ignore_case.toggle()
                old_cursor_position -= 2
                new_text += " "
            else:
                new_text += word + " "
        else:
            new_text += word + " "
    ui.search_bar.setText(new_text[:-1])
    ui.search_bar.setCursorPosition(old_cursor_position)
    return new_text[:-1]


def search(text):
    color_alternate()
    text = handle_settings(text)
    for entry_pair in entry_list:
        entry = entry_pair[0]
        next_action = entry[1]
        if ui.check_ignore_case.isChecked():
            matches = text.replace(" ", "").casefold() in next_action.replace(" ", "").casefold()
        else:
            matches = text.replace(" ", "") in next_action.replace(" ", "")
        if matches:
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


def set_location_text(text):
    ui.groupBox.setTitle(text)
