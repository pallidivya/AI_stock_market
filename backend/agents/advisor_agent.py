from tools.yahoo_tool import YahooFinanceTool
from agents.base_agent import BaseAgent
from agents.news_agent import NewsAgent
from agents.financial_agent import FinancialAgent
from agents.technical_agent import TechnicalAgent
from agents.risk_agent import RiskAgent

from prompts.advisor_prompt import INVESTMENT_ADVISOR_PROMPT
from schemas.advisor_schema import InvestmentAdvice


class AdvisorAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            prompt=INVESTMENT_ADVISOR_PROMPT,
            output_schema=InvestmentAdvice
        )

        self.news_agent = NewsAgent()
        self.financial_agent = FinancialAgent()
        self.technical_agent = TechnicalAgent()
        self.risk_agent = RiskAgent()

    def analyze(self, symbol: str, pdf_path: str):
        company = YahooFinanceTool.get_company_info(symbol)
        news = self.news_agent.analyze(symbol)
        financial = self.financial_agent.analyze(
        company_name=company["company"],
        pdf_path=pdf_path
    )
        technical = self.technical_agent.analyze(symbol)
        risk = self.risk_agent.analyze(symbol)
        result = self.invoke(
        {
            "company": company["company"],
            "news": news.model_dump_json(indent=2),
            "financial": financial.model_dump_json(indent=2),
            "technical": technical.model_dump_json(indent=2),
            "risk": risk.model_dump_json(indent=2),
        }
    )
        return result
   