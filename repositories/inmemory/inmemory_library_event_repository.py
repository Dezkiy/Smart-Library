# repositories/inmemory/inmemory_event_repository.py

from typing import Optional, List
from repositories.event_repository import EventRepository
from src.library_event import LibraryEvent
from datetime import date

class InMemoryEventRepository(EventRepository):
    """
    In-memory implementation of EventRepository using a dictionary.
    """

    def __init__(self):
        self._storage = {}  # {event_id: LibraryEvent}

    def save(self, event: LibraryEvent) -> None:
        self._storage[event.get_event_id()] = event

    def find_by_id(self, id: str) -> Optional[LibraryEvent]:
        return self._storage.get(id)

    def find_all(self) -> List[LibraryEvent]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]

    def find_by_title(self, title: str) -> List[LibraryEvent]:
        return [event for event in self._storage.values() if event._title == title]

    def find_by_date(self, event_date: str) -> List[LibraryEvent]:
        return [event for event in self._storage.values() if str(event._event_date) == event_date]

    def find_upcoming_events(self) -> List[LibraryEvent]:
        today = date.today()
        return [event for event in self._storage.values() if event._event_date > today]

    def find_past_events(self) -> List[LibraryEvent]:
        today = date.today()
        return [event for event in self._storage.values() if event._event_date < today]
