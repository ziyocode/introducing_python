import re
import string

# 리터럴은 모든 비특수 문자와 일치한다.
# . : \n을 제외한 하나의 문자
# * : 이전 문자 0회 이상
# ? : 이전 문자 0회 또는 1회
# \d : 숫자
# \D : 비숫자
# \w : 알파벳 문자
# \W : 비알파벳 문자
# \s : 공백문자
# \S : 비공백 문자
# \b : 단어 경계 (\w 와 \W 또는 \W 와 \w 사이의 경계)

printable = string.printable
# string 모듈은 문자열 상수가 미리 정해져 있다. 대소 문자, 숫자, 공백문자, 구두점을 포함한 아스키 문자 100개
print(printable)
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(len(printable))

print(re.findall("\d", printable))
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] : printable 에서 숫자만 리스트 자료형으로 반환

print(re.findall("\w", printable))
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
#  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
#  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_'] : 숫자, 문자, 언더바

print(re.findall("\s", printable))
# [' ', '\t', '\n', '\r', '\x0b', '\x0c'] : 공백문자


x = "abc" + "-/*" + "\u00ea" + "\u0115"
print(x)
print(re.findall("\w", x))
# ['a', 'b', 'c', 'ê', 'ĕ']
