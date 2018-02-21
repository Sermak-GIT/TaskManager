from PyQt5 import QtCore, QtWidgets

from src.manager.sqlmanager import *

entry_list = []


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

    entry_list += [[entry, new_entry, lineTop, lineBot], ]


def remove_widget(entry):
    for entry_element in entry_list:
        if entry[0] == entry_element[0][0]:
            ui.scrollLayout.removeRow(entry_element[1])
            ui.scrollLayout.removeRow(entry_element[2])
            ui.scrollLayout.removeRow(entry_element[3])
            entry_list.remove(entry_element)
            return


def remove_all_widgets():
    for i in range(10):
        for entry_element in entry_list:
            ui.scrollLayout.removeRow(entry_element[1])
            ui.scrollLayout.removeRow(entry_element[2])
            ui.scrollLayout.removeRow(entry_element[3])
            entry_list.remove(entry_element)


def show_widget(entry):
    for entry_element in entry_list:
        if entry[0] == entry_element[0][0]:
            ui.scrollLayout.addRow(entry_element[1])
            ui.scrollLayout.addRow(entry_element[2])
            ui.scrollLayout.addRow(entry_element[3])
            return
    add_widget(entry)


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


def search(text):
    global entry_list
    text = handle_settings(text)
    remove_all_widgets()
    for entry_pair in get_all_entries():
        next_action = entry_pair[1]
        if ui.check_ignore_case.isChecked():
            matches = text.replace(" ", "").casefold() in next_action.replace(" ", "").casefold()
        else:
            matches = text.replace(" ", "") in next_action.replace(" ", "")
        if matches:
            show_widget(entry_pair)


def set_location_text(text):
    ui.groupBox.setTitle(text)


def clear_search_bar():
    ui.search_bar.setText("")


def set_search_bar_focus():
    ui.search_bar.setFocus()


def get_selected_entry_data():
    for entry in entry_list:
        if "background-color:#999999;" in entry[1].label.styleSheet():
            return entry[0]


def select_next():
    next_needs_focus = False
    for entry in entry_list:
        if next_needs_focus:
            entry[1].label.setStyleSheet("background-color:#999999;")
            entry[1].big_mode()
            ui.scrollArea.ensureWidgetVisible(entry[1])
            return
        elif "background-color:#999999;" in entry[1].label.styleSheet():
            next_needs_focus = True
            entry[1].label.setStyleSheet("")
            entry[1].small_mode()
    if next_needs_focus:
        entry_list[-1][1].label.setStyleSheet("background-color:#999999;")
        entry_list[-1][1].big_mode()
        ui.scrollArea.ensureWidgetVisible(entry_list[-1][1])
    else:
        if entry_list.__len__() > 0:
            entry_list[0][1].label.setStyleSheet("background-color:#999999;")
            entry_list[0][1].big_mode()
            ui.scrollArea.ensureWidgetVisible(entry_list[0][1])


def select_prev():
    prev = None
    for entry in entry_list:
        if "background-color:#999999;" in entry[1].label.styleSheet():
            if prev:
                prev[1].label.setStyleSheet("background-color:#999999;")
                prev[1].big_mode()
                ui.scrollArea.ensureWidgetVisible(prev[1])
                entry[1].label.setStyleSheet("")
                entry[1].small_mode()
            else:
                entry_list[0][1].label.setStyleSheet("background-color:#999999;")
                entry_list[0][1].big_mode()
                ui.scrollArea.ensureWidgetVisible(entry_list[0][1])
            return
        else:
            prev = entry


def delete():
    for entry in entry_list:
        if "background-color:#999999;" in entry[1].label.styleSheet():
            select_prev()
            delete_entry(entry[0][0])
            remove_widget(entry)
            search(ui.search_bar.text())
            select_next()
            return
