import logging

from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut


def init_shortcuts(ui):
    # Switch right and left
    from src.reference.reference import master_level_shortcuts
    ui.switch_right_shortcut = QShortcut(QKeySequence(master_level_shortcuts[2][1]), ui)
    from src.ui_handler.main_handler import change_ui_right, change_ui_left
    ui.switch_right_shortcut.activated.connect(change_ui_right)
    ui.switch_right_shortcut2 = QShortcut(QKeySequence(master_level_shortcuts[3][1]), ui)
    ui.switch_right_shortcut2.activated.connect(change_ui_right)
    ui.switch_left_shortcut = QShortcut(QKeySequence(master_level_shortcuts[4][1]), ui)
    ui.switch_left_shortcut.activated.connect(change_ui_left)
    ui.switch_left_shortcut2 = QShortcut(QKeySequence(master_level_shortcuts[5][1]), ui)
    ui.switch_left_shortcut2.activated.connect(change_ui_left)

    # show top_level shortcuts
    ui.show_top_shortcut = QShortcut(QKeySequence(master_level_shortcuts[0][1]), ui)
    ui.show_top_shortcut2 = QShortcut(QKeySequence(master_level_shortcuts[1][1]), ui)
    from src.ui_handler.help_handler import show_top_shortcuts
    ui.show_top_shortcut.activated.connect(show_top_shortcuts)
    ui.show_top_shortcut2.activated.connect(show_top_shortcuts)


def init_help_screen_shortcuts(ui):
    # m Shortcuts
    ui.m_shortcut = QShortcut(QKeySequence('m'), ui)
    ui.m_shortcut.activated.connect(m_shortcuts)

    # n Shortcuts
    ui.n_shortcut = QShortcut(QKeySequence('n'), ui)
    ui.n_shortcut.activated.connect(n_shortcuts)

    # a Shortcuts
    ui.n_shortcut = QShortcut(QKeySequence('a'), ui)
    ui.n_shortcut.activated.connect(a_shortcuts)


def init_new_note_shortcuts(ui):
    # r Shortcuts
    ui.r_shortcut = QShortcut(QKeySequence('r'), ui)
    ui.r_shortcut.activated.connect(r_shortcuts)

    # b Shortcuts
    ui.notes_back_shortcut = QShortcut(QKeySequence('b'), ui)
    ui.notes_back_shortcut.activated.connect(b_shortcuts)

    # s Shortcuts
    ui.s_shortcut = QShortcut(QKeySequence('s'), ui)
    ui.s_shortcut.activated.connect(s_shortcuts)


def init_all_shortcuts(ui):
    # c Shortcuts
    ui.s_shortcut = QShortcut(QKeySequence('c'), ui)
    ui.s_shortcut.activated.connect(c_shortcuts)

    # b Shortcuts
    ui.notes_back_shortcut = QShortcut(QKeySequence('b'), ui)
    ui.notes_back_shortcut.activated.connect(b_shortcuts)

    # s Shortcuts
    ui.s_shortcut = QShortcut(QKeySequence('s'), ui)
    ui.s_shortcut.activated.connect(s_shortcuts)

    # p Shortcuts
    ui.s_shortcut = QShortcut(QKeySequence('p'), ui)
    ui.s_shortcut.activated.connect(p_shortcuts)

    # d Shortcuts
    ui.d_shortcuts = QShortcut(QKeySequence('d'), ui)
    ui.d_shortcuts.activated.connect(d_shortcuts)

    # y Shortcuts
    ui.y_shortcuts = QShortcut(QKeySequence('y'), ui)
    ui.y_shortcuts.activated.connect(y_shortcuts)

    # i Shortcuts
    ui.i_shortcuts = QShortcut(QKeySequence('i'), ui)
    ui.i_shortcuts.activated.connect(i_shortcuts)

    # q Shortcuts
    ui.q_shortcuts = QShortcut(QKeySequence('q'), ui)
    ui.q_shortcuts.activated.connect(q_shortcuts)


def b_shortcuts():
    from src.ui_handler.help_handler import force_show_top_shortcuts
    from src.reference.reference import get_shortcut_mode
    mode = get_shortcut_mode()
    logging.info(mode + " b")
    if mode == "new_note":
        force_show_top_shortcuts()
    elif mode == "all":
        force_show_top_shortcuts()
    elif mode == "info":
        force_show_top_shortcuts()
    return


