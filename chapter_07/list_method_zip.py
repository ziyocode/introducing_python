days = ["Monday", "Tuesday", "Wednesday"]
fruits = ["banana", "orange", "peach"]
drinks = ["coffee", "tea", "beer"]
desserts = ["tiramisu", "ice cream", "pie", "pudding"]

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

# 가장 짧은 시퀀스가 완료되면 zip()은 멈춤

english = ["monday", "Tuesday", "Wednesday"]
french = ["Lundi", "Mardi", "Mercredi"]

day_list = list(zip(english, french))
print(day_list)

day_dict = dict(zip(english, french))
print(day_dict)