

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False   

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book: Book):
        if book.book_id in self.books:
            raise ValueError("Duplicate Book ID")
        self.books[book.book_id] = book
    
    def borrow_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found")

        book = self.books[book_id]
        if book.is_borrowed:
            raise ValueError("Book already borrowed")

        book.is_borrowed = True

    def return_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found")

        self.books[book_id].is_borrowed = False


    def get_all_books(self):
        return list(self.books.values())
    
    def generate_report(self):
        report = "ID | Title | Author | Status\n"
        report += "-" * 40 + "\n"

        for book in self.books.values():
            status = "Borrowed" if book.is_borrowed else "Available"
            report += f"{book.book_id} | {book.title} | {book.author} | {status}\n"

        return report

