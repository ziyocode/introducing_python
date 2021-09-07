a = {1:1, 2:2, 3:3}
b = {2:2, 1:1, 3:3}
print(a == b)
print(a != b)

accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
for card in accusation:
    print(card)
# key 추출
#room
#weapon
#person
for card in accusation.values():
    print(card)
#ballroom
#lead pipe
#Col. Mustard
for card in accusation.items():
    print(card)
#('room', 'ballroom')
#('weapon', 'lead pipe')
#('person', 'Col. Mustard')


# dictionary comprehension
# {키_표현식: 값_표현식 for 표현식 in 순회 가능한 객체}
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)
#{'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}

vowels = 'aeiou'
word = 'onomatopoeia'
vowel_counts = {letter: word.count(letter) for letter in set(word) if letter in vowels}
print(vowel_counts)
#{'o': 4, 'e': 1, 'i': 1, 'a': 2}