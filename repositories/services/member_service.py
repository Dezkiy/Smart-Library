# services/member_service.py

from repositories.library_member_repository import LibraryMemberRepository
from src.library_member import LibraryMember

class MemberService:
    def __init__(self, repo: LibraryMemberRepository):
        self._repo = repo

    def register_member(self, member: LibraryMember):
        if self._repo.find_by_id(member.get_member_id()):
            raise ValueError("Member already exists")
        self._repo.save(member)
        return member
