# read : 전체를 한번에 읽기 (메모리 소모가 심함, while + chunk로 나눠서 읽기 권장)
# readline : 한 줄씩 읽기 (while로 한 줄씩 추가)
# for iterator로 한 줄씩 읽기 : 권장됨
# readlines : 한번에 읽어서 줄별로 리스트로 반환 (줄 마지막에 줄바꿈 문자도 포함됨 "\n")

fin = open("getting_started.txt", "rt")
getting_started = fin.read()
fin.close()
print(len(getting_started))


# 나눠서 읽기 : 한번에 너무 많은 양을 읽으면 너무 많은 메모리 소비를 할 수 있음
getting_started01 = ""
fin1 = open("getting_started.txt", "rt")
chunk = 100
while True:
    fragment = fin1.read(chunk)
    if not fragment:
        break
    getting_started01 += fragment

fin1.close()
print(len(getting_started01))


# readline() 함수를 이용해 한 줄씩 읽기
getting_started02 = ""
fin2 = open("getting_started.txt", "rt")
while True:
    line = fin2.readline()
    if not line:
        break
    getting_started02 += line

fin2.close()
print(len(getting_started02))

# iterator를 이용한 파일 읽기 : 가장 좋은 방법이라 한다.
getting_started03 = ""
fin3 = open("getting_started.txt", "rt")
for line in fin3:
    getting_started03 += line

fin3.close()
print(len(getting_started03))


# readlines()는 전체 파일을 읽어 한줄로 된 문자열 list로 반환한다.
fin4 = open("getting_started.txt", "rt")
lines = fin4.readlines()
fin4.close()
print(len(lines), "lines read")
print(lines)
# ['\n', 'Getting Started with Java in VS Code\n', 'This tutorial shows you how to write and run Hello World program in Java with Visual Studio Code. It also covers a few advanced features, which you can explore by reading other documents in this section.\n', '\n', 'For an overview of the features available for Java in VS Code, see Java Language Overview.\n', '\n', 'If you run into any issues when following this tutorial, you can contact us by entering an issue.\n', '\n', 'Setting up VS Code for Java development#\n', 'Coding Pack for Java#\n', 'To help you set up quickly, you can install the Coding Pack for Java, which includes VS Code, the Java Development Kit (JDK), and essential Java extensions. The Coding Pack can be used as a clean installation, or to update or repair an existing development environment.\n']
print(type(lines))
# <class 'list'>