from prompts.report_prompt import REPORT_PROMPT

prompt = REPORT_PROMPT.invoke(
    {
        "company": "Apple Inc.",
        "news": "Positive AI announcements.",
        "financial": "Revenue continues to grow.",
        "technical": "Bearish short-term trend.",
        "risk": "Medium risk.",
        "advisor": "Buy with confidence score 80."
    }
)

print(prompt)