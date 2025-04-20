from typing import List, Optional  # For type hinting

 class Book:
    def __init__(self, title: str, isbn: str, publication_year: int,
                 authors: List[str], genre: str, edition: int,
                 publisher: str, total_copies: int, available_copies: int,
                 cover_image_url: Optional[str]):
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
        # Implementation for reservation logic (e.g., adding to a reservation list)
        # This might involve another class (Reservation)
        pass

    def is_available(self) -> bool:
        return self._available_copies > 0

    # Getters (if needed)
    def get_title(self) -> str:
        return self._title

    def get_isbn(self) -> str:
        return self._isbn

    # Setters (if needed - use with caution and validation)
    def set_available_copies(self, copies: int):
        if 0 <= copies <= self._total_copies:
            self._available_copies = copies
        else:
            raise ValueError("Invalid number of available copies")

    def __str__(self):
        return f"Book(title='{self._title}', ISBN='{self._isbn}')"
