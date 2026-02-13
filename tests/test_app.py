import unittest
from src.app import LibrarySystem

class TestSprint1(unittest.TestCase):

    def test_add_book_success(self):
        lib = LibrarySystem()
        lib.add_book("B101", "Clean Code", "Robert C. Martin")

        self.assertIn("B101", lib.books)
        self.assertEqual(lib.books["B101"].title, "Clean Code")
        self.assertEqual(lib.books["B101"].author, "Robert C. Martin")

    def test_add_book_duplicate(self):
        lib = LibrarySystem()
        lib.add_book("B101", "Clean Code", "Robert C. Martin")

        with self.assertRaises(ValueError):
            lib.add_book("B101", "Refactoring", "Martin Fowler")

    def test_add_book_missing_fields(self):
        lib = LibrarySystem()

        with self.assertRaises(ValueError):
            lib.add_book("", "Clean Code", "Robert C. Martin")

        with self.assertRaises(ValueError):
            lib.add_book("B101", "", "Robert C. Martin")

        with self.assertRaises(ValueError):
            lib.add_book("B101", "Clean Code", "")
            
class TestSprint2(unittest.TestCase):
   
   def test_borrow_book_success(self):
        lib=LibrarySystem()
        lib.add_book("B101", "Clean Code", "Robert C. Martin")

        lib.borrow_book("B101")
        self.assertTrue(lib.books["B101"].is_borrowed)
   
   def test_borrow_already_borrowed_book(self):
        lib=LibrarySystem()
        lib.add_book("B101", "Clean Code", "Robert C. Martin")
        lib.borrow_book("B101")
        with self.assertRaises(ValueError):
            lib.borrow_book("B101")
    
   def test_return_book_success(self):
        lib = LibrarySystem()
        lib.add_book("B101", "Clean Code", "Robert C. Martin")

        lib.borrow_book("B101")
        lib.return_book("B101")

        self.assertFalse(lib.books["B101"].is_borrowed)


   def test_return_not_borrowed_book(self):
        lib = LibrarySystem()
        lib.add_book("B101", "Clean Code", "Robert C. Martin")
        
        with self.assertRaises(ValueError):
            lib.return_book("B101")

if __name__ == "__main__":
    unittest.main()

