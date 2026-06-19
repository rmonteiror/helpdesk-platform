from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_attachments_endpoint_requires_auth():
    response = client.get(
        "/attachments/tickets/1"
    )

    assert response.status_code in [
        401,
        403
    ]