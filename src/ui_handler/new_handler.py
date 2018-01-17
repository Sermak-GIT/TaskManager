from src.helper.threading_helper import schedule_later
from src.manager.sqlmanager import *
from src.reference.reference import entry, get_shortcut_mode
import logging

from src.ui_handler.main_handler import reset_status_text, set_status_text


def init_handler(ui_instance):
    global ui
    ui = ui_instance
    from src.ui_handler.shortcuts import init_new_note_shortcuts
    init_new_note_shortcuts(ui)


def clear_ui():
    ui.textEdit.setText("")
    ui.nextAction.setText("")


def save():
    mode = get_shortcut_mode()
    if mode != "new_note":
        return
    global ui
    next_action = ui.nextAction.text()
    notes = ui.textEdit.toPlainText()
    if next_action.strip() == "":
        set_status_text("Please enter a next action")
        return
    logging.debug("Saved: " + next_action + ", " + notes)
    init()
    add_entry(entry(issue_new_id(), next_action, notes, None, None, None, None, None, None, None))
    set_status_text("Saved \"" + next_action + "\"")
    schedule_later(reset_status_text, 15.0)
    clear_ui()
    from src.ui_handler.help_handler import show_top_shortcuts
    show_top_shortcuts(force=True)


def focus_next_action():
    mode = get_shortcut_mode()
    if mode != "new_note":
        return
    ui.nextAction.setFocus()


def focus_notes():
    mode = get_shortcut_mode()
    if mode != "new_note":
        return
    ui.textEdit.setFocus()


def reset():
    mode = get_shortcut_mode()
    if mode != "new_note":
        return
    ui.nextAction.setText("")
    ui.textEdit.setText("")
    focus_next_action()