from repositories.inmemory.inmemory_reservation_repository import InMemoryReservationRepository
from src.reservation import Reservation
from src.book import Book
from src.library_member import LibraryMember
from datetime import date

def test_inmemory_reservation_repository_crud():
    repo = InMemoryReservationRepository()
    
    book = Book(
        title="Clean Code",
        isbn="CC001",
        publication_year=2008,
        authors=["Robert C. Martin"],
        genre="Programming",
        edition=1,
        publisher="Prentice Hall",
        total_copies=3,
        available_copies=3
    )
    member = LibraryMember(
        member_id="M005",
        first_name="Eve",
        last_name="Adams",
        date_of_birth=date(1992, 7, 11),
        email="eve@example.com",
        phone="777-888-9999",
        address="987 Garden",
        registration_date=date.today(),
        member_type="Premium",
        account_status="Active"
    )
    
    reservation = Reservation(
        reservation_id="RS001",
        book=book,
        member=member,
        reservation_date=date.today(),
        notification_date=date.today()  # Provide notification_date as required
    )
    
    repo.save(reservation)
    assert repo.find_by_id("RS001") == reservation
    assert len(repo.find_by_book(book)) == 1
    assert len(repo.find_by_member(member)) == 1
    repo.delete("RS001")
    assert repo.find_by_id("RS001") is None
