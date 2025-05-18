from typing import List, Optional  # For type hinting

class Book:
    """
    Represents a book in the Smart Library system.

    Attributes:
        _title (str): The title of the book.
        _isbn (str): The International Standard Book Number (ISBN) of the book.
        _publication_year (int): The year the book was published.
        _authors (List[str]): A list of authors for the book.
        _genre (str): The genre of the book.
        _edition (int): The edition number of the book.
        _publisher (str): The publisher of the book.
        _total_copies (int): The total number of copies available in the library.
        _available_copies (int): The number of copies currently available for checkout.
        _cover_image_url (Optional[str]): The URL to the book's cover image, if available.

    Methods:
        check_out(): Attempts to check out the book if available.
        return_book(): Returns a book, increasing the available copies.
        reserve(): Placeholder for reservation logic.
        is_available(): Returns True if at least one copy is available.
        Getters and setters for book attributes.
    """
    def __init__(self, title: str, isbn: str, publication_year: int,
                 authors: List[str], genre: str, edition: int,
                 publisher: str, total_copies: int, available_copies: int,
                 cover_image_url: Optional[str] = None):
        self._title = title
        self._isbn = isbn
        self._publication_year = publication_year
        self._authors = authors
        self._genre = genre
        self._edition = edition
        self._publisher = publisher
        self._total_copies = total_copies
        self._available_copies = available_copies
        self._cover_image_url = cover_image_url

    def check_out(self):
        if self._available_copies > 0:
            self._available_copies -= 1
            return True
        return False

    def return_book(self):
        if self._total_copies > self._available_copies:
            self._available_copies += 1
            return True
        return False

    def reserve(self):
        raise NotImplementedError("Reservation logic is handled elsewhere.")

    def is_available(self) -> bool:
        return self._available_copies > 0

    # Getters
    def get_title(self) -> str:
        return self._title

    def get_isbn(self) -> str:
        return self._isbn
    
    def get_edition(self) -> int:
        return self._edition

    def get_publisher(self) -> str:
        return self._publisher

    def get_total_copies(self) -> int:
        return self._total_copies

    def get_available_copies(self) -> int:
        return self._available_copies


    # Setters
    def set_available_copies(self, copies: int):
        if 0 <= copies <= self._total_copies:
            self._available_copies = copies
        else:
            raise ValueError("Invalid number of available copies")

    def __str__(self):
        return f"Book(title='{self._title}', ISBN='{self._isbn}')"