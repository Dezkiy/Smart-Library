##   2.  Activity Workflow Modeling with Activity Diagrams (40 Marks)

 ###   2.1 User Registration

 ```mermaid
  graph TD
    Start --> User[User: Fill Registration Form]
    User --> System[System: Submit Form]
    System --> Validate[System: Validate Data]
    Validate --> Decision{Data Valid?}
    Decision -->|Yes| Create[System: Create Account]
    Decision -->|No| Error[User: Display Error Message]
    Create --> Confirm[System: Send Confirmation Email]
    Error --> Confirm
    Confirm --> End[End]
  ```

 **Explanation:**

 This diagram illustrates the user registration workflow. The user fills out a registration form, submits it, and the system validates the data. If the data is valid, the system creates an account and sends a confirmation email. If the data is invalid, an error message is displayed to the user. This workflow addresses stakeholder concerns by ensuring accurate user data and providing feedback to the user during the registration process.

 ###   2.2 Borrow Book

 ```mermaid
  graph TD
    Start --> User[User: Initiate Borrowing]
    User --> Scan[System: Scan Book]
    Scan --> Check[System: Check Availability]
    Check --> Availability{Available?}
    Availability -->|Yes| Record[System: Record Loan]
    Availability -->|No| NotAvailable[User: Display Not Available Message]
    Record --> Print[System: Print Due Date Slip]
    NotAvailable --> Print
    Print --> End[End]
  ```

 **Explanation:**

 This diagram illustrates the process of borrowing a book. The user initiates the borrowing process, the system checks the book's availability, and if available, records the loan and provides a due date slip. If the book is not available, a message is displayed to the user. This workflow addresses the librarian's need to efficiently manage book loans and provide accurate availability information to library members.

 ###   2.3 Return Book

 ```mermaid
  graph TD
    Start --> User[User: Initiate Return]
    User --> Scan[System: Scan Book]
    Scan --> UpdateStatus[System: Update Book Status]
    UpdateStatus --> UpdateAccount[System: Update Member Account]
    UpdateAccount --> End[End]
  ```

 **Explanation:**

 This diagram illustrates the process of returning a book. The user initiates the return, the system scans the book, updates the book's status to "Available," and updates the member's account. This workflow ensures that returned books are properly recorded and that member records are accurately maintained.

 ###   2.4 Reserve Book

 ```mermaid
  graph TD
    Start --> User[User: Request Reservation]
    User --> Check[System: Check Availability]
    Check --> Availability{Available?}
    Availability -->|Yes| Create[System: Create Reservation]
    Availability -->|No| NotAvailable[User: Display Not Available Message]
    Create --> Notify[System: Notify Member]
    NotAvailable --> Notify
    Notify --> End[End]
  ```

 **Explanation:**

 This diagram illustrates the book reservation process. The user requests a reservation, the system checks availability, and if available, creates a reservation and notifies the member when the book is available. If the book is not available, a message is displayed. This workflow supports the member's need to reserve books and the system's ability to manage reservations efficiently.

 ###   2.5 Search Resources

 ```mermaid
  graph TD
    Start --> User[User: Enter Search Criteria]
    User --> Execute[System: Execute Search]
    Execute --> Display[System: Display Results]
    Display --> Select[User: Select Resource]
    Select --> End[End]
  ```

 **Explanation:**

 This diagram illustrates the process of searching for resources. The user enters search criteria, the system executes the search, displays the results, and the user selects a resource. This workflow directly addresses the user's primary need to find library resources quickly and efficiently.

 ###   2.6 Manage Member Account

 ```mermaid
  graph TD
   Start --> Librarian[Librarian: Select Account Management]
   Librarian --> Action[System: Perform Action - Create/Update/Delete]
   Action --> Validate[System: Validate Data]
   Validate --> Decision{Data Valid?}
   Decision -->|Yes| Update[System: Update Account]
   Decision -->|No| Error[User: Display Error Message]
   Update --> End[End]
   Error --> End
  ```

 **Explanation:**

 This diagram illustrates the workflow for managing member accounts. The librarian selects the account management function, performs an action (create, update, delete), the system validates the data, and updates the account if the data is valid or displays an error message if invalid. This workflow ensures that member account information is accurately maintained and that librarians can effectively manage member accounts.

 ###   2.7 Process Payment

 ```mermaid
 graph TD
    Start --> User[User: Initiate Payment]
    User --> EnterDetails[System: Enter Payment Details]
    EnterDetails --> Validate[System: Validate Payment]
    Validate --> Decision{Payment Valid?}
    Decision -->|Yes| Record[System: Record Payment]
    Decision -->|No| PaymentFailed[User: Display Payment Failed Message]
    Record --> Receipt[System: Generate Receipt]
    PaymentFailed --> Receipt
    Receipt --> End[End]
  ```

 **Explanation:**

 This diagram illustrates the payment processing workflow. The user initiates the payment, enters payment details, the system validates the payment, records the payment if valid, or displays a failure message if invalid, and generates a receipt for successful payments. This workflow supports the user's need to make payments and the system's ability to process payments securely and accurately.

 ###   2.8 Generate Reports

 ```mermaid
  graph TD
    Start --> Librarian[Librarian: Select Report Type]
    Librarian --> Generate[System: Generate Report]
    Generate --> Display[System: Display Report]
    Display --> Export[Librarian: Export Report]
    Export --> End[End]
  ```

 **Explanation:**

 This diagram illustrates the workflow for generating reports. The librarian selects the report type, the system generates the report, displays it, and the librarian can export the report. This workflow addresses the librarian's need to analyze data and generate reports on library activities.
