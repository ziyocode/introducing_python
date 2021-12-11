# ** keyword args
def print_kwargs(**kwargs):
    print("Keyword arguments:", kwargs)

print(print_kwargs())

print(print_kwargs(wine="merlot", entree="mutton", dessert="macaroon"))
# Keyword arguments: {'wine': 'merlot', 'entree': 'mutton', 'dessert': 'macaroon'}