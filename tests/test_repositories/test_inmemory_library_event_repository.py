from repositories.inmemory.inmemory_library_event_repository import InMemoryEventRepository
from src.library_event import LibraryEvent

from datetime import datetime, date, time


def test_inmemory_event_repository_crud():
    repo = InMemoryEventRepository()
    


    event = LibraryEvent(
        event_id="EV002",
        title="Coding Workshop",
    description="Learn Python",
        event_date=date(2024, 10, 15),  # event date
        start_time=datetime(2024, 10, 15, 9, 0).time(),  # start time as time object
        end_time=datetime(2024, 10, 15, 17, 0).time(),   # end time as time object
        location="Main Hall",  # event location
        capacity=50,           # capacity
        registration_deadline=datetime(2024, 10, 10, 23, 59).date()  # registration deadline as date object
    )
    
    repo.save(event)
    assert repo.find_by_id("EV002") == event  # Assert that the saved event matches the created one
    assert len(repo.find_all()) == 1
    assert len(repo.find_by_title("Coding Workshop")) == 1
    repo.delete("EV002")
    assert repo.find_by_id("EV002") is None
