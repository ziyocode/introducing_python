bdata = bytes(range(0, 256))
print(len(bdata))

fout = open("bfile.txt", "wb")
fout.write(bdata)
fout.close()


# text 파일처럼 chunk 단위로 데이터 쓰기
fout1 = open("bfile1.txt", "wb")
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout1.write(bdata[offset:offset+chunk])
    offset += chunk
fout1.close()


fin = open("bfile.txt", "rb")
bdata = fin.read()
print(bdata)

fin.close()
