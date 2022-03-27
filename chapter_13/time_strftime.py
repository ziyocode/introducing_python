import time

now = time.time()
print(time.ctime(now))



fmt = "It's %A, %B, %d, %Y, local time %I:%M:%S%p"
t = time.localtime()
print(t)
# time.struct_time(tm_year=2022, tm_mon=1, tm_mday=29, tm_hour=17, tm_min=58, tm_sec=10, tm_wday=5, tm_yday=29, tm_isdst=0)
print(time.strftime(fmt, t))
# It's Saturday, January, 29, 2022, local time 05:59:03PM

fmt1 = "%Y-%m-%d"
print(time.strptime("2022-01-29", fmt1))
# time.struct_time(tm_year=2022, tm_mon=1, tm_mday=29, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=29, tm_isdst=-1)


fmt2 = "%Y %m %d"
print(time.strptime("2019 01 29", fmt2))
# time.struct_time(tm_year=2019, tm_mon=1, tm_mday=29, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=29, tm_isdst=-1)
