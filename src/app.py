from dataclasses import dataclass, field
from typing import Dict


# Book class
@dataclass
class Book:
    book_id: str
    title: str
    author: str
    is_borrowed: bool = False



# Library System class
@dataclass
class LibrarySystem:
    books: Dict[str, Book] = field(default_factory=dict)

    def add_book(self, book_id: str, title: str, author: str) -> None:
        # Check for missing fields
        if not book_id or not title or not author:
            raise ValueError("book_id, title and author are required")

        # Check for duplicate book ID
        if book_id in self.books:
            raise ValueError("book already exists")

        # Add book to dictionary
        self.books[book_id] = Book(
            book_id=book_id,
            title=title,
            author=author
        )
    
    def borrow_book(self, book_id: str) -> None:
        # Check if book exists
        if book_id not in self.books:
            raise KeyError("book not found")

        # Check if already borrowed
        if self.books[book_id].is_borrowed:
            raise ValueError("book already borrowed")

        # Mark book as borrowed
        self.books[book_id].is_borrowed = True


    def return_book(self, book_id: str) -> None:
        # Check if book exists
        if book_id not in self.books:
            raise KeyError("book not found")

        # Check if book is not borrowed
        if not self.books[book_id].is_borrowed:
            raise ValueError("book not borrowed")

        # Mark book as returned
        self.books[book_id].is_borrowed = False


