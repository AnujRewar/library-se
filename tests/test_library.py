import unittest
from src.library import Book, Library


class TestLibrary(unittest.TestCase):

    def test_add_book_success(self):
        lib = Library()
        lib.add_book(Book(1, "DSA", "Anuj"))
        self.assertEqual(len(lib.get_all_books()), 1)

    def test_duplicate_book(self):
        lib = Library()
        lib.add_book(Book(1, "DSA", "Anuj"))
        with self.assertRaises(ValueError):
            lib.add_book(Book(1, "OS", "Someone"))


if __name__ == "__main__":
    unittest.main()

