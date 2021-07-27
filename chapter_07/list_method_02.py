country = ["korea", "japan", "china", "thai"]

# offset으로 항목 바꾸기
country[1] = "canada"
print(country)

# offsel으로 항목 삭제하게 del
del country[2]
print(country)

# 존재하는지 확인 : in
print("canada" in country)
print("seoul" in country)

# 문자열로 변환하기 : join()
ToString = ", ".join(country)
print(ToString)

# len() list 의 item 개수 세기
print(len(country))
