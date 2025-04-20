from typing import Optional
 from datetime import date

 class LibraryMember:
    def __init__(self, member_id: str, first_name: str, last_name: str,
                 date_of_birth: date, email: str, phone: str, address: str,
                 registration_date: date, member_type: str,
                 account_status: str):
        self._member_id = member_id
        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._email = email
        self._phone = phone
        self._address = address
        self._registration_date = registration_date
        self._member_type = member_type
        self._account_status = account_status

    def borrow_book(self, book):  # Book object as parameter
        # Implementation for borrowing a book (e.g., creating a Loan record)
        # This will likely interact with the Loan class
        pass

    def return_book(self, book):  # Book object as parameter
        # Implementation for returning a book (e.g., updating a Loan record)
        # This will likely interact with the Loan class
        pass

    def reserve_book(self, book):  # Book object as parameter
        # Implementation for reserving a book (e.g., creating a Reservation)
        # This will likely interact with the Reservation class
        pass

    def update_profile(self, new_email: Optional[str] = None,
                       new_phone: Optional[str] = None,
                       new_address: Optional[str] = None):
        if new_email:
            self._email = new_email
        if new_phone:
            self._phone = new_phone
        if new_address:
            self._address = new_address

    def pay_fine(self, amount: float):
        # Implementation for paying a fine (e.g., creating a Payment record)
        # This will likely interact with the Payment class
        pass

    # Getters and setters as needed
    def get_member_id(self) -> str:
        return self._member_id

    def __str__(self):
        return f"LibraryMember(member_id='{self._member_id}', name='{self._first_name} {self._last_name}')"
