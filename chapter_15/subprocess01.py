import subprocess

# getoutput() shell 에서 수행
ret = subprocess.getoutput("date -u | wc")
print(ret)

# check_output() 명령과 인수를 취함, 출력으로 문자열이 아닌 바이트 유형을 사용, shell을 사용하지 않는다.
ret1 = subprocess.check_output(['date', '-u'])
print(ret1)

# getstatusoutput() 프로그램의 상태 코드와 결과를 튜플로 반환
ret2 = subprocess.getstatusoutput('date')
print(ret2)
# (0, '2022년 2월 26일 토요일 09시 11분 04초 KST')

# call() 프로그램 상태 코드만 반환
ret3 = subprocess.call('date')
print(ret3)
# 0 <-- 정상종료

ret4 = subprocess.call('date -u', shell=True)
print(ret4)

ret5 = subprocess.call(['date', '-u'])
print(ret5)
# 2022년 2월 26일 토요일 00시 15분 45초 UTC
# 0