from typing import Optional, List
from repositories.library_member_repository import LibraryMemberRepository
from src.library_member import LibraryMember


class InMemoryLibraryMemberRepository(LibraryMemberRepository):
    def __init__(self):
        self._storage = {}  # {member_id: LibraryMember}

    def save(self, member: LibraryMember) -> None:
        self._storage[member.get_member_id()] = member

    def find_by_id(self, id: str) -> Optional[LibraryMember]:
        return self._storage.get(id)

    def find_all(self) -> List[LibraryMember]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]

    def find_by_last_name(self, last_name: str) -> List[LibraryMember]:
        return [member for member in self._storage.values() if member._last_name == last_name]

    def find_by_email(self, email: str) -> Optional[LibraryMember]:
        for member in self._storage.values():
            if member._email == email:
                return member
        return None
