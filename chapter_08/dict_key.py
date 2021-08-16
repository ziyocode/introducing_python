pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}

print(pythons)

# 딕셔너리 item 추가
pythons['Gilliam'] = 'Gerry'
print(pythons)

# 딕셔너리 item 수정
pythons['Gilliam'] = 'Terry'
print(pythons)

print(pythons['Idle'])
print(pythons.get('Jones'))

# get 을 통한 key 값을 사용할 때 키가 존재하지 않으면, default value를 지정하여 사용
print(pythons.get('Cho', 'Not in Pythons' ))                # Not in Pythons
# --> 옵션을 지정하지 않으면, None을 얻는다. 아무것도 출력되지 않는다.

# 모든 키 얻기
print(pythons.keys())
# dict_keys(['Chapman', 'Cleese', 'Idle', 'Jones', 'Palin', 'Gilliam'])
pythons_keys = list(pythons.keys())
print(pythons_keys)

