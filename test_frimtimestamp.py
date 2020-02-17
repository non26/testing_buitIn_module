import datetime
import os
modify_time = os.stat(r"C:\nonContent\python\python\testpython\test14_mix.py").st_mtime
print(modify_time)
print(datetime.datetime.fromtimestamp(modify_time))
