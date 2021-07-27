# split()
talk_like_a_pirate_day = "9/19/2019"
list_talk = talk_like_a_pirate_day.split("/")
print(list_talk)

country = ["korea", "japan", "china"]

# append()
country.append("USA")
print(country)

# insert()
country.insert(2, "thai")
print(country)

# extend()
city = ["seoul", "LA"]
country.extend(city)
print(country)

person = ["youngkook", "insung"]
country.append(person)
print(country)

# 값으로 항목 삭제하기 : remove()
country.remove("USA")
print(country)

# offset으로 항목의 값을 얻은 후 삭제하기 : pop()
my_country = country.pop(0)
print(country)
print(my_country)

# 값으로 offset을 찾기 : index()
print(country.index("seoul"))

# 값 세기 : count()
print(country.count("LA"))
print(country.count("XX"))



# sort() 는 리스트 자체를 내부적으로 정렬
# sorted() 는 리스트의 정렬된 복사본을 반환
del country[-1] # sort 전 list in list 삭제

country.sort()
print(country)
country.sort(reverse=True)
print(country)
sorted_country = sorted(country)
print(sorted_country)

# len() list 의 item 개수 세기
print(len(country))

# copy()
country2 = country.copy()
print(country2)
# list()
country3 = list(country)
print(country3)
# country2, country3 는 모두 새로운 객체, 참조가 아니다.
# country 를 변경하더라도 country2, country3 는 변하지 않는다.
print(id(country))
print(id(country2))
print(id(country3))


