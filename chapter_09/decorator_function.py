# decorator 는 하나의 함수를 취해 또 다른 함수를 반환하는 함수다.
# 코드를 바꾸지 않고, 사용하고 있는 함수를 수정하고 싶을 때 사용


def document_it(func):
    def new_function(*args, **kwargs):
        print("Running function:", func.__name__)
        print("Posional arguments:", args)
        print("Keyword arguemnts:", kwargs)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result

    return new_function


def add_ints(a, b):
    return a + b


print(add_ints(3, 5))

cooler_add_ints = document_it(add_ints)
print(cooler_add_ints(3, 5))


# Running function: add_ints
# Posional arguments: (3, 5)
# Keyword arguemnts: {}
# Result: 8
# 8

# 위와 같이 수동으로 decorator를 할당하는 대신 @데터레이터_이름 을 사용하고자 하는 함수에 할당하여 사용 가능
@document_it
def deco_add_ints(a, b):
    return a + b


print(deco_add_ints(3, 5))


# 한 함수에 여러 decorator를 설정할 수 있다.
# result를 제곱하는 decorator 작성
def result_square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result

    return new_function


@document_it
@result_square_it
def new_add_ints(a, b):
    return a + b


# decorator는 함수와 가까운 순서부터 수행된다. result_square_it --> document_it

print(new_add_ints(3, 4))
