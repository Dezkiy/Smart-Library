# repositories/inmemory/inmemory_book_repository.py

from typing import Optional, List
from repositories.book_repository import BookRepository
from src.book import Book


class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self._storage = {}  # {isbn (str): Book}

    def save(self, book: Book) -> None:
        self._storage[book.get_isbn()] = book

    def find_by_id(self, id: str) -> Optional[Book]:
        return self._storage.get(id)

    def find_all(self) -> List[Book]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]

    def find_by_title(self, title: str) -> List[Book]:
        return [book for book in self._storage.values() if book.get_title() == title]

    def find_by_author(self, author: str) -> List[Book]:
        return [book for book in self._storage.values() if author in book._authors]
