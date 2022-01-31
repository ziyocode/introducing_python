place = "caf\u00e9"
print(place)
# café

print(type(place))
# <class 'str'>

place_bytes = place.encode("utf-8")
# place 변수를 utf-8 형식으로 encode
print(place_bytes)
print(type(place_bytes))
# <class 'bytes'>
# café <-- 5byte (앞 3byte + 2byte)

