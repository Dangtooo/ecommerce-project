import mysql.connector
import os
from dotenv import load_dotenv
import streamlit as st

# Load biến môi trường từ file .env
load_dotenv()

def get_db_connection():
    """
    Tạo kết nối đến database.
    Sử dụng st.cache_resource để không phải kết nối lại mỗi khi load trang.
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return connection
    except mysql.connector.Error as err:
        st.error(f"Lỗi kết nối Database: {err}")
        return None