from collections import namedtuple

Duck = namedtuple("Duck", "bill tail")
duck = Duck("wide orange", "long")
print(duck)
# Duck(bill='wide orange', tail='long')

print(duck.bill)
print(duck.tail)


# dictionary to namedtuple
parts = {"bill": "wide orange", "tail": "long"}
duck2 = Duck(**parts)
# --> duck2 = Duck(bill="wide orange", tail="long")
print(duck2)


# namedtuple replace
duck3 = duck2._replace(tail="magnificent", bill="crushing")
print(duck3)
# Duck(bill='crushing', tail='magnificent')


# 네임드 튜플의 특징
#  - 블변 객체처럼 행동한다.
#  - 객체보다 공간 효율성과 시간 효율성이 좋다.
#  - 딕셔너리 형식의 대괄호 [] 대신, 온점(.)표기법으로 속성을 접급할 수 있다. (Ex> duck.bill)
#  - 네임드 튜플을 딕셔너리이 키처럼 사용할 수 있다.