import pysftp
import sys

host = "sermak-v.goip.de"  # hard-coded
password = "mM32582657!"  # hard-coded
user = "taskmanager"  # hard-coded

sftp = pysftp.Connection(host, username=user, password=password)

print(sftp.lstat(sftp.pwd))


print('Upload done.')
