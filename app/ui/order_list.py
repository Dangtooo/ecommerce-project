import streamlit as st
from app.models import order_dao

def render_order_list():
    st.header("📦 Quản lý Đơn hàng")
    
    # 1. Tìm kiếm
    col1, col2 = st.columns([3, 1])
    search = col1.text_input("🔍 Tìm kiếm theo tên khách hàng:")
    
    # 2. Xóa đơn hàng (Nhập ID để xóa cho an toàn)
    with col2:
        with st.popover("🗑️ Xóa đơn hàng"):
            del_id = st.number_input("Nhập ID đơn cần xóa", min_value=1, step=1)
            if st.button("Xác nhận xóa", type="primary"):
                success, msg = order_dao.delete_order(del_id)
                if success:
                    st.success(msg)
                    st.rerun()
                else:
                    st.error(msg)

    # 3. Hiển thị bảng
    df_orders = order_dao.fetch_orders(search)
    
    if df_orders is not None:
        # Highlight trạng thái Cancelled màu đỏ
        st.dataframe(
            df_orders.style.apply(
                lambda x: ['background-color: #ffcccc' if x['order_status'] == 'Cancelled' else '' for i in x], 
                axis=1
            ),
            use_container_width=True
        )
    else:
        st.info("Không tìm thấy đơn hàng nào.")