class Cat:
    def __init__(self, name):
        self.name = name
# __init__() 는 클래스 정의에서 개별 객체를 초기화하는 특수 메서드다.
# self 는 개별 객체 자신을 참조하도록 지정한다.
# __init__() 을 정의할 때 첫 번째 매개변수 이름은 self 이어야 한다. (self는 예약어는 아니지만 일반적으로 사용한다.)

furball = Cat("Grumpy")

print(furball.name)