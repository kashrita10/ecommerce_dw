import os
import pandas as pd
from sqlalchemy import create_engine

# -------------------------
# DEFINE PROJECT PATHS
# -------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# -------------------------
# EXTRACT DATA FROM CSV FILES
# -------------------------

customers = pd.read_csv(os.path.join(DATA_DIR, "customers.csv"))
products = pd.read_csv(os.path.join(DATA_DIR, "products.csv"))
orders = pd.read_csv(os.path.join(DATA_DIR, "orders.csv"))
order_items = pd.read_csv(os.path.join(DATA_DIR, "order_items.csv"))

# -------------------------
# TRANSFORM DATA
# -------------------------

# Remove unwanted empty columns (Unnamed columns)
customers = customers.loc[:, ~customers.columns.str.contains("^Unnamed")]
products = products.loc[:, ~products.columns.str.contains("^Unnamed")]
orders = orders.loc[:, ~orders.columns.str.contains("^Unnamed")]
order_items = order_items.loc[:, ~order_items.columns.str.contains("^Unnamed")]

# Remove duplicate records
customers = customers.drop_duplicates()
products = products.drop_duplicates()
orders = orders.drop_duplicates()
order_items = order_items.drop_duplicates()

# Convert order_date to datetime format
orders["order_date"] = pd.to_datetime(orders["order_date"])

print("Transformation completed successfully!")

# -------------------------
# CONNECT TO POSTGRESQL
# -------------------------

engine = create_engine(
    "postgresql://postgres:your_password@localhost:5432/ecommerce_dw"
)

print("Connected to PostgreSQL successfully!")

# -------------------------
# LOAD DATA INTO DATABASE
# -------------------------

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

print("ETL Pipeline completed successfully!")
