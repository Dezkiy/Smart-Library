from typing import Optional, List
from abc import ABC, abstractmethod
from repositories.repository import Repository
from src.book import Book  # Import the Book entity class

class BookRepository(Repository[Book, str], ABC):  # ID type is str (ISBN)
    """
    Repository interface for Book entities.
    """
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
