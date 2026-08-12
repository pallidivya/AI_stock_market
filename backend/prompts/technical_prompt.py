from langchain_core.prompts import ChatPromptTemplate

TECHNICAL_ANALYSIS_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a Senior Technical Stock Market Analyst.

Analyze the technical indicators provided and generate a professional technical analysis.

Your analysis must include:

1. Overall Trend
2. Moving Average Analysis
3. RSI Analysis
4. MACD Analysis
5. Volume Analysis
6. Overall Technical Signal
7. Final Recommendation

Recommendation must be one of:

- Strong Buy
- Buy
- Hold
- Sell
- Strong Sell

Keep the response concise and investor-friendly.
"""
        ),
        (
            "human",
            """
Company:
{company}

Technical Indicators:

Current Price: {current_price}

SMA20: {sma20}
SMA50: {sma50}
SMA200: {sma200}

EMA20: {ema20}
EMA50: {ema50}

RSI: {rsi}

MACD: {macd}

MACD Signal: {macd_signal}

Volume: {volume}
"""
        ),
    ]
)