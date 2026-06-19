from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_comments_without_token():
    response = client.get(
        "/tickets/1/comments"
    )

    assert response.status_code == 403