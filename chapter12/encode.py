
snowman = "\u2603"
print(snowman)
print(len(snowman))
# 1

ds = snowman.encode("utf-8")
print(len(ds))
# 3

print(ds)

#ds1 = snowman.encode("ascii")
#print(ds)
# UnicodeEncodeError: 'ascii' codec can't encode character '\u2603' in position 0: ordinal not in range(128)

print(snowman.encode("ascii", "ignore"))
# b''
# encode 함수의 두번째 필드를 "ignore"로 설정
# encode 함수의 두번째 필드는 변환 오류가 생길경우 action을 지정 
# default : strict / ignore / replace / backslashreplace / xmlcharrefreplace 가 있다.

print(snowman.encode("ascii", "replace"))
# b'?' (replace 할 수 없는 문자를 "?" 로 반환")

print(snowman.encode('ascii', 'backslashreplace'))
# b'\\u2603' (유니코드 문자열을 반환한다.)
print("\u2603")

print(snowman.encode("ascii", "xmlcharrefreplace"))
# b'&#9731;' (html-safe 문자열 생성을 위해 사용, 유니코드 이스케이프 시퀀스를 출력)


