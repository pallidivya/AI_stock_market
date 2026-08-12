from pydantic import BaseModel, Field


class RiskRequest(BaseModel):
    symbol: str


class RiskAnalysis(BaseModel):
    company: str = Field(
        description="Company name"
    )

    volatility_analysis: str = Field(
        description="Analysis of annualized volatility"
    )

    drawdown_analysis: str = Field(
        description="Analysis of maximum drawdown"
    )

    sharpe_ratio_analysis: str = Field(
        description="Analysis of Sharpe ratio"
    )

    risk_level: str = Field(
        description="Low, Medium, or High"
    )

    risk_score: int = Field(
        ge=0,
        le=100,
        description="Overall risk score from 0 to 100"
    )

    investment_suitability: str = Field(
        description="Suitable investor profile"
    )

    recommendation: str = Field(
        description="Buy, Hold, or Sell"
    )