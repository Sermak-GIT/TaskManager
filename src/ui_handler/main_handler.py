import logging


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
    ui.stackedWidget.setCurrentWidget(ui.new_page)
    ui.new_page.nextAction.setFocus()
    from src.ui_handler.help_handler import show_new_note_shortcuts
    show_new_note_shortcuts()