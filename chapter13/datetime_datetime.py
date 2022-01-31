from datetime import datetime, time, date

some_day = datetime(2019, 1, 2, 3, 4, 5, 6)
print(some_day)
# 2019-01-02 03:04:05.000006

print(some_day.isoformat())
# 2019-01-02T03:04:05.000006

now = datetime.now()
print(now)
# 2022-01-29 15:38:57.933201

print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
print(noon_today)
# 2022-01-29 12:00:00
