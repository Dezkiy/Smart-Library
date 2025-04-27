from typing import Optional, List
from repositories.reservation_repository import ReservationRepository
from src.reservation import Reservation


class InMemoryReservationRepository(ReservationRepository):
    def __init__(self):
        self._storage = {}  # {reservation_id: Reservation}

    def save(self, reservation: Reservation) -> None:
        self._storage[reservation._reservation_id] = reservation

    def find_by_id(self, id: str) -> Optional[Reservation]:
        return self._storage.get(id)

    def find_all(self) -> List[Reservation]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]

    def find_by_book(self, book) -> List[Reservation]:
        return [res for res in self._storage.values() if res.get_book() == book]

    def find_by_member(self, member) -> List[Reservation]:
        return [res for res in self._storage.values() if res.get_member() == member]

    def find_active_reservations(self) -> List[Reservation]:
        return [res for res in self._storage.values() if res._status == Reservation.STATUS_ACTIVE]

    def find_completed_reservations(self) -> List[Reservation]:
        return [res for res in self._storage.values() if res._status == Reservation.STATUS_COMPLETED]

    def find_canceled_reservations(self) -> List[Reservation]:
        return [res for res in self._storage.values() if res._status == Reservation.STATUS_CANCELED]
