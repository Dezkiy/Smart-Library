import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_and_get_book():
    # Create a book
    response = client.post("/api/books", json={
        "isbn": "123-TEST",
        "title": "Test Driven Development",
        "publication_year": 2003,
        "authors": ["Kent Beck"],
        "genre": "Software Engineering",
        "edition": 1,
        "publisher": "Addison-Wesley",
        "total_copies": 5,
        "available_copies": 5,
        "description": "A book on TDD"
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Test Driven Development"

    # Get all books
    get_response = client.get("/api/books")
    assert get_response.status_code == 200
    assert any(book["isbn"] == "123-TEST" for book in get_response.json())
