import logging

import os


def init_handler(ui_instance):
    global ui
    ui = ui_instance


def set_status_text(text):
    ui.statusLabel.setText(text)
    ui.helpWidget.hide()


def reset_status_text():
    ui.statusLabel.setText("")
    ui.helpWidget.show()


def change_ui_right():
    i = (ui.stackedWidget.currentIndex() + 1) % (ui.stackedWidget.count())
    ui.stackedWidget.setCurrentIndex(i)


def change_ui_left():
    i = (ui.stackedWidget.currentIndex() - 1) % (ui.stackedWidget.count())
    ui.stackedWidget.setCurrentIndex(i)


def switch_to_new_note():
    from src.reference.reference import get_shortcut_mode
    mode = get_shortcut_mode()
    if mode != "top":
        return
    ui.stackedWidget.setCurrentWidget(ui.new_page)
    ui.new_page.nextAction.setFocus()
    from src.ui_handler.help_handler import show_new_note_shortcuts
    show_new_note_shortcuts()


def switch_to_info():
    from src.reference.reference import get_shortcut_mode
    mode = get_shortcut_mode()
    if mode != "all":
        return
    ui.stackedWidget.setCurrentWidget(ui.new_page)
    ui.new_page.nextAction.setFocus()
    from src.ui_handler.help_handler import show_info_shortcuts
    show_info_shortcuts()
    from src.ui_handler.info_handler import populate
    populate(("", "1", "2"))


def switch_to_all():
    from src.reference.reference import get_shortcut_mode
    mode = get_shortcut_mode()
    if mode != "top" and mode != "confirm":
        return
    ui.stackedWidget.setCurrentWidget(ui.all_page)
    from src.ui_handler.all_handler import set_search_bar_focus
    set_search_bar_focus()
    from src.ui_handler.help_handler import show_all_shortcuts
    show_all_shortcuts()


def confirm_message():
    from src.reference.reference import get_shortcut_mode
    mode = get_shortcut_mode()
    if mode == "confirm":
        return
    from src.ui_handler.help_handler import show_confirm_shortcuts
    show_confirm_shortcuts()


def select_pane(pane):
    if pane == "all":
        from src.ui_handler.all_handler import search
        search(ui.all_page.search_bar.text())
        ui.stackedWidget.setCurrentWidget(ui.all_page)
    elif pane == "new":
        ui.stackedWidget.setCurrentWidget(ui.new_page)


def quit_tmgr():
    from src.manager.ftpmanager import force_pushdb
    force_pushdb()
    quit()


def add_taskbar_icon(app):
    from PyQt5.QtGui import QIcon
    app_icon = QIcon()
    from PyQt5.QtCore import QSize
    icon_path = os.path.join(os.path.abspath(""), "src", "ui", "images", "main_icon.png")
    app_icon.addFile(icon_path, QSize(1600, 1600))
    app.setWindowIcon(app_icon)
