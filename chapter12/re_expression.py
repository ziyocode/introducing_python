import abc
from os import preadv
import re

# Abc             : 리터럴 abc
# ( expr)         : expr
# expr1 | expr2   : expr1 or expr2
# .               : \n을 제외한 모든 문자
# ^               : 소스 문자열 시작
# $               : 소스 문자열 끝
# prev ?          : 0 또는 1회 preadv
# prev *          : 0회 이상의 최대 prev
# prev *?         : 0회 이상의 최소 prev
# prev +          : 1회 이상의 최대 prev
# prev +?         : 1회 이상의 최소 prev m회 prev
# prev {m}        : m회 prev
# prev {m, n}     : m에서 n회 최대 prev
# prev {m, n}?    : m에서 n회 최소 prev
# [abc]           : a 또는 b 또는 c (a|b|c와 같음)
# [^abc]          : (a 또는 b 또는 c)가 아님
# prev (?=next)   : 뒤에 next가 오면 prev
# prev (?!next)   : 뒤에 next가 오지 않으면 prev
# (?<=prev) next  : 앞에 prev 가 오면 next
# (?<!prev) next  : 앞에 prev 가 오지 않으면 next

source = """I wish I may, I wish I might
Have a dish of fish tonight."""
print(source)

# wish를 모두 찾는다.
print(re.findall("wish", source))

# wish 또는 fish를 모두 찾는다.
print(re.findall("wish|fish", source))

# wish 로 시작하는 것을 찾는다.
print(re.findall("^wish", source))

# I wish 로 시작하는 것을 찾는다.
print(re.findall("^I wish", source))

# fish로 끝나는 것을 찾는다.
print(re.findall("fish$", source))

# fish tonight. 으로 끝나는 것을 찾는다.
print(re.findall("fish tonight.$", source))

# w 또는 f 다음에 ish 가 오는 것을 찾는다.
print(re.findall("[w|f]ish", source))
# ['wish', 'wish', 'fish']

# w, s, h가 하나 이상인 것을 찾는다.
print(re.findall("[wsh]+", source))
# ['w', 'sh', 'w', 'sh', 'h', 'sh', 'sh', 'h']

# ght 다음에 알파벳이 아닌 것을 찾는다.
print(re.findall('ght\W', source))
# ['ght\n', 'ght.']

# wish 이전에 나오는 I를 찾는다.
print(re.findall("I (?=wish)", source))
# ['I ', 'I ']

# I 다음에 나오는 wish를 찾는다.
print(re.findall("(?<=I) wish", source))
# [' wish', ' wish']

print(re.findall('\bfish', source))
# [] : 파이썬 문자열에서 \b는 백스페이스를 의미하지만, 정규 표현식에서는 단어의 시작 부분을 의미한다.
print(re.findall(r'\bfish', source))
# ['fish'] 정규 표현식의 패턴 입력 전에 항상 r(raw string)을 입력하라.

# 패턴 : 매칭 결과 지정하기
m = re.search(r'(.dish\b).*(\bfish)', source)
print(m)
# <re.Match object; span=(35, 48), match=' dish of fish'>
print(m.group())
#  dish of fish
print(m.groups())
# (' dish', 'fish')



