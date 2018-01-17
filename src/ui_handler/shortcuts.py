from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut


def init_shortcuts(ui):
    # Switch right and left
    from src.reference.reference import master_level_shortcuts
    ui.switch_right_shortcut = QShortcut(QKeySequence(master_level_shortcuts[1][1]), ui)
    from src.ui_handler.main_handler import change_ui_right, change_ui_left
    ui.switch_right_shortcut.activated.connect(change_ui_right)
    ui.switch_right_shortcut2 = QShortcut(QKeySequence(master_level_shortcuts[2][1]), ui)
    ui.switch_right_shortcut2.activated.connect(change_ui_right)
    ui.switch_left_shortcut = QShortcut(QKeySequence(master_level_shortcuts[3][1]), ui)
    ui.switch_left_shortcut.activated.connect(change_ui_left)
    ui.switch_left_shortcut2 = QShortcut(QKeySequence(master_level_shortcuts[4][1]), ui)
    ui.switch_left_shortcut2.activated.connect(change_ui_left)

    # top shortcuts

    from src.reference.reference import master_level_shortcuts
    ui.show_top_shortcut = QShortcut(QKeySequence(master_level_shortcuts[0][1]), ui)
    from src.ui_handler.help_handler import show_top_shortcuts
    ui.show_top_shortcut.activated.connect(show_top_shortcuts)


def init_help_screen_shortcuts(ui):
    # Show master Shortcuts
    from src.reference.reference import top_level_shortcuts
    ui.show_master_shortcut = QShortcut(QKeySequence(top_level_shortcuts[0][1]), ui)
    from src.ui_handler.help_handler import show_master_shortcuts
    ui.show_master_shortcut.activated.connect(show_master_shortcuts)

    # New note
    ui.new_note_shortcut = QShortcut(QKeySequence(top_level_shortcuts[1][1]), ui)
    from src.ui_handler.main_handler import switch_to_new_note
    ui.new_note_shortcut.activated.connect(switch_to_new_note)


def init_new_note_shortcuts(ui):
    # Save
    from src.reference.reference import new_note_level_shortcuts
    ui.save_shortcut = QShortcut(QKeySequence(new_note_level_shortcuts[0][1]), ui)
    from src.ui_handler.new_handler import save
    ui.save_shortcut.activated.connect(save)