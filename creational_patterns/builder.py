from typing import List
from src.book import Book

class BookBuilder:
    """
    Builder class for constructing a Book instance with optional attributes.
    """

    def __init__(self, title: str, isbn: str, publication_year: int, authors: List[str], genre: str):
        self._title = title
        self._isbn = isbn
        self._publication_year = publication_year
        self._authors = authors
        self._genre = genre
        self._edition = None
        self._publisher = None
        self._total_copies = None
        self._available_copies = None
        self._cover_image_url = None

    def set_edition(self, edition: int):
        self._edition = edition
        return self

    def set_publisher(self, publisher: str):
        self._publisher = publisher
        return self

    def set_total_copies(self, total_copies: int):
        self._total_copies = total_copies
        return self

    def set_available_copies(self, available_copies: int):
        self._available_copies = available_copies
        return self

    def set_cover_image_url(self, cover_image_url: str):
        self._cover_image_url = cover_image_url
        return self

    def build(self) -> Book:
        """
        Returns the final constructed Book object.
        """
        return Book(
            title=self._title,
            isbn=self._isbn,
            publication_year=self._publication_year,
            authors=self._authors,
            genre=self._genre,
            edition=self._edition,
            publisher=self._publisher,
            total_copies=self._total_copies,
            available_copies=self._available_copies,
            cover_image_url=self._cover_image_url
        )

# === Example Usage ===
if __name__ == "__main__":
    builder = BookBuilder(
        title="The Lord of the Rings",
        isbn="978-0544928210",
        publication_year=1954,
        authors=["J.R.R. Tolkien"],
        genre="Fantasy"
    )

    book = (builder
            .set_edition(3)
            .set_publisher("Allen & Unwin")
            .set_total_copies(20)
            .set_available_copies(5)
            .set_cover_image_url("https://example.com/lotr.jpg")
            .build())

    print(book)
