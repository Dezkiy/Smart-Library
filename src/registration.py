from datetime import date
from src.library_member import LibraryMember
from src.library_event import LibraryEvent

class Registration:
    def __init__(self, registration_id: str, member: LibraryMember,
                 event: LibraryEvent, registration_date: date):
        self._registration_id = registration_id
        self._member = member
        self._event = event
        self._registration_date = registration_date

    def get_member(self) -> LibraryMember:
        return self._member

    def get_event(self) -> LibraryEvent:
        return self._event

    def get_registration_date(self) -> date:
        return self._registration_date

    def __str__(self):
        return (f"Registration(registration_id='{self._registration_id}', "
                f"member='{self._member}', event='{self._event}')")