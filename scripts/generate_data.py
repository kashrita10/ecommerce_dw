import pandas as pd
import random
from faker import Faker

fake = Faker("en_IN")
random.seed(42)

# -----------------------------
# CUSTOMERS (200)
# -----------------------------
cities = [
    "Delhi", "Mumbai", "Bangalore", "Chennai", "Hyderabad",
    "Pune", "Kolkata", "Ahmedabad", "Jaipur", "Lucknow"
]

customers = []

for i in range(1, 201):
    customers.append({
        "customer_id": i,
        "name": fake.name(),
        "email": f"user{i}@gmail.com",
        "city": random.choice(cities)
    })

customers_df = pd.DataFrame(customers)

# -----------------------------
# PRODUCTS (50)
# -----------------------------
products_list = [
    ("iPhone 15", "Electronics"),
    ("Samsung Galaxy", "Electronics"),
    ("Laptop", "Electronics"),
    ("Smart Watch", "Electronics"),
    ("Keyboard", "Electronics"),
    ("Mouse", "Electronics"),
    ("Headphones", "Electronics"),
    ("Power Bank", "Electronics"),
    ("Bluetooth Speaker", "Electronics"),
    ("Monitor", "Electronics"),
    ("T-Shirt", "Fashion"),
    ("Jeans", "Fashion"),
    ("Shoes", "Fashion"),
    ("Backpack", "Fashion"),
    ("Jacket", "Fashion"),
    ("Coffee Maker", "Home"),
    ("Mixer Grinder", "Home"),
    ("Water Bottle", "Home"),
    ("Study Table", "Home"),
    ("Chair", "Home"),
    ("Novel", "Books"),
    ("Python Book", "Books"),
    ("SQL Book", "Books"),
    ("Notebook", "Books"),
    ("Football", "Sports"),
    ("Cricket Bat", "Sports"),
    ("Yoga Mat", "Sports"),
    ("Dumbbells", "Sports"),
    ("Perfume", "Beauty"),
    ("Face Wash", "Beauty"),
    ("Lipstick", "Beauty"),
    ("Shampoo", "Beauty"),
    ("Conditioner", "Beauty"),
    ("Face Cream", "Beauty"),
    ("Gaming Mouse", "Electronics"),
    ("Gaming Keyboard", "Electronics"),
    ("Tablet", "Electronics"),
    ("Printer", "Electronics"),
    ("SSD", "Electronics"),
    ("Hard Disk", "Electronics"),
    ("Sneakers", "Fashion"),
    ("Sunglasses", "Fashion"),
    ("Cap", "Fashion"),
    ("Watch", "Fashion"),
    ("Cookware Set", "Home"),
    ("Bedsheet", "Home"),
    ("Pillow", "Home"),
    ("Wall Clock", "Home"),
    ("Tennis Racket", "Sports"),
    ("Hair Dryer", "Beauty")
]

products = []

for i, (name, category) in enumerate(products_list, start=1):
    products.append({
        "product_id": i,
        "product_name": name,
        "category": category,
        "price": random.randint(500, 80000)
    })

products_df = pd.DataFrame(products)

# -----------------------------
# ORDERS (500)
# -----------------------------
orders = []

for i in range(1, 501):
    orders.append({
        "order_id": 1000 + i,
        "customer_id": random.randint(1, 200),
        "order_date": fake.date_between(
            start_date="-12M",
            end_date="today"
        ),
        "total_amount": random.randint(1000, 100000)
    })

orders_df = pd.DataFrame(orders)

# -----------------------------
# ORDER ITEMS (1000)
# -----------------------------
order_items = []

for i in range(1, 1001):
    order_items.append({
        "order_item_id": i,
        "order_id": random.randint(1001, 1500),
        "product_id": random.randint(1, 50),
        "quantity": random.randint(1, 5)
    })

order_items_df = pd.DataFrame(order_items)

# -----------------------------
# SAVE CSV FILES
# -----------------------------

customers_df.to_csv(r"C:\Users\Kashrita Thapa\OneDrive\Desktop\ecommerce_dw\data\customers.csv", index=False)
products_df.to_csv(r"C:\Users\Kashrita Thapa\OneDrive\Desktop\ecommerce_dw\data\products.csv", index=False)
orders_df.to_csv(r"C:\Users\Kashrita Thapa\OneDrive\Desktop\ecommerce_dw\data\orders.csv", index=False)
order_items_df.to_csv(r"C:\Users\Kashrita Thapa\OneDrive\Desktop\ecommerce_dw\data\/order_items.csv", index=False)

print("✅ All CSV files generated successfully!")
print("Customers:", len(customers_df))
print("Products:", len(products_df))
print("Orders:", len(orders_df))
print("Order Items:", len(order_items_df))