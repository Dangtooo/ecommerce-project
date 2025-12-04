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
def add_new_product(name, category, price, stock):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            # Check existing
            check_sql = "SELECT product_id, stock_quantity FROM PRODUCTS WHERE product_name = %s"
            cursor.execute(check_sql, (name,))
            existing_product = cursor.fetchone()

            if existing_product:
                prod_id = existing_product[0]
                current_stock = existing_product[1]
                new_stock = current_stock + int(stock)
                
                update_sql = """
                    UPDATE PRODUCTS 
                    SET stock_quantity = %s, unit_price = %s, category = %s
                    WHERE product_id = %s
                """
                cursor.execute(update_sql, (new_stock, float(price), category, prod_id))
                msg = f"Product '{name}' exists. Stock updated: {current_stock} -> {new_stock}."
            else:
                insert_sql = """
                    INSERT INTO PRODUCTS (product_name, category, unit_price, stock_quantity) 
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(insert_sql, (name, category, float(price), int(stock)))
                msg = f"New product '{name}' added successfully!"

            conn.commit()
            return True, msg
        except Exception as e:
            return False, str(e)
        finally:
            cursor.close()
            conn.close()
    return False, "Database connection error"

def add_new_customer(full_name, email, phone, address):
    """Thêm khách hàng mới"""
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            sql = "INSERT INTO CUSTOMERS (full_name, email, phone_number, address) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (full_name, email, phone, address))
            conn.commit()
            cursor.close()
            conn.close()
            return True, "Thêm khách hàng thành công!"
        except Exception as e:
            conn.close()
            return False, str(e)
    return False, "Lỗi kết nối"
def delete_order(order_id):
    """Xóa đơn hàng theo ID (Xóa sạch các dữ liệu liên quan trước)"""
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            # BƯỚC 1: Xóa dữ liệu Vận chuyển liên quan trước
            sql_ship = "DELETE FROM SHIPMENTS WHERE order_id = %s"
            cursor.execute(sql_ship, (order_id,))

            # BƯỚC 2: Xóa dữ liệu Thanh toán liên quan
            sql_pay = "DELETE FROM PAYMENTS WHERE order_id = %s"
            cursor.execute(sql_pay, (order_id,))
            
            # Lưu ý: Bảng ORDER_DETAILS đã có ON DELETE CASCADE trong SQL 
            # nên không cần xóa thủ công, nó sẽ tự mất khi xóa ORDERS.

            # BƯỚC 3: Xóa Đơn hàng gốc
            sql_order = "DELETE FROM ORDERS WHERE order_id = %s"
            cursor.execute(sql_order, (order_id,))
            
            conn.commit()
            cursor.close()
            conn.close()
            return True, f"Đã xóa thành công đơn hàng #{order_id} và các dữ liệu liên quan."
        except Exception as e:
            conn.close()
            # In lỗi ra để dễ debug nếu có vấn đề khác
            print(f"Error deleting order: {e}") 
            return False, f"Không thể xóa đơn hàng: {str(e)}"
    return False, "Lỗi kết nối Database"

def fetch_detailed_report():
    """Lấy báo cáo chi tiết cho yêu cầu xuất CSV"""
    conn = get_db_connection()
    if conn:
        # LEFT JOIN theo yêu cầu số [81]
        sql = """
        SELECT c.full_name, c.email, o.order_id, o.order_date, o.total_amount, o.order_status
        FROM CUSTOMERS c
        LEFT JOIN ORDERS o ON c.customer_id = o.customer_id
        ORDER BY o.order_date DESC
        """
        df = pd.read_sql(sql, conn)
        conn.close()
        return df
    return None
def update_product_stock(product_id, new_quantity):
    """Cập nhật số lượng tồn kho cho sản phẩm"""
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            sql = "UPDATE PRODUCTS SET stock_quantity = %s WHERE product_id = %s"
            cursor.execute(sql, (new_quantity, product_id))
            conn.commit()
            return True, "Updated successfully"
        except Exception as e:
            return False, str(e)
        finally:
            cursor.close()
            conn.close()
    return False, "Connection error"

def delete_product(product_id):
    """Xóa sản phẩm (Chỉ xóa được nếu chưa có đơn hàng nào mua nó)"""
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            sql = "DELETE FROM PRODUCTS WHERE product_id = %s"
            cursor.execute(sql, (product_id,))
            conn.commit()
            return True, f"Deleted Product #{product_id}"
        except Exception as e:
            # Lỗi thường gặp: Sản phẩm đã nằm trong đơn hàng cũ -> Không xóa được (Ràng buộc khóa ngoại)
            if "foreign key constraint fails" in str(e).lower():
                return False, "Cannot delete: This product is part of existing orders."
            return False, str(e)
        finally:
            cursor.close()
            conn.close()
    return False, "Connection error"

def delete_customer(customer_id):
    """Xóa khách hàng (Chỉ xóa được nếu họ chưa đặt đơn nào)"""
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            sql = "DELETE FROM CUSTOMERS WHERE customer_id = %s"
            cursor.execute(sql, (customer_id,))
            conn.commit()
            return True, f"Deleted Customer #{customer_id}"
        except Exception as e:
            if "foreign key constraint fails" in str(e).lower():
                return False, "Cannot delete: This customer has existing orders."
            return False, str(e)
        finally:
            cursor.close()
            conn.close()
    return False, "Connection error"