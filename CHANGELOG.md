# CHANGELOG

## Recent Changes

* **Creational Patterns Implementation:**
    * Implemented all six creational design patterns (Simple Factory, Factory Method, Abstract Factory, Builder, Prototype, Singleton) in the `/creational_patterns` directory. (Related to task in assignment)
* **Class Implementation:**
    * Implemented core library classes (Book, LibraryMember, Loan, etc.) in the `/src` directory as per the design. (Related to task in assignment)
* **Bug Fixes:**
    * Fixed #16: Corrected the loan due date calculation logic to account for weekends and holidays.
* **Improvements:**
    * Implemented #17: Added basic search functionality for book titles, allowing users to search the catalog.
    * Refactored error handling in the book borrowing process for better user feedback (addresses #18).
 

# 📦 CHANGELOG.md (Assignment 11)

> All notable changes to this project are documented in this file.  
> This project adheres to [Semantic Versioning](https://semver.org/).

---

## [1.0.0] - 2025-05-05

### 🚀 Added

- 📘 **Books API**
  - `POST /api/books/`: Create a new book entry.
  - `GET /api/books/`: Retrieve all books.
  - `GET /api/books/{book_id}`: Get a specific book by ID.
  - `DELETE /api/books/{book_id}`: Delete a book by ID.

- 👤 **Members API**
  - `POST /api/members/`: Register a new library member.
  - `GET /api/members/`: List all members.
  - `GET /api/members/{member_id}`: Retrieve member details.
  - `DELETE /api/members/{member_id}`: Remove a member.

- 📅 **Reservations API**
  - `POST /api/reservations/`: Reserve a book.
  - `GET /api/reservations/`: List all reservations.

- 📑 **API Schema Models**
  - `BookRequest`, `BookResponse`
  - `MemberRequest`, `MemberResponse`
  - `ReservationRequest`, `ReservationResponse`
  - Standardized `ValidationError` schema for error responses

- 🧪 **Unit Tests**
  - Added `test_book_routes.py`
  - Added `test_member_routes.py`
  - Added `test_reservation_routes.py`

- 🧾 **Documentation**
  - Swagger UI auto-generated at `/docs`
  - Markdown documentation of all endpoints, schemas, and error handling
  - Included screenshots and sample payloads in `/docs`

### 🛠️ Changed

- 🔧 Updated `main.py` to modularize routing with FastAPI's `include_router`.
- 🧼 Replaced deprecated `.dict()` with `model_dump()` for Pydantic v2+ compatibility.
- 🏷️ Added `tags` for better categorization of endpoints in Swagger.

### 🐞 Fixed

- 🛑 Fixed missing `get_all_books()` implementation in `BookService`.
- 🧱 Resolved 404 error when attempting to get a member that does not exist.
- 🩹 Improved request validation for required fields using Pydantic.
- 🧹 Cleaned up route imports and test files for better maintainability.

---


