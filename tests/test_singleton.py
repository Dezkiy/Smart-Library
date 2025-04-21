from creational_patterns.singleton import LibraryCatalog
from src.book import Book


def test_singleton_instance():
    catalog1 = LibraryCatalog()
    catalog2 = LibraryCatalog()
    assert catalog1 is catalog2  # Ensure both variables point to the same instance


def test_singleton_add_and_find_book():
    catalog = LibraryCatalog()
    book = Book(
        title="Test Book",
        isbn="123-456",
        publication_year=2024,
        authors=["Test Author"],
        genre="Fiction",
        edition=1,
        publisher="Test Publisher",
        total_copies=10,
        available_copies=10,
        cover_image_url="test.jpg",
    )
    catalog.add_book(book)
    found_book = catalog.find_book("123-456")
    assert found_book is book


def test_singleton_remove_book():
    catalog = LibraryCatalog()
    book = Book(
        title="Test Book",
        isbn="123-456",
        publication_year=2024,
        authors=["Test Author"],
        genre="Fiction",
        edition=1,
        publisher="Test Publisher",
        total_copies=5,
        available_copies=5
    )
    catalog.add_book(book)
    catalog.remove_book("123-456")
    found_book = catalog.find_book("123-456")
    assert found_book is None
