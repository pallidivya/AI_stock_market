import numpy as np
import yfinance as yf
from ta.trend import SMAIndicator, EMAIndicator, MACD
from ta.momentum import RSIIndicator


class YahooFinanceTool:
    """
    Utility class for fetching stock market data
    and calculating technical indicators.
    """

    @staticmethod
    def get_stock_data(symbol: str, period: str = "1y"):

        stock = yf.Ticker(symbol)
        df = stock.history(period=period)

        if df.empty:
            raise ValueError(f"No data found for symbol: {symbol}")

        return df

    @staticmethod
    def get_company_info(symbol: str):

        stock = yf.Ticker(symbol)
        info = stock.info

        return {
            "company": info.get("longName"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "market_cap": info.get("marketCap"),
            "currency": info.get("currency"),
            "country": info.get("country"),
        }

    @staticmethod
    def calculate_indicators(df):

        close = df["Close"]

        # SMA
        df["SMA20"] = SMAIndicator(close, window=20).sma_indicator()
        df["SMA50"] = SMAIndicator(close, window=50).sma_indicator()
        df["SMA200"] = SMAIndicator(close, window=200).sma_indicator()

        # EMA
        df["EMA20"] = EMAIndicator(close, window=20).ema_indicator()
        df["EMA50"] = EMAIndicator(close, window=50).ema_indicator()

        # RSI
        df["RSI"] = RSIIndicator(close, window=14).rsi()

        # MACD
        macd = MACD(close)

        df["MACD"] = macd.macd()
        df["MACD_SIGNAL"] = macd.macd_signal()

        latest = df.iloc[-1]

        return {
            "current_price": round(float(latest["Close"]), 2),
            "sma20": round(float(latest["SMA20"]), 2),
            "sma50": round(float(latest["SMA50"]), 2),
            "sma200": round(float(latest["SMA200"]), 2),
            "ema20": round(float(latest["EMA20"]), 2),
            "ema50": round(float(latest["EMA50"]), 2),
            "rsi": round(float(latest["RSI"]), 2),
            "macd": round(float(latest["MACD"]), 2),
            "macd_signal": round(float(latest["MACD_SIGNAL"]), 2),
            "volume": int(latest["Volume"])
        }
    @staticmethod
    def calculate_risk_metrics(df):
        """
        Calculate financial risk metrics from historical prices.
        """

        # Daily percentage returns
        returns = df["Close"].pct_change().dropna()

        # Annualized Volatility
        volatility = returns.std() * np.sqrt(252)

        # Maximum Drawdown
        cumulative = (1 + returns).cumprod()
        running_max = cumulative.cummax()
        drawdown = (cumulative - running_max) / running_max
        max_drawdown = drawdown.min()

        # Sharpe Ratio (assuming risk-free rate = 0)
        sharpe_ratio = (returns.mean() / returns.std()) * np.sqrt(252)

        return {
            "volatility": f"{volatility:.2%}",
            "drawdown": f"{max_drawdown:.2%}",
            "sharpe_ratio": float(round(sharpe_ratio, 2))
        }