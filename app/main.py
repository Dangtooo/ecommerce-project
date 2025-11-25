import streamlit as st
import sys
import os

# Thêm thư mục gốc vào đường dẫn để Python tìm thấy các module 'app'
# (Dòng này giúp tránh lỗi ModuleNotFound khi chạy từ folder con)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.ui.dashboard import render_dashboard
from app.ui.order_list import render_order_list
from app.ui.create_order import render_create_order_page

# Cấu hình trang
st.set_page_config(page_title="E-commerce Manager", layout="wide")

def main():
    st.sidebar.title("E-Shop Admin")
    menu = st.sidebar.radio(
        "Menu",
        ["Dashboard", "Quản lý Đơn hàng", "Tạo Đơn mới"]
    )

    if menu == "Dashboard":
        render_dashboard()
    elif menu == "Quản lý Đơn hàng":
        render_order_list()
    elif menu == "Tạo Đơn mới":
        render_create_order_page()

if __name__ == "__main__":
    main()