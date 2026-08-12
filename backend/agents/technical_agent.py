from agents.base_agent import BaseAgent
from prompts.technical_prompt import TECHNICAL_ANALYSIS_PROMPT
from schemas.technical_schema import TechnicalAnalysis
from tools.yahoo_tool import YahooFinanceTool


class TechnicalAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            prompt=TECHNICAL_ANALYSIS_PROMPT,
            output_schema=TechnicalAnalysis
        )

    def analyze(self, symbol: str):

        # Fetch stock history (1 year for SMA200)
        df = YahooFinanceTool.get_stock_data(
            symbol=symbol,
            period="1y"
        )

        # Calculate indicators
        indicators = YahooFinanceTool.calculate_indicators(df)

        # Company info
        company = YahooFinanceTool.get_company_info(symbol)

        # Invoke LLM
        result = self.invoke(
            {
                "company": company["company"],
                **indicators
            }
        )

        return result