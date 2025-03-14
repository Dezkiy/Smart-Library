```mermaid
   %% Use Case Diagram for Smart Library System
   
   actor "Library Member" as Member
   actor "Librarian" as Librarian
   actor "IT Staff" as IT
   actor "Admin" as Admin
   actor "Digital Content Provider" as Provider
   actor "Library Staff" as Staff
   
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
   
   Member -- Search
   Member -- Borrow
   Member -- Return
   Member -- Reserve
   Member -- ManageAccounts
   Member -- Payments
   
   Librarian -- Catalog
   Librarian -- ManageContent
   Librarian -- ManageAccounts
   Librarian -- Reports
   Librarian -- Return
   Librarian -- Borrow
   Librarian -- Reserve
   Librarian -- Events
   
   IT -- ManageContent
   IT -- Reports
   
   Admin -- ManageAccounts
   Admin -- ManageContent
   Admin -- Reports
   Admin -- Catalog
   Admin -- Events
   
   Provider -- ManageContent
   
   Staff -- Search
   Staff -- Borrow
   Staff -- Return
   Staff -- Reserve
   Staff -- ManageAccounts
   Staff -- Payments
   Staff -- Events
   
   Search --> Borrow : includes
   Borrow --> Return : includes
   Reserve --> Search : extends
