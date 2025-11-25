import pandas as pd
from app.db.connection import get_db_connection
from app.queries import sql_queries as sql

def fetch_summary_data():
    conn = get_db_connection()
    if conn:
        df = pd.read_sql(sql.GET_MONTHLY_SUMMARY, conn)
        conn.close()
        return df
    return None

def fetch_top_products():
    conn = get_db_connection()
    if conn:
        df = pd.read_sql(sql.GET_TOP_PRODUCTS, conn)
        conn.close()
        return df
    return None

def fetch_orders(search_term=None):
    conn = get_db_connection()
    if conn:
        query = sql.BASE_GET_ORDERS
        if search_term:
            query += f" WHERE full_name LIKE '%{search_term}%'"
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    return None

def fetch_customers():
    conn = get_db_connection()
    if conn:
        df = pd.read_sql(sql.GET_ALL_CUSTOMERS, conn)
        conn.close()
        return df
    return None

def fetch_products_for_sale():
    conn = get_db_connection()
    if conn:
        df = pd.read_sql(sql.GET_AVAILABLE_PRODUCTS, conn)
        conn.close()
        return df
    return None

def create_new_order(customer_id, product_id, quantity, price):
    conn = get_db_connection()
    success = False
    message = ""
    if conn:
        cursor = conn.cursor()
        try:
            args = (customer_id, product_id, quantity, float(price))
            cursor.callproc('sp_create_simple_order', args)
            conn.commit()
            success = True
            message = "Tạo đơn hàng thành công!"
        except Exception as e:
            message = str(e)
        finally:
            cursor.close()
            conn.close()
    return success, message