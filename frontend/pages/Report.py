import streamlit as st
from api import generate_report


st.title("📑 Daily Investment Research Report")

st.write(
    "Generate a comprehensive AI-powered stock research report "
    "using news, financial, technical, risk, and investment analysis."
)

st.divider()


symbol = st.text_input(
    "Enter Stock Symbol",
    value="AAPL"
).upper().strip()


pdf_file = st.file_uploader(
    "Upload Annual Financial Report",
    type=["pdf"]
)


if st.button("Generate Daily Report"):

    if not symbol:
        st.warning("Please enter a stock symbol.")

    elif pdf_file is None:
        st.warning("Please upload the annual financial report.")

    else:

        with st.spinner(
            "Generating comprehensive research report..."
        ):

            result = generate_report(
                symbol,
                pdf_file
            )

        if "error" in result:

            st.error("Report generation failed.")
            st.code(result["error"])

        else:

            st.success("Daily Report Generated Successfully!")

            st.divider()

            st.subheader("🏢 Company")
            st.write(result["company"])

            st.divider()

            st.subheader("📑 Investment Research Report")

            st.markdown(
                result["report"]
            )

            st.divider()

            st.download_button(
                label="📥 Download Report",
                data=result["report"],
                file_name=f"{symbol}_daily_report.txt",
                mime="text/plain"
            )