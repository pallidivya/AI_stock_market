from api import check_backend
import streamlit as st

st.set_page_config(
    page_title="AI Stock Market Research Company",
    page_icon="📈",
    layout="wide"
)

st.write("APP VERSION 2")

st.title("📈 AI Stock Market Research Company")

st.markdown(
    """
Welcome to the **AI Stock Market Research Company**.

This application uses multiple AI agents powered by **LangChain** to analyze stocks.
"""
)

st.divider()

st.subheader("Available Features")

col1, col2 = st.columns(2)

with col1:
    st.success("📰 News Analysis")
    st.success("📄 Financial Report Analysis")
    st.success("📈 Technical Indicators")
    st.success("⚠️ Risk Analysis")

with col2:
    st.success("💼 Portfolio Management")
    st.success("💡 Investment Advice")
    st.success("📑 Daily Reports")

st.divider()

st.info("Use the left sidebar to navigate.")



if check_backend():
    st.success("🟢 Backend Connected")
else:
    st.error("🔴 Backend Not Running")