import streamlit as st
from api import analyze_news

st.title("📰 News Analysis")

st.write("Analyze the latest news for any stock.")

symbol = st.text_input(
    "Enter Stock Symbol",
    value="AAPL"
)

if st.button("Analyze News"):

    with st.spinner("Analyzing latest news..."):

        result = analyze_news(symbol)

    if "error" in result:
        st.error(result["error"])

    else:

        st.success("Analysis Completed")

        st.subheader("🏢 Company")
        st.write(result["company"])

        st.subheader("📝 Summary")
        st.write(result["summary"])

        st.subheader("📈 Sentiment")
        st.info(result["sentiment"])

        st.subheader("📰 Important Events")

        for event in result["important_events"]:
            st.write("•", event)

        st.subheader("📊 Stock Price Impact")
        st.write(result["impact"])

        st.subheader("⚠️ Risk Factors")
        st.write(result["risk"])

        st.subheader("💡 Recommendation")
        st.success(result["recommendation"])