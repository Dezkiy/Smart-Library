##   Object State Modeling with State Transition Diagrams

 ###   1.2.1 Book

 ```mermaid
  stateDiagram-v2
    state Available
    state Borrowed
    state Reserved
    state Lost
    state Damaged
    state Canceled

    Available --> Borrowed : Borrow Book
    Available --> Reserved : Reserve Book
    Available --> Damaged : Report Damage
    Available --> Lost : Report Lost

    Borrowed --> Available : Return Book
    Borrowed --> Lost : Report Lost
    Borrowed --> Damaged : Report Damage

    Reserved --> Available : Book Returned
    Reserved --> Borrowed : Borrow Book
    Reserved --> Canceled : Cancel Reservation

    Damaged --> Available : Repair Book

    Lost --> Available : Replace Book
  ```

 **Explanation:**

 * **States:** `Available`, `Borrowed`, `Reserved`, `Lost`, `Damaged`
 * **Transitions:**
     * `Available` to `Borrowed`: When a member borrows a book.
     * `Available` to `Reserved`: When a member reserves a book.
     * `Available` to `Damaged`/`Lost`: When a book is reported damaged or lost.
     * `Borrowed` to `Available`: When a member returns a book.
     * `Reserved` to `Available`: When a reserved book becomes available.
     * `Reserved` to `Borrowed`: When a reserved book is borrowed.
     * `Reserved` to `Canceled`: When a member cancels a reservation.
     * `Damaged` to `Available`: When a damaged book is repaired.
     * `Lost` to `Available`: When a lost book is replaced.
 * **Mapping to Functional Requirements:**
     * The `Borrowed` and `Return Book` transitions relate to functional requirements for borrowing and returning resources.
     * The `Reserved` state and related transitions support the functional requirement for reserving unavailable resources.

 ###   1.2.2 MemberAccount

 ```mermaid
  stateDiagram-v2
     state Active
     state Suspended
     state Closed

     Active --> Suspended : Report overdue
     Active --> Closed : Close Account

     Suspended --> Active : Pay Fines

     Closed --> Active : Reopen Account
  ```

 **Explanation:**

 * **States:**
     * `Active`: The member account is in good standing and can use library services.
     * `Suspended`: The member account has borrowing privileges temporarily revoked (e.g., due to overdue fines).
     * `Closed`: The member account is permanently terminated.
 * **Transitions:**
     * `Active` to `Suspended`: This transition occurs when the member has overdue resources or unpaid fines ("Report overdue").
     * `Active` to `Closed`: This happens when the member chooses to close their account ("Close Account").
     * `Suspended` to `Active`: The account returns to active status when the member pays all outstanding fines ("Pay Fines").
     * `Closed` to `Active`: In some systems, there might be a provision to reopen a closed account ("Reopen Account").
 * **Mapping to Functional Requirements:**
     * These states and transitions directly support functional requirements related to member account management, including creating, updating, suspending, and closing accounts, as well as handling fines and account reactivation.

 ###   1.2.3 Loan

 ```mermaid
  stateDiagram-v2
     state Current
     state Overdue
     state Returned

     Current --> Overdue : Due Date Passed
     Current --> Returned : Return Book

     Overdue --> Returned : Return Book
  ```

 **Explanation:**

 * **States:** `Current`, `Overdue`, `Returned`
 * **Transitions:**
     * `Current` to `Overdue`: When the book's due date has passed.
     * `Current` to `Returned`: When the book is returned before the due date.
     * `Overdue` to `Returned`: When the overdue book is returned.
 * **Mapping to Functional Requirements:**
     * These states and transitions directly relate to the borrowing and returning of books and the management of overdue items.

 ###   1.2.4 Reservation

 ```mermaid
  stateDiagram-v2
     state Pending
     state Active
     state Canceled
     state Completed

     Pending --> Active : Availability Confirmed
     Pending --> Canceled : Member Cancels
     Pending --> Canceled : Expired

     Active --> Completed : Book Borrowed
     Active --> Canceled : Member Cancels
  ```

 **Explanation:**

 * **States:** `Pending`, `Active`, `Canceled`, `Completed`
 * **Transitions:**
     * `Pending` to `Active`: When the reserved book becomes available.
     * `Pending` to `Canceled`: When the member cancels the reservation or it expires.
     * `Active` to `Completed`: When the member borrows the reserved book.
     * `Active` to `Canceled`: When the member cancels the active reservation
 * **Mapping to Functional Requirements:**
     * These states and transitions support the functional requirements for reserving books.

 ###   1.2.5 Payment

 ```mermaid
  stateDiagram-v2
     state Pending
     state Approved
     state Rejected
     state Refunded

     Pending --> Approved : Payment Received
     Pending --> Rejected : Payment Failed

     Approved --> Refunded : Refund Requested
  ```

 **Explanation:**

 * **States:** `Pending`, `Approved`, `Rejected`, `Refunded`
 * **Transitions:**
     * `Pending` to `Approved`: When the payment is successfully received.
     * `Pending` to `Rejected`: When the payment fails.
     * `Approved` to `Refunded`: When a refund is requested and processed.
 * **Mapping to Functional Requirements:**
     * These states and transitions support the online payment functional requirement.

 ###   1.2.6 Event

 ```mermaid
  stateDiagram-v2
     state Scheduled
     state Active
     state Completed
     state Canceled

     Scheduled --> Active : Start Event
     Scheduled --> Canceled : Cancel Event

     Active --> Completed : End Event
  ```

 **Explanation:**

 * **States:** `Scheduled`, `Active`, `Completed`, `Canceled`
 * **Transitions:**
     * `Scheduled` to `Active`: When the event starts.
     * `Scheduled` to `Canceled`: When the event is canceled.
     * `Active` to `Completed`: When the event ends.
 * **Mapping to Functional Requirements:**
     * These states and transitions support the event management functional requirement.

 ###   1.2.7 LibraryResource

 ```mermaid
  stateDiagram-v2
     state Available
     state Unavailable

     Available --> Unavailable : Resource Unavailable
     Unavailable --> Available : Resource Available
  ```

 **Explanation:**

 * **States:** `Available`, `Unavailable`
 * **Transitions:**
     * `Available` to `Unavailable`: When the resource is borrowed, under maintenance, or otherwise not accessible.
     * `Unavailable` to `Available`: When the resource becomes available again.
 * **Mapping to Functional Requirements:**
     * These states and transitions support the general management of library resources and their availability.
