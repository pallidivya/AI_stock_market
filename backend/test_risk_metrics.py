from tools.yahoo_tool import YahooFinanceTool

df = YahooFinanceTool.get_stock_data(
    symbol="AAPL",
    period="1y"
)

risk = YahooFinanceTool.calculate_risk_metrics(df)

print(risk)