import gc
from PyQt5 import QtWidgets

from src.reference.reference import help_screen_max_columns, top_level_shortcuts, master_level_shortcuts, master_ui, \
    new_note_level_shortcuts, get_shortcut_mode, set_shortcut_mode, all_level_shortcuts, confirm_level_shortcuts, \
    info_level_shortcuts
from src.ui_handler.shortcuts import init_help_screen_shortcuts

row = 0
column = 0


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
    for entry in shortcuts:
        add_entry(entry[0])


def show_master_shortcuts():
    mode = get_shortcut_mode()
    ui.setFocus()
    if mode != "top":
        return
    else:
        set_shortcut_mode("master")
        add_entries(master_level_shortcuts)
    master_ui.helpWidget.show()


def show_top_shortcuts(force=False):
    mode = get_shortcut_mode()
    ui.setFocus()
    if mode == "top":
        return
    elif mode == "new_note" and not force:
        add_entries(new_note_level_shortcuts)
    elif mode == "info" and not force:
        add_entries(info_level_shortcuts)
    elif mode == "all" and not force:
        add_entries(all_level_shortcuts)
    else:
        set_shortcut_mode("top")
        add_entries(top_level_shortcuts)
    master_ui.helpWidget.show()


def show_new_note_shortcuts():
    mode = get_shortcut_mode()
    if mode == "new_note" or mode == "all":
        return
    set_shortcut_mode("new_note")
    add_entries(new_note_level_shortcuts)
    master_ui.helpWidget.show()


def show_info_shortcuts():
    mode = get_shortcut_mode()
    if mode != "all":
        return
    set_shortcut_mode("info")
    add_entries(info_level_shortcuts)
    master_ui.helpWidget.show()
    print(get_shortcut_mode())


def show_all_shortcuts():
    mode = get_shortcut_mode()
    if mode == "all":
        return
    set_shortcut_mode("all")
    add_entries(all_level_shortcuts)
    master_ui.helpWidget.show()


def show_confirm_shortcuts():
    mode = get_shortcut_mode()
    if mode == "confirm":
        return
    set_shortcut_mode("confirm")
    add_entries(confirm_level_shortcuts)
    master_ui.helpWidget.show()


def force_show_top_shortcuts():
    show_top_shortcuts(True)
