class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"
class EBook:
    def __init__(self, title, author, file_size):
        self.file_size = file_size
        self.book = Book(title, author)
    def __str__(self):
        return f"{self.book.__str__()}, File Size: {self.file_size} "
class PrintBook:
    def __init__(self, title, author, page_count):
        self.page_count = page_count
        self.book = Book(title, author)
    def __str__(self):
        return f"{self.book.__str__()}, Page Count: {self.page_count} "
class Library:
    books = []
    def add_book(self, book):
        self.books.append(book)
    def list_books(self):
        for book in self.books:
            print(str(book))
