a = {1, 2}
b = {2, 3}

# intersection 교집합
print(a & b)
print(a.intersection(b))

# union 합집합
print(a | b)
print(a.union(b))

# difference 차집합
print(a - b)
print(a.difference(b))

# symmetric difference 교차 차집합 // 양 집합에 교집합을 뺀 것
print(a ^ b)
print(a.symmetric_difference(b))

# issubset 집합의 부분집합인지 확인
print(a <= b)
print(a.issubset(b))

# issuperset 상위집합인지 확인
print(a >= b)
print(a.issuperset(b))