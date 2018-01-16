import logging
import os


def entry(id, next_action, notes, icon, deadline, time, Setting, Willpower, audio, prio):
    return id, next_action, notes, icon, deadline, time, Setting, Willpower, audio, prio


logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s- %(message)s')

db_path = os.path.abspath("")[:-2] + "db\\taskmanager.db"

switch_right_shortcut_keys = "Ctrl+Right"
switch_right_shortcut_keys2 = "Alt+Right"
switch_left_shortcut_keys = "Ctrl+Left"
switch_left_shortcut_keys2 = "Alt+Left"
help_shortcut_keys = "Alt+h"
help_screen_max_columns = 6

master_level_shortcuts = ("M-h Help",  # TODO: Do as below
                          "C-▶ Switch Right",
                          "M-▶ Switch Right",
                          "M-◀ Switch Left",
                          "C-◀ Switch Left")

top_level_shortcuts = (("(m)aster shortcuts", 'm'),
                       ("(n)ew note", 'n'))

new_note_level_shortcuts = (("(s)ave", 's'),
                            )

# master level vars
master_ui = None


def init_master_ui(ui):
    global master_ui
    master_ui = ui
