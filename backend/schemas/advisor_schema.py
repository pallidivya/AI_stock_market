from pydantic import BaseModel


class InvestmentAdvice(BaseModel):
    company: str

    news_summary: str

    financial_summary: str

    technical_summary: str

    risk_summary: str

    final_rating: str

    confidence_score: int

    recommendation: str

    explanation: str