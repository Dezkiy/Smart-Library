from abc import ABC, abstractmethod
from src.library_member import LibraryMember
from datetime import date


class MemberPrototype(ABC):
    """
    Abstract base class for defining cloneable library member prototypes.
    """
    @abstractmethod
    def clone(self) -> 'MemberPrototype':
        pass


class DefaultMember(MemberPrototype):
    """
    Concrete prototype with default attributes to clone and customize members.
    """

    def __init__(self, first_name: str, last_name: str, email: str, address: str, member_type: str):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._address = address
        self._member_type = member_type

    def clone(self) -> 'DefaultMember':
        """
        Returns a shallow copy of the prototype.
        """
        return DefaultMember(
            first_name=self._first_name,
            last_name=self._last_name,
            email=self._email,
            address=self._address,
            member_type=self._member_type
        )

    def create_member(
        self,
        member_id: str,
        date_of_birth: date,
        phone: str,
        registration_date: date,
        account_status: str
    ) -> LibraryMember:
        """
        Creates a new LibraryMember from the prototype with customized details.
        """
        return LibraryMember(
            member_id=member_id,
            first_name=self._first_name,
            last_name=self._last_name,
            date_of_birth=date_of_birth,
            email=self._email,
            phone=phone,
            address=self._address,
            registration_date=registration_date,
            member_type=self._member_type,
            account_status=account_status
        )

# === Example Usage ===
if __name__ == "__main__":
    default_member_prototype = DefaultMember(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        address="123 Main St",
        member_type="Regular"
    )

    new_member1 = default_member_prototype.create_member(
        member_id="LM002",
        date_of_birth=date(1985, 8, 20),
        phone="555-9876",
        registration_date=date(2024, 2, 1),
        account_status="Active"
    )

    new_member2 = default_member_prototype.create_member(
        member_id="LM003",
        date_of_birth=date(1992, 3, 15),
        phone="555-1122",
        registration_date=date(2024, 2, 1),
        account_status="Active"
    )

    print(new_member1)
    print(new_member2)

