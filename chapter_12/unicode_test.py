import unicodedata

def unicode_test(value):
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))

unicode_test("A")
unicode_test("%")
unicode_test("$")

unicode_test("\u20ac")
unicode_test("\u00a2")

print(unicodedata.name("\u00e9"))
print(unicodedata.lookup("LATIN SMALL LETTER E WITH ACUTE"))

print("caf%s" % (unicodedata.lookup("LATIN SMALL LETTER E WITH ACUTE")))

