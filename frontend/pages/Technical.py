import streamlit as st
from api import analyze_technical


st.title("📈 Technical Analysis")

st.write(
    "Analyze technical indicators and trading signals "
    "for a stock."
)

st.divider()


symbol = st.text_input(
    "Enter Stock Symbol",
    value="AAPL"
).upper().strip()


if st.button("Analyze Technical"):

    if not symbol:
        st.warning("Please enter a stock symbol.")

    else:

        with st.spinner(
            f"Analyzing technical indicators for {symbol}..."
        ):

            result = analyze_technical(symbol)

        if "error" in result:

            st.error("Technical analysis failed.")
            st.code(result["error"])

        else:

            st.success("Technical Analysis Completed!")

            st.divider()

            st.subheader("🏢 Company")
            st.write(result["company"])

            st.subheader("📊 Trend")
            st.write(result["trend"])

            st.subheader("📈 Moving Average Analysis")
            st.write(result["moving_average_analysis"])

            st.subheader("RSI Analysis")
            st.write(result["rsi_analysis"])

            st.subheader("MACD Analysis")
            st.write(result["macd_analysis"])

            st.subheader("📊 Volume Analysis")
            st.write(result["volume_analysis"])

            st.subheader("🚦 Overall Signal")

            signal = result["overall_signal"]

            if signal.lower() in ["buy", "strong buy"]:
                st.success(signal)

            elif signal.lower() in ["sell", "strong sell"]:
                st.error(signal)

            else:
                st.warning(signal)

            st.subheader("💡 Recommendation")

            recommendation = result["recommendation"]

            if recommendation.lower() == "buy":
                st.success(recommendation)

            elif recommendation.lower() == "sell":
                st.error(recommendation)

            else:
                st.warning(recommendation)