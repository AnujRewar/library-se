| Req ID | User Story | Sprint | Implementation (Code) | Verification ( Tests) | Release Tag | Status |

| US1 | Add and store books | Spring-1 | src/app.py → LibrarySystem.add_book() |tests/test_app.py → test_add_book_success, test_add_book_duplicate | v0.1 | Planned |
| US2 | Reject Duplicate Book IDs | Sprint-1 |  src/app.py → LibrarySystem.add_book() | tests/test_app.py → test_add_book_missing_fields |  v0.1 |  Planned | 
| US3 | Manage Borrowing status | Sprint-2 | src/app.py->LibrarySystem.borrow_book, return_book | tests/test_app.py -> test_borrow_book_success,test_borrow_already_borrowed_book,test_return_book_success,test_return_not_borrowed_book | v0.2 | Planned |
| US4 | Generate a library status report | Sprint-3 |        |           |          | Planned |

