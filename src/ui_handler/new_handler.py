from src.helper.threading_helper import schedule_later
from src.manager.sqlmanager import *
from src.reference.reference import entry
import logging


def init_handler(ui_instance):
    global ui
    ui = ui_instance


def clear_ui():
    ui.textEdit.setText("")
    ui.nextAction.setText("")


def save(next_action, notes):
    logging.debug("Saved: " + next_action + ", " + notes)
    init()
    add_entry(entry(issue_new_id(), next_action, notes, None, None, None, None, None, None, None))
    from src.ui_handler.main_handler import set_status_text
    set_status_text("Saved \"" + next_action + "\"")
    schedule_later(set_status_text, 15.0)
    clear_ui()
