from collections import OrderedDict

quotes = {
    "Moe": "A wise quy, huh?",
    "Larry": "Ow!",
    "Curly": "Nyuk nyuk!",
}

for stooge in quotes:
    print(stooge)


quotes1 = OrderedDict([
    ("Moe", "A wise quy, huh?"),
    ("Larry", "Ow!"),
    ("Curly", "Nyuk nyuk!"),
    ])

for stooge in quotes1:
    print(stooge)

