from datetime import date
from src.library_member import LibraryMember

class Payment:
    def __init__(self, payment_id: str, member: LibraryMember, payment_date: date,
                 amount: float, payment_method: str, transaction_id: str,
                 payment_type: str):
        self._payment_id = payment_id
        self._member = member
        self._payment_date = payment_date
        self._amount = amount
        self._payment_method = payment_method
        self._transaction_id = transaction_id
        self._payment_type = payment_type

    def process_payment(self):
        # Implementation for processing the payment (e.g., interacting with a payment gateway)
        pass

    def record_payment(self):
        # Implementation for recording the payment details in the system
        pass

    def get_member(self) -> LibraryMember:
        return self._member

    def __str__(self):
        return (f"Payment(payment_id='{self._payment_id}', "
                f"member='{self._member}', amount={self._amount})")