tweet_limit = 280
tweet_string = "Blah" * 50
diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))

# == using walrus_operator
# 비교를 위한 변수를 선언과 동시에 할당해서 바로 조건문을 생성
if diff := tweet_limit - len(tweet_string) >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))