from typing import Optional
from datetime import date, timedelta
from src.book import Book
from src.library_member import LibraryMember

class Loan:
    def __init__(self, loan_id: str, book: Book, member: LibraryMember,
                 borrow_date: date, due_date: date, return_date: Optional[date] = None):
        self._loan_id = loan_id
        self._book = book
        self._member = member
        self._borrow_date = borrow_date
        self._due_date = due_date
        self._return_date = return_date

    def calculate_overdue_fine(self, return_date: date, fine_rate: float) -> float:
        if return_date > self._due_date:
            days_overdue = (return_date - self._due_date).days
            return days_overdue * fine_rate
        return 0.0

    def extend_due_date(self, extension_days: int):
        self._due_date += timedelta(days=extension_days)

    def mark_as_returned(self, return_date: date):
        self._return_date = return_date

    # Getters
    def get_book(self) -> Book:
        return self._book

    def get_member(self) -> LibraryMember:
        return self._member

    def __str__(self):
        return f"Loan(loan_id='{self._loan_id}', book='{self._book}', member='{self._member}')"
