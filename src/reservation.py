from datetime import date
 from typing import Optional
 from src.book import Book
 from src.library_member import LibraryMember

 class Reservation:
    def __init__(self, reservation_id: str, book: Book, member: LibraryMember,
                 reservation_date: date, notification_date: Optional[date],
                 status: str):
        self._reservation_id = reservation_id
        self._book = book
        self._member = member
        self._reservation_date = reservation_date
        self._notification_date = notification_date
        self._status = status

    def send_notification(self):
        # Implementation for sending a notification to the member
        pass

    def cancel_reservation(self):
        self._status = "Canceled"

    def mark_as_active(self):
        self._status = "Active"

    def mark_as_completed(self):
        self._status = "Completed"

    # Getters and setters as needed
    def get_book(self) -> Book:
        return self._book

    def get_member(self) -> LibraryMember:
        return self._member

    def __str__(self):
        return f"Reservation(reservation_id='{self._reservation_id}', book='{self._book}', member='{self._member}')"
