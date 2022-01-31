import re

result = re.match("You", "Young Frankenstein")
print(type(result))
# <class 're.Match'>
print(result)
# <re.Match object; span=(0, 3), match='You'>

youpattern = re.compile("You")
print(youpattern)
# re.compile('You')
result = youpattern.match("Young Frankenstein")
print(result)
# <re.Match object; span=(0, 3), match='You'>