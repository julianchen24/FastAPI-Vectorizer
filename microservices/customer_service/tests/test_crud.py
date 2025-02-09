# test_crud.py

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from ..main import app
from ..models import Customer
from ..database import get_session, SessionDep



client = TestClient(app)

# pip install pytest
# pip install httpx

def test_create_customer():
    response = client.post(
        "/customers/",
        json={
            "customer_id": 1,
            "name": "John Doe",
            "phone": "123-456-7890",
            "address": "123 Main Street",
            "email": "john@example.com"

        }
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {
        "customer_id": 1,
        "name": "John Doe",
        "phone": "123-456-7890",
        "address": "123 Main Street",
        "email": "john@example.com"
        }

    
def test_read_customers():
    response = client.get("/customers/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    
def test_read_customer():
    response = client.get("/customers/1")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.headers["content-type"] == "application/json"


def test_update_customer():
    response = client.patch("/customers/1", json = {"name":"John Updated"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Updated"
    assert response.headers["content-type"] == "application/json"


def test_delete_customer():
    response = client.delete("/customers/1")
    assert response.status_code == 200
    assert response.json() == {"ok": True}
    assert response.headers["content-type"] == "application/json"

    response = client.get("/customers/1")
    assert response.status_code == 404