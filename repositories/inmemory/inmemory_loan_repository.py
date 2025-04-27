from typing import Optional, List
from repositories.loan_repository import LoanRepository
from src.loan import Loan
from datetime import date


class InMemoryLoanRepository(LoanRepository):
    def __init__(self):
        self._storage = {}  # {loan_id: Loan}

    def save(self, loan: Loan) -> None:
        self._storage[loan._loan_id] = loan

    def find_by_id(self, id: str) -> Optional[Loan]:
        return self._storage.get(id)

    def find_all(self) -> List[Loan]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]

    def find_by_member(self, member_id: str) -> List[Loan]:
        return [loan for loan in self._storage.values() if loan.get_member().get_member_id() == member_id]

    def find_by_book(self, isbn: str) -> List[Loan]:
        return [loan for loan in self._storage.values() if loan.get_book().get_isbn() == isbn]

    def find_overdue_loans(self) -> List[Loan]:
        today = date.today()
        return [loan for loan in self._storage.values() if loan._due_date < today and loan._return_date is None]
