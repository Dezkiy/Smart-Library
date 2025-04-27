from typing import Optional, List
from abc import ABC, abstractmethod
from repositories.repository import Repository
from src.library_event import LibraryEvent  # Import the LibraryEvent entity class


class EventRepository(Repository[LibraryEvent, str], ABC):  # ID type is str (event_id)
    """
    Repository interface for LibraryEvent entities.
    """

    @abstractmethod
    def find_by_title(self, title: str) -> List[LibraryEvent]:
        """
        Finds all events with a given title.
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_date(self, event_date: str) -> List[LibraryEvent]:
        """
        Finds all events on a given date.
        """
        raise NotImplementedError

    @abstractmethod
    def find_upcoming_events(self) -> List[LibraryEvent]:
        """
        Finds all events that are scheduled to occur in the future.
        """
        raise NotImplementedError

    @abstractmethod
    def find_past_events(self) -> List[LibraryEvent]:
        """
        Finds all events that have already occurred.
        """
        raise NotImplementedError
