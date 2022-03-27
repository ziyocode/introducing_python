from concurrent.futures import thread


blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)
# b'\x01\x02\x03\xff'

the_byte_array = bytearray(blist)
print(the_byte_array)
# bytearray(b'\x01\x02\x03\xff')

# the_bytes[1] = 127
# bytes 변수는 변경이 안 된다.

the_byte_array[1] = 127
print(the_byte_array)
# bytearray(b'\x01\x7f\x03\xff') <-- byte array 변수는 수정이 가능


