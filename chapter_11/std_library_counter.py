from collections import Counter

breakfast = ["spam", "spam", "eggs", "spam"]
breakfast_counter = Counter(breakfast)
print(breakfast_counter)
# Counter({'spam': 3, 'eggs': 1})

# most_common() 함수는 모든 요소를 내림차순으로 반환한다.
print(breakfast_counter.most_common())
# [('spam', 3), ('eggs', 1)]

lunch = ["eggs", "eggs", "bacon"]
lunch_counter = Counter(lunch)
print(lunch_counter)


# + 연산자로 두 카운터를 결합할 수 있다.
meal_counter = breakfast_counter + lunch_counter
print(meal_counter)
# Counter({'spam': 3, 'eggs': 3, 'bacon': 1})

# - 연산자로 두 카운터의 - 연산을 할 수 있다.
blunch = lunch_counter - breakfast_counter
print(blunch)
# Counter({'eggs': 1, 'bacon': 1})

# set() 자료구조와 마찬가지로, 교집합 & / 합집합 | 연산도 가능하다.
favorit_meal = breakfast_counter & lunch_counter
print(favorit_meal)
# Counter({'eggs': 1})
total_meal = breakfast_counter | lunch_counter
print(total_meal)
# Counter({'spam': 3, 'eggs': 2, 'bacon': 1})
# + 연산과 다르게 eggs 값이 2로 두 집합 중 높은 숫자의 공통 항목을 반환하다.