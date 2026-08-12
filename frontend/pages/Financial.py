import streamlit as st
from api import analyze_financial


st.title("📄 Financial Analysis")

st.write(
    "Upload a company's annual report PDF to generate "
    "an AI-powered financial analysis."
)

st.divider()


company = st.text_input(
    "Company Name",
    value="Apple Inc."
)

uploaded_file = st.file_uploader(
    "Upload Annual Report (PDF)",
    type=["pdf"]
)


if st.button("Analyze Financial Report"):

    if not company.strip():
        st.warning("Please enter a company name.")

    elif uploaded_file is None:
        st.warning("Please upload an annual report PDF.")

    else:

        with st.spinner("Analyzing financial report..."):

            result = analyze_financial(
                company,
                uploaded_file
            )

        if "error" in result:

            st.error("Financial analysis failed.")
            st.code(result["error"])

        else:

            st.success("Financial Analysis Completed!")

            st.divider()

            st.subheader("🏢 Company")
            st.write(result["company"])

            st.subheader("💰 Revenue Analysis")
            st.write(result["revenue_analysis"])

            st.subheader("📈 Profitability")
            st.write(result["profitability"])

            st.subheader("🏦 Balance Sheet")
            st.write(result["balance_sheet"])

            st.subheader("💵 Cash Flow")
            st.write(result["cash_flow"])

            st.subheader("⚠️ Financial Risk")
            st.write(result["financial_risk"])

            st.subheader("🚀 Growth Outlook")
            st.write(result["growth_outlook"])

            st.subheader("💡 Investment Recommendation")

            recommendation = result["investment_recommendation"]

            if "buy" in recommendation.lower():
                st.success(recommendation)

            elif "sell" in recommendation.lower():
                st.error(recommendation)

            else:
                st.warning(recommendation)