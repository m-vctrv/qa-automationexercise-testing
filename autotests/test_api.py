import requests

def test_products_list_status():
    url = "https://automationexercise.com/api/productsList"
    response = requests.get(url)
    data = response.json()
    assert data["responseCode"] == 200

def test_products_list_not_empty():
    url = "https://automationexercise.com/api/productsList"
    response = requests.get(url)
    data = response.json()
    assert "products" in data
    assert len(data["products"]) > 0


def test_search_product():
    url = "https://automationexercise.com/api/searchProduct"
    response = requests.post(url, data={"search_product": "dress"})
    data = response.json()
    assert data["responseCode"] == 200
    assert "products" in data
    assert len(data["products"]) > 0

def test_search_product_no_data():
    url = "https://automationexercise.com/api/searchProduct"
    response = requests.post(url, data={})
    data = response.json()
    assert data["responseCode"] == 400
    assert "products" not in data
    assert "is missing" in data["message"]

def test_verify_login():
    url = "https://automationexercise.com/api/verifyLogin"
    response = requests.post(url, data= {"email": "milka@mail.ru", "password": "12345"})
    data = response.json()
    assert data["responseCode"] == 200
    assert data["message"] == "User exists!"

def test_verify_login_wrong_password():
    url = "https://automationexercise.com/api/verifyLogin"
    response = requests.post(url, data= {"email": "milka@mail.ru", "password": "123dgwr23"})
    data = response.json()
    assert data["responseCode"] == 404

def test_verify_login_no_params():
    url = "https://automationexercise.com/api/verifyLogin"
    response = requests.post(url, data= {})
    data = response.json()
    assert data["responseCode"] == 400
    