import streamlit as st
from app.models import order_dao

def render_reports_page():
    st.header("Report & Export CSV")
    st.info("Function to export data to CSV file for accounting purposes.")

    # Lấy dữ liệu báo cáo chi tiết (Left Join)
    df_report = order_dao.fetch_detailed_report()

    if df_report is not None:
        st.dataframe(df_report, use_container_width=True)

        # Chuyển đổi DataFrame sang CSV
        csv = df_report.to_csv(index=False).encode('utf-8')

        # Nút Download đúng chuẩn yêu cầu
        st.download_button(
            label="Download CSV (Export)",
            data=csv,
            file_name='detailed_report.csv',
            mime='text/csv',
        )
    else:
        st.error("Không tải được dữ liệu báo cáo.")