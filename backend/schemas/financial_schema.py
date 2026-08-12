from pydantic import BaseModel


class FinancialAnalysis(BaseModel):
    company: str
    revenue_analysis: str
    profitability: str
    balance_sheet: str
    cash_flow: str
    financial_risk: str
    growth_outlook: str
    investment_recommendation: str