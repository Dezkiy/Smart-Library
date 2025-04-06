##   3.  Integration with Prior Work

 ###   Traceability: Mapping Object State and Activity Workflow Diagrams to Prior Work

 ####   Functional Requirements (Assignment 4)

 | Diagram | Functional Requirement(s) |
 | :------ | :--------------------------- |
 | Book State Transition | FR-003: Implement Resource Borrowing, FR-004: Implement Resource Returning, FR-005: Implement Resource Reservation |
 | MemberAccount State Transition | FR-003: Implement Resource Borrowing, FR-009: Implement Online Payments |
 | Loan State Transition | FR-004: Implement Resource Returning |
 | Reservation State Transition | FR-005: Implement Resource Reservation |
 | Payment State Transition | FR-011: Implement Online Payments |
 | Event State Transition | FR-012: Implement Library Event Management |
 | LibraryResource State Transition | FR-001: Implement Resource Cataloging, FR-002: Implement Inventory Management, FR-006: Implement Search and Discovery |
 | User Registration Activity | FR-003: Implement Resource Borrowing, FR-009: Implement Online Payments |
 | Borrow Book Activity | FR-004: Implement Resource Returning |
 | Return Book Activity | FR-004: Implement Resource Returning |
 | Reserve Book Activity | FR-005: Implement Resource Reservation |
 | Search Resources Activity | FR-006: Implement Search and Discovery |
 | Manage Member Account Activity | FR-003: Implement Resource Borrowing, FR-009: Implement Online Payments |
 | Process Payment Activity | FR-011: Implement Online Payments |
 | Generate Reports Activity | FR-008: Implement Reporting and Analytics |

 ####   User Stories and Sprint Tasks (Assignment 6)

 | Diagram | User Story(ies) | Sprint Task(s) |
 | :----------------------------- | :--------------- | :------------- |
 | Book State Transition | US-003: As a Library Member, I want to borrow available resources, US-004: As a Library Member, I want to return borrowed resources, US-005: As a Library Member, I want to reserve unavailable resources | T-007: Develop checkout API endpoint, T-008: Implement checkout functionality, T-009: Develop return API endpoint, T-010: Implement return functionality |
 | MemberAccount State Transition | US-003: As a Library Member, I want to borrow available resources, US-009: As a Library Member, I want to manage my account online | T-011: Develop account management API, T-012: Implement account management |
 | Loan State Transition | US-004: As a Library Member, I want to return borrowed resources | T-009: Develop return API endpoint, T-010: Implement return functionality |
 | Reservation State Transition | US-005: As a Library Member, I want to reserve unavailable resources | None |
 | Payment State Transition | US-011: As a Library Member, I want to pay fines and fees online | None |
 | Event State Transition | US-012: As a Library Member, I want to view and register for library events | None |
 | LibraryResource State Transition | US-001: As a Library Member, I want to search for library resources, US-002: As a Librarian, I want to catalog library resources | T-001: Develop search API endpoint, T-002: Design UI for search results page, T-003: Implement search functionality, T-004: Develop cataloging API endpoint, T-006: Implement cataloging functionality |
 | User Registration Activity | US-003: As a Library Member, I want to borrow available resources, US-009: As a Library Member, I want to manage my account online | T-011: Develop account management API, T-012: Implement account management |
 | Borrow Book Activity | US-004: As a Library Member, I want to return borrowed resources | T-007: Develop checkout API endpoint, T-008: Implement checkout functionality |
 | Return Book Activity | US-004: As a Library Member, I want to return borrowed resources | T-009: Develop return API endpoint, T-010: Implement return functionality |
 | Reserve Book Activity | US-005: As a Library Member, I want to reserve unavailable resources | None |
 | Search Resources Activity | US-001: As a Library Member, I want to search for library resources | T-001: Develop search API endpoint, T-002: Design UI for search results page, T-003: Implement search functionality |
 | Manage Member Account Activity | US-003: As a Library Member, I want to borrow available resources, US-009: As a Library Member, I want to manage my account online | T-011: Develop account management API, T-012: Implement account management |
 | Process Payment Activity | US-011: As a Library Member, I want to pay fines and fees online | None |
 | Generate Reports Activity | US-008: As a Librarian, I want to generate reports on library usage and activity | None |
