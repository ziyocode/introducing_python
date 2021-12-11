short_list = [1, 2, 3]
position = 5

try:
    shor_list[position]
    # IndexError 발생
except:
    print("Need a position between 0 and", len(short_list) -1, " but got", position)

