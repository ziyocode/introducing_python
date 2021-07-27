number_list = list(range(1, 6))
print(number_list)

number_list2 = [ number for number in range(1,6)]
print(number_list2)

# if만 있을 때는 뒤에
number_odd_list = [ number for number in range(1,6) if number % 2 != 0]
print(number_odd_list)

# if / else 문은 앞에
number_odd_list1 = [ number if number % 2 !=0 else "even" for number in range(1,6)]
print(number_odd_list1)

# list를 사용한 unpacking
odds = [1, 3, 5]
evens = [2, 4, 6]
cells = [(odd, even) for odd in odds for even in evens]
print(cells)

for o, e in cells:
    print(o, e)