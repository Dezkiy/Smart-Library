from typing import Optional, List
from repositories.payment_repository import PaymentRepository
from src.payment import Payment
from datetime import datetime


class InMemoryPaymentRepository(PaymentRepository):
    def __init__(self):
        self._storage = {}  # {payment_id: Payment}

    def save(self, payment: Payment) -> None:
        self._storage[payment._payment_id] = payment

    def find_by_id(self, id: str) -> Optional[Payment]:
        return self._storage.get(id)

    def find_all(self) -> List[Payment]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]

    def find_by_member(self, member) -> List[Payment]:
        return [payment for payment in self._storage.values() if payment.get_member() == member]

    def find_by_status(self, status: str) -> List[Payment]:
        # Assuming payment_type is used as status here; modify if needed
        return [payment for payment in self._storage.values() if payment._payment_type == status]

    def find_payments_in_date_range(self, start_date: str, end_date: str) -> List[Payment]:
        start = datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.strptime(end_date, "%Y-%m-%d").date()
        return [payment for payment in self._storage.values() if start <= payment._payment_date <= end]
