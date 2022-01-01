from collections import defaultdict

# 딕셔너리에 존재하지 않는 key로 접근하면 exception이 발생한다.
# 기본값을 반환하는 딕셔너리에 get() 함수를 사용하면 exception을 피할 수 있다.
# setdefault()함수는 get()과 같지만 key가 누락된 경우 딕셔너리에 item을 할당한다.

periodic_table = {"Hydrogen": 1, "Helium": 2}
print(periodic_table)

carbon = periodic_table.setdefault("Carbon", 12)
print(carbon)
print(periodic_table)


# defaultdic() 는 setdefault()와 비슷하지만 딕셔너리를 생성할 때 모든 새 key에 대한 기본값을 먼저 지정한다.
periodic_table1 = defaultdict(int)
periodic_table1["Hydrogen"] = 1
periodic_table1["Lead"]

print(periodic_table1)
print(type(periodic_table))


def no_idea():
    return "Huh?"


bestiary = defaultdict(no_idea)
bestiary["A"] = "Abominable Snowman"
bestiary["B"] = "Basilisk"

print(bestiary["C"]# # + # ㅇ여연연ㅅ사산산ㄱ고과과 과 ㄷ다달다다르륵르르게게 게 ㄷㄷㅎㅎeggs rkqtㄱ가갑값값ㅇ이이 이 2ㄹ로로 로 ㄷ두 집합 중 높은 숫자의 공통 항목을 반환하다.)
# Huh? -> defaultdict()의 입력은 값이 누락된 key에 할당하여 반환하는 함수다.
