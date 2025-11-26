# FILE: app/main.py (Thay thế toàn bộ file cũ)
import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.ui.dashboard import render_dashboard
from app.ui.order_list import render_order_list
from app.ui.create_order import render_create_order_page
# Import 2 trang mới
from app.ui.management import render_management_page 
from app.ui.reports import render_reports_page

st.set_page_config(page_title="E-commerce Manager", layout="wide", page_icon="🛒")

def main():
    st.sidebar.title("🛒 E-Shop Admin")
    st.sidebar.write("Hệ thống quản lý bán hàng v1.0")
    
    menu = st.sidebar.radio(
        "Menu chức năng",
        [
            "📊 Dashboard (Tổng quan)", 
            "📦 Đơn hàng (Orders)", 
            "📝 Tạo đơn mới", 
            "🛠️ Quản lý Kho & Khách",  # Mới
            "📑 Báo cáo & Export CSV"   # Mới
        ]
    )

    if menu == "📊 Dashboard (Tổng quan)":
        render_dashboard()
    elif menu == "📦 Đơn hàng (Orders)":
        render_order_list()
    elif menu == "📝 Tạo đơn mới":
        render_create_order_page()
    elif menu == "🛠️ Quản lý Kho & Khách":
        render_management_page()
    elif menu == "📑 Báo cáo & Export CSV":
        render_reports_page()

if __name__ == "__main__":
    main()