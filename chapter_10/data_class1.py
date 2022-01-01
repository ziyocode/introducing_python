from dataclasses import dataclass

@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0

snowman = AnimalClass("sunae", "Himalayas", 42)

print(snowman)
print(snowman.habitat)

duck = AnimalClass(name="YoungKook", habitat="seoul")
print(duck)
print(duck.name)

# __init__() 을 통한 변수 초기화 설정의 대안으로 dataclass를 사용할 수 있다.
# dataclass 의 인수 입력은 초기화 순서대로 입력하거나, 이름을 지정하여 임의의 순서로 줄 수 있다.
# teeth 의 경우 초기화 값(0)을 넣어서 객체를 생성할 때 제공하지 않아도 된다. 