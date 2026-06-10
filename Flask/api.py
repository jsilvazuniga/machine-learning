# PUT and DELETE hhtp verbs
# working with API's JSON data

from flask import Flask, request, render_template, redirect, url_for, jsonify

app = Flask(__name__)

# initialize a list to store data
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
    {"id": 3, "name": "Item 3", "description": "This is item 3"}
]

@app.route('/')
def home():
    return "Welcome to the Flask API, this is the sample to do list operations!"

# get retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# get retrieve a single item by id
@app.route('/items/<int:item_id>', methods=['GET']) 
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

# POST create a new item
@app.route('/items', methods=['POST'])
def create_item():
    if not request.is_json or not 'name' in request.get_json():
        return jsonify({"error": "name is required"}), 400
    
    new_item = {
        "id": items[-1]['id'] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json.get('description', '')
    }

    items.append(new_item)
    return jsonify(new_item), 201

# PUT update an existing item by id
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    
    return jsonify(item)

# DELETE delete an existing item by id
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    items = [i for i in items if i['id'] != item_id]
    return jsonify({"message": "Item deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)