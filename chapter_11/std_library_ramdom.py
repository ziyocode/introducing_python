from random import choice
from random import sample
from random import randint
from random import randrange
from random import random

c = choice([23, 9, 46, "bacon"])
print(c)
# choice()는 인수 중 하나를 선택하여 반환한다.


sample1 = sample([23, 9, 46, "bacon", "eggs"], 2)
print(sample1)
random_int = sample(range(100), 4)
print(random_int)
# sample()은 인수 중 하나 이상의 값을 반환한다.


print(randint(38, 74))
print(randint(1, 200))
# randint 는 시작값, 끝값 사이의 임의 수를 받환한다.

print(randrange(1, 10, 2))
print(randrange(1, 10))
# randrange() 는 range() 함수와 같은 인자를 같는다. 시작(포함), 끝(제외), 스탭(옵션값)



print(random())
print(random())
# random() 는 0.0 ~ 0.1 사이의 부동소수점 숫자를 얻는다.


