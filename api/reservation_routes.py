from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import date
from typing import List
from src.reservation import Reservation
from repositories.services.reservation_service import ReservationService
from repositories.inmemory.inmemory_reservation_repository import InMemoryReservationRepository
from repositories.inmemory.inmemory_book_repository import InMemoryBookRepository
from repositories.inmemory.inmemory_library_member_repository import InMemoryLibraryMemberRepository

reservation_repository = InMemoryReservationRepository()
book_repository = InMemoryBookRepository()
member_repository = InMemoryLibraryMemberRepository()
reservation_service = ReservationService(reservation_repository, book_repository, member_repository)

router = APIRouter(prefix="/api/reservations", tags=["Reservations"])


class ReservationRequest(BaseModel):
    """Request model for creating a reservation."""
    reservation_id: str
    book_id: str
    member_id: str
    reservation_date: date


class ReservationResponse(ReservationRequest):
    """Response model for returning reservation data to the client."""
    pass


# 🔁 Domain-to-response conversion function
def reservation_to_response(res: Reservation) -> ReservationResponse:
    """Convert a Reservation domain model instance to a ReservationResponse Pydantic model."""
    return ReservationResponse(
        reservation_id=res._reservation_id,
        book_id=res._book_id,
        member_id=res._member_id,
        reservation_date=res._reservation_date
    )


@router.post("/", response_model=ReservationResponse)
def make_reservation(res_data: ReservationRequest) -> ReservationResponse:
    """Create a new reservation for a book."""
    reservation = Reservation(**res_data.dict())
    success = reservation_service.reserve_book(reservation)
    if not success:
        raise HTTPException(status_code=400, detail="Reservation failed")
    return reservation_to_response(reservation)


@router.get("/", response_model=List[ReservationResponse])
def get_all_reservations() -> List[ReservationResponse]:
    """Retrieve all reservations in the system."""
    reservations = reservation_service.get_all_reservations()
    return [reservation_to_response(r) for r in reservations]
