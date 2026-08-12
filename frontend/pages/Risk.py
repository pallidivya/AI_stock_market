import streamlit as st
from api import analyze_risk


st.title("⚠️ Risk Analysis")

st.write(
    "Analyze the risk profile of a stock using "
    "volatility, drawdown, and Sharpe ratio."
)

st.divider()


symbol = st.text_input(
    "Enter Stock Symbol",
    value="AAPL"
).upper().strip()


if st.button("Analyze Risk"):

    if not symbol:
        st.warning("Please enter a stock symbol.")

    else:

        with st.spinner(
            f"Analyzing risk for {symbol}..."
        ):

            result = analyze_risk(symbol)

        if "error" in result:

            st.error("Risk analysis failed.")
            st.code(result["error"])

        else:

            st.success("Risk Analysis Completed!")

            st.divider()

            st.subheader("🏢 Company")
            st.write(result["company"])

            st.subheader("📊 Volatility Analysis")
            st.write(result["volatility_analysis"])

            st.subheader("📉 Maximum Drawdown Analysis")
            st.write(result["drawdown_analysis"])

            st.subheader("📈 Sharpe Ratio Analysis")
            st.write(result["sharpe_ratio_analysis"])

            st.subheader("⚠️ Overall Risk Level")

            risk_level = result["risk_level"]

            if risk_level.lower() == "low":
                st.success(risk_level)

            elif risk_level.lower() == "high":
                st.error(risk_level)

            else:
                st.warning(risk_level)

            st.subheader("🎯 Risk Score")

            risk_score = result["risk_score"]

            st.progress(
                risk_score / 100
            )

            st.write(
                f"**{risk_score}/100**"
            )

            st.subheader("👤 Investment Suitability")
            st.write(result["investment_suitability"])

            st.subheader("💡 Recommendation")

            recommendation = result["recommendation"]

            if recommendation.lower() == "buy":
                st.success(recommendation)

            elif recommendation.lower() == "sell":
                st.error(recommendation)

            else:
                st.warning(recommendation)