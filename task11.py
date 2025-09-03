'''11. Composition
Task: Book classida Author obyektidan foydalaning.
'''

class Author:
    def __init__(self, name):
        self.name = name


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author   

    def get_info(self):
        return f"Book: {self.title}, Author: {self.author.name}"


a = Author("Alisher Navoiy")
b = Book("Xamsa", a)
print(b.get_info())
