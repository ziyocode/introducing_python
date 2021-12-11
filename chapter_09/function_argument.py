# positional argument
def menu(wine, entree, dessert):
    return {"wine": wine, "entree": entree, "dessert": dessert}

print(menu("chardoonay", "chicken", "cake"))

# keyword argument
print(menu(entree="beef", dessert="bagel", wine="bordeaux"))
# {'wine': 'bordeaux', 'entree': 'beef', 'dessert': 'bagel'}
print(menu("frontenac", dessert="flan", entree="fish"))
# {'wine': 'frontenac', 'entree': 'fish', 'dessert': 'flan'}

# default argument
def menu1(wine, entree, dessert="pudding"):
    return {"wine": wine, "entree": entree, "dessert": dessert}

print(menu1("chardonnay", "chicken"))
# {'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'pudding'}     // dessert -> default arguemnt

