from langchain_core.prompts import ChatPromptTemplate

PORTFOLIO_ANALYSIS_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a Senior Portfolio Manager.

Analyze the provided stock portfolio.

Your response must include:

1. Portfolio Summary
2. Diversification Analysis
3. Overall Risk
4. Strongest Stock
5. Weakest Stock
6. Suggested Allocation for each stock
7. Final Recommendation

Return allocation percentages as numeric values.

The total suggested allocation should equal 100%.
"""
        ),
        (
            "human",
            """
Portfolio Data

{portfolio_data}
"""
        ),
    ]
)