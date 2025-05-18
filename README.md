# Smart-Library-01

# Smart Library System

## Description

The Smart Library System aims to modernize library operations by providing a comprehensive platform for managing physical and digital resources, facilitating member interactions, and offering enhanced services.

This system will enable:

* Efficient management of books, journals, and digital media.
* Streamlined member registration and borrowing processes.
* Online access to digital content and library resources.
* Automated notifications and reminders.

## Links

* [SPECIFICATION.md](SPECIFICATION.md)
* [ARCHITECTURE.md](ARCHITECTURE.md)

## Assignment 5:
- [Use Case Diagrams.md](./Use%20Case%20Diagram.md)
- [Use Case Specification.md](./Use%20Case%20Specification.md)
- [Test Case Development.md](./Test%20Case%20Development.md)

## Assignment 6:
- [User Story Creation.md](./User%20Story%20Creation.md)
- [Product Backlog Creation.md](./Product%20Backlog%20Creation.md)
- [Sprint Planning.md](./Sprint%20Planning.md)


 ## Kanban Board Customization Choices

 The Kanban board for this project was customized to align with the specific workflow and quality assurance requirements of the Smart Library System. The following columns were added to the base template:

 * **To Do:** This column represents the initial stage of tasks that are ready for development but have not yet been started.
   
 * **In Progress:** This column tracks tasks that are currently being worked on by the development team.
   
 * **Testing:** This column was added to explicitly track tasks that are undergoing quality assurance. This allows the development team to visualize which tasks have been completed from a development standpoint but still require validation before deployment.
   
 * **Blocked:** This column is used to highlight tasks that are currently impeded or cannot progress due to external dependencies or unresolved issues. This provides visibility into any bottlenecks or delays in the workflow, enabling the team to address them promptly.
   
 * **Done:** This column represents the final stage of tasks that have been completed, tested, and are ready for deployment.

 These customizations enhance the board's utility by providing a more detailed view of the task lifecycle and supporting a more robust Agile development process.


