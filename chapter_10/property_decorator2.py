class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(7)
print(c.radius)
print(c.diameter)    

# 속성에 대한 setter 프로퍼티를 명시하지 않으면, 외부에서 이 속성을 설정할 수 없다. (read-only)

c.diameter = 20
# 상기 코드는 error를 유발한다. // AttributeError: can't set attribute