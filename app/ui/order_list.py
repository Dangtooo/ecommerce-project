import streamlit as st
from app.models import order_dao

def render_order_list():
    st.header("📦 Danh sách Đơn hàng")
    
    search = st.text_input("🔍 Tìm kiếm theo tên khách hàng:")
    
    df_orders = order_dao.fetch_orders(search)
    
    if df_orders is not None:
        st.dataframe(df_orders, use_container_width=True)
    else:
        st.info("Không tìm thấy đơn hàng nào.")