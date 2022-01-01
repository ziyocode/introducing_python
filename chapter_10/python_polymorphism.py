# 다형성 (polymorphism)


class Quote:
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + "."


class QuestionQuote(Quote):
    def says(self):
        return self.words + "?"


class ExclaimationQuote(Quote):
    def says(self):
        return self.words + "!"


hunter = Quote("Elmer Fudd", "I'm hunting rabbits")
print(hunter.who(), "says: ", hunter.says())

hunter1 = QuestionQuote("Bugs Bunny", "What's up, doc")
print(hunter1.who(), "says: ", hunter1.says())

hunter2 = ExclaimationQuote("Daffy Duck", "It's rabbit season")
print(hunter2.who(), "says: ", hunter2.says())