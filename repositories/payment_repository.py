from typing import Optional, List
from abc import ABC, abstractmethod
from repositories.repository import Repository
from src.payment import Payment  # Import the Payment entity class
from src.library_member import LibraryMember


class PaymentRepository(Repository[Payment, str], ABC):  # ID type is str (payment_id)
    """
    Repository interface for Payment entities.
    """

    @abstractmethod
    def find_by_member(self, member: LibraryMember) -> List[Payment]:
        """
        Finds all payments made by a given member.
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_status(self, status: str) -> List[Payment]:
        """
        Finds all payments with a given status (e.g., "Pending", "Completed").
        """
        raise NotImplementedError

    @abstractmethod
    def find_payments_in_date_range(self, start_date: str, end_date: str) -> List[Payment]:
        """
        Finds all payments made within a specific date range.
        """
        raise NotImplementedError
