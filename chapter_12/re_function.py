import re

# re.match() source의 첫 패턴이 검색 될 경우 반환 (type = class 're.Match')
# re.search() source의 어디에서든 패턴이 검색되면 반환
# re.findall() source의 어디에서든 패턴에 맞는 부분을 모두 찾아 list로 반환
# re.split() source의 패턴을 기준으로 분할하여 list로 반환
# re.sub() source의 패턴을 찾아 변환하여 반환


source = "Young Frankenstein"
m = re.match("You", source)

if m:
    print(m.group())
# match()는 source의 시작에서 패턴이 일치하는지 확인한다.

m = re.match("^You", source)
if m:
    print(m.group())
# ^You 는 시작 부분의 같은 패턴인지 확인

m = re.match("Frank", source)
if m:
    print(m.group())
# match()는 시작부분에서 패턴이 일친하는지 확인하기 때문에 아무것도 반환하지 않는다.

m = re.search("Frank", source)
if m:
    print(m.group())
# search는 패턴이 어떤 위치에 있더라도 확인한다.
# Frank

m = re.match(".*Frank", source)
if m:
    print(m.group())
# Young Frank
# "." 은 한 문자를 의미 / * 는 어떤 패턴이 0 회 이상 올 수 있다는 것을 의미

m = re.findall("n", source)
print(m)
# ['n', 'n', 'n', 'n']
# 찾은 모든 패턴을 리스트로 반환
print("Found", len(m), "matches")
# Found 4 matches

m = re.findall("n.", source)
print(m)
# ['ng', 'nk', 'ns']

m = re.split("n", source)
print(m)
# ['You', 'g Fra', 'ke', 'stei', '']
# 패턴으로 나눠서 list로 반환

m = re.sub("n", "?", source)
print(m)
# You?g Fra?ke?stei?
# n 을 ?로 바꿔서 반환