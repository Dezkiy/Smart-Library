from abc import ABC, abstractmethod
from repositories.repository import Repository
from src.book import Book
from typing import List, Optional  # Importing Optional and List from typing

class BookRepository(Repository[Book, str], ABC):  # ID type is str (ISBN)
    """
    Repository interface for Book entities.
    """
    @abstractmethod
    def save(self, book: Book) -> None:
        """
        Save a book entity to the storage.
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[Book]:
        """
        Finds a book by its unique identifier (ISBN).
        Returns None if the book is not found.
        """
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[Book]:
        """
        Finds all books stored in the repository.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> None:
        """
        Delete a book by its unique identifier (ISBN).
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_title(self, title: str) -> List[Book]:
        """
        Finds all books with the given title.
        """
        raise NotImplementedError
    
    @abstractmethod
    def find_by_author(self, author: str) -> List[Book]:
        """
        Finds all books by the given author.
        """
        raise NotImplementedError
