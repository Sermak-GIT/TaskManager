import logging
import os
import getpass

import msvcrt

import sys

from src.helper.aes_helper import string_encrypt


def entry(id, next_action, notes, icon, deadline, time, Setting, Willpower, audio, prio):
    return id, next_action, notes, icon, deadline, time, Setting, Willpower, audio, prio


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
                       ("(a)ll notes", 'a'))

new_note_level_shortcuts = (("(s)ave", 's'),
                            ("(a)ction", 'a'),
                            ("(n)otes", 'n'),
                            ("(r)eset", 'r'),
                            ("(b)ack", 'b'))

all_level_shortcuts = (("(c)lear", 'c'),
                       ("(s)earch bar", 's'),
                       ("(n)ext", 'n'),
                       ("(p)revious", 'p'),
                       ("(d)elete", 'd'),
                       ("(i)nfo", 'i'),  # TODO
                       ("(b)ack", 'b'))

confirm_level_shortcuts = (("(y)es", 'y'),
                           ("(n)o", 'n'))

# master level vars
master_ui = None
shortcut_mode = None


def init_master_ui(ui):
    global master_ui
    master_ui = ui


def set_shortcut_mode(mode):
    global shortcut_mode
    shortcut_mode = mode


def get_shortcut_mode():
    global shortcut_mode
    return shortcut_mode
