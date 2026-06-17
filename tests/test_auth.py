from fastapi.testclient import TestClient

from app.main import app
from app.core.security import (
    hash_password,
    verify_password
)

client = TestClient(app)


def test_password_hash():
    password = "123456"

    hashed = hash_password(password)

    assert hashed != password
    assert len(hashed) > 20


def test_password_verification():
    password = "123456"

    hashed = hash_password(password)

    assert verify_password(
        password,
        hashed
    ) is True


def test_root():
    response = client.get("/")

    assert response.status_code == 200


def test_login_invalid_credentials():
    response = client.post(
        "/auth/login",
        json={
            "email": "fake@email.com",
            "password": "wrongpassword"
        }
    )

    assert response.status_code == 401