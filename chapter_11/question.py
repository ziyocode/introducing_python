import sys
from sources import fast, advice

print("Let's go to", fast.pick())
print("Should. we take out?", advice.give())

for place in sys.path:
    print(place)
