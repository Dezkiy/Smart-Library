from typing import Optional, List
from abc import ABC, abstractmethod
from repositories.repository import Repository
from src.registration import Registration  # Import the Registration entity class
from src.library_event import LibraryEvent
from src.library_member import LibraryMember


class RegistrationRepository(Repository[Registration, str], ABC):  # ID type is str (registration_id)
    """
    Repository interface for Registration entities.
    """

    @abstractmethod
    def find_by_event(self, event: LibraryEvent) -> List[Registration]:
        """
        Finds all registrations for a given event.
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_member(self, member: LibraryMember) -> List[Registration]:
        """
        Finds all registrations made by a given member.
        """
        raise NotImplementedError

    @abstractmethod
    def find_registrations_in_date_range(self, start_date: str, end_date: str) -> List[Registration]:
        """
        Finds all registrations within a specific date range.
        """
        raise NotImplementedError
