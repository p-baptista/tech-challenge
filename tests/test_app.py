from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_read_by_csv():

    expected_result = {
                            "cpf": 154,
                            "name": "Otto Flowers",
                            "age": 22
                        }

    response = client.get("api/v1/user/154")
    assert response.status_code == 200
    assert response.json() == expected_result

def test_non_existing_user():
    response = client.get("api/v1/user/000")
    assert response.status_code == 404

def test_invalid_query():
    response = client.get("api/v1/user/abc")
    assert response.status_code == 422
