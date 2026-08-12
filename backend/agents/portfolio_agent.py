from agents.base_agent import BaseAgent
from agents.news_agent import NewsAgent
from agents.technical_agent import TechnicalAgent
from agents.risk_agent import RiskAgent

from prompts.portfolio_prompt import PORTFOLIO_ANALYSIS_PROMPT
from schemas.portfolio_schema import PortfolioAnalysis


class PortfolioAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            prompt=PORTFOLIO_ANALYSIS_PROMPT,
            output_schema=PortfolioAnalysis
        )

        self.news_agent = NewsAgent()
        self.technical_agent = TechnicalAgent()
        self.risk_agent = RiskAgent()

    def analyze(self, symbols: list[str]):

        portfolio_data = ""

        for symbol in symbols:

            news = self.news_agent.analyze(symbol)
            technical = self.technical_agent.analyze(symbol)
            risk = self.risk_agent.analyze(symbol)

            portfolio_data += f"""
Company: {symbol}

News Recommendation:
{news.recommendation}

Technical Recommendation:
{technical.recommendation}

Risk Level:
{risk.risk_level}

Risk Recommendation:
{risk.recommendation}

------------------------------------
"""

        return self.invoke(
            {
                "portfolio_data": portfolio_data
            }
        )