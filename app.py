from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for products
products = []

# POST /products: Create a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()

    # Input validation
    if not data or not all(key in data for key in ('name', 'description', 'price')):
        return jsonify({"error": "Invalid input"}), 400

    # Add product to the list
    product = {
        "id": len(products) + 1,
        "name": data['name'],
        "description": data['description'],
        "price": float(data['price'])
    }
    products.append(product)
    return jsonify(product), 201

# GET /products: Retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

# Run the API server
if __name__ == '__main__':
    app.run(debug=True)
