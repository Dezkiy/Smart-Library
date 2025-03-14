# Test Case Development
   
   Here are eight test cases to validate functional requirements from Assignment 4, along with two non-functional test scenarios:
   
   **Test Case Table**
   
   | Test Case ID | Requirement ID | Description | Steps | Expected Result | Actual Result | Status (Pass/Fail) |
   | :---------- | :------------- | :---------- | :---- | :-------------- | :------------ | :--------------- |
   | TC-001 | FR-001 | Librarian catalogs a new book | 1. Librarian logs in. 2. Librarian navigates to the cataloging section. 3. Librarian enters book details (title, author, ISBN). 4. Librarian saves the record. | The book is successfully cataloged with all entered details. |  |  |
   | TC-002 | FR-002 | Member searches for a book by title | 1. Member accesses the library system. 2. Member enters a book title in the search field. 3. Member initiates the search. | A list of books matching the title is displayed, including availability. |  |  |
   | TC-003 | FR-003 | Member borrows an available book | 1. Member logs in. 2. Member locates an available book. 3. Member initiates the borrowing process. 4. System confirms the checkout. | The book is successfully checked out to the member, and the due date is displayed. |  |  |
   | TC-004 | FR-004 | Member returns a borrowed book | 1. Librarian/Library Staff scans the book. 2. Librarian/Library Staff confirms the return. | The book's status is updated to "Available," and the member's record is updated. |  |  |
   | TC-005 | FR-005 | Member reserves a book | 1. Member logs in. 2. Member searches for a book and finds it unavailable. 3. Member initiates a reservation. | The book is successfully reserved for the member, and a confirmation message is displayed. |  |  |
   | TC-006 | FR-006 | Member registers for a new account | 1. Member navigates to the registration page. 2. Member enters all required details (name, email, etc.). 3. Member submits the registration form. | The member's account is created successfully, and the member is logged in. |  |  |
   | TC-007 | FR-007 | System sends overdue item notification | 1. A book becomes overdue. 2. System is scheduled to send overdue notifications. | The system sends an overdue notification to the member. |  |  |
   | TC-008 | FR-008 | Librarian generates a resource usage report | 1. Librarian logs in. 2. Librarian navigates to the reports section. 3. Librarian selects "Resource Usage Report" and specifies the date range. 4. Librarian generates the report. | The system generates a report showing resource usage for the specified period. |  |  |
   
   **Non-Functional Test Scenarios**
   
   1.  **Performance Test:**
       * **Description:** Verify system response time under concurrent user load.
       * **Steps:** Simulate 1,000 concurrent users searching for books. Measure the time it takes for search results to be displayed.
       * **Expected Result:** The system displays search results in ≤ 2 seconds.
   2.  **Security Test:**
       * **Description:** Validate user data encryption.
       * **Steps:** 1. Attempt to access user data in the database without proper authorization. 2. Verify that user data is encrypted.
       * **Expected Result:** User data is encrypted and cannot be accessed without proper authorization.
