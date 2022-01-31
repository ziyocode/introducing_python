import html
from html.entities import html5

print(html.unescape("&#233;"))
print(html.unescape("&#xe9;"))
# é

print(html5["egrave"])
print(html5["egrave;"])


# html entity
char = '\u00e9'
dec_value = ord(char)
print(html.entities.codepoint2name[dec_value])
# eacute



place = 'caf\u00e9'
byte_value = place.encode('ascii', 'xmlcharrefreplace')
print(byte_value)
# b'caf&#233;'
print(byte_value.decode())
# caf&#233;


