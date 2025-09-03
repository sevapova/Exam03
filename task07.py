'''7. Classmethod & Staticmethod
Task: StringTools classida:

is_palindrome(text) static methodi yozing
from_sentence("I love Python") classmethod orqali obyekt yarating va so‘zlar ro‘yxatini saqlang.'''

class StringTools:
    def __init__(self, word):
        self.word = word

    @staticmethod
    def is_palindrome(text):
        text = text.lower()
        return text == text[::-1]

    @classmethod
    def from_sentence(cls, sentence):
        word = sentence.split()
        return cls(word)


print(StringTools.is_palindrome("level"))   

stringtools = StringTools.from_sentence("I love Python")
print(stringtools.word)                             