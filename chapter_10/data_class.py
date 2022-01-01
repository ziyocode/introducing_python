from dataclasses import dataclass

# name 속성
class TeenyClass:
    def __init__(self, name):
        self.name = name


teeny = TeenyClass("Yunwoo")
print(teeny.name)


# dataclass
# name: type (이름: 타입)
@dataclass
class TeenyDataClass:
    name: str


data_teeny = TeenyDataClass("Insung")
print(data_teeny.name)
