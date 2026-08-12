from agents.base_agent import BaseAgent
from prompts.financial_prompt import FINANCIAL_ANALYSIS_PROMPT
from schemas.financial_schema import FinancialAnalysis
from tools.pdf_tool import PDFTool


class FinancialAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            prompt=FINANCIAL_ANALYSIS_PROMPT,
            output_schema=FinancialAnalysis
        )

    def analyze(self, company_name: str, pdf_path: str):

        report_text = PDFTool.extract_text(pdf_path)

        # Limit the text for now to avoid exceeding the model's context window.
        report_text = report_text[:15000]

        result = self.invoke(
            {
                "company": company_name,
                "report": report_text
            }
        )

        return result