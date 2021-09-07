import copy

# 할당하기 =
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
save_signals = signals  # save_signals 에 signals 할당
print(save_signals)

signals['green'] = 'go go'
print(save_signals)  # save_signals 는 signals를 가리키고 있어 signals 변경 시 save_signals도 같이 변경

# 얕은 복사 copy()
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(signals)
print(original_signals)  #

print("signals", signals)
print("save_signals", save_signals)  # save_signals = signals // signals 변경을 따라가 update 된다.
print("original_signals", original_signals)  # signals = original_signals // 복사 시점 이후 변경을 따라 가지 않는다.
