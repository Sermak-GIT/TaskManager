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

save_shortcut_keys = "Ctrl+S"
