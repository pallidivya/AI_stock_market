from agents.base_agent import BaseAgent
from prompts.prompts import NEWS_ANALYSIS_PROMPT
from schemas.news_schema import NewsAnalysis
from tools.news_tool import get_stock_news


class NewsAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            prompt=NEWS_ANALYSIS_PROMPT,
            output_schema=NewsAnalysis
        )

    def analyze(self, company_name: str):

        news = get_stock_news(company_name)

        if isinstance(news, dict):
            return news

        formatted_news = ""

        for i, article in enumerate(news, start=1):

            formatted_news += f"""
Article {i}

Title:
{article['title']}

Description:
{article['description']}

Source:
{article['source']}

Published:
{article['published_at']}

------------------------------------
"""

        return self.invoke(
            {
                "company": company_name,
                "news": formatted_news,
            }
        )