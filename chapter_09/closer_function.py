def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knights2("Duck")
b = knights2("Hasenpfeffer")

print(a)
print(b)
# <function knights2.<locals>.inner2 at 0x10a17baf0>
# <function knights2.<locals>.inner2 at 0x10a17bb80>

print(a())
print(b())
# We are the knights who say: 'Duck'
# We are the knights who say: 'Hasenpfeffer'

print(type(a))
print(type(b))
# <class 'function'>
# <class 'function'>
