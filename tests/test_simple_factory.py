import pytest
from creational_patterns.simple_factory import ResourceFactory
from src.book import Book


def test_create_book_resource():
    book = ResourceFactory.create_resource(
        "book",
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
    assert isinstance(book, Book)
    assert book.get_title() == "Test Book"
    assert book.get_isbn() == "123-456"


def test_create_invalid_resource_type():
    with pytest.raises(ValueError) as exc_info:
        ResourceFactory.create_resource("invalid", title="Test")
    assert "Invalid resource type" in str(exc_info.value)