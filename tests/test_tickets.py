from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_tickets_without_token():
    response = client.get(
        "/tickets/"
    )

    assert response.status_code == 401


def test_get_invalid_ticket_without_token():
    response = client.get(
        "/tickets/999"
    )

    assert response.status_code == 401


def test_create_ticket_without_token():
    response = client.post(
        "/tickets/",
        json={
            "title": "System error",
            "description": "Cannot access portal",
            "priority": "high"
        }
    )

    assert response.status_code == 401