![Screenshot (3)](https://github.com/user-attachments/assets/bdb9fa80-16c5-485a-94c3-6f7f82f6279e)

![Screenshot (4)](https://github.com/user-attachments/assets/04612543-a78c-4999-9ebd-1d7ad571d7d8)


## Assignment 7:
- [Template Analysis and Selection.md](./Template%20Analysis%20and%20Selection.md)
- [Kanboard Board Explanation.md](./Kanboard%20Board%20Explanation.md)
- [Reflection.md](./Reflection.md)


## Assignment 8:
- [Object State Modeling.md](./Object%20State%20Modeling.md)
- [Activity Workflow Modeling.md](./Activity%20Workflow%20Modeling.md)
- [Integration with Prior Work.md](./Integration%20with%20Prior%20Work.md)
- [Reflection Assignment 8.md](./Reflection%20Assignment%208.md)

## Assignment 9:
- [Domain Model](Domain%20Model.md)  
- [Class Diagram in Mermaid](Class%20Diagram%20in%20Mermaid.md)  
- [Reflection Assignment 9](Reflection%20Assignment%209.md)

 
## Assignment 10:

- [Class Implementation Details Assignment 10.md](Class%20Implementation%20Details%20Assignment%2010.md) - For details on the language choice and key design decisions
- [Source Code Directory](src/) - Contains the source code files.
- [Creational Patterns Justification.md](./Creational%20Patterns%20Justification.md) - For details on the creational design patterns used
- [Creational Patterns Directory](creational_patterns/) - Implementation of various creational design patterns.
- [Tests Directory](./tests/) - Contains all test files
- [Test Coverage Report.md](./Test%20Coverage%20Report.md) - View test coverage metrics
- [CHANGELOG.md](./CHANGELOG.md) - Version history and updates


## Assignment 11:

## Justification: Repository Layer Design

The repository layer is implemented using a generic `Repository` interface (`repositories/repository.py`). This approach leverages Python's typing system (specifically, `TypeVar` and `Generic`) to avoid code duplication across entity-specific repositories.  For example, instead of writing separate CRUD implementations for `Book`, `LibraryMember`, etc., we define the common operations once in the `Repository` interface and then create entity-specific interfaces (e.g., `BookRepository`) that inherit from it.  This promotes code reuse and maintainability. Each entity-specific repository interface can also define methods unique to that entity (e.g., `BookRepository`'s `find_by_title`).

- [Storage Abstraction Mechanism](./factories/Storage%20Abstraction%20Mechanism.md) - For explanation of Abstraction Mechanism choice.


## Future-Proofing: Adding New Storage Backends

### DatabaseBookRepository (SQLite)
The system is designed to easily add new storage backends in the future. As an example, we have created a stub implementation for a `DatabaseBookRepository` that will save book data to an SQLite database.

You can find the stub implementation here:
- **[DatabaseBookRepository Stub](https://github.com/Mongameli-Shasha-01/Smart-Library/blob/main/repositories/database_book_repository.py)**


### SQLite Database File
For SQLite storage, we have also provided a basic `database.db` file that can be used for storing the data. You can refer to it in the project’s database integration section:
- **[SQLite Database File](https://github.com/Mongameli-Shasha-01/Smart-Library/blob/main/data/database.db)**


## Assignment 12:
## 📄 API Documentation

The **Smart Library API** is documented using **FastAPI's Swagger UI**, providing interactive and auto-generated docs at runtime.

### 🔗 Access the Swagger UI

Start your FastAPI server and open:

👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**


---

## 📚 Endpoints Overview

### 🔸 Books

| Method | Endpoint         | Description           |
|--------|------------------|-----------------------|
| GET    | `/api/books/`    | List all books        |
| POST   | `/api/books/`    | Add a new book        |
| GET    | `/api/books/{id}`| Get a book by ID      |
| DELETE | `/api/books/{id}`| Delete a book by ID   |

### 🔸 Members

| Method | Endpoint           | Description              |
|--------|--------------------|--------------------------|
| GET    | `/api/members/`    | List all members         |
| POST   | `/api/members/`    | Register a new member    |
| GET    | `/api/members/{id}`| Get a member by ID       |
| DELETE | `/api/members/{id}`| Delete a member by ID    |

### 🔸 Reservations

| Method | Endpoint               | Description                |
|--------|------------------------|----------------------------|
| GET    | `/api/reservations/`   | List all reservations      |
| POST   | `/api/reservations/`   | Make a new reservation     |

---

# 📘 Smart Library API Documentation

## 📌 Overview

This FastAPI-based Smart Library System offers RESTful endpoints to manage books, library members, and reservations.

---

## 🔗 Base URL

```
http://localhost:8000
```

---

## 📚 Endpoints

### 📘 Books

#### ➕ Create Book

* **POST** `/api/books/`
* **Request Body:** `BookRequest`
* **Response:** `BookResponse`
* **Error:** 422 (Validation Error)

#### 📄 List All Books

* **GET** `/api/books/`
* **Response:** `List[BookResponse]`

#### 🔍 Get Book by ID

* **GET** `/api/books/{book_id}`
* **Response:** `BookResponse`
* **Error:** 404 (Book not found)

#### ❌ Delete Book

* **DELETE** `/api/books/{book_id}`
* **Response:** Success message
* **Error:** 404 (Book not found)

---

### 👤 Members

#### ➕ Create Member

* **POST** `/api/members/`
* **Request Body:** `MemberRequest`
* **Response:** `MemberResponse`
* **Error:** 422 (Validation Error)

#### 📄 List All Members

* **GET** `/api/members/`
* **Response:** `List[MemberResponse]`

#### 🔍 Get Member by ID

* **GET** `/api/members/{member_id}`
* **Response:** `MemberResponse`
* **Error:** 404 (Member not found)

#### ❌ Delete Member

* **DELETE** `/api/members/{member_id}`
* **Response:** Success message
* **Error:** 404 (Member not found)

---

### 📝 Reservations

#### ➕ Create Reservation

* **POST** `/api/reservations/`
* **Request Body:** `ReservationRequest`
* **Response:** `ReservationResponse`
* **Error:** 422 (Validation Error)

#### 📄 List All Reservations

* **GET** `/api/reservations/`
* **Response:** `List[ReservationResponse]`

#### 🔍 Get Reservation by ID

* **GET** `/api/reservations/{reservation_id}`
* **Response:** `ReservationResponse`
* **Error:** 404 (Reservation not found)

#### ❌ Delete Reservation

* **DELETE** `/api/reservations/{reservation_id}`
* **Response:** Success message
* **Error:** 404 (Reservation not found)

---

## 🧾 Schema Models

### 🔹 BookRequest

```json
{
  "isbn": "978-1234567890",
  "title": "Sample Book",
  "publication_year": 2020,
  "authors": ["Author One", "Author Two"],
  "genre": "Fiction",
  "edition": 1,
  "publisher": "Book Publisher",
  "total_copies": 10,
  "available_copies": 10,
  "description": "Optional book description"
}
```

### 🔹 BookResponse

```json
{
  "book_id": "B001",
  "isbn": "978-1234567890",
  "title": "Sample Book",
  "publication_year": 2020,
  "authors": ["Author One", "Author Two"],
  "genre": "Fiction",
  "edition": 1,
  "publisher": "Book Publisher",
  "total_copies": 10,
  "available_copies": 10,
  "description": "Optional book description"
}
```

### 🔹 MemberRequest

```json
{
  "member_id": "M001",
  "first_name": "John",
  "last_name": "Doe",
  "date_of_birth": "1995-08-15",
  "email": "john@example.com",
  "phone_number": "1234567890",
  "address": "123 Main St",
  "membership_date": "2024-01-01",
  "membership_type": "Regular",
  "status": "Active"
}
```

### 🔹 MemberResponse

```json
{
  "member_id": "M001",
  "first_name": "John",
  "last_name": "Doe",
  "date_of_birth": "1995-08-15",
  "email": "john@example.com",
  "phone_number": "1234567890",
  "address": "123 Main St",
  "membership_date": "2024-01-01",
  "membership_type": "Regular",
  "status": "Active"
}
```

### 🔹 ReservationRequest

```json
{
  "reservation_id": "R001",
  "book_id": "B001",
  "member_id": "M001",
  "reservation_date": "2024-05-05"
}
```

### 🔹 ReservationResponse

```json
{
  "reservation_id": "R001",
  "book_id": "B001",
  "member_id": "M001",
  "reservation_date": "2024-05-05"
}
```

### 🔹 ValidationError Example

```json
{
  "detail": [
    {
      "loc": ["body", "title"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

---

## 📷 Swagger UI Screenshot

> ✅ Launch the server and visit: `http://localhost:8000/docs`
>
> 📸 Take a screenshot and save it under your `/docs` directory as `swagger_ui.png`

---

## 📁 Optional OpenAPI File

If you're exporting the OpenAPI spec:

* JSON: `http://localhost:8000/openapi.json`
* Save it as: `/docs/openapi.json` or `/docs/openapi.yaml`


## 🧾 Swagger UI Screenshot

![swagger-ui-screenshot](https://github.com/user-attachments/assets/94c9e8fd-1019-40ce-97ca-171304d51241)


## 📁 Project Structure Quick Links

### 🔗 API Endpoints
- [`api/book_routes.py`](./api/book_routes.py) – Book API endpoints
- [`api/member_routes.py`](./api/member_routes.py) – Member API endpoints
- [`api/reservation_routes.py`](./api/reservation_routes.py) – Reservation API endpoints

### 🧪 API Tests
- [`tests/api/test_book_routes.py`](./tests/api/test_book_routes.py)
- [`tests/api/test_member_routes.py`](./tests/api/test_member_routes.py)
- [`tests/api/test_reservation_routes.py`](./tests/api/test_reservation_routes.py)

### ⚙️ Service Layer
- [`repositories/services/book_service.py`](./repositories/services/book_service.py)
- [`repositories/services/member_service.py`](./repositories/services/member_service.py)
- [`repositories/services/reservation_service.py`](./repositories/services/reservation_service.py)

### 🧪 Service Layer Tests
- [`tests/services/test_book_service.py`](./tests/services/test_book_service.py)
- [`tests/services/test_member_service.py`](./tests/services/test_member_service.py)
- [`tests/services/test_reservation_service.py`](./tests/services/test_reservation_service.py)

## Assignment 13:
- [Branch Protection](./Protection.md)
- [Reflection on CI Test Failures](./Reflection%20on%20CI%20Test%20Failures.md)
- [CI Workflow Configuration](.github/workflows/ci.yml)
