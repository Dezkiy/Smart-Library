from datetime import date
 from src.book import Book
 from src.library_member import LibraryMember
 from src.loan import Loan

 # Create some objects
 book1 = Book("The Hitchhiker's Guide to the Galaxy", "978-0345391802", 1979,
              ["Douglas Adams"], "Science Fiction", 1, "Pan Books", 10, 5, None)
 member1 = LibraryMember("LM001", "Alice", "Smith", date(1990, 5, 10),
                      "alice@example.com", "555-1234", "123 Main St",
                      date(2023, 1, 15), "Regular", "Active")
 loan1 = Loan("LN001", book1, member1, date(2024, 1, 20), date(2024, 2, 10))

 # Demonstrate relationships
 print(f"{member1} borrowed {loan1.get_book().get_title()}")
 print(f"{loan1.get_book()} is borrowed by {loan1.get_member()}")

 # Example of using methods
 if book1.check_out():
    print(f"{book1.get_title()} checked out successfully")
 else:
    print(f"{book1.get_title()} is not available")
