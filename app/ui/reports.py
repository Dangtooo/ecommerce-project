import streamlit as st
from app.models import order_dao

def render_reports_page():
    st.header("📑 Báo cáo & Xuất dữ liệu")
    st.info("Chức năng xuất dữ liệu ra file CSV phục vụ kế toán.")

    # Lấy dữ liệu báo cáo chi tiết (Left Join)
    df_report = order_dao.fetch_detailed_report()

    if df_report is not None:
        st.dataframe(df_report, use_container_width=True)

        # Chuyển đổi DataFrame sang CSV
        csv = df_report.to_csv(index=False).encode('utf-8')

        # Nút Download đúng chuẩn yêu cầu
        st.download_button(
            label="⬇️ Tải xuống CSV (Export)",
            data=csv,
            file_name='bao_cao_chi_tiet.csv',
            mime='text/csv',
        )
    else:
        st.error("Không tải được dữ liệu báo cáo.")