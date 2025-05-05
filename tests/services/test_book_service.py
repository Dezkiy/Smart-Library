import unittest
from unittest.mock import MagicMock
from datetime import date
from repositories.services.book_service import BookService
from src.book import Book


class TestBookService(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MagicMock()
        self.service = BookService(self.mock_repo)

        self.book = Book(
            title="Effective Python",
            isbn="PY123",
            publication_year=2019,
            authors=["Brett Slatkin"],
            genre="Programming",
            edition=2,
            publisher="Pearson",
            total_copies=5,
            available_copies=3
        )

    def test_add_book(self):
        self.service.add_book(self.book)
        self.mock_repo.save.assert_called_once_with(self.book)

    def test_get_book_success(self):
        self.mock_repo.find_by_id.return_value = self.book
        result = self.service.get_book("PY123")
        self.assertEqual(result, self.book)

    def test_get_book_not_found(self):
        self.mock_repo.find_by_id.return_value = None
        with self.assertRaises(ValueError):
            self.service.get_book("UNKNOWN")

    def test_remove_book_success(self):
        self.mock_repo.find_by_id.return_value = self.book
        result = self.service.remove_book("PY123")
        self.assertTrue(result)
        self.mock_repo.delete.assert_called_once_with("PY123")

    def test_remove_book_not_found(self):
        self.mock_repo.find_by_id.return_value = None
        result = self.service.remove_book("UNKNOWN")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
