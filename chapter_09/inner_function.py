def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

print(outer(4, 7))
# 함수 안에 복잡한 작업을 함수로 정의하여 내부 함수로 사용

def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)

print(knights("Ni!"))
# We are the knights who say: 'Ni!'