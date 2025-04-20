from datetime import date, time
from typing import Optional
from src.library_member import LibraryMember  # Needed if you track registered members here

class LibraryEvent:
    def __init__(self, event_id: str, title: str, description: str,
                 event_date: date, start_time: time, end_time: time,
                 location: str, capacity: int, registration_deadline: Optional[date]):
        self._event_id = event_id
        self._title = title
        self._description = description
        self._event_date = event_date
        self._start_time = start_time
        self._end_time = end_time
        self._location = location
        self._capacity = capacity
        self._registration_deadline = registration_deadline
        self._registered_members = []  # Temporarily handles registrations

    def register_member(self, member: LibraryMember):
        if len(self._registered_members) < self._capacity:
            self._registered_members.append(member)
            return True
        return False

    def cancel_registration(self, member: LibraryMember):
        if member in self._registered_members:
            self._registered_members.remove(member)
            return True
        return False

    def get_available_seats(self) -> int:
        return self._capacity - len(self._registered_members)

    def get_event_id(self) -> str:
        return self._event_id

    def __str__(self):
        return f"LibraryEvent(event_id='{self._event_id}', title='{self._title}', date='{self._event_date}')"
