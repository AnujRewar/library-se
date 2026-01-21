

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book: Book):
        if book.book_id in self.books:
            raise ValueError("Duplicate Book ID")
        self.books[book.book_id] = book

    def get_all_books(self):
        return list(self.books.values())
