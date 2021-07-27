while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
        # break 문을 만나면 iteration 종료
        # continue는 아래 실행문은 수행하지 않고 iteration 수행
    print(stuff.capitalize())

while True:
    value = input("Integer, please [q to quit]: ")
    if value == "q":
        break
    number = int(value)
    if number % 2 == 0:
        continue
        # 짝수는 skip 
    print(number, "square is", number*number)