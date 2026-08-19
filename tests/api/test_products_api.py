import requests

BASE_URL = "https://automationexercise.com/api"

def test_get_all_products():
    response = requests.get(f"{BASE_URL}/productsList")

    assert response.status_code == 200
    data = response.json()
    assert "products" in data


def test_post_to_products_list_not_allowed():
    response = requests.post(f"{BASE_URL}/productsList")

    assert response.status_code == 200  
    data = response.json()
    assert data["message"] == "This request method is not supported."