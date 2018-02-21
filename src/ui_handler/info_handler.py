# This file uses the "new" ui


def init_handler(ui_instance):
    global ui
    ui = ui_instance


def populate(entry):
    ui.nextAction.setText(entry[1])
    ui.textEdit.setText(entry[2])