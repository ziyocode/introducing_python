def my_range(first=0, last=10, setp=1):
    number = first
    while number < last:
        yield number                # return 이 아니라 yield 사용
        number += setp

ranger = my_range(1, 5)
print(ranger)
# <generator object my_range at 0x10c1c2580>

for x in ranger:
    print(x)
# 1
# 2
# 3
# 4

for try_again in ranger:
    print(try_again)
# 한번 순회한 제너레이터는 아무 것도 반환하지 않는다.

# generator comprehension
genobj = (pair for pair in zip(["a", "b"], ["1", "2"]))
print(genobj)
# <generator object <genexpr> at 0x107829dd0>

for thing in genobj:
    print(thing)
# ('a', '1')
# ('b', '2')