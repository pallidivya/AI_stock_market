import streamlit as st

st.title("📊 Dashboard")

symbol = st.text_input(
    "Enter Stock Symbol",
    placeholder="Example: AAPL"
)

uploaded_pdf = st.file_uploader(
    "Upload Annual Report (PDF)",
    type=["pdf"]
)

if st.button("🔍 Analyze Stock"):

    if symbol == "":
        st.error("Please enter a stock symbol.")

    elif uploaded_pdf is None:
        st.error("Please upload the annual report.")

    else:
        st.success("Everything looks good!")

        st.write("Stock:", symbol)

        st.write("PDF:", uploaded_pdf.name)