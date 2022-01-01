class Fruit:
    color = "red"

blueberry = Fruit()
print(Fruit.color)

blueberry.color = "blue"
print(blueberry.color)

Fruit.color = "orange"
print(Fruit.color)
print(blueberry.color)

# 나중에 클래스(Fruit) 속성을 변경해도 자식 객체에는 영향을 미치지 않는다.