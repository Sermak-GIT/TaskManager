import time

from src.manager.time_manager import get_total_seconds

s = time.strftime("%Y-%m-%d %H:%M:%S")
print(s)
a = time.strptime("2019-03-18 01:26:52", "%Y-%m-%d %H:%M:%S")
b = time.strptime(s, "%Y-%m-%d %H:%M:%S")

print(get_total_seconds("2018-03-18 01:55:00"))
