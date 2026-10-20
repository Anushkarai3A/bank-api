from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_branches():
    response = client.get("/branches?limit=5")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 5


def test_search_branches():
    response = client.get("/branches/search?q=Mumbai&limit=5")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 5


def test_branch_not_found():
    response = client.get("/branches/INVALIDIFSC")

    assert response.status_code == 404


def test_branch_pagination_validation():
    response = client.get("/branches?limit=0")

    assert response.status_code == 422