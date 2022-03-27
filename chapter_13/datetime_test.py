import sys
from datetime import date

halloween = date(2019, 10, 31)
print(halloween)

print(halloween.day)
print(halloween.month)
print(halloween.year)


print(halloween.isoformat())
# iso 8601 포멧으로 구성


now = date.today()
print(now)