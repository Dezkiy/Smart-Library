# services/book_service.py

from typing import List
from src.book import Book
from repositories.book_repository import BookRepository


class BookService:
    def __init__(self, book_repo: BookRepository):
        self._book_repo = book_repo

    def get_all_books(self) -> List[Book]:
        return self._book_repo.find_all()

    def create_book(self, book: Book):
        self._book_repo.save(book)

    def update_book(self, isbn: str, updated_book: Book) -> bool:
        existing_book = self._book_repo.find_by_id(isbn)
        if not existing_book:
            return False
        self._book_repo.save(updated_book)
        return True

    def checkout_book(self, isbn: str) -> bool:
        book = self._book_repo.find_by_id(isbn)
        if not book or book.get_available_copies() <= 0:
            return False
        book.set_available_copies(book.get_available_copies() - 1)
        self._book_repo.save(book)
        return True

