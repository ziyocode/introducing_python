acme_customer = {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}
print(type(acme_customer))
print(acme_customer)

# dict로 변경
acme_customer1 = dict(first="wile", middle="E", last="Coyote")
print(acme_customer1)

lol = [['a', 'b'], ['c', 'b'], ['e', 'f']]
print(dict(lol))                            # {'a': 'b', 'c': 'b', 'e': 'f'}

lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
print(dict(lot))                            # {'a': 'b', 'c': 'b', 'e': 'f'}

tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print(dict(tol))                            # {'a': 'b', 'c': 'b', 'e': 'f'}

los = [ 'ab', 'cb', 'ef']
print(dict(los))                            # {'a': 'b', 'c': 'b', 'e': 'f'}

tos = ('ab', 'cd', 'ef')
print(dict(tos))
