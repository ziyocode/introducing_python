class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
# 자식 클래스에서 __init__을 선언하면 부모클래스의 __init__ 을 무시하고 대체 된다.
# 때문에 동일한 code(name에 대한)를 사용하기 위해 super().__init__(name) 을 추가한다.

bob = EmailPerson("Bob Frapples", "bob@frapples.com")

print(bob.name)
print(bob.email)