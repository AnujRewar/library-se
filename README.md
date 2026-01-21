Library Management System (Agile Project)
Overview

This project implements a simple Library Management System developed using Agile methodology. The system allows managing books by supporting book registration, borrowing and returning of books, and generating a library status report. The project follows proper software engineering practices including sprint-based development, unit testing, version control, and traceability.
Features
Sprint 1 – Book Registration

Add a book with unique Book ID, Title, and Author.

Prevent duplicate Book IDs.

Sprint 2 – Borrow and Return

Borrow an available book.

Return a borrowed book.

Prevent borrowing of already borrowed books.

Sprint 3 – Library Report

Generate a report containing:

Book ID

Title

Author

Status (Available / Borrowed)

Project Structure
library-se/
├── src/
│   ├── __init__.py
│   └── library.py
│
├── tests/
│   ├── __init__.py
│   └── test_library.py
│
├── docs/
│   ├── USER_STORIES.md
│   └── TRACEABILITY.md
│
└── README.md
Technologies Used

Language: Python 3

Testing Framework: unittest

Version Control: Git & GitHub

How to Run Tests

From the project root directory:

python -m unittest discover -s tests -p "test_*.py" -v
