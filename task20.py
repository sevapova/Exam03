'''20. Real Project Mini-task
Task: Library system yozing.'''

class Library:
    def __init__(self):
        self.books = {}  

    def add_book(self, title, author):
        self.books[title] = True

    def borrow_book(self, title):
        if self.books.get(title):
            self.books[title] = False
            return f"You borrowed '{title}'"
        return f"Sorry, '{title}' is not available"

    def return_book(self, title):
        if title in self.books and not self.books[title]:
            self.books[title] = True
            return f"You returned '{title}'"
        return f"'{title}' was not borrowed"


lib = Library()
lib.add_book("1984", "George Orwell")
lib.add_book("Xamsa", "Alisher Navoiy")

print(lib.borrow_book("1984"))
print(lib.borrow_book("1984"))
print(lib.return_book("1984"))
