import streamlit as st
import pandas as pd
from app.models import order_dao

def render_management_page():
    st.header("🛠️ Quản lý Dữ liệu gốc (Master Data)")
    
    tab1, tab2 = st.tabs(["📦 Quản lý Sản phẩm", "busts_in_silhouette: Quản lý Khách hàng"])

    # --- TAB 1: SẢN PHẨM ---
    with tab1:
        st.subheader("Danh sách Sản phẩm hiện có")
        df_prods = order_dao.fetch_products_for_sale()
        if df_prods is not None:
            st.dataframe(df_prods, use_container_width=True)
        
        st.divider()
        st.subheader("➕ Thêm Sản phẩm mới")
        with st.form("add_product_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            name = col1.text_input("Tên sản phẩm")
            category = col2.selectbox("Danh mục", ["Electronics", "Fashion", "Furniture", "Accessories"])
            price = col1.number_input("Đơn giá (VNĐ)", min_value=1000, step=1000)
            stock = col2.number_input("Tồn kho ban đầu", min_value=1, step=1)
            
            if st.form_submit_button("Lưu sản phẩm"):
                if name and price:
                    success, msg = order_dao.add_new_product(name, category, price, stock)
                    if success:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)
                else:
                    st.warning("Vui lòng nhập tên và giá.")

    # --- TAB 2: KHÁCH HÀNG ---
    with tab2:
        st.subheader("Danh sách Khách hàng")
        df_cust = order_dao.fetch_customers()
        if df_cust is not None:
            st.dataframe(df_cust, use_container_width=True)

        st.divider()
        st.subheader("➕ Thêm Khách hàng mới")
        with st.form("add_customer_form", clear_on_submit=True):
            c_name = st.text_input("Họ và tên")
            c_email = st.text_input("Email")
            c_phone = st.text_input("Số điện thoại")
            c_address = st.text_area("Địa chỉ")
            
            if st.form_submit_button("Lưu khách hàng"):
                if c_name and c_email:
                    success, msg = order_dao.add_new_customer(c_name, c_email, c_phone, c_address)
                    if success:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)
                else:
                    st.warning("Họ tên và Email là bắt buộc.")