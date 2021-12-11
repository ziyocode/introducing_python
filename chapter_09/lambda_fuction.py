def edit_story(words, func):
    for word in words:
        print(func(word))


stairs = ["thud", "meow", "thud", "hiss"]


def enliven(word):
    return word.capitalize() + "!"

print(edit_story(stairs, enliven))
# Thud!
# Meow!
# Thud!
# Hiss!
# None

print(edit_story(stairs, lambda word: word.capitalize() + "!"))
# func 부분에 lambda 식을 넣음 간결하게 처리