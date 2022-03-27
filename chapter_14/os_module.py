import os
import shutil
import glob
from pathlib import Path

print(os.path.exists("bfile.txt"))
print(os.path.exists("./bfile.txt"))

print(os.path.isfile("bfile.txt"))
print(os.path.isdir("chapter_01"))

# isabs() 는 인수가 절대경로인지 확인한다.
print(os.path.isabs("bfile.txt"))
# False
print(os.path.isabs("/etc/passwd"))
# True

# copy
shutil.copy("bfile1.txt", "bfile_copy.txt")
# rename
#os.rename("bfile.txt", "bfile_rename.txt")
# link
# os.link("bfile1.txt", "bfile_hardlink.txt")
# os.symlink("bfile1.txt", "bfile_symlink.txt")

# os command
os.chmod("bfile1.txt", 444)
os.remove("bfile_copy.txt")
os.mkdir("bfile_dir")
os.listdir("bfile_dir")
os.rmdir("bfile_dir")

# glob() : 복잡한 정규 표현식이 아닌, 유닉스 셸 규칙을 사용하여 일치하는 파일이나, 디렉터리 이름을 검색해준다.
print(glob.glob("b*"))
# ['bfile1.txt', 'bfile_symlink.txt', 'bfile_rename.txt', 'bfile_hardlink.txt']
print(glob.glob("bfile?.txt"))

# 절대 경로 얻기 : abspath()
print(os.path.abspath("bfile1.txt"))
# /Users/ziyomac/Documents/workspaces/python/introducing_python/bfile1.txt

# 심볼릭 링크의 원본 패스을 얻기 : realpath()
print(os.path.realpath("bfile_symlink.txt"))

# 경로 이름 작성하기 : os.path.join()
password_file = os.path.join("/etc", "password")
print(password_file)
# /etc/password


password_file1 = Path("/etc") / "passwd"
print(password_file1)
# /etc/passwd









