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
    st.sidebar.write("Ecommerce manager system")
    
    menu = st.sidebar.radio(
        "Menu chức năng",
        [
            "Dashboard", 
            "Orders", 
            "Create new order", 
            "Store and customers management",  # Mới
            "Report & Export CSV"   # Mới
        ]
    )

    if menu == "Dashboard":
        render_dashboard()
    elif menu == "Orders":
        render_order_list()
    elif menu == "Create new order":
        render_create_order_page()
    elif menu == "Store and customers management":
        render_management_page()
    elif menu == "Report & Export CSV":
        render_reports_page()

if __name__ == "__main__":
    main()