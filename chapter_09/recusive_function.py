# 재귀함수는 일반적으로 리스트의 리스트 같이 고르지 않은 데이터를 처리할 때 유용하다.

def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item

lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]

print(list(flatten(lol)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# yield from 표현식을 추가하여 제너레이터의 일부를 전달할 수 있다.
def yield_flatten(lol):
    for item in lol:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
print(list(yield_flatten(lol)))

