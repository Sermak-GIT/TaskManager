#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import logging
import pprint

from src.manager.ftpmanager import pulldb, pushdb
from src.reference.reference import db_path

logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s- %(message)s')


def issue_new_id():
    pulldb()
    logging.debug("issue_new_id() called")
    i = 0
    while is_id_in_use(i):
        i += 1
        is_id_in_use(i)
    logging.debug("issue_new_id() issued %i", i)
    return i


def is_id_in_use(to_check_id):
    pulldb()
    logging.debug("is_id_in_use() checks id " + to_check_id.__str__())
    con = lite.connect(db_path)
    with con:
        ret_id = con.cursor().execute("SELECT * FROM Entries WHERE Id = " + to_check_id.__str__()).fetchone()
        if ret_id is None:
            logging.debug("ID " + to_check_id.__str__() + " not in use")
            return False
        logging.debug("ID " + to_check_id.__str__() + " already in use")
        return True


def init():
    db_exists = True
    try:
        pulldb()
    except Exception:
        db_exists = False
    connection = lite.connect(db_path.replace("/manager/src", ""))
    with connection:
        cursor = connection.cursor()
        try:
            cursor.execute("CREATE TABLE Entries(Id INT, NextAction TEXT, Notes INT, Icon BLOB, Deadline DATE, "
                           "Time TIME, Setting TEXT, Willpower INT, Audio INT, Prio INT, State INT)")
            logging.info("Table Entries created")
        except lite.OperationalError:
            logging.info("Table Entries found")
    if not db_exists:
        pushdb()


def add_entry(entry):
    pulldb()
    logging.info("Adding entry: " + entry.__str__())
    connection = lite.connect(db_path)
    with connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Entries VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", entry)
    pushdb()


def read_entry(entryid):
    pulldb()
    logging.info("Reading entry: " + entryid.__str__())
    con = lite.connect(db_path)
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Entries WHERE Id=" + entryid.__str__())
        rows = cur.fetchall()
        try:
            logging.info("Reading entry: " + entryid.__str__() + " successful")
            return rows[0]
        except IndexError:
            logging.info("Entry: " + entryid.__str__() + " does not exist")
            return None


def update_entry(entry):
    pulldb()
    entryid = entry[0]
    entry = entry[1:]
    logging.info("Updating entry: " + entryid.__str__())
    con = lite.connect(db_path)
    with con:
        cur = con.cursor()
        cur.execute("UPDATE Entries "
                    "SET NextAction=?, Notes = ?, Icon=?, Deadline=?, Time=?, "
                    "Setting=?, Willpower=?, Audio=?, Prio=?, State=? "
                    "WHERE Id = " + entryid.__str__(), entry)
        cur.fetchall()
    pushdb()


def get_all_entries():
    pulldb()
    logging.info("Reading all entries")
    con = lite.connect(db_path)
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Entries")
        rows = cur.fetchall()
        try:
            logging.info("Reading all entries successful")
            return rows
        except IndexError:
            logging.info("There are no entries")
            return None


def delete_entry(entryid):
    pulldb()
    logging.info("Deleting entry " + entryid.__str__())
    con = lite.connect(db_path)
    with con:
        cur = con.cursor()
        cur.execute("DELETE FROM Entries WHERE Id=" + entryid.__str__())
        rows = cur.fetchall()
    pushdb()


def delete_everything():
    pulldb()
    logging.warning("Deleting EVERYTHING")
    con = lite.connect(db_path)
    with con:
        cur = con.cursor()
        cur.execute("DELETE FROM Entries")
        rows = cur.fetchall()
    pushdb()


init()
'''
pprint.pprint(read_entry(1))
update_entry((1, 'Do #3', 'Hello', 324, '23.03.12', '23:22', 'pc', 100, 0, 12))
pprint.pprint(read_entry(1))
delete_everything()
pprint.pprint(read_entry(1))
'''
'''
cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)

with con:
    cur = con.cursor()

    cur.lastrowid
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)

con = lite.connect('test.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")
    rows = cur.fetchall()
    for row in rows:
        print(row)'''
