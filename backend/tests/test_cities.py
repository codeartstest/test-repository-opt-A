from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_all_cities():
    response = client.get("/api/cities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 6


def test_get_city_by_id():
    response = client.get("/api/cities/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Istanbul"


def test_get_city_not_found():
    response = client.get("/api/cities/999")
    assert response.status_code == 404


def test_city_schema():
    response = client.get("/api/cities/2")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "region" in data
    assert "description" in data
    assert "highlights" in data
    assert "icon" in data
    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["region"], str)
    assert isinstance(data["description"], str)
    assert isinstance(data["highlights"], list)
    assert isinstance(data["icon"], str)