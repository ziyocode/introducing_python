pythons = {
    'Champman': 'Graham',
    'Cleese': 'John',
    'Gilliam': 'Terry',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}

print(pythons)
others = {'Marx': 'Groucho', 'Howard': 'Moe'}
updated_python = pythons.update(others)
print(updated_python)

# get method
print(pythons.get("Champman"))
print(pythons.get("Champ", "not found"))

# 결합하기
first = {'a': 'agnoy', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
third = {**first, **second}
print(third)
# {'a': 'agnoy', 'b': 'bagels', 'c': 'candy'} // b는 second의 값으로 update
fourth = {**second, **first}
print(fourth)
# {'b': 'bliss', 'c': 'candy', 'a': 'agnoy'}

first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
print(first.update(second))

# del 로 항목 삭제하기
del pythons['Champman']
print(pythons)

# pop() 으로 항목 가져오고 삭제
print(len(pythons))                 # 7
pop_item = pythons.pop('Idle')
print(pop_item)                     # Eric
print(len(pythons))                 # 6

# clear()로 모든 항목 삭제
pythons.clear()
print(pythons)
# {}로 초기화
pythons = {}
