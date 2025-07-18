import pytest
from app import app

def test_get_inventory():
    with app.test_client() as client:
        response = client.get('/inventory')
        assert response.status_code == 200

def test_add_and_get_item():
    with app.test_client() as client:
        new_item = {"name": "Test", "brand": "TestBrand", "barcode": "000000", "stock": 1, "price": 1.0}
        post = client.post('/inventory', json=new_item)
        assert post.status_code == 201

        new_id = post.get_json()["id"]
        get = client.get(f'/inventory/{new_id}')
        assert get.status_code == 200

def test_external_fetch_mock(monkeypatch):
    def mock_get_product_details(query):
        return {"product_name": "Mock", "brand": "MockBrand"}
    from external_api import get_product_details
    monkeypatch.setattr("external_api.get_product_details", mock_get_product_details)

    with app.test_client() as client:
        res = client.get("/fetch/123")
        assert res.status_code == 200
