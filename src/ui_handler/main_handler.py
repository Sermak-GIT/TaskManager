import logging


def init_handler(ui_instance):
    global ui
    ui = ui_instance


def set_status_text(text=""):
    ui.statusLabel.setText(text)


def change_ui_right():
    i = (ui.stackedWidget.currentIndex() + 1) % (ui.stackedWidget.count())
    ui.stackedWidget.setCurrentIndex(i)


def change_ui_left():
    i = (ui.stackedWidget.currentIndex() - 1) % (ui.stackedWidget.count())
    ui.stackedWidget.setCurrentIndex(i)
