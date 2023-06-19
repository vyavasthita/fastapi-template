from fastapi import status
import pytest
from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_create_user():
    payload = {
        "first_name": "dilip",
        "last_name": "sharma",
        "email": "temp@gmail.com",
        "password": "x8lkkls",
        "confirm_password": "x8lkkls",
    }

    response = client.post("/api/users/", json=payload)

    assert response.status_code == status.HTTP_201_CREATED

    assert response.json() == {
        "first_name": "dilip",
        "last_name": "sharma",
        "email": "temp@gmail.com",
    }
