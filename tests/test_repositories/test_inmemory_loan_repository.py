from repositories.inmemory.inmemory_loan_repository import InMemoryLoanRepository
from src.loan import Loan
from src.book import Book
from src.library_member import LibraryMember
from datetime import date

def test_inmemory_loan_repository_crud():
    repo = InMemoryLoanRepository()
    
    book = Book(
        title="Python Basics",
        isbn="PY123",
        publication_year=2022,
        authors=["Author One"],
        genre="Programming",
        edition=1,
        publisher="Tech Books",
        total_copies=5,
        available_copies=5
    )

    member = LibraryMember(
        member_id="M002",
        first_name="Jane",
        last_name="Smith",
        date_of_birth=date(1985, 8, 21),
        email="jane.smith@example.com",
        phone="321-654-0987",
        address="456 Avenue",
        registration_date=date.today(),
        member_type="Premium",
        account_status="Active"
    )

    loan = Loan(
        loan_id="L001",
        book=book,
        member=member,
        borrow_date=date.today(),  # Corrected to 'borrow_date'
        due_date=date.today()
    )
    
    repo.save(loan)
    assert repo.find_by_id("L001") == loan
    assert len(repo.find_by_member("M002")) == 1
    assert len(repo.find_by_book("PY123")) == 1
    repo.delete("L001")
    assert repo.find_by_id("L001") is None
