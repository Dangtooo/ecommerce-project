import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from app.models import order_dao

def render_dashboard():
    st.header("Báo cáo Doanh thu & Xu hướng")

    # 1. Lấy dữ liệu tổng hợp từ SQL
    df_summary = order_dao.fetch_summary_data()
    
    if df_summary is not None and not df_summary.empty:
        # ---------------------------------------------------------
        # KHU VỰC BỘ LỌC (FILTER)
        # ---------------------------------------------------------
        st.subheader("Chọn thời gian xem báo cáo")
        
        col_filter_1, col_filter_2 = st.columns(2)
        
        with col_filter_1:
            # Lấy danh sách Năm duy nhất có trong dữ liệu
            unique_years = sorted(df_summary['Year'].unique(), reverse=True)
            selected_year = st.selectbox("Chọn Năm", unique_years)

        with col_filter_2:
            # Lọc ra các tháng chỉ thuộc về Năm đã chọn (để không hiện tháng trống)
            months_in_year = df_summary[df_summary['Year'] == selected_year]['Month'].unique()
            unique_months = sorted(months_in_year, reverse=True) # Tháng mới nhất lên đầu
            selected_month = st.selectbox("Chọn Tháng", unique_months)

        # ---------------------------------------------------------
        # XỬ LÝ SỐ LIỆU THEO LỰA CHỌN
        # ---------------------------------------------------------
        
        # Tìm dòng dữ liệu khớp với Năm và Tháng đã chọn
        # Dùng hàm loc để lọc: (Year == selected) AND (Month == selected)
        selected_data = df_summary[
            (df_summary['Year'] == selected_year) & 
            (df_summary['Month'] == selected_month)
        ]

        st.divider()

        if not selected_data.empty:
            # Lấy dòng đầu tiên (thực ra cũng chỉ có 1 dòng thôi)
            row = selected_data.iloc[0]

            # Hiển thị KPI Cards
            col1, col2, col3 = st.columns(3)
            
            # KPI 1: Tổng đơn hàng
            col1.metric(
                label=f"Tổng đơn (Tháng {selected_month}/{selected_year})", 
                value=f"{row['Total_Orders']} đơn"
            )
            
            # KPI 2: Doanh thu (Tô màu xanh cho đẹp nếu > 0)
            col2.metric(
                label="Doanh thu", 
                value=f"{row['Total_Revenue']:,.0f} VNĐ",
                delta="Doanh thu thực tế" # Chỉ để trang trí
            )
            
            # KPI 3: Đơn hủy (Tô màu đỏ nếu có đơn hủy)
            col3.metric(
                label="Đơn bị hủy", 
                value=f"{row['Total_Cancelled']} đơn",
                delta_color="inverse" # Màu đỏ thể hiện tiêu cực
            )

        else:
            st.warning(f"Không có dữ liệu cho Tháng {selected_month}/{selected_year}")

        # ---------------------------------------------------------
        # BIỂU ĐỒ (Giữ nguyên biểu đồ CẢ NĂM để so sánh)
        # ---------------------------------------------------------
        st.divider()
        st.subheader(f"Xu hướng kinh doanh năm {selected_year}")
        
        df_chart = df_summary[df_summary['Year'] == selected_year].copy()
        
        df_chart = df_chart.sort_values(by='Month')
        
        df_chart['Time_Label'] = "Tháng " + df_chart['Month'].astype(str)
        df_chart['Total_Revenue'] = df_chart['Total_Revenue'].astype(float)

        # Vẽ biểu đồ cột
        st.bar_chart(df_chart, x='Time_Label', y='Total_Revenue')

    else:
        st.info("Chưa có dữ liệu đơn hàng nào trong hệ thống.")

    # ---------------------------------------------------------
    # TOP SẢN PHẨM
    # ---------------------------------------------------------
    st.divider()
    st.subheader("Top Sản phẩm bán chạy nhất (Theo số lượng)")
    
    df_products = order_dao.fetch_top_products()
    
    if df_products is not None:
        col_L, col_R = st.columns([2, 1])
        
        with col_L:
            st.dataframe(df_products, use_container_width=True)
            
        with col_R:
            st.write("Tỷ trọng số lượng bán ra:")
            fig, ax = plt.subplots()

            ax.pie(
                df_products['Total_Quantity_Sold'], 
                labels=df_products['product_name'], 
                autopct='%1.0f%%',
                startangle=90
            )
            ax.axis('equal') 
            st.pyplot(fig)