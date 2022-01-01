class Animal:
    def says(self):
        return "I speak!"


class Horse(Animal):
    def says(self):
        return "말말말"


class Donkey(Animal):
    def says(self):
        return "히하"


class Mule(Donkey, Horse):
    pass


class Hinny(Horse, Donkey):
    pass


mule = Mule()
hinny = Hinny()

print(mule.says())
print(hinny.says())

