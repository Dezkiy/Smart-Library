from typing import Optional, List
from abc import ABC, abstractmethod
from repositories.repository import Repository
from src.loan import Loan  # Import the Loan entity class

class LoanRepository(Repository[Loan, str], ABC):  # ID type is str (loan_id)
    """
    Repository interface for Loan entities.
    """
    @abstractmethod
    def find_by_member(self, member_id: str) -> List[Loan]:
        """
        Finds all loans associated with a given member.
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_book(self, isbn: str) -> List[Loan]:
        """
        Finds all loans for a given book (by ISBN).
        """
        raise NotImplementedError

    @abstractmethod
    def find_overdue_loans(self) -> List[Loan]:
        """
        Finds all loans that are currently overdue.
        """
        raise NotImplementedError
