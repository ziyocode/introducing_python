class Word():
    def __init__(self, text):
        self.text = text
    # def equals(self, word2):
    def __eq__(self, word2):                                # magic method
        return self.text.lower() == word2.text.lower()

first = Word("ha")
second = Word("HA")
third = Word("eh")

# print(first.equals(second))
# print(first.equals(third))

print(first == second)
print(first == third)