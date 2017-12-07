#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)


def issue_new_id():
    con = lite.connect("taskmanager.db")
    with con:
        ret_id = con.cursor().lastrowid
        if ret_id is None:
            return 0
        return ret_id + 1


def init():
    connection = lite.connect("taskmanager.db")
    with connection:
        cursor = connection.cursor()
        try:
            cursor.execute("CREATE TABLE Entries(Id INT, NextAction TEXT, Notes INT, Icon BLOB, Deadline DATE, "
                           "Time TIME, Setting TEXT, Willpower INT, Audio INT, Prio INT)")
        except lite.OperationalError:
            print("Table found")


init()

print(issue_new_id())
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