def i_shortcuts():
    from src.reference.reference import get_shortcut_mode
    mode = get_shortcut_mode()
    logging.info(mode + " i")
    if mode == "all":
        from src.ui_handler.main_handler import switch_to_info
        switch_to_info()
    return


def r_shortcuts():
    from src.ui_handler.new_handler import reset
    from src.reference.reference import get_shortcut_mode
    mode = get_shortcut_mode()
    logging.info(mode + " r")
    if mode == "new_note":
        reset()
    elif mode == "info":
        reset()
    return


def c_shortcuts():
    from src.reference.reference import get_shortcut_mode
    mode = get_shortcut_mode()
    logging.info(mode + " c")
    if mode == "all":
        from src.ui_handler.all_handler import clear_search_bar
        clear_search_bar()
    return


def d_shortcuts():
    from src.reference.reference import get_shortcut_mode
    mode = get_shortcut_mode()
    logging.info(mode + " d")
    if mode == "all":
        from src.ui_handler.main_handler import confirm_message
        from src.ui_handler.main_handler import set_status_text
        set_status_text("Really delete?")
        confirm_message()
        from src.reference.reference import master_ui
        master_ui.helpWidget.setFocus(True)
    return


def y_shortcuts():
    from src.reference.reference import get_shortcut_mode
    mode = get_shortcut_mode()
    logging.info(mode + " y")
    if mode == "confirm":
        from src.ui_handler.all_handler import delete
        from src.ui_handler.main_handler import switch_to_all
        from src.ui_handler.main_handler import set_status_text
        set_status_text("")
        switch_to_all()
        delete()
        from src.reference.reference import master_ui
        master_ui.helpWidget.setFocus(True)
    return


def a_shortcuts():
    from src.ui_handler.new_handler import focus_next_action
    from src.reference.reference import get_shortcut_mode
    mode = get_shortcut_mode()
    logging.info(mode + " a")
    if mode == "top":
        from src.ui_handler.main_handler import switch_to_all
        switch_to_all()
    elif mode == "new_note":
        focus_next_action()
    elif mode == "info":
        focus_next_action()
    return


def q_shortcuts():
    from src.reference.reference import get_shortcut_mode
    mode = get_shortcut_mode()
    logging.info(mode + " q")
    if mode == "top":
        from src.ui_handler.main_handler import quit_tmgr
        quit_tmgr()
    return


def s_shortcuts():
    from src.ui_handler.new_handler import save
    from src.reference.reference import get_shortcut_mode
    mode = get_shortcut_mode()
    logging.info(mode + " s")
    if mode == "new_note":
        save()
    elif mode == "all":
        from src.ui_handler.all_handler import set_search_bar_focus
        set_search_bar_focus()
    return


def m_shortcuts():
    from src.reference.reference import get_shortcut_mode
    mode = get_shortcut_mode()
    logging.info(mode + " m")
    from src.ui_handler.help_handler import show_master_shortcuts
    if mode == "top":
        show_master_shortcuts()
    return


def p_shortcuts():
    from src.reference.reference import get_shortcut_mode
    mode = get_shortcut_mode()
    logging.info(mode + " p")
    if mode == "all":
        from src.ui_handler.all_handler import select_prev
        select_prev()
    return


def n_shortcuts():
    from src.reference.reference import get_shortcut_mode
    from src.ui_handler.main_handler import switch_to_new_note
    mode = get_shortcut_mode()
    logging.info(mode + " n")
    from src.ui_handler.new_handler import focus_notes
    if mode == "new_note":
        # Focus notes edit from new_note_level
        focus_notes()
    elif mode == "info":
        focus_notes()
    elif mode == "top":
        # open new note screen from top_level
        switch_to_new_note()
    elif mode == "all":
        from src.ui_handler.all_handler import select_next
        select_next()
    elif mode == "confirm":
        from src.ui_handler.main_handler import switch_to_all
        from src.ui_handler.main_handler import set_status_text
        set_status_text("")
        switch_to_all()
        from src.reference.reference import master_ui
        master_ui.helpWidget.setFocus(True)
    return
