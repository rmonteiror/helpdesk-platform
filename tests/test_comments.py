from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_comments_endpoint_requires_auth():
    response = client.get(
        "/tickets/1/comments"
    )

    assert response.status_code in [
        401,
        403
    ]