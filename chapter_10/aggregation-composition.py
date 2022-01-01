class Bill:
    def __init__(self, description):
        self.description = description


class Tail:
    def __init__(self, length):
        self.length = length


class Duck:
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print("This duck has a", self.bill.description, "bill and a", self.tail.length, "tail")


a_tail = Tail("long")
a_bill = Bill("wide orange")
duck = Duck(a_bill, a_tail)

print(duck.about())


# aggregation 과 Composition 은 상속의 좋은 대안이다.
# 오리는 조류이다. (상속관계, 자식 is a 부모)
# 오리는 꼬리를 가지고 있다. (aggregation or composition, 오리 has a 꼬리)
# 한 객체는 다른 객체를 사용하지만, 둘 다 독립적으로 존재한다.
