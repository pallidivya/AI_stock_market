from langchain_core.prompts import ChatPromptTemplate

REPORT_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an experienced Equity Research Analyst.

Using the provided analyses, generate a professional stock research report.

The report should contain:

1. Executive Summary

2. News Analysis

3. Financial Analysis

4. Technical Analysis

5. Risk Analysis

6. Final Investment Recommendation

7. Confidence Score

8. Conclusion

Write the report in a professional style suitable for investors.
"""
        ),
        (
            "human",
            """
Company:
{company}

News Analysis:
{news}

Financial Analysis:
{financial}

Technical Analysis:
{technical}

Risk Analysis:
{risk}

Investment Advice:
{advisor}
"""
        ),
    ]
)