import logging
import os
import getpass
from src.helper.aes_helper import string_encrypt


def entry(id, next_action, notes, icon, deadline, time, Setting, Willpower, audio, prio, state, parentid):
    return id, next_action, notes, icon, deadline, time, Setting, Willpower, audio, prio, state, parentid


db_push_pull_timeout = 30

logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s- %(message)s')

db_path = os.path.join(os.path.abspath(""), "src", "db", "taskmanager.db")

help_screen_max_columns = 6

master_pass = getpass.getpass("Master password: ")
server_pass = string_encrypt("<remote_server_password>" + master_pass + "</remote_server_password>", 64)
server = "sermak-v.goip.de"
server_user = "taskmanager"
server_path = "/home/taskmanager/"

# Shortcuts
master_level_shortcuts = (("M-h Help", "Alt+h"),
                          ("C-h Help", "Ctrl+h"),
                          ("C-▶ Switch Right", "Ctrl+Right"),
                          ("M-▶ Switch Right", "Alt+Right"),
                          ("M-◀ Switch Left", "Alt+Left"),
                          ("C-◀ Switch Left", "Ctrl+Left"))

top_level_shortcuts = (("(m)aster shortcuts", 'm'),
                       ("(n)ew note", 'n'),
                       ("(a)ll notes", 'a'),
                       ("(q)uit", 'q'))

new_note_level_shortcuts = (("(s)ave", 's'),
                            ("(a)ction", 'a'),
                            ("(n)otes", 'n'),
                            ("(r)eset", 'r'),
                            ("(b)ack", 'b'))

all_level_shortcuts = (("(c)lear", 'c'),
                       ("(s)earch bar", 's'),
                       ("(j) next", 'j'),
                       ("(k) previous", 'k'),
                       ("(h) parent", 'h'),
                       ("(l) childs", 'l'),
                       ("(d)elete", 'd'),
                       ("(i)nfo", 'i'),
                       ("e(x)ecute", 'x'),
                       ("(m)ove", 'm'),
                       ("(u)ndo", 'u'),
                       ("(b)ack", 'b')
                       )

move_level_shortcuts = (
    ("(m)ove", 'm'),
    ("(t)op", 't'),
    ("(c)ancel", 'c'),
)

confirm_level_shortcuts = (("(y)es", 'y'),
                           ("(n)o", 'n'))

info_level_shortcuts = (("(s)ave", 's'),
                        ("(a)ction", 'a'),
                        ("(n)otes", 'n'),
                        ("(r)eset", 'r'),
                        ("(b)ack", 'b'))

# master level vars
master_ui = None
shortcut_mode = None
global_app = None


def init_master_ui(ui):
    global master_ui
    master_ui = ui


def set_shortcut_mode(mode):
    global shortcut_mode
    shortcut_mode = mode


def get_shortcut_mode():
    global shortcut_mode
    return shortcut_mode


def set_global_app(app):
    global global_app
    global_app = app


def get_global_thread():
    global global_thread
    return global_thread


def set_global_thread(thread):
    global global_thread
    global_thread = thread


def toggle_global_app():
    global global_app
    if global_app.isVisible():
        global_app.hide()
    else:
        global_app.show()
