import time

deadlined_tasks = []


def deadline_tasks(entrylist):
    for entry in entrylist:
        if not entry[4] is None and not entry[4] is "":
            alert(entry)


def get_total_seconds(timestring):
    try:
        time = ["", "", "", "", "", "", "", ""]
        time[0] = int(timestring.split(" ")[0].split("-")[0])
        time[1] = int(timestring.split(" ")[0].split("-")[1])
        time[2] = int(timestring.split(" ")[0].split("-")[2])
        time[3] = int(timestring.split(" ")[1].split(":")[0])
        time[4] = int(timestring.split(" ")[1].split(":")[1])
        time[5] = int(timestring.split(" ")[1].split(":")[2])

        return time[0] * 31557600 + time[1] * 2629800 + time[2] * 86400 + \
               time[3] * 3600 + time[4] * 60 + time[5]
    except Exception:
        pass


def currtimediff(entry):
    try:
        entrytime = get_total_seconds(entry[4])
        currtime = get_total_seconds(time.strftime("%Y-%m-%d %H:%M:%S"))
        return int(entrytime) - int(currtime)
    except Exception:
        pass


def alert(entry):
    try:
        for dt in deadlined_tasks:
            if dt[0] == entry:
                return
        from src.helper.threading_helper import schedule_later
        diff = currtimediff(entry)
        if diff < 0:
            return
        schedule_later(message, diff)
        deadlined_tasks.append((entry, get_total_seconds(time.strftime("%Y-%m-%d %H:%M:%S")) + diff))
    except Exception:
        pass


def message():
    from src.reference.reference import get_global_tray
    get_global_tray().tray_message_deadline(get_message())


def get_message():
    curr = get_total_seconds(time.strftime("%Y-%m-%d %H:%M:%S"))
    for entry in deadlined_tasks:
        if int(entry[1]) == int(curr):
            return entry[0][1]
        elif int(entry[1]) - 1 == int(curr):
            return entry[0][1]
        elif int(entry[1]) + 1 == int(curr):
            return entry[0][1]
