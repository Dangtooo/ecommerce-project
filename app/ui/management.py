import streamlit as st
import pandas as pd
from app.models import order_dao

def render_management_page():
    st.header("Master Data")
    
    tab1, tab2 = st.tabs(["Product management", "Customer management"])

    # --- TAB 1: SẢN PHẨM ---
    with tab1:
        st.subheader("List of available products")
        df_prods = order_dao.fetch_products_for_sale()
        if df_prods is not None:
            st.dataframe(df_prods, use_container_width=True)
        
        st.divider()
        st.subheader("Create new product")
        with st.form("add_product_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            name = col1.text_input("Product's name")
            category = col2.selectbox("category", ["Electronics", "Fashion", "Furniture", "Accessories"])
            price = col1.number_input("Price (VNĐ)", min_value=1000, step=1000)
            stock = col2.number_input("Initial inventory", min_value=1, step=1)
            
            if st.form_submit_button("Save product"):
                if name and price:
                    success, msg = order_dao.add_new_product(name, category, price, stock)
                    if success:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)
                else:
                    st.warning("Please enter name and price")

    # --- TAB 2: KHÁCH HÀNG ---
    with tab2:
        st.subheader("List of customers")
        df_cust = order_dao.fetch_customers()
        if df_cust is not None:
            st.dataframe(df_cust, use_container_width=True)

        st.divider()
        st.subheader("Create new customer")
        with st.form("add_customer_form", clear_on_submit=True):
            c_name = st.text_input("Full name")
            c_email = st.text_input("Email")
            c_phone = st.text_input("Phone number")
            c_address = st.text_area("Address")
            
            if st.form_submit_button("Save customer"):
                if c_name and c_email:
                    success, msg = order_dao.add_new_customer(c_name, c_email, c_phone, c_address)
                    if success:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)
                else:
                    st.warning("Full name and email is required.")