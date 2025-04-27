from typing import Optional, List
from repositories.registration_repository import RegistrationRepository
from src.registration import Registration
from datetime import datetime


class InMemoryRegistrationRepository(RegistrationRepository):
    def __init__(self):
        self._storage = {}  # {registration_id: Registration}

    def save(self, registration: Registration) -> None:
        self._storage[registration._registration_id] = registration

    def find_by_id(self, id: str) -> Optional[Registration]:
        return self._storage.get(id)

    def find_all(self) -> List[Registration]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]

    def find_by_event(self, event) -> List[Registration]:
        return [reg for reg in self._storage.values() if reg.get_event() == event]

    def find_by_member(self, member) -> List[Registration]:
        return [reg for reg in self._storage.values() if reg.get_member() == member]

    def find_registrations_in_date_range(self, start_date: str, end_date: str) -> List[Registration]:
        start = datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.strptime(end_date, "%Y-%m-%d").date()
        return [reg for reg in self._storage.values() if start <= reg._registration_date <= end]
