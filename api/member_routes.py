from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import date
from typing import List
from src.library_member import LibraryMember
from repositories.services.member_service import MemberService
from repositories.inmemory.inmemory_library_member_repository import InMemoryLibraryMemberRepository

member_repository = InMemoryLibraryMemberRepository()
member_service = MemberService(member_repository)

router = APIRouter(prefix="/api/members", tags=["Members"])

class MemberRequest(BaseModel):
    member_id: str
    first_name: str
    last_name: str
    date_of_birth: date
    email: str
    phone_number: str
    address: str
    membership_date: date
    membership_type: str
    status: str

class MemberResponse(MemberRequest):
    pass

# 🔁 Helper function to convert domain model to Pydantic response
def member_to_response(member: LibraryMember) -> MemberResponse:
    return MemberResponse(
        member_id=member._member_id,
        first_name=member._first_name,
        last_name=member._last_name,
        date_of_birth=member._date_of_birth,
        email=member._email,
        phone_number=member._phone_number,
        address=member._address,
        membership_date=member._membership_date,
        membership_type=member._membership_type,
        status=member._status
    )

@router.post("/", response_model=MemberResponse)
def create_member(member: MemberRequest):
    member_obj = LibraryMember(**member.dict())
    member_service.register_member(member_obj)
    return member_to_response(member_obj)

@router.get("/", response_model=List[MemberResponse])
def list_members():
    members = member_service.get_all_members()
    return [member_to_response(m) for m in members]

@router.get("/{member_id}", response_model=MemberResponse)
def get_member(member_id: str):
    member = member_service.get_member(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member_to_response(member)

@router.delete("/{member_id}")
def delete_member(member_id: str):
    if member_service.remove_member(member_id):
        return {"message": f"Member {member_id} deleted"}
    raise HTTPException(status_code=404, detail="Member not found")
