import streamlit as st
from api import analyze_portfolio


st.title("💼 Portfolio Management")

st.write(
    "Analyze multiple stocks and generate an AI-powered "
    "portfolio allocation."
)

st.divider()


symbols_input = st.text_input(
    "Enter Stock Symbols",
    value="AAPL, MSFT",
    help="Enter multiple stock symbols separated by commas."
)


if st.button("Analyze Portfolio"):

    symbols = [
        symbol.strip().upper()
        for symbol in symbols_input.split(",")
        if symbol.strip()
    ]

    if not symbols:
        st.warning("Please enter at least one stock symbol.")

    elif len(symbols) < 2:
        st.warning("Please enter at least two stocks for portfolio analysis.")

    else:

        with st.spinner(
            "Analyzing portfolio... This may take a little while."
        ):

            result = analyze_portfolio(symbols)

        if "error" in result:

            st.error("Portfolio analysis failed.")
            st.code(result["error"])

        else:

            st.success("Portfolio Analysis Completed!")

            st.divider()

            st.subheader("📊 Portfolio Summary")
            st.write(result["portfolio_summary"])

            st.subheader("🔄 Diversification Analysis")
            st.write(result["diversification"])

            st.subheader("⚠️ Overall Risk")
            st.write(result["overall_risk"])

            st.subheader("🏆 Strongest Stock")
            st.success(result["strongest_stock"])

            st.subheader("📉 Weakest Stock")
            st.warning(result["weakest_stock"])

            st.subheader("💰 Suggested Allocation")

            allocations = result["suggested_allocations"]

            for allocation in allocations:

                symbol = allocation["symbol"]
                percentage = allocation["allocation_percent"]

                st.write(
                    f"**{symbol}: {percentage:.1f}%**"
                )

                st.progress(
                    int(percentage)
                )

            total = sum(
                allocation["allocation_percent"]
                for allocation in allocations
            )

            st.write(f"**Total Allocation: {total:.1f}%**")

            st.subheader("💡 Final Recommendation")

            st.info(result["recommendation"])