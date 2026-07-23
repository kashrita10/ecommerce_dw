
 E-Commerce Data Warehouse Analysis Queries


-- 1. View Customers
SELECT * FROM customers;

-- 2. View Products
SELECT * FROM products;

-- 3. View Orders
SELECT * FROM orders;

-- 4. View Order Items
SELECT * FROM order_items;

-- 5. Total Revenue
SELECT
    SUM(total_amount) AS total_revenue
FROM orders;

-- 6. Total Orders
SELECT
    COUNT(order_id) AS total_orders
FROM orders;

-- 7. Average Order Value
SELECT
    AVG(total_amount) AS average_order_value
FROM orders;

-- 8. Sales by City
SELECT
    c.city,
    SUM(o.total_amount) AS city_sales
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.city
ORDER BY city_sales DESC;

-- 9. Revenue by Category
SELECT
    p.category,
    SUM(o.total_amount) AS revenue
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
JOIN orders o
ON oi.order_id = o.order_id
GROUP BY p.category
ORDER BY revenue DESC;

-- 10. Monthly Sales Trend
SELECT
    EXTRACT(YEAR FROM order_date) AS year,
    EXTRACT(MONTH FROM order_date) AS month,
    SUM(total_amount) AS revenue
FROM orders
GROUP BY
    EXTRACT(YEAR FROM order_date),
    EXTRACT(MONTH FROM order_date)
ORDER BY
    year,
    month;

-- 11. Top 10 Customers
SELECT
    c.name,
    SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.name
ORDER BY total_spent DESC
LIMIT 10;

-- 12. Top 10 Selling Products
SELECT
    p.product_name,
    SUM(oi.quantity) AS total_quantity_sold
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_quantity_sold DESC
LIMIT 10;


-- 13. Revenue by Year
SELECT
    EXTRACT(YEAR FROM order_date) AS year,
    SUM(total_amount) AS revenue
FROM orders
GROUP BY year
ORDER BY year;


-- 14. Number of Customers by City
SELECT
    city,
    COUNT(customer_id) AS total_customers
FROM customers
GROUP BY city
ORDER BY total_customers DESC;


-- 15. Highest Value Orders
SELECT
    order_id,
    customer_id,
    total_amount
FROM orders
ORDER BY total_amount DESC
LIMIT 10;

