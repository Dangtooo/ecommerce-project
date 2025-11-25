import streamlit as st
import matplotlib.pyplot as plt
from app.models import order_dao

def render_dashboard():
    st.header("📊 Báo cáo Doanh thu & Xu hướng")

    df_summary = order_dao.fetch_summary_data()
    
    if df_summary is not None and not df_summary.empty:
        last_month = df_summary.iloc[0]
        col1, col2, col3 = st.columns(3)
        col1.metric("Tổng đơn (Mới nhất)", f"{last_month['Total_Orders']}")
        col2.metric("Doanh thu", f"{last_month['Total_Revenue']:,.0f} VNĐ")
        col3.metric("Đơn hủy", f"{last_month['Total_Cancelled']}")

        st.divider()
        st.subheader("Biểu đồ Doanh thu")
        
        # Xử lý dữ liệu vẽ biểu đồ
        df_chart = df_summary.copy()
        df_chart['Total_Revenue'] = df_chart['Total_Revenue'].astype(float)
        df_chart['Time'] = df_chart['Month'].astype(str) + '-' + df_chart['Year'].astype(str)
        st.bar_chart(df_chart, x='Time', y='Total_Revenue')

    st.divider()
    st.subheader("🏆 Top Sản phẩm bán chạy")
    df_products = order_dao.fetch_top_products()
    
    if df_products is not None:
        col_L, col_R = st.columns([2, 1])
        with col_L:
            st.dataframe(df_products, use_container_width=True)
        with col_R:
            fig, ax = plt.subplots()
            df_products['Total_Revenue_Generated'] = df_products['Total_Revenue_Generated'].astype(float)
            ax.pie(df_products['Total_Revenue_Generated'], labels=df_products['product_name'], autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
            st.pyplot(fig)