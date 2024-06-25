import requests

def test_cheap_mock_connection():
    expected_result = {
                            "cpf": 154,
                            "name": "Otto Flowers",
                            "age": 22
                        }

    response = requests.get(f"http://localhost:8001/users/154")
    assert response.status_code == 200, "Can't estabilish connection to CheapAPI mock."
    assert response.json() == expected_result

def test_premium_mock_connection():
    expected_result = {
                            "cpf": 154,
                            "name": "Otto Flowers",
                            "age": 22
                        }

    response = requests.get(f"http://localhost:8002/users/154")
    assert response.status_code == 200, "Can't estabilish connection to PremiumAPI mock."
    assert response.json() == expected_result