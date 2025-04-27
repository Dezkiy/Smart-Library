from typing import Optional, List
from abc import ABC, abstractmethod
from repositories.repository import Repository
from src.library_member import LibraryMember  # Import the LibraryMember entity class

class LibraryMemberRepository(Repository[LibraryMember, str], ABC):  # ID type is str (member_id)
    """
    Repository interface for LibraryMember entities.
    """
    @abstractmethod
    def find_by_last_name(self, last_name: str) -> List[LibraryMember]:
        """
        Finds all members with the given last name.
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[LibraryMember]:
        """
        Finds a member by their email address.
        """
        raise NotImplementedError
