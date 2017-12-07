import pysftp


def connect(host, user, passwd, port):
    if host != "" and user != "" and passwd != "" and port != 0:
        return pysftp.Connection(host=host, username=user, password=passwd, port=port)
    else:
        return None
