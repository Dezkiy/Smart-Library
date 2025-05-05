import pytest
from fastapi.testclient import TestClient
from src.main import app  # Make sure your FastAPI app is defined in main.py

from datetime import date

client = TestClient(app)

# Sample test member data
sample_member = {
    "member_id": "MEM001",
    "first_name": "Alice",
    "last_name": "Johnson",
    "date_of_birth": "1990-05-15",
    "email": "alice@example.com",
    "phone_number": "1234567890",
    "address": "123 Library St",
    "membership_date": "2024-01-01",
    "membership_type": "Standard",
    "status": "Active"
}

def test_create_member():
    response = client.post("/api/members/", json=sample_member)
    assert response.status_code == 200
    data = response.json()
    assert data["member_id"] == sample_member["member_id"]
    assert data["first_name"] == sample_member["first_name"]

def test_get_member():
    response = client.get(f"/api/members/{sample_member['member_id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == sample_member["email"]

def test_list_members():
    response = client.get("/api/members/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(member["member_id"] == sample_member["member_id"] for member in data)

def test_delete_member():
    response = client.delete(f"/api/members/{sample_member['member_id']}")
    assert response.status_code == 200
    assert response.json()["message"] == f"Member {sample_member['member_id']} deleted"

def test_get_nonexistent_member():
    response = client.get("/api/members/UNKNOWN")
    assert response.status_code == 404
    assert response.json()["detail"] == "Member not found"
