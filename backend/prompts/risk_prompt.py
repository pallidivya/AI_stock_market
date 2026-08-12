from langchain_core.prompts import ChatPromptTemplate

RISK_ANALYSIS_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a Senior Risk Analyst working for a global investment firm.

Analyze the stock risk metrics provided.

Your response must include:

1. Volatility Analysis
2. Maximum Drawdown Analysis
3. Sharpe Ratio Analysis
4. Overall Risk Level
   (Low / Medium / High)
5. Risk Score
   Return ONLY an integer between 0 and 100.

Example:
25
60
87

Do NOT return it as a string.
6. Investment Suitability
7. Final Recommendation

Recommendations must be one of:

- Buy
- Hold
- Sell

Keep the explanation concise, factual, and suitable for investors.
"""
        ),
        (
            "human",
            """
Company:
{company}

Risk Metrics

Annualized Volatility:
{volatility}

Maximum Drawdown:
{drawdown}

Sharpe Ratio:
{sharpe_ratio}
"""
        ),
    ]
)