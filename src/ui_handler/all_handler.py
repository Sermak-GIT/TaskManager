import pyautogui as pyautogui
from PyQt5 import QtCore, QtWidgets

from src.manager.sqlmanager import *

entry_list = ()
shown_entries = ()


def init_handler(ui_instance):
    global ui
    from src.ui_handler.shortcuts import init_all_shortcuts
    ui = ui_instance
    init_all_shortcuts(ui)


def init_from_db():
    init()
    entries = get_all_entries()
    for e in entries:
        add_widget(e)
    set_shown_entries()


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

    entry_list += ((entry, new_entry, lineTop, lineBot),)


def color_alternate():
    pass  # TODO
    # i = 0
    # while ui.scrollLayout.takeAt(i) is not None:
    #    if i % 2 == 0:
    #        pass
    #        ui.scrollLayout.takeAt(i).setStyleSheet("background-color:#999999;")
    #    else:
    #        pass
    #    # ui.scrollLayout.takeAt(i).setStyleSheet("background-color:#ffffff;")
    #    i += 1
    #    print(i)
    #
    # for entry in shown_entries:
    #    if i % 2 == 0:
    #        ui.scrollLayout.takeAt(i).setStyleSheet("background-color:#999999;")
    #    i += 1


def handle_settings(text):
    new_text = ""
    old_cursor_position = ui.search_bar.cursorPosition()
    for word in text.split(" "):
        if word.startswith("-"):
            if word[1:].upper() == "I":
                ui.check_ignore_case.toggle()
                old_cursor_position -= 3
            else:
                new_text += word + " "
        else:
            new_text += word + " "
    ui.search_bar.setText(new_text[:-1])
    ui.search_bar.setCursorPosition(old_cursor_position)
    return new_text[:-1]


def set_shown_entries():
    global shown_entries
    shown_entries = ()
    for entry_pair in entry_list:
        if entry_pair[1].isVisible():
            shown_entries += (entry_pair,)


def search(text):
    global entry_list
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
            show(entry_pair)
        else:
            hide(entry_pair)
    set_shown_entries()


def show(entry):
    entry[1].setMaximumHeight(100)
    entry[1].show()
    entry[1].setVisible(True)
    entry[2].setMaximumHeight(3)
    entry[2].setVisible(True)
    entry[2].show()
    entry[3].setMaximumHeight(3)
    entry[3].setVisible(True)
    entry[3].show()


def hide(entry):
    entry[1].hide()
    entry[1].resize(0, 0)
    entry[1].setVisible(False)
    entry[2].hide()
    entry[2].setVisible(False)
    entry[2].resize(0, 0)
    entry[3].hide()
    entry[3].setVisible(False)
    entry[3].resize(0, 0)


def set_location_text(text):
    ui.groupBox.setTitle(text)


def clear_search_bar():
    ui.search_bar.setText("")


def set_search_bar_focus():
    ui.search_bar.setFocus()


def select_next():
    global shown_entries
    set_shown_entries()
    next_needs_focus = False
    for entry in shown_entries:
        if next_needs_focus:
            entry[1].label.setStyleSheet("background-color:#999999;")
            ui.scrollArea.ensureWidgetVisible(entry[1])
            return
        elif "background-color:#999999;" in entry[1].label.styleSheet():
            next_needs_focus = True
            entry[1].label.setStyleSheet("")
    if next_needs_focus:
        shown_entries[-1][1].label.setStyleSheet("background-color:#999999;")
        ui.scrollArea.ensureWidgetVisible(shown_entries[-1][1])
    else:
        shown_entries[0][1].label.setStyleSheet("background-color:#999999;")
        ui.scrollArea.ensureWidgetVisible(shown_entries[0][1])


def select_prev():
    global shown_entries
    set_shown_entries()
    prev = None
    for entry in shown_entries:
        if "background-color:#999999;" in entry[1].label.styleSheet():
            if prev:
                prev[1].label.setStyleSheet("background-color:#999999;")
                ui.scrollArea.ensureWidgetVisible(prev[1])
                entry[1].label.setStyleSheet("")
            else:
                shown_entries[0][1].label.setStyleSheet("background-color:#999999;")
                ui.scrollArea.ensureWidgetVisible(shown_entries[0][1])
            return
        else:
            prev = entry


def refresh():
    pass
    #init_from_db()


def delete():
    for entry in shown_entries:
        if "background-color:#999999;" in entry[1].label.styleSheet():
            print(entry[0][0])
            for entry2 in shown_entries:
                hide(entry2)
            delete_entry(entry[0][0])
            init_from_db()
            #select_next()
            #refresh from db, handle search_bar
            return
