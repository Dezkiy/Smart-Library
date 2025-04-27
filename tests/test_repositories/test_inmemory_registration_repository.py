from repositories.inmemory.inmemory_registration_repository import InMemoryRegistrationRepository
from src.registration import Registration
from src.library_event import LibraryEvent
from src.library_member import LibraryMember
from datetime import date

def test_inmemory_registration_repository_crud():
    repo = InMemoryRegistrationRepository()
    
    event = LibraryEvent(
        event_id="EV002",
        title="Coding Workshop",
        description="Learn Python",
        event_date=date(2024, 10, 15)
    )
    member = LibraryMember(
        member_id="M004",
        first_name="Bob",
        last_name="Builder",
        date_of_birth=date(1980, 12, 1),
        email="bob@example.com",
        phone="654-321-0987",
        address="321 Lane",
        registration_date=date.today(),
        member_type="Regular",
        account_status="Active"
    )
    
    registration = Registration(
        registration_id="R001",
        event=event,
        member=member,
        registration_date=date.today()
    )
    
    repo.save(registration)
    assert repo.find_by_id("R001") == registration
    assert len(repo.find_by_event(event)) == 1
    assert len(repo.find_by_member(member)) == 1
    repo.delete("R001")
    assert repo.find_by_id("R001") is None
