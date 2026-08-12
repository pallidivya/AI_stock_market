import os
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()

newsapi = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))


def get_stock_news(company_name: str, page_size: int = 5):
    """
    Fetch latest news articles for a company.

    Args:
        company_name: Company name (e.g., Apple, Tesla, Microsoft)
        page_size: Number of news articles

    Returns:
        List of dictionaries containing news articles
    """

    try:
        response = newsapi.get_everything(
            q=company_name,
            language="en",
            sort_by="publishedAt",
            page_size=page_size,
        )

        articles = []

        for article in response["articles"]:
            articles.append(
                {
                    "title": article["title"],
                    "description": article["description"],
                    "source": article["source"]["name"],
                    "published_at": article["publishedAt"],
                    "url": article["url"],
                }
            )

        return articles

    except Exception as e:
        return {"error": str(e)}