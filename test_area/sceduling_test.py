from src.helper.threading_helper import schedule_later


def print_something():
    print("HEllo")


schedule_later(print_something, 1)
print("Important")
