from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from src.book import Book
from repositories.services.book_service import BookService
from repositories.inmemory.inmemory_book_repository import InMemoryBookRepository

# Initialize repository and service
book_repository = InMemoryBookRepository()
book_service = BookService(book_repository)

router = APIRouter(prefix="/api/books", tags=["Books"])

# Pydantic models
class BookRequest(BaseModel):
    title: str
    isbn: str
    publication_year: int
    authors: List[str]
    genre: str
    edition: int
    publisher: str
    total_copies: int
    available_copies: int
    cover_image_url: Optional[str] = None

class BookResponse(BookRequest):
    pass

# 🔁 Helper function: Convert domain model to Pydantic model
def book_to_response(book: Book) -> BookResponse:
    return BookResponse(
        title=book.get_title(),
        isbn=book.get_isbn(),
        publication_year=book._publication_year,
        authors=book._authors,
        genre=book._genre,
        edition=book.get_edition(),
        publisher=book.get_publisher(),
        total_copies=book.get_total_copies(),
        available_copies=book.get_available_copies(),
        cover_image_url=book._cover_image_url
    )

@router.get("/", response_model=List[BookResponse])
def get_all_books():
    books = book_service.get_all_books()
    return [book_to_response(book) for book in books]

@router.post("/", response_model=BookResponse)
def create_book(book_data: BookRequest):
    """Create a new book entry in the library. Return 400 if ISBN already exists."""
    # Check for duplicate ISBN
    existing_books = book_service.get_all_books()
    if any(book.get_isbn() == book_data.isbn for book in existing_books):
        raise HTTPException(status_code=400, detail="Book with this ISBN already exists")
    book = Book(**book_data.model_dump())
    book_service.create_book(book)
    return book_to_response(book)

@router.put("/{isbn}", response_model=BookResponse)
def update_book(isbn: str, book_data: BookRequest):
    updated_book = Book(**book_data.dict())
    result = book_service.update_book(isbn, updated_book)
    if not result:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_to_response(updated_book)

@router.post("/{isbn}/checkout")
def checkout_book(isbn: str):
    success = book_service.checkout_book(isbn)
    if not success:
        raise HTTPException(status_code=400, detail="Book not available or not found")
    return {"message": f"Book with ISBN {isbn} checked out successfully"}
