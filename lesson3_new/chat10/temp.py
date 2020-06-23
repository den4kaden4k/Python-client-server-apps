import time
from datetime import datetime


def my_time():
    return time.time()


t1 = time.time()
dt1 = datetime.timestamp(datetime.now())
print(t1)
print(dt1)
