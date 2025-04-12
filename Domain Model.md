# Domain Model for Smart Library System

This document describes the domain model for the Smart Library System. It identifies the key entities within the system, their attributes and responsibilities, the relationships between them, and relevant business rules.

## Key Entities

| Entity          | Attributes                                                                 | Methods                                                                                                  | Relationships                                                                                                             |
|-----------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| **Book**        | `title: String`, `ISBN: String`, `publicationYear: Int`, `author(s): String[]`, `genre: String`, `edition: String`, `publisher: String`, `totalCopies: Int`, `availableCopies: Int`, `coverImageURL: String` | `checkOut()`: Marks the book as checked out and updates availability. <br> `returnBook()`: Marks as returned. <br> `reserve()`: Creates a reservation. <br> `isAvailable()`: Returns a boolean status. | `One-to-Many` with `Loan` (A book can be involved in many loans). `One-to-Many` with `Reservation` (A book can have many reservations).                 |
| **LibraryMember** | `memberID: String`, `firstName: String`, `lastName: String`, `dateOfBirth: Date`, `email: String`, `phone: String`, `address: String`, `registrationDate: Date`, `memberType: Enum`, `accountStatus: Enum` | `borrowBook()`: Initiates a loan. <br> `returnBook()`: Completes a loan. <br> `reserveBook()`: Adds to reservation list. <br> `updateProfile()`: Edits member details. <br> `payFine()`: Pays fines. |  `One-to-Many` with `Loan` (A member can have many current and past loans). `One-to-Many` with `Reservation` (A member can make many reservations). `One-to-Many` with `Payment` (A member can make many payments).     |
| **Loan**        | `loanID: String`, `book: Book`, `member: LibraryMember`, `borrowDate: Date`, `dueDate: Date`, `returnDate: Date` | `calculateOverdueFine()`: Computes the fine based on due and return dates. <br> `extendDueDate()`: Extends borrowing period. <br> `markAsReturned()`: Marks the loan as completed. |  `Many-to-One` with `Book` (A loan involves one specific book). `Many-to-One` with `LibraryMember` (A loan is made by one specific member).                                                                      |
| **Reservation** | `reservationID: String`, `book: Book`, `member: LibraryMember`, `reservationDate: Date`, `notificationDate: Date`, `status: Enum` | `sendNotification()`: Notifies member of availability. <br> `cancelReservation()`: Cancels reservation. <br> `markAsActive()`, `markAsCompleted()` | `Many-to-One` with `Book` (A reservation is for one specific book). `Many-to-One` with `LibraryMember` (A reservation is made by one specific member).                                                                      |
| **Payment**     | `paymentID: String`, `member: LibraryMember`, `paymentDate: Date`, `amount: Float`, `paymentMethod: Enum`, `transactionID: String`, `paymentType: Enum` | `processPayment()`: Initiates payment logic. <br> `recordPayment()`: Stores payment info in system.      | `Many-to-One` with `LibraryMember` (A payment is made by one specific member).                                                                                      |
| **LibraryEvent**| `eventID: String`, `title: String`, `description: String`, `eventDate: Date`, `startTime: Time`, `endTime: Time`, `location: String`, `capacity: Int`, `registrationDeadline: Date` | `registerMember()`: Registers a user. <br> `cancelRegistration()`: Removes registration. <br> `getAvailableSeats()`: Calculates spots left. | `Many-to-Many` with `LibraryMember` (Members can register for many events, and events can have many registered members - through a registration entity, implicitly).                                                      |
| **Registration** _(New)_ | `registrationID: String`, `member: LibraryMember`, `event: LibraryEvent`, `registrationDate: Date` | `confirmRegistration()`: Confirms a member’s spot. <br> `cancelRegistration()`: Removes the link.         |  `One-to-Many` with `LibraryMember` (A member can register for many events). `One-to-Many` with `LibraryEvent` (An event can have many registered members).                                                              |

---

## Business Rules

1. **Borrowing Limit:** A library member can borrow a maximum of **5 books** at any time.
2. **Loan Duration:** The default duration is **21 days**, but can vary based on member or book type.
3. **Reservation Limit:** A library member can have **3 active reservations** at a time.
4. **Overdue Fines:** Calculated at **R9.90/day/item**.
5. **Reservation Priority:** Reservations are typically fulfilled on a **first-come, first-served** basis when a book becomes available.
6. **Account Suspension:** Triggered if overdue books exceed **30 days** or unpaid fines exceed **R200**.
7. **Digital Content Rules:** Different licensing terms apply (e.g., eBooks may not support reservation or loan extension).

---

## Relationships (Detailed)

- A `LibraryMember` borrows zero or more `Book`s through one or more `Loan` records.
- A `Book` can be borrowed by many `LibraryMember`s via `Loan`.
- A `LibraryMember` can place reservations on books via `Reservation`.
- A `Book` can be reserved by many members.
- A `LibraryMember` makes zero or more `Payment`s.
- A `LibraryMember` registers for `LibraryEvent`s through `Registration`.
- `LibraryEvent`s have many participants through `Registration`.

---

###   Alignment with Prior Assignments

 The Domain Model is designed to align with and build upon the work from previous assignments:

 * **Functional Requirements (Assignment 4):** Entities like `Book`, `LibraryMember`, `Loan`, and `Reservation` directly support functional requirements such as FR-003 (Implement Resource Borrowing), FR-004 (Implement Resource Returning), FR-005 (Implement Resource Reservation), and FR-006 (Implement Member Account Management). The attributes and methods defined here will be crucial for implementing these functionalities.
 * **Use Cases (Assignment 5):** The entities and their relationships map to various use cases, such as "Borrow a Book" (involving `LibraryMember`, `Book`, `Loan`), "Return a Book" (involving `LibraryMember`, `Book`, `Loan`), and "Reserve a Book" (involving `LibraryMember`, `Book`, `Reservation`).
 * **State and Activity Diagrams (Assignment 8):** The state transitions of entities like `Book` and `LibraryMember` are driven by the methods defined in this domain model (e.g., `checkOut()` triggers the `Available` to `Borrowed` state transition). Activity diagrams illustrate the workflows involving these entities and their methods.

---

