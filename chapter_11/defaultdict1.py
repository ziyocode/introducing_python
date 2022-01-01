from collections import defaultdict

food_counter = defaultdict(int)

for food in ["spam", "spam", "eggs", "spam"]:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)

# food_counter 가 일반 딕셔너리였다면, food_counter[food]를 증가시키려고 할 때마다 예외를 발생시킨다.


dict_counter = {}

for food1 in ["spam", "spam", "eggs", "spam"]:
    if not food1 in dict_counter:
        dict_counter[food1] = 0
    dict_counter[food1] += 1

for food1, count in dict_counter.items():
    print(food1, count)