# This file uses the "new" ui


def init_handler(ui_instance):
    global ui
    ui = ui_instance


def populate(entry):
    ui.nextAction.setText(entry[1])
    ui.textEdit.setText(entry[2])


def overwrite(entry):
    from src.reference.reference import get_shortcut_mode
    mode = get_shortcut_mode()
    if mode != "info":
        return
    global ui
    next_action = ui.nextAction.text()
    notes = ui.textEdit.toPlainText()
    from src.ui_handler.main_handler import set_status_text
    if next_action.strip() == "":
        set_status_text("Please enter a next action")
        return
    import logging
    logging.debug("Saved: " + next_action + ", " + notes)
    from src.manager.sqlmanager import init
    init()
    from src.reference.reference import entry as create_entry
    entry = create_entry(entry[0], next_action, notes, entry[3], entry[4], entry[5], entry[6], entry[7], entry[8], entry[9], entry[10])
    from src.manager.sqlmanager import update_entry
    update_entry(entry)
    set_status_text("Saved \"" + next_action + "\"")
    from src.ui_handler.main_handler import reset_status_text
    from src.helper.threading_helper import schedule_later
    schedule_later(reset_status_text, 15.0)
    from src.ui_handler.new_handler import clear_ui
    clear_ui()
    from src.ui_handler.help_handler import show_top_shortcuts
    show_top_shortcuts(force=True)
    from src.ui_handler.main_handler import select_pane
    select_pane("all")
