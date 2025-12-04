import streamlit as st
import pandas as pd
from app.models import order_dao

def render_management_page():
    st.header("Master Data Management")
    
    tab1, tab2 = st.tabs(["Product Management", "Customer Management"])

    with tab1:
        st.subheader("Inventory List")
        
        df_prods = order_dao.fetch_products_for_sale()
        
        if df_prods is not None and not df_prods.empty:
            cols = st.columns([1, 3, 2, 2, 2])
            cols[0].markdown("**ID**")
            cols[1].markdown("**Product Name**")
            cols[2].markdown("**Price**")
            cols[3].markdown("**Quantity**")
            cols[4].markdown("**Actions**")
            
            for index, row in df_prods.iterrows():
                c1, c2, c3, c4, c5 = st.columns([1, 3, 2, 2, 2])
                
                c1.write(str(row['product_id']))
                c2.write(row['product_name'])
                c3.write(f"{row['unit_price']:,.0f}")
                
                new_qty = c4.number_input(
                    "Qty", 
                    min_value=0, 
                    value=int(row['stock_quantity']), 
                    label_visibility="collapsed",
                    key=f"stock_{row['product_id']}"
                )
                
                if new_qty != row['stock_quantity']:
                    success, _ = order_dao.update_product_stock(row['product_id'], new_qty)
                    if success:
                        st.toast(f"Updated quantity for {row['product_name']}")
                        
                with c5:
                    with st.popover("Delete"):
                        st.write("Are you sure?")
                        if st.button("Confirm", key=f"del_prod_{row['product_id']}"):
                            success, msg = order_dao.delete_product(row['product_id'])
                            if success:
                                st.success(msg)
                                st.rerun()
                            else:
                                st.error(msg)
            
        st.divider()
        st.subheader("Add New Product")
        with st.form("add_product_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            name = col1.text_input("Product Name")
            category = col2.selectbox("Category", ["Electronics", "Fashion", "Furniture", "Accessories"])
            price = col1.number_input("Unit Price", min_value=1000, step=1000)
            stock = col2.number_input("Initial Quantity", min_value=1, step=1)
            
            if st.form_submit_button("Save New Product"):
                if name and price:
                    success, msg = order_dao.add_new_product(name, category, price, stock)
                    if success:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)
                else:
                    st.warning("Product Name and Price are required.")

    with tab2:
        st.subheader("Customer List")
        df_cust = order_dao.fetch_customers()
        
        if df_cust is not None and not df_cust.empty:
            cust_cols = st.columns([1, 3, 3, 2])
            cust_cols[0].markdown("**ID**")
            cust_cols[1].markdown("**Full Name**")
            cust_cols[2].markdown("**Email**")
            cust_cols[3].markdown("**Actions**")
            
            for index, row in df_cust.iterrows():
                cc1, cc2, cc3, cc4 = st.columns([1, 3, 3, 2])
                
                cc1.write(str(row['customer_id']))
                cc2.write(row['full_name'])
                cc3.write(row['email'])
                
                with cc4:
                    with st.popover("Delete"):
                        st.write("Are you sure?")
                        if st.button("Confirm", key=f"del_cust_{row['customer_id']}"):
                            success, msg = order_dao.delete_customer(row['customer_id'])
                            if success:
                                st.success(msg)
                                st.rerun()
                            else:
                                st.error(msg)

        st.divider()
        st.subheader("Add New Customer")
        with st.form("add_customer_form", clear_on_submit=True):
            c_name = st.text_input("Full Name")
            c_email = st.text_input("Email")
            c_phone = st.text_input("Phone Number")
            c_address = st.text_area("Address")
            
            if st.form_submit_button("Save Customer"):
                if c_name and c_email:
                    success, msg = order_dao.add_new_customer(c_name, c_email, c_phone, c_address)
                    if success:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)
                else:
                    st.warning("Full Name and Email are required.")