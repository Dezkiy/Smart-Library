from creational_patterns.builder import BookBuilder
from src.book import Book


def test_book_builder_creation():
    builder = BookBuilder(
        title="Test Book",
        isbn="123-456",
        publication_year=2024,
        authors=["Test Author"],
        genre="Fiction",
    )
    assert isinstance(builder, BookBuilder)


def test_book_builder_builds_book():
    builder = BookBuilder(
        title="Test Book",
        isbn="123-456",
        publication_year=2024,
        authors=["Test Author"],
        genre="Fiction",
    )
    book = builder.build()
    assert isinstance(book, Book)
    assert book.get_title() == "Test Book"
    assert book.get_isbn() == "123-456"


def test_book_builder_with_optional_attributes():
    builder = BookBuilder(
        title="Test Book",
        isbn="123-456",
        publication_year=2024,
        authors=["Test Author"],
        genre="Fiction",
    )
    book = (
        builder.set_edition(2)
        .set_publisher("Test Publisher")
        .set_total_copies(5)
        .set_available_copies(5)
        .build()
    )
    assert book.get_edition() == 2
    assert book.get_publisher() == "Test Publisher"
    assert book.get_total_copies() == 5
    assert book.get_available_copies() == 5
