from repositories.inmemory.inmemory_library_member_repository import InMemoryLibraryMemberRepository
from src.library_member import LibraryMember
from datetime import date

def test_inmemory_library_member_repository_crud():
    repo = InMemoryLibraryMemberRepository()
    
    member = LibraryMember(
        member_id="M001",
        first_name="John",
        last_name="Doe",
        date_of_birth=date(1990, 5, 17),
        email="john.doe@example.com",
        phone="123-456-7890",
        address="123 Street",
        registration_date=date.today(),
        member_type="Regular",
        account_status="Active"
    )
    
    repo.save(member)
    assert repo.find_by_id("M001") == member
    assert len(repo.find_all()) == 1
    assert len(repo.find_by_last_name("Doe")) == 1
    assert repo.find_by_email("john.doe@example.com") == member
    repo.delete("M001")
    assert repo.find_by_id("M001") is None
