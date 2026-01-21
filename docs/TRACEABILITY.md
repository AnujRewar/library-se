# Traceability Matrix

| Requirement | Implementation | Test |
|------------|----------------|------|
| Add book | Library.add_book() | test_add_book_success |
| Reject duplicate | Library.add_book() | test_duplicate_book |
| Borrow book | Library.borrow_book() | test_borrow_available_book |
| Reject double borrow | Library.borrow_book() | test_borrow_unavailable_book |
| Return book | Library.return_book() | test_return_book |
| Generate report | Library.generate_report() | test_report_contains_header |
| Report entry | Library.generate_report() | test_report_contains_book_entry |
