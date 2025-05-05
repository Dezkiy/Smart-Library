import pytest
from fastapi.testclient import TestClient
from src.main import app  # Make sure your FastAPI app is defined in main.py

client = TestClient(app)

# Sample test reservation data
sample_reservation = {
    "reservation_id": "R001",
    "book_id": "B001",  # Assuming a book with this ID exists
    "member_id": "M001",  # Assuming a member with this ID exists
    "reservation_date": "2024-01-01"
}

def test_create_reservation():
    response = client.post("/api/reservations/", json=sample_reservation)
    assert response.status_code == 200
    data = response.json()
    assert data["reservation_id"] == sample_reservation["reservation_id"]
    assert data["book_id"] == sample_reservation["book_id"]
    assert data["member_id"] == sample_reservation["member_id"]

def test_get_reservation():
    response = client.get(f"/api/reservations/{sample_reservation['reservation_id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["reservation_id"] == sample_reservation["reservation_id"]
    assert data["book_id"] == sample_reservation["book_id"]

def test_list_reservations():
    response = client.get("/api/reservations/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(reservation["reservation_id"] == sample_reservation["reservation_id"] for reservation in data)

def test_delete_reservation():
    response = client.delete(f"/api/reservations/{sample_reservation['reservation_id']}")
    assert response.status_code == 200
    assert response.json()["message"] == f"Reservation {sample_reservation['reservation_id']} deleted"

def test_get_nonexistent_reservation():
    response = client.get("/api/reservations/UNKNOWN")
    assert response.status_code == 404
    assert response.json()["detail"] == "Reservation not found"
