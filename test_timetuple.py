import datetime
import time
d = datetime.datetime(2019, 5, 2)
print(d.timetuple())
print(time.mktime(d.timetuple()))
# print(time.localtime())
