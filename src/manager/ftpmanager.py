import logging
import os
import pysftp
import time

from src.reference.reference import server_pass, server, server_user, server_path, db_push_pull_timeout

last_push_access = 0
last_pull_access = 0


def connect(host, user, passwd, port):
    if host != "" and user != "" and passwd != "" and port != 0:
        return pysftp.Connection(host=host, username=user, password=passwd, port=port)
    else:
        return None


def pushdb():
    global last_push_access
    if last_push_access == 0:
        last_push_access = int(time.strftime("%M%S"))
    else:
        currtime = int(time.strftime("%M%S"))
        if currtime - last_push_access < db_push_pull_timeout:
            return
        last_push_access = currtime
    with connect(server, server_user, server_pass, 22) as con:
        con.cd(server_path)
        con.put(os.path.join(os.getcwd()[:], "src", "db", "taskmanager.db"))
        logging.info("Pushed db successfully")


def pulldb():
    global last_pull_access
    if last_pull_access == 0:
        last_pull_access = int(time.strftime("%M%S"))
    else:
        currtime = int(time.strftime("%M%S"))
        if currtime - last_pull_access < db_push_pull_timeout:
            return
        last_pull_access = currtime
    with connect(server, server_user, server_pass, 22) as con:
        con.cd(server_path)
        con.get("taskmanager.db", os.path.join(os.getcwd()[:], "src", "db", "taskmanager.db"))
        logging.info("Pushed db successfully")

