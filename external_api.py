import requests

def get_product_details(query):
    url = f"https://world.openfoodfacts.org/api/v0/product/{query}.json"
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "Failed to fetch product"}
    data = response.json()
    if data.get('status') == 0:
        return {"error": "Product not found"}
    product = data.get("product", {})
    return {
        "product_name": product.get("product_name", "N/A"),
        "brand": product.get("brands", "N/A"),
        "ingredients": product.get("ingredients_text", "N/A"),
        "barcode": product.get("code", "N/A")
    }
