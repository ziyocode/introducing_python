some_pythons = {
    'Graham': 'Chapman',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael'
}

print(some_pythons)
print(some_pythons['Graham'])
print(some_pythons.get('Graham'))
print(some_pythons.get("Ziyo", "Not found"))

signals = {"green": 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(signals.keys())

# key 만 list에 넣기
list_keys = list(signals.keys())
print(list_keys)

# value 만 list에 넣기
list_values = list(signals.values())
print(list_values)

# 모든 items 가져오기
list_items = list(signals.items())
print(list_items)

# length 확인
print(len(some_pythons))


