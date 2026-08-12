from agents.base_agent import BaseAgent

from agents.news_agent import NewsAgent
from agents.financial_agent import FinancialAgent
from agents.technical_agent import TechnicalAgent
from agents.risk_agent import RiskAgent
from agents.advisor_agent import AdvisorAgent

from prompts.report_prompt import REPORT_PROMPT
from schemas.report_schema import DailyReport

from tools.yahoo_tool import YahooFinanceTool


class ReportAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            prompt=REPORT_PROMPT,
            output_schema=DailyReport
        )

        self.news_agent = NewsAgent()
        self.financial_agent = FinancialAgent()
        self.technical_agent = TechnicalAgent()
        self.risk_agent = RiskAgent()
        self.advisor_agent = AdvisorAgent()

    def generate_report(self, symbol: str, pdf_path: str):

        # Company information
        company = YahooFinanceTool.get_company_info(symbol)

        company_name = company["company"]

        # Individual analyses
        news = self.news_agent.analyze(symbol)

        financial = self.financial_agent.analyze(
            company_name=company_name,
            pdf_path=pdf_path
        )

        technical = self.technical_agent.analyze(symbol)

        risk = self.risk_agent.analyze(symbol)

        advisor = self.advisor_agent.analyze(
            symbol=symbol,
            pdf_path=pdf_path
        )

        # Generate final report
        result = self.invoke(
            {
                "company": company_name,
                "news": news.model_dump_json(indent=2),
                "financial": financial.model_dump_json(indent=2),
                "technical": technical.model_dump_json(indent=2),
                "risk": risk.model_dump_json(indent=2),
                "advisor": advisor.model_dump_json(indent=2),
            }
        )

        return result