from src.manager.sqlmanager import *
from src.reference.reference import entry
import logging


def save(next_action, notes):
    logging.debug("Saved: "+next_action + ", " + notes)
    init()
    add_entry(entry(issue_new_id(), next_action, notes, None, None, None, None, None, None, None))
