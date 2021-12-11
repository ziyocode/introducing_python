# global variable
animal = "fruitbat"
def print_global():
    print("inside print_global:", animal)

print("at the top level:", animal, id(animal))
print_global()

def change_local():
    animal = "wombat"
    print("inside print_local:", animal, id(animal))

change_local()

# global 설정 후 수정하기
def change_and_print_global():
    # global animal
    animal = "cat"
    print("after the change:", animal)
    print("locals: ",locals())
    print("globals: ",globals())

change_and_print_global()

# locals() : 지역 변수를 dict 형식으로 반환
# globals() : 전연 변수를 dict 형식으로 반환
