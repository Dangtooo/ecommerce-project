# SQL constants

GET_MONTHLY_SUMMARY = "SELECT * FROM v_monthly_sales_summary"

GET_TOP_PRODUCTS = "SELECT * FROM v_popular_products LIMIT 10"

GET_ALL_CUSTOMERS = "SELECT customer_id, full_name, email, phone_number, address FROM CUSTOMERS"

GET_AVAILABLE_PRODUCTS = "SELECT product_id, product_name, unit_price, stock_quantity, category FROM PRODUCTS"
# Query tìm kiếm đơn hàng (Dynamic query sẽ xử lý ở DAO)
BASE_GET_ORDERS = "SELECT * FROM v_orders_by_customer"