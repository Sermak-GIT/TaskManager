import gc
from PyQt5 import QtWidgets

from src.reference.reference import help_screen_max_columns, top_level_shortcuts, master_level_shortcuts, master_ui
from src.ui_handler.shortcuts import init_help_screen_shortcuts

row = 0
column = 0
mode = None


def init_handler(ui_instance):
    global ui
    ui = ui_instance
    init_help_screen_shortcuts(ui)


def add_entry(entry):
    global column, row
    label = QtWidgets.QLabel(ui)
    label.setText(entry)
    ui.gridLayout.addWidget(label, row, column)
    column += 1
    if column > (help_screen_max_columns - 1):
        column = 0
        row += 1


def reset_layout():
    global column, row
    for i in reversed(range(ui.gridLayout.count())):
        ui.gridLayout.itemAt(i).widget().deleteLater()
    row = 0
    column = 0
    gc.collect()


def add_entries(shortcuts):
    reset_layout()
    if shortcuts == master_level_shortcuts:
        for entry in shortcuts:
            add_entry(entry)
    else:
        for entry in shortcuts:
            add_entry(entry[0])


def show_master_shortcuts():
    global mode
    ui.setFocus()
    if mode == "master":
        return
    mode = "master"
    add_entries(master_level_shortcuts)
    master_ui.helpWidget.show()


def show_top_shortcuts():
    global mode
    ui.setFocus()
    if mode == "top":
        return
    mode = "top"
    add_entries(top_level_shortcuts)
    master_ui.helpWidget.show()
