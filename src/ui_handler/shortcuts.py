from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut


def init_shortcuts(ui):
    # Switch right and left
    from src.reference.reference import switch_right_shortcut_keys
    ui.switch_right_shortcut = QShortcut(QKeySequence(switch_right_shortcut_keys), ui)
    from src.ui_handler.main_handler import change_ui_right, change_ui_left
    ui.switch_right_shortcut.activated.connect(change_ui_right)
    from src.reference.reference import switch_right_shortcut_keys2
    ui.switch_right_shortcut2 = QShortcut(QKeySequence(switch_right_shortcut_keys2), ui)
    ui.switch_right_shortcut2.activated.connect(change_ui_right)
    from src.reference.reference import switch_left_shortcut_keys
    ui.switch_left_shortcut = QShortcut(QKeySequence(switch_left_shortcut_keys), ui)
    ui.switch_left_shortcut.activated.connect(change_ui_left)
    from src.reference.reference import switch_left_shortcut_keys2
    ui.switch_left_shortcut2 = QShortcut(QKeySequence(switch_left_shortcut_keys2), ui)
    ui.switch_left_shortcut2.activated.connect(change_ui_left)

    # top shortcuts
    from src.reference.reference import help_shortcut_keys
    ui.show_top_shortcut = QShortcut(QKeySequence(help_shortcut_keys), ui)
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


"""self.save_shortcut = QShortcut(QKeySequence(save_shortcut_keys), self)
        self.save_shortcut.activated.connect(self.save_entry)"""
