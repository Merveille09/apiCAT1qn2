import requests

BASE_URL = "http://127.0.0.1:5000"

def add_product(name, description, price):
    payload = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(f"{BASE_URL}/products", json=payload)
    if response.status_code == 201:
        print("Product added successfully:", response.json())
    else:
        print("Failed to add product:", response.json())

def get_all_products():
    response = requests.get(f"{BASE_URL}/products")
    if response.status_code == 200:
        print("All products:", response.json())
    else:
        print("Failed to retrieve products:", response.json())

# Example interaction
if __name__ == "__main__":
    add_product("Laptop", "A high-performance laptop", 1500.00)
    add_product("Mouse", "A wireless mouse", 25.99)
    add_product("Keyboard", "A mechanical keyboard", 100.00)
    add_product("Monitor", "A 4K monitor", 500.00)
    add_product("Headphones", "Noise-cancelling headphones", 200.00)
    add_product("Desk", "A standing desk", 350.00)
    add_product("Chair", "An ergonomic chair", 200.00)
    add_product("Lamp", "A smart lamp", 50.00)
    add_product("Plant", "An indoor plant", 20.00)
    add_product("Notebook", "A notebook for writing", 10.00)
    add_product("Pen", "A ballpoint pen", 2.00)
    get_all_products()
