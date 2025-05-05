# services/reservation_service.py

from repositories.reservation_repository import ReservationRepository
from repositories.book_repository import BookRepository
from repositories.library_member_repository import LibraryMemberRepository
from src.reservation import Reservation

class ReservationService:
    def __init__(self, reservation_repo: ReservationRepository, book_repo: BookRepository, member_repo: LibraryMemberRepository):
        self._reservation_repo = reservation_repo
        self._book_repo = book_repo
        self._member_repo = member_repo

    def create_reservation(self, reservation: Reservation):
        # Example business rules (expand as needed):
        book = self._book_repo.find_by_id(reservation.book.id)
        member = self._member_repo.find_by_id(reservation.member.id)

        if not book:
            raise ValueError("Book does not exist")
        if not member:
            raise ValueError("Member does not exist")

        # Possibly check if book is available or if member has too many reservations

        self._reservation_repo.save(reservation)
        return reservation
