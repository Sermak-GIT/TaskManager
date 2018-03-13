import threading


def schedule_later(method, time):
    threading.Timer(time, method).start()