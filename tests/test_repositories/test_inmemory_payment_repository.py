from repositories.inmemory.inmemory_payment_repository import InMemoryPaymentRepository
from src.payment import Payment
from src.library_member import LibraryMember
from datetime import date

def test_inmemory_payment_repository_crud():
    repo = InMemoryPaymentRepository()
    
    member = LibraryMember(
        member_id="M003",
        first_name="Alice",
        last_name="Wonder",
        date_of_birth=date(1995, 3, 5),
        email="alice@example.com",
        phone="987-654-3210",
        address="789 Road",
        registration_date=date.today(),
        member_type="Regular",
        account_status="Active"
    )

    payment = Payment(
        payment_id="P001",
        member=member,
        payment_date=date.today(),
        amount=50.0,
        payment_method="Credit Card",   # Added payment_method
        transaction_id="TX123456789",   # Added transaction_id
        payment_type="Completed"
    )
    
    repo.save(payment)
    assert repo.find_by_id("P001") == payment
    assert len(repo.find_all()) == 1
    assert len(repo.find_by_member(member)) == 1
    assert len(repo.find_by_status("Completed")) == 1
    repo.delete("P001")
    assert repo.find_by_id("P001") is None
