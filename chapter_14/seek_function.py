import os

# seek(offset, origin)
# origin 0 일 때, 시작 위치에서 offset 바이트로 이동한다.
# origin 1 일 때, 현재 위치에서 offset 바이트로 이동한다.
# origin 2 일 때, 마지막 위치에서 offset 바이트 전 위치로 이동한다.

fin = open("bfile.txt", "rb")
print(fin.tell())
# 0
# 파일 시작 위치에서 현재 offset을 바이트 단위로 반환한다.
print(fin.seek(255))
# 255

print(fin.tell())
# 255 <-- seek 255로 넘긴 후 offset 확인
bdata = fin.read()
# offset을 255까지 넘긴 후 읽기
fin.close()

print(len(bdata))

print(os.SEEK_SET) # 표준 os 모듈에 0
print(os.SEEK_CUR) # 1
print(os.SEEK_END) # 2


fin1 = open("bfile.txt", "rb")
print(fin1.seek(-1, 2))
# 255
print(fin1.seek(25,0))
# 25
print(fin1.seek(30,1))
# 55
