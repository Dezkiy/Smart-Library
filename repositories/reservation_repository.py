from typing import Optional, List
from abc import ABC, abstractmethod
from repositories.repository import Repository
from src.reservation import Reservation  # Import the Reservation entity class
from src.book import Book
from src.library_member import LibraryMember


class ReservationRepository(Repository[Reservation, str], ABC):  # ID type is str (reservation_id)
    """
    Repository interface for Reservation entities.
    """

    @abstractmethod
    def find_by_book(self, book: Book) -> List[Reservation]:
        """
        Finds all reservations for a given book.
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_member(self, member: LibraryMember) -> List[Reservation]:
        """
        Finds all reservations made by a given member.
        """
        raise NotImplementedError

    @abstractmethod
    def find_active_reservations(self) -> List[Reservation]:
        """
        Finds all reservations that are currently active.
        """
        raise NotImplementedError

    @abstractmethod
    def find_completed_reservations(self) -> List[Reservation]:
        """
        Finds all reservations that are completed.
        """
        raise NotImplementedError

    @abstractmethod
    def find_canceled_reservations(self) -> List[Reservation]:
        """
        Finds all reservations that are canceled.
        """
        raise NotImplementedError
