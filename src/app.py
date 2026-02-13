from dataclasses import dataclass, field
from typing import Dict


# Book class
@dataclass
class Book:
    book_id: str
    title: str
    author: str



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

