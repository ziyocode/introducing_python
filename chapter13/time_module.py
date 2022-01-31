import time

now = time.time()
print(now)
# 1643443047.047795

print(time.ctime(now))
# Sat Jan 29 17:35:39 2022
print(time.localtime(now))
# time.struct_time(tm_year=2022, tm_mon=1, tm_mday=29, tm_hour=17, tm_min=36, tm_sec=48, tm_wday=5, tm_yday=29, tm_isdst=0)


