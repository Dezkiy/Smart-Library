from creational_patterns.prototype import DefaultMember
from datetime import date


def test_default_member_prototype_creation():
    prototype = DefaultMember(
        first_name="Test",
        last_name="Member",
        email="test@example.com",
        address="Test Address",
        member_type="Regular",
    )
    assert isinstance(prototype, DefaultMember)


def test_default_member_prototype_clone():
    prototype = DefaultMember(
        first_name="Test",
        last_name="Member",
        email="test@example.com",
        address="Test Address",
        member_type="Regular",
    )
    clone = prototype.clone()
    assert isinstance(clone, DefaultMember)
    assert clone._first_name == "Test"
    assert clone._last_name == "Member"


def test_default_member_prototype_create_member():
    prototype = DefaultMember(
        first_name="Test",
        last_name="Member",
        email="test@example.com",
        address="Test Address",
        member_type="Regular",
    )
    member = prototype.create_member(
        member_id="TM001",
        date_of_birth=date(1990, 1, 1),
        phone="123-456-7890",
        registration_date=date(2024, 1, 1),
        account_status="Active",
    )
    assert member.get_member_id() == "TM001"
    assert member._first_name == "Test"
    assert member._last_name == "Member"