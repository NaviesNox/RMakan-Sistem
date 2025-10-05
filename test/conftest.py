import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from main import app

import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from fastapi.testclient import TestClient

client = TestClient(app)

@pytest_asyncio.fixture
async def auth_token():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/api/v1/auth/login",
            data={"username": "Nox", "password": "HaruYama"}
        )
        print("LOGIN RESPONSE:", response.status_code, response.json())  # debug
        data = response.json()
        return data.get("access_token")  # pakai .get biar ga KeyError


"""Unit Test untuk Register new user yg role nya customer """
def test_register_user():
    response = client.post(
        "/api/v1/auth/register",
        json={
            "name": "Test User",
            "username": "testuser",
            "password": "testpassword",
            "role": "customer",
            "email": "reg@gmail.com",
            "phone": "0812345678000500"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test User"
    assert data["username"] == "testuser"
    assert data["role"] == "customer"
    assert data["email"] == "reg@gmail.com"
    assert data["phone"] == "0812345678000500"
