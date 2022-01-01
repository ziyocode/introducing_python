class Car:
    def exclaim(self):
        print("I am a Car")


class Yugo:
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")


give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()


class Person:
    def __init__(self, name):
        self.name = name


class MDPerson(Person):
    def __init__(self, name):
        self.name = "Docter " + name


class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

person = Person("Insung")
doctor = MDPerson("Insung")
lawyer = JDPerson("Insung")

print(person.name)
print(doctor.name)
print(lawyer.name)