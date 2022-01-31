from datetime import timedelta
from datetime import date
from tkinter import W

now = date.today()

one_day = timedelta(days=1)
print(one_day)
# 1 day, 0:00:00

tomorrow = now + one_day
print(tomorrow)

yesterday = now - one_day
print(yesterday)