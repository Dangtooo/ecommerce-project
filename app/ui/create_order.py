import streamlit as st
from app.models import order_dao

def render_create_order_page():
    st.header("Tạo Đơn hàng Mới")
    
    # Lấy dữ liệu dropdown
    df_customers = order_dao.fetch_customers()
    df_products = order_dao.fetch_products_for_sale()
    
    if df_customers is None or df_products is None:
        st.error("Không tải được danh sách khách hàng hoặc sản phẩm.")
        return

    # Tạo dictionary để map tên -> id
    customer_dict = dict(zip(df_customers['full_name'], df_customers['customer_id']))
    product_map = {row['product_name']: (row['product_id'], row['unit_price']) for index, row in df_products.iterrows()}

    # Form nhập liệu
    with st.form("order_form"):
        cust_name = st.selectbox("Khách hàng", options=customer_dict.keys())
        prod_name = st.selectbox("Sản phẩm", options=product_map.keys())
        qty = st.number_input("Số lượng", min_value=1, value=1)
        
        # Hiển thị giá tạm tính (bên ngoài form khó cập nhật realtime trong streamlit basic, nên ta hiển thị sau khi submit hoặc dùng session state, ở đây làm đơn giản)
        current_price = product_map[prod_name][1]
        
        submitted = st.form_submit_button("Xác nhận tạo đơn")
        
        if submitted:
            cust_id = customer_dict[cust_name]
            prod_id = product_map[prod_name][0]
            
            success, msg = order_dao.create_new_order(cust_id, prod_id, qty, current_price)
            
            if success:
                st.success(f"{msg}")
                st.balloons()
            else:
                st.error(f"Lỗi: {msg}")