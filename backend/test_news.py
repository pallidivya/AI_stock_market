from tools.news_tool import get_stock_news

news = get_stock_news("Apple")

for article in news:
    print(article)
    print("-" * 80)