from src.manager.sqlmanager import *
from src.reference.reference import entry


def save(next_action, notes):
    print("Test123")
    init()
    add_entry(entry(issue_new_id(), next_action, notes, None, None, None, None, None, None, None))
