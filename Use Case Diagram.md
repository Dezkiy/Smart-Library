```mermaid
   usecase "Use Case Diagram for Smart Library System"
   
   actor LibraryMember as Member
   actor Librarian as Librarian
   actor ITStaff as IT
   actor Admin as Admin
   actor DigitalContentProvider as Provider
   actor LibraryStaff as Staff
   
   usecase SearchResources as Search
   usecase BorrowResources as Borrow
   usecase ReturnResources as Return
   usecase ReserveResources as Reserve
   usecase ManageMemberAccounts as ManageAccounts
   usecase CatalogResources as Catalog
   usecase ManageDigitalContent as ManageContent
   usecase GenerateReports as Reports
   usecase ProcessPayments as Payments
   usecase ManageEvents as Events
   
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
