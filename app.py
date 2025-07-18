from flask import Flask, jsonify, request
from inventory_data import inventory
import external_api

app = Flask(__name__)

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in inventory if item["id"] == item_id), None)
    return jsonify(item or {"error": "Item not found"}), 200 if item else 404

@app.route('/inventory', methods=['POST'])
def add_item():
    data = request.get_json()
    data['id'] = max(i['id'] for i in inventory) + 1 if inventory else 1
    inventory.append(data)
    return jsonify(data), 201

@app.route('/inventory/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    item = next((item for item in inventory if item["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    data = request.get_json()
    item.update(data)
    return jsonify(item)

@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global inventory
    inventory = [item for item in inventory if item["id"] != item_id]
    return jsonify({"message": "Item deleted"}), 200

@app.route('/fetch/<string:query>', methods=['GET'])
def fetch_from_external(query):
    return jsonify(external_api.get_product_details(query))

if __name__ == '__main__':
    app.run(debug=True)
