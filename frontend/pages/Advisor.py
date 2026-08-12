import streamlit as st
from api import analyze_advisor


st.title("💡 Investment Advisor")

st.write(
    "Get a final AI-powered investment recommendation "
    "by combining news, financial, technical, and risk analysis."
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


if st.button("Generate Investment Advice"):

    if not symbol:
        st.warning("Please enter a stock symbol.")

    elif pdf_file is None:
        st.warning("Please upload the annual financial report.")

    else:

        with st.spinner(
            "Analyzing stock and generating investment advice..."
        ):

            result = analyze_advisor(
                symbol,
                pdf_file
            )

        if "error" in result:

            st.error("Investment analysis failed.")
            st.code(result["error"])

        else:

            st.success("Investment Advice Generated!")

            st.divider()

            st.subheader("🏢 Company")
            st.write(result["company"])

            st.subheader("📰 News Summary")
            st.write(result["news_summary"])

            st.subheader("📄 Financial Summary")
            st.write(result["financial_summary"])

            st.subheader("📈 Technical Summary")
            st.write(result["technical_summary"])

            st.subheader("⚠️ Risk Summary")
            st.write(result["risk_summary"])

            st.divider()

            st.subheader("🎯 Final Rating")

            rating = result["final_rating"]

            if rating == "Strong Buy":
                st.success(rating)

            elif rating == "Buy":
                st.success(rating)

            elif rating == "Hold":
                st.warning(rating)

            elif rating == "Sell":
                st.error(rating)

            elif rating == "Strong Sell":
                st.error(rating)

            else:
                st.info(rating)

            st.subheader("📊 Confidence Score")

            confidence = result["confidence_score"]

            st.progress(
                confidence / 100
            )

            st.write(
                f"**{confidence}/100**"
            )

            st.subheader("💡 Final Recommendation")
            st.info(result["recommendation"])

            st.subheader("📝 Overall Explanation")
            st.write(result["explanation"])