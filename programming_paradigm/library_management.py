class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def get_title_author(self):
        return self.title, self.author, self._is_checked_out
class Library():
    _books = []
    #def __init__(self):
     #   self._books = []
    def add_book(self, book):
        Library._books.append(Book.get_title_author(book))
    def check_out_book(self, title):
        i = 0
        for item in Library._books:
            if item[0] == title:
                Library._books[i] = (item[0], item[1], True)
            i += 1
    def list_available_books(self):
        for item in Library._books:
            if item[2] == False:
                print(f"\n{item[0]} by {item[1]}")
    def return_books(self, title):
        i = 0
        for item in Library._books:
            if item[0] == title:
                Library._books[i] = (item[0], item[1], False)
            i += 1
    def return_book(self):
        pass
