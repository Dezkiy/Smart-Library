from typing import List, Dict, Optional
from src.book import Book


class LibraryCatalog:
    """
    Singleton class that holds a catalog of books.
    Only one instance of this class can exist at a time.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Ensure initialization only happens once
        if not hasattr(self, '_initialized'):
            self._books: Dict[str, Book] = {}  # ISBN as key
            self._initialized = True

    def add_book(self, book: Book):
        """Add a book to the catalog using its ISBN as the key."""
        self._books[book.get_isbn()] = book

    def find_book(self, isbn: str) -> Optional[Book]:
        """Find and return a book by its ISBN."""
        return self._books.get(isbn)

    def remove_book(self, isbn: str):
        """Remove a book from the catalog by its ISBN."""
        if isbn in self._books:
            del self._books[isbn]

    def get_all_books(self) -> List[Book]:
        """Return a list of all books in the catalog."""
        return list(self._books.values())

    def __str__(self):
        return f"LibraryCatalog with {len(self._books)} book(s)"


# === Example Usage ===
if __name__ == "__main__":
    catalog1 = LibraryCatalog()
    catalog2 = LibraryCatalog()

    print(f"Same instance? {catalog1 is catalog2}")  # True

    book1 = Book(
        title="The Shining",
        isbn="978-0385121790",
        publication_year=1977,
        authors=["Stephen King"],
        genre="Horror",
        edition=1,
        publisher="Doubleday",
        total_copies=5,
        available_copies=5,
        cover_image_url=None
    )

    catalog1.add_book(book1)

    found = catalog2.find_book("978-0385121790")
    if found:
        print(f"Found book: {found.get_title()} in catalog2")

    print(catalog1)  # Should show 1 book