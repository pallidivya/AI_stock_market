from agents.base_agent import BaseAgent
from prompts.risk_prompt import RISK_ANALYSIS_PROMPT
from schemas.risk_schema import RiskAnalysis
from tools.yahoo_tool import YahooFinanceTool


class RiskAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            prompt=RISK_ANALYSIS_PROMPT,
            output_schema=RiskAnalysis
        )

    def analyze(self, symbol: str):

        # Get historical data
        df = YahooFinanceTool.get_stock_data(
            symbol=symbol,
            period="1y"
        )

        # Calculate risk metrics
        risk_metrics = YahooFinanceTool.calculate_risk_metrics(df)

        # Get company details
        company_info = YahooFinanceTool.get_company_info(symbol)

        # Ask the LLM to analyze the metrics
        result = self.invoke(
            {
                "company": company_info["company"],
                **risk_metrics
            }
        )

        return result