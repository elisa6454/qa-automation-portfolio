import requests

BASE_URL = "https://automationexercise.com/api"

def test_search_product_success():
    response = requests.post(f"{BASE_URL}/searchProduct", data={"search_product": "top"})

    assert response.status_code == 200
    data = response.json()
    assert "products" in data
    assert len(data["products"]) > 0


def test_search_product_missing_parameter():
    response = requests.post(f"{BASE_URL}/searchProduct")

    assert response.status_code == 200  
    data = response.json()
    assert data["message"] == "Bad request, search_product parameter is missing in POST request."