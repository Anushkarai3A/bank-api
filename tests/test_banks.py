from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Bank API is running!"
    }


def test_list_banks():
    response = client.get("/banks?limit=5")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 5


def test_get_bank_not_found():
    response = client.get("/banks/999999999")

    assert response.status_code == 404


def test_bank_pagination_validation():
    response = client.get("/banks?limit=0")

    assert response.status_code == 422