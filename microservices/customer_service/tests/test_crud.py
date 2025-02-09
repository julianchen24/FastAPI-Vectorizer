# test_crud.py

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from ..main import app
from ..models import Customer
from ..database import get_session, SessionDep
from httpx import ASGITransport, AsyncClient

client = TestClient(app)

# pip install pytest
# pip install httpx

@pytest.mark.anyio
async def test_create_customer():
    async with AsyncClient (
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.post(
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


@pytest.mark.anyio
async def test_read_customers():
    async with AsyncClient (
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/customers/")
    
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"


@pytest.mark.anyio
async def test_read_customer():
    async with AsyncClient (
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/customers/1")
    
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.headers["content-type"] == "application/json"


@pytest.mark.anyio
async def test_update_customer():
    async with AsyncClient (
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.patch(
            "/customers/1", 
            json={
                "name":"John Updated"
            }
        )
        assert response.status_code == 200
        assert response.json()["name"] == "John Updated"
        assert response.headers["content-type"] == "application/json"


@pytest.mark.anyio
async def test_delete_customer():
    async with AsyncClient (
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.delete("/customers/1")
        assert response.status_code == 200
        assert response.json() == {"ok": True}
        assert response.headers["content-type"] == "application/json"

        response = await ac.get("/customers/1")
        assert response.status_code == 404