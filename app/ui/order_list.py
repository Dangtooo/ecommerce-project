import streamlit as st
from app.models import order_dao

def render_order_list():
    st.header("Order Management")
    
    # 1. Search
    search = st.text_input("Search by Customer Name:")
    
    # 2. Table View
    df_orders = order_dao.fetch_orders(search)
    
    if df_orders is not None:
        st.dataframe(
            df_orders.style.apply(
                lambda x: ['background-color: #ffcccc' if x['order_status'] == 'Cancelled' else '' for i in x], 
                axis=1
            ),
            use_container_width=True
        )
    else:
        st.info("No orders found.")

    # 3. Delete Order Section (Moved to bottom or separate section)
    st.divider()
    st.subheader("Delete Order")
    
    col1, col2 = st.columns([3, 1])
    del_id = col1.number_input("Enter Order ID to Delete", min_value=1, step=1, key="del_order_input")
    
    # Step 1: Request Delete
    if col2.button("Delete Order"):
        st.session_state['confirm_del_order'] = True
        st.session_state['target_order_id'] = del_id

    # Step 2: Confirm
    if st.session_state.get('confirm_del_order'):
        st.warning(f"Are you sure you want to delete Order ID {st.session_state['target_order_id']}? This will also remove related Shipments and Payments.")
        col_conf_1, col_conf_2 = st.columns([1, 5])
        
        if col_conf_1.button("Yes, Delete"):
            success, msg = order_dao.delete_order(st.session_state['target_order_id'])
            if success:
                st.success(msg)
                st.session_state['confirm_del_order'] = False
                st.rerun()
            else:
                st.error(msg)
        
        if col_conf_2.button("Cancel"):
            st.session_state['confirm_del_order'] = False
            st.rerun()