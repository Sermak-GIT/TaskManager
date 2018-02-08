import logging
import os
import pysftp

from src.reference.reference import server_pass, server, server_user, server_path


def connect(host, user, passwd, port):
    if host != "" and user != "" and passwd != "" and port != 0:
        return pysftp.Connection(host=host, username=user, password=passwd, port=port)
    else:
        return None


def pushdb():
    with connect(server, server_user, server_pass, 22) as con:
        con.cd(server_path)
        con.put(os.path.join(os.getcwd()[:-8], "db", "taskmanager.db"))
        logging.info("Pushed db successfully")


def pulldb():
    with connect(server, server_user, server_pass, 22) as con:
        con.cd(server_path)
        con.get("taskmanager.db", os.path.join(os.getcwd()[:], "src", "db", "taskmanager.db"))
        logging.info("Pushed db successfully")

