empty_set = set()
print(empty_set)

even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers)
print(odd_numbers)
print(type(odd_numbers))

# set() 으로 리스트, 문자열, 튜플, 딕셔너리를 set으로 변환할 수 있다. 단 이때 중복값은 제거 된다.
set_strings = set('letters')
print(set_strings)
# {'e', 's', 't', 'r', 'l'}

set_list = set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon', 'Dancer', 'Prancer'])
print(set_list)
# {'Mason-Dixon', 'Dasher', 'Dancer', 'Prancer'}

set_dict = set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'})
print(set_dict)
# {'cherry', 'apple', 'orange'}         // key를 중복 없이 set type 으로 가져옴
print(type(set_dict))

reindeer = set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
print(len(reindeer))
