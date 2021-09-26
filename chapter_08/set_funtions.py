s = set([1, 2, 3])
print(s)

s.add(4)
print(s)

s.remove(2)
print(s)

furniture = set(('sofa', 'ottoman', 'table'))
for piece in furniture:
    print(piece)

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

# 보드카가 포함된 음료는?
for name, contents in drinks.items():
    if "vodka" in contents:
        print(name)

# 셋 교집합 (&)
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)
# martini
# manhattan
# screwdriver

print("#####")
for name, contents in drinks.items():
    if 'vodca' in contents and not contents & {'vermouth', 'cream'}:
        print(name)