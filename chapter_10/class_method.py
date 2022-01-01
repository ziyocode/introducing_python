class A:
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I am an A!")

    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")


easy_a = A()
breezy_a = A()
wheezy_a = A()
temp_a = A()

print(A.kids())
print(A.count)

# self.count 를 참조하지 않고 A.count(클래스 속성)를 참조했다.
# kids() 메서드에서 A.count를 사용하지 않고, cls.count를
