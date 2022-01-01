import itertools

for item in itertools.chain([1, 2], ["a", "b"]):
    print(item)
# chain() 함수는 순회 가능한 인수를 차례로 반환한다.

# for item in itertools.cycle([1, 2]):
#     print(item)
# cycle() 함수는 인수를 무한 순환하는 iterator 이다.

for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)
# 1
# 3
# 6
# 10
# accumulate() 함수는 인수의 누적 합을 반환한다.

def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)
# 1
# 2
# 6
# 24

