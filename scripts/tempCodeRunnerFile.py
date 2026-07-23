import pandas as pd
from sqlalchemy import create_engine

# Extract data from CSV files

customers = pd.read_csv(r"C:\Users\Kashrita Thapa\OneDrive\Desktop\ecommerce_dw\data\customers.csv")

products = pd.read_csv(r"C:\Users\Kashrita Thapa\OneDrive\Desktop\ecommerce_dw\data\products.csv")

orders = pd.read_csv(r"C:\Users\Kashrita Thapa\OneDrive\Desktop\ecommerce_dw\data\orders.csv")

order_items = pd.read_csv(r"C:\Users\Kashrita Thapa\OneDrive\Desktop\ecommerce_dw\data\order_items.csv")


# -------------------------
# TRANSFORM DATA
# -------------------------

# Remove duplicate records
customers = customers.drop_duplicates()
products = products.drop_duplicates()
orders = orders.drop_duplicates()
order_items = order_items.drop_duplicates()


# Convert order_date to date format
orders["order_date"] = pd.to_datetime(orders["order_date"])


# Check missing values
print("Missing values in customers:")
print(customers.isnull().sum())


print("\nTransformation completed successfully!")
# Display the data

print("CUSTOMERS DATA")
print(customers)

print("\nPRODUCTS DATA")
print(products)

print("\nORDERS DATA")
print(orders)

print("\nORDER ITEMS DATA")
print(order_items)

# -------------------------
# CONNECT TO POSTGRESQL
# -------------------------

from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:9507@localhost:5432/ecommerce_dw"
)

print("Connected to PostgreSQL successfully!")

# Load data into PostgreSQL tables

customers.to_sql(
    "customers",
    engine,
    if_exists="append",
    index=False
)

print("Customers loaded successfully!")



products.to_sql(
    "products",
    engine,
    if_exists="append",
    index=False
)

print("Products loaded successfully!")


orders.to_sql(
    "orders",
    engine,
    if_exists="append",
    index=False
)

print("Orders loaded successfully!")


order_items.to_sql(
    "order_items",
    engine,
    if_exists="append",
    index=False
)

print("Order items loaded successfully!")