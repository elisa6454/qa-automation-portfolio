import requests

BASE_URL = "https://automationexercise.com/api"

def test_verify_login_success():
    response = requests.post(f"{BASE_URL}/verifyLogin", data={
        "email": "qatest1234@example.com",
        "password": "1234"
    })

    assert response.status_code == 200
    data = response.json()
    
    assert data["message"] == "User exists!"


def test_verify_login_missing_email():
    response = requests.post(f"{BASE_URL}/verifyLogin", data={
        "password": "1234"
    })

    assert response.status_code == 200
    data = response.json()
    
    assert data["message"] == "Bad request, email or password parameter is missing in POST request."


def test_verify_login_invalid_details():
    response = requests.post(f"{BASE_URL}/verifyLogin", data={
        "email": "notexist@example.com",
        "password": "wrongpassword"
    })

    assert response.status_code == 200
    data = response.json()
    
    assert data["message"] == "User not found!"