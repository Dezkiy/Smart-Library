```mermaid
 usecaseDiagram

actor LibraryMember
actor Librarian
actor ITStaff
actor Admin
actor DigitalContentProvider
actor LibraryStaff

usecase "Search Resources" as Search
usecase "Borrow Resources" as Borrow
usecase "Return Resources" as Return
usecase "Reserve Resources" as Reserve
usecase "Manage Member Accounts" as ManageAccounts
usecase "Catalog Resources" as Catalog
usecase "Manage Digital Content" as ManageContent
usecase "Generate Reports" as Reports
usecase "Process Payments" as Payments
usecase "Manage Events" as Events

LibraryMember --> Search
LibraryMember --> Borrow
LibraryMember --> Return
LibraryMember --> Reserve
LibraryMember --> ManageAccounts
LibraryMember --> Payments

Librarian --> Catalog
Librarian --> ManageContent
Librarian --> ManageAccounts
Librarian --> Reports
Librarian --> Return
Librarian --> Borrow
Librarian --> Reserve
Librarian --> Events

ITStaff --> ManageContent
ITStaff --> Reports

Admin --> ManageAccounts
Admin --> ManageContent
Admin --> Reports
Admin --> Catalog
Admin --> Events

DigitalContentProvider --> ManageContent

LibraryStaff --> Search
LibraryStaff --> Borrow
LibraryStaff --> Return
LibraryStaff --> Reserve
LibraryStaff --> ManageAccounts
LibraryStaff --> Payments
LibraryStaff --> Events

Search -->|<<includes>>| Borrow
Borrow -->|<<includes>>| Return
Reserve -->|<<extends>>| Search


Search -->|<<includes>>| Borrow
Borrow -->|<<includes>>| Return
Reserve -->|<<extends>>| Search

