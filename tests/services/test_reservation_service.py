import unittest
from unittest.mock import MagicMock
from datetime import date
from repositories.services.reservation_service import ReservationService
from src.book import Book
from src.library_member import LibraryMember
from src.reservation import Reservation


class TestReservationService(unittest.TestCase):

    def setUp(self):
        # Create mocks for repositories
        self.mock_reservation_repo = MagicMock()
        self.mock_book_repo = MagicMock()

        # Create the service instance
        self.service = ReservationService(self.mock_reservation_repo, self.mock_book_repo)

        # Sample test objects
        self.book = Book(
            title="Clean Code",
            isbn="CC123",
            publication_year=2008,
            authors=["Robert C. Martin"],
            genre="Programming",
            edition=1,
            publisher="Prentice Hall",
            total_copies=3,
            available_copies=2
        )

        self.member = LibraryMember(
            member_id="M001",
            first_name="Alice",
            last_name="Smith",
            date_of_birth=date(1990, 5, 10),
            email="alice@example.com",
            phone="123456789",
            address="123 Main Street",
            registration_date=date.today(),
            member_type="Standard",
            account_status="Active"
        )

    def test_reserve_book_success(self):
        self.mock_book_repo.find_by_id.return_value = self.book
        self.mock_book_repo.save.return_value = None

        reservation = self.service.reserve_book(self.member, "CC123")

        self.assertEqual(reservation.book, self.book)
        self.assertEqual(reservation.member, self.member)
        self.assertEqual(reservation.reservation_date, date.today())
        self.mock_reservation_repo.save.assert_called_once()
        self.assertEqual(self.book.get_available_copies(), 1)

    def test_reserve_book_not_found(self):
        self.mock_book_repo.find_by_id.return_value = None

        with self.assertRaises(ValueError) as context:
            self.service.reserve_book(self.member, "INVALID_ID")

        self.assertIn("Book with ID INVALID_ID not found", str(context.exception))

    def test_reserve_book_no_copies(self):
        self.book._available_copies = 0
        self.mock_book_repo.find_by_id.return_value = self.book

        with self.assertRaises(ValueError) as context:
            self.service.reserve_book(self.member, "CC123")

        self.assertIn("No copies available", str(context.exception))

    def test_cancel_reservation_success(self):
        reservation = Reservation(
            reservation_id="RSV001",
            book=self.book,
            member=self.member,
            reservation_date=date.today(),
            notification_date=None
        )

        self.book._available_copies = 1

        self.mock_reservation_repo.find_by_id.return_value = reservation
        self.mock_book_repo.save.return_value = None

        result = self.service.cancel_reservation("RSV001")

        self.assertTrue(result)
        self.assertEqual(self.book.get_available_copies(), 2)
        self.mock_reservation_repo.delete.assert_called_once_with("RSV001")

    def test_cancel_reservation_not_found(self):
        self.mock_reservation_repo.find_by_id.return_value = None

        result = self.service.cancel_reservation("INVALID_ID")

        self.assertFalse(result)
        self.mock_reservation_repo.delete.assert_not_called()


if __name__ == '__main__':
    unittest.main()
