import pandas as pd
from sqlalchemy import create_engine

# -------------------------
# EXTRACT DATA FROM CSV FILES
# -------------------------

customers = pd.read_csv(r"C:\Users\Kashrita Thapa\OneDrive\Desktop\ecommerce_dw\data\customers.csv")

products = pd.read_csv(r"C:\Users\Kashrita Thapa\OneDrive\Desktop\ecommerce_dw\data\products.csv")

orders = pd.read_csv(r"C:\Users\Kashrita Thapa\OneDrive\Desktop\ecommerce_dw\data\orders.csv")

order_items = pd.read_csv(r"C:\Users\Kashrita Thapa\OneDrive\Desktop\ecommerce_dw\data\order_items.csv")


# -------------------------
# TRANSFORM DATA
# -------------------------

# Remove unwanted empty columns (Unnamed columns)
customers = customers.loc[:, ~customers.columns.str.contains('^Unnamed')]
products = products.loc[:, ~products.columns.str.contains('^Unnamed')]
orders = orders.loc[:, ~orders.columns.str.contains('^Unnamed')]
order_items = order_items.loc[:, ~order_items.columns.str.contains('^Unnamed')]


# Remove duplicate records
customers = customers.drop_duplicates()
products = products.drop_duplicates()
orders = orders.drop_duplicates()
order_items = order_items.drop_duplicates()


# Convert order_date to date format
orders["order_date"] = pd.to_datetime(orders["order_date"])


print("Transformation completed successfully!")


# -------------------------
# CONNECT TO POSTGRESQL
# -------------------------

engine = create_engine(
    "postgresql://postgres:9507@localhost:5432/ecommerce_dw"
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