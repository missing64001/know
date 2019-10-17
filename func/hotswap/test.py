import datetime
import time



times = datetime.datetime.fromtimestamp(1571015700.0)


time_now_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

print(time_now_str